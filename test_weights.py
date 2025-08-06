import torch
import os
import sys

def test_weights():
    weights_path = "weights/best.pt"
    print(f"Checking weights file: {weights_path}")
    print(f"File exists: {os.path.exists(weights_path)}")
    print(f"File size: {os.path.getsize(weights_path) if os.path.exists(weights_path) else 'File not found'} bytes")
    
    # Add yolov5 to path first
    yolov5_path = os.path.join(os.getcwd(), 'yolov5')
    if yolov5_path not in sys.path:
        sys.path.append(yolov5_path)
    print(f"\nAdded yolov5 path: {yolov5_path}")
    print(f"Current sys.path: {sys.path}")
    
    try:
        # Try loading with torch.load
        print("\nAttempting to load with torch.load...")
        model_data = torch.load(weights_path, map_location='cpu')
        print("Successfully loaded with torch.load")
        print(f"Model data type: {type(model_data)}")
        if isinstance(model_data, dict):
            print(f"Model data keys: {list(model_data.keys())}")
        
        # Try with local yolov5 first
        print("\nAttempting to load from local yolov5...")
        try:
            # Check if models module exists
            print(f"Checking if models module exists in yolov5...")
            try:
                import yolov5.models
                print("yolov5.models module exists")
            except ImportError as e:
                print(f"Error importing yolov5.models: {str(e)}")
            
            # Try to import experimental module
            try:
                from yolov5.models import experimental
                print("Successfully imported experimental module")
            except ImportError as e:
                print(f"Error importing experimental module: {str(e)}")
            
            # Try to import attempt_load function
            try:
                from yolov5.models.experimental import attempt_load
                print("Successfully imported attempt_load function")
                model = attempt_load(weights_path, device='cpu')
                print("Successfully loaded with attempt_load")
            except ImportError as e:
                print(f"Error importing attempt_load: {str(e)}")
            except Exception as load_error:
                print(f"Error using attempt_load: {str(load_error)}")
        except Exception as local_error:
            print(f"Error loading from local yolov5: {str(local_error)}")
        
        # Try loading with hub
        print("\nAttempting to load with torch.hub...")
        try:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=False)
            print("Successfully loaded with torch.hub")
        except Exception as e:
            print(f"Error loading with torch.hub: {str(e)}")
    
    except Exception as e:
        print(f"Error loading weights file: {str(e)}")

if __name__ == "__main__":
    test_weights()