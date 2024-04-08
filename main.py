import json
import cv2
import base64
import numpy as np
from face_recognition_system import register
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    # print('Received message: ' + message)
    try:
        print('Received message: ' , type(message))
        if message=="stop":
           socketio.emit("message",json.dumps( {"status": "False", "message": "stop"}))
        else:
            #    async def send_response(message):
                response =  recognize_face(message)
                print("done")
                socketio.emit("message", json.dumps(response))
          
    except Exception as e:
        print(f"WebSocket Error: {str(e)}")
        

def bs64_to_frame(bs64):
        if bs64:
            decoded_bytes = base64.b64decode(bs64)
            decoded_image = np.frombuffer(decoded_bytes, dtype=np.uint8)
            decoded_image = cv2.imdecode(decoded_image, flags=cv2.IMREAD_COLOR)
            return decoded_image
        else:
            return 'Unable to process image'
        



@app.route('/testing',methods=['GET'])
def testing():
    try:

                return json.dumps("OK")
    except Exception as e:    
        return json.dumps("")




def bytes_to_frame(byte_array):
    nparr = np.frombuffer(byte_array, np.uint8)
    
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return frame

async def recv_and_display(frame):
    cv2.imshow("Video Stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pass

def recognize_face(message):
    try:
        print("type(message)",type(message))
        by= bytes_to_frame(message)

        data =register.getFace(by)
        print("data",type(data))
        
        return data
    except Exception as e:
        return {"status": False, "message": str(e)}




if __name__ == '__main__':
    # socketio.run(app)
    socketio.run(app,debug=True)
