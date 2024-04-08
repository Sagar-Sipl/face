from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Welcom Flash'

@socketio.on('message')
def handle_message(message):
    # print('Received message: ' + message)
    try:
            socketio.emit("message", json.dumps("Hi user"))
          
    except Exception as e:
        print(f"WebSocket Error: {str(e)}")
        




@app.route('/testing',methods=['GET'])
def testing():
    try:

                return json.dumps("OK")
    except Exception as e:    
        return json.dumps("")






if __name__ == '__main__':
    # socketio.run(app)
    socketio.run(app,debug=True)
