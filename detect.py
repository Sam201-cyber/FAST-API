from ultralytics import YOLO
import os
import uuid
from pathlib import Path

def detect_video(weights="weights/best.pt", source="uploads/input.mp4"):
    # Make sure source path exists
    source_path = Path(source).resolve()
    weights_path = Path(weights).resolve()
    print(f"[DEBUG] Source video: {source_path}")
    print(f"[DEBUG] Weights: {weights_path}")

    if not source_path.exists():
        raise FileNotFoundError(f"[ERROR] Source video not found: {source_path}")
    if not weights_path.exists():
        raise FileNotFoundError(f"[ERROR] Weights file not found: {weights_path}")

    # Prepare output directory
    output_dir = f"static/runs_detect_{uuid.uuid4().hex[:8]}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"[DEBUG] Output directory: {output_dir}")

    # Load YOLO model and run detection
    try:
        model = YOLO(str(weights_path))
        results = model(str(source_path), save=True, save_dir=output_dir, conf=0.25, iou=0.45)
    except Exception as e:
        print(f"[ERROR] YOLO detection failed: {e}")
        raise

    # Get first output video
    for file in os.listdir(output_dir):
        if file.endswith(".mp4"):
            output_video_path = os.path.join(output_dir, file)
            print(f"[DEBUG] Output video path: {output_video_path}")
            return output_video_path

    raise FileNotFoundError("No output video (.mp4) was found in the result directory.")



