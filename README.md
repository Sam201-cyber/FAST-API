# 🔥 Real-Time Fire Detection Using YOLOv5 and FastAPI

This project is a robust real-time fire detection system built using FastAPI and YOLOv5. It is designed for quick deployment in surveillance and safety environments such as industrial facilities, forests, or buildings where fire hazards are critical. The system supports both video upload and live streaming through a WebSocket connection, performs object detection using a YOLOv5 model, and displays annotated results through a browser interface.

---

## 📽️ Demo

Demo videos of the system in action can be found here:

- [Demo 1 - Fire Detection](https://github.com/yourusername/demo1)
- [Demo 2 - WebSocket Live Feed](https://github.com/yourusername/demo2)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [FastAPI Endpoints](#fastapi-endpoints)
- [Output and Logs](#output-and-logs)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Known Issues](#known-issues)
- [Future Work](#future-work)
- [Credits](#credits)
- [License](#license)

---

## 🔍 Overview

This project integrates YOLOv5 with FastAPI to perform object detection on uploaded video files or real-time streams. The main use-case is the detection of fire in environments that require early warnings and monitoring. Users can interact via a web interface or API endpoints to upload footage, trigger detection, and review results.

---

## 🌟 Features

- Real-time fire detection using YOLOv5  
- FastAPI-powered lightweight web backend  
- Upload video or stream live via WebSocket  
- Output annotated video showing fire detection  
- Saves detection results and frames  
- Easily deployable and extendable  
- Simple UI with HTML & Jinja2 templates

---

## 🧱 System Architecture

User -> Web Interface / API
-> FastAPI Server (main.py)
-> detect.py (YOLOv5 inference)
-> best.pt (Trained Fire Detection Model)
-> WebSocket endpoint (/ws) for live stream
-> File Upload endpoint (/upload) for video files
-> Output served via /video or /runs folder

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fire-detection-fastapi.git
cd fire-detection-fastapi
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
Install requirements

bash
Copy
Edit
pip install -r requirements.txt
Download the trained YOLOv5 model
Place best.pt in the root directory.

Prepare folders
Ensure you have the following directories: uploads/, runs/, templates/, static/.

🗂️ Project Structure
graphql
Copy
Edit
├── main.py               # FastAPI app with API and WebSocket
├── detect.py             # YOLOv5 detection logic
├── templates/
│   └── index.html        # Upload & live view HTML page
├── uploads/              # Uploaded videos
├── runs/                 # Annotated output videos
├── static/               # JS, CSS (optional)
├── best.pt               # YOLOv5 trained model
└── requirements.txt
🚀 Usage Guide
Start the server

bash
Copy
Edit
uvicorn main:app --reload
Open your browser
Navigate to http://127.0.0.1:8000

Upload a video
Click upload, choose a .mp4 video, and wait for the detection process to complete.

View Results
Processed video will be saved in /runs and accessible via /video endpoint.

Live Detection (Optional)
Implement client-side stream and connect to /ws WebSocket endpoint to get real-time detection from webcam.

🔌 FastAPI Endpoints
Endpoint	Method	Description
/	GET	Renders index.html upload interface
/upload	POST	Accepts video file and runs detection
/video	GET	Serves output video file
/ws	WebSocket	Accepts real-time stream and returns frames

📤 Output and Logs
Detection videos are saved in runs/ folder.

Bounding boxes are drawn on detected fire.

Logs print out number of frames processed, detections, and save status.

🧪 Customization
Model: Replace best.pt with your own trained YOLOv5 model.

Classes: Update detect.py to detect other classes (e.g. smoke, person, car).

Thresholds: Modify confidence thresholds in detection code.

📦 Dependencies
Python 3.8+

FastAPI

Uvicorn

PyTorch

OpenCV (cv2)

Ultralytics YOLOv5

Jinja2

numpy

starlette

Install with:

bash
Copy
Edit
pip install -r requirements.txt
🐞 Known Issues
WebSocket live detection may lag on slow hardware

Upload size is limited by default FastAPI settings (adjust manually)

Detection accuracy depends on quality of model (best.pt)

🔮 Future Work
Add SMS/Email alert system for fire detection

Store detection logs to database

Implement smoke detection

Add front-end webcam UI for live preview

🙏 Credits
.Ultralytics YOLOv5

.FastAPI Documentation

.OpenCV Community
