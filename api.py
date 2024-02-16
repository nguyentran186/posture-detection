from flask import Flask, request, Response, send_file, jsonify
from io import BytesIO
import zipfile
from PIL import Image
from flask_cors import CORS
import random
import cv2
from flask_socketio import SocketIO

from utils import get_prediction

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

CORS(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)

@socketio.on('pose_landmarks')
def handle_pose_landmarks(data):
    pred = get_prediction(data)
    print(pred)
    socketio.emit('response', pred)

def process_pose_landmarks(data):
    # Dummy processing function, replace with your actual processing logic
    return {'message': 'Processed pose landmarks'}

if __name__ == '__main__':
    socketio.run(app, port = 5000)