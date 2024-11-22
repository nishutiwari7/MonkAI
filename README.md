### MonkAI - Object Detection Microservice
This project demonstrates a microservice architecture for object detection using YOLOv3. The system processes images uploaded by users, performs object detection using a pre-trained YOLOv3 model, and returns annotated images along with structured JSON outputs. The application uses a UI backend and an AI backend to provide a seamless user experience.

## Features
# Image Upload: Users can upload images through a web interface.
# YOLOv3 Object Detection: Lightweight object detection with YOLOv3 for detecting multiple objects in the images.
# Annotated Images: Detected objects are highlighted in the images with bounding boxes.
# JSON Output: The system returns a JSON file with structured information about the detected objects.
# Microservice Architecture: The system is split into UI and AI services that communicate seamlessly.
# Dockerized Deployment: The application is containerized using Docker for easy deployment and scaling.

## Project Structure
graphql

#MonkAI/
├── AIService/
│   ├── app.py                  # Main API for AI backend (object detection)
│   ├── requirements.txt        # Python dependencies for AI service
│   ├── Dockerfile              # Docker configuration for AI service
│   ├── yolo_model/             # YOLOv3 model files
│   ├── tests/
│   │   └── TestAIService.py    # Unit tests for AI service
├── UIService/
│   ├── app.py                  # Web application for UI (image upload and results display)
│   ├── requirements.txt        # Python dependencies for UI service
│   ├── Dockerfile              # Docker configuration for UI service
│   ├── templates/
│   │   └── index.html          # HTML file for image upload interface
│   ├── static/
│   │   └── styles.css          # CSS for UI styling
│   └── tests/
│       └── TestUIService.py    # Unit tests for UI service
├── docker-compose.yaml         # Configuration to orchestrate services using Docker
└── README.md                   # This file
## Getting Started
# Prerequisites
Docker: For containerized deployment of services.
Python: Required for local development and testing (for AI and UI services).

# Installation
Clone the repository:

Copy code
git clone https://github.com/yourusername/MonkAI.git
cd MonkAI
Install Python dependencies for both services (if you are running locally):

AIService:

Copy code
cd AIService
python -m pip install -r requirements.txt

UIService:

Copy code
cd ../UIService
python -m pip install -r requirements.txt
Docker Setup (if you're using Docker):

Make sure Docker and Docker Compose are installed.
Build and run both services:

Copy code
docker-compose up --build
Running the Application
Local Testing

Start the AIService (object detection):

Copy code
cd AIService
python app.py

Start the UIService (web interface):

Copy code
cd ../UIService
python app.py
Access the Web Interface: Open your browser and navigate to http://localhost:5000. This will allow you to upload images and view detection results.

Docker Deployment
To deploy both services using Docker Compose:

Build and start the services:

Copy code
docker-compose up --build
Once the services are up and running, access the UI by visiting http://localhost:5000 in your web browser.

Stop the containers when done:

Copy code
docker-compose down


## How It Works

# UI Service: The web interface allows users to upload images. Upon submission, the UI sends the image to the AI service.
# AI Service: The AI service processes the image using a pre-trained YOLOv3 model. The detected objects are then highlighted with bounding boxes, and the results are returned as an annotated image and a structured JSON file with object labels, coordinates, and confidence scores.
# JSON Output: Each object detected in the image is returned with details such as:
Object class (e.g., person, car, etc.)
Confidence score
Coordinates of the bounding box
Testing
Run Unit Tests
# To test the AI service:

Copy code
cd AIService
python -m unittest discover -s tests

#To test the UI service:

Copy code
cd UIService
python -m unittest discover -s tests
Contributing
Fork the repository.

Create a feature branch:

Copy code
git checkout -b feature-name

Commit your changes:

Copy code
git commit -m "Add new feature"
Push to your branch and open a pull request.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For queries or suggestions, reach out to Nishu Tiwari at u.nishu703@gmail.com.

# Feel free to customize this further based on any additional configurations or features in your project!








