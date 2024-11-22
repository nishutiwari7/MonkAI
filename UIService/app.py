from flask import Flask, render_template, request, jsonify
import requests
import logging

# Initialize app
app = Flask(__name__)

# Setup logging
logging.basicConfig(filename="ui_service.log", level=logging.INFO, format="%(asctime)s - %(message)s")

AI_SERVICE_URL = "http://ai_service:5000/detect"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        logging.error("No file uploaded")
        return "No file uploaded", 400

    image = request.files['image']
    files = {'image': image}
    response = requests.post(AI_SERVICE_URL, files=files)

    if response.status_code == 200:
        logging.info("Image successfully processed")
        return jsonify(response.json())
    else:
        logging.error(f"Error from AI service: {response.text}")
        return f"Error: {response.text}", response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
