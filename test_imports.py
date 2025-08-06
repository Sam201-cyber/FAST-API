import torch
import os
import sys
from pathlib import Path

# Add YOLOv5 to path if not already there
yolov5_path = os.path.join(os.getcwd(), 'yolov5')
if yolov5_path not in sys.path:
    sys.path.append(yolov5_path)
    print(f"Added {yolov5_path} to sys.path")

# Import necessary functions from YOLOv5 utils
try:
    from yolov5.utils.general import check_img_size, make_divisible, LOGGER
    print("Successfully imported check_img_size and make_divisible")
    
    # Test check_img_size function
    img_size = 640
    stride = 32
    new_size = check_img_size(img_size, s=stride)
    print(f"Original size: {img_size}, Adjusted size: {new_size}")
    
    print("All imports working correctly!")
except Exception as e:
    print(f"Error importing or using functions: {str(e)}")

print("Test completed")