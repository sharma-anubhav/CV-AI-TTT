import json,time
from camera import VideoCamera
from camera import playermove, getBestMove, print_board, print_state, play_move, copy_game_state, check_current_state

from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2
import time
from math import inf as infinity

app=Flask(__name__)
output=[]#("message stark","hi")]
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output)
@app.route('/about')
def about_page():
    return render_template("about.html",result=output)
@app.route('/contact')
def contact_page():
    return render_template("contact.html",result=output)
@app.route('/charts')
def charts_page():
    return render_template("charts.html",result=output)

@app.route('/cam')
def sign_page():
    return render_template("camera.html")


@app.route('/camera',methods=['POST'])
def camera():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("static/cam.png",img)

        # return render_template("camera.html",result=)
        time.sleep(0.01)
        return json.dumps({'status': 'OK', 'result': "static/cam.png"})
        if cv2.waitKey(0) & 0xFF ==ord('q'):
            break
    cap.release()
    # file="/home/ashish/Downloads/THOUGHT.png"
    # with open(file,'rb') as file:
    #     image=base64.encodebytes(file.read())
    #     print(type(image))
    # return json.dumps({'status': 'OK', 'user': user, 'pass': password});
    return json.dumps({'status': 'OK', 'result': "static/cam.png"});




def gen(camera):
    timeout = time.time() + 5
    global game, players
    while True:
        data= camera.get_frame()
        frame1=data[0] 
        evaluate = data[2]
        if time.time() > timeout:
            game = playermove(evaluate)
            winner, current_state = check_current_state(game)
            timeout = time.time() + 5
            if current_state != "Not Done":
                if current_state == "Draw":
                    winner = "Draw"
                    break
                else:
                    winner = "Human"
                    break
            AI = getBestMove(game, 'O')
            game[int((AI - 1) / 3)][(AI - 1) % 3] = 'O'
            winner, current_state = check_current_state(game)
            if current_state != "Not Done":
                if current_state == "Draw":
                    winner = "Draw"
                    break
                else:
                    winner = "Computer"
                    break

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/result',methods=["POST","GET"])
def Result():
    if request.method=="POST":
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if result.lower()=="restart":
            output.clear()
        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                print("Bot says, ")
                for i in r.json():
                    bot_message = i['text']
                    print(f"{i['text']}")
                output.extend([("message parker",result),("message stark",bot_message)])
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])

        print(output)
        return render_template("IY_Home_page.html",result=output)

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")



