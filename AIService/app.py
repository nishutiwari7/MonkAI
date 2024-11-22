import os
import logging
from flask import Flask, request, jsonify
from ultralytics import YOLO
import json

# Initialize app
app = Flask(__name__)

# Setup logging
logging.basicConfig(filename="ai_service.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load model
logging.info("Loading YOLOv3 model...")
model = YOLO("yolov3.pt")  # Ensure you have the YOLOv3 weights in the correct directory

# Directories
TEMP_DIR = "temp"
OUTPUT_IMAGES_DIR = "output/images"
OUTPUT_JSON_DIR = "output/json"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        logging.error("No image provided in request")
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    image_path = os.path.join(TEMP_DIR, image.filename)
    image.save(image_path)

    logging.info(f"Processing image: {image.filename}")
    results = model.predict(source=image_path, save=True, save_dir=OUTPUT_IMAGES_DIR)

    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class": result.names[int(box.cls)],
                "confidence": box.conf.tolist(),
                "bounding_box": box.xyxy.tolist()
            })

    json_output_path = os.path.join(OUTPUT_JSON_DIR, f"{image.filename}.json")
    with open(json_output_path, "w") as json_file:
        json.dump(detections, json_file)

    logging.info(f"Image processed and results saved: {json_output_path}")
    return jsonify({"detections": detections, "output_image": os.path.join(OUTPUT_IMAGES_DIR, image.filename)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
