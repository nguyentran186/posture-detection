from flask import Flask, request, Response, send_file, jsonify
from io import BytesIO
import zipfile
from PIL import Image
from flask_cors import CORS
import random
import cv2

from utils import get_predict

app = Flask(__name__)

CORS(app)

@app.route('/api/process', methods=['POST'])
def process():
    print(request.files)
    image = request.files['file']
    image_path = 'temp.mp4'
    image.save(image_path)
    temp_data, pred = get_predict(image_path)

    result_image_path = 'result.jpg'
    cv2.imwrite(result_image_path, temp_data)
    response_data = {
            'image_url': f'/api/get_image/{result_image_path}',
            'pred': pred
        }
    return jsonify(response_data)


# Serve the processed image
@app.route('/api/get_image/<image_path>')
def get_image(image_path):
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port = 5000)