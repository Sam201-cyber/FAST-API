import requests
import os
import time

def test_upload():
    # Path to the video file
    video_path = "uploads/video.mp4"
    
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return
    
    print(f"Uploading video from {video_path}")
    print(f"File size: {os.path.getsize(video_path)} bytes")
    print(f"File exists: {os.path.exists(video_path)}")
    
    # Check if the file is readable
    try:
        with open(video_path, 'rb') as test_file:
            test_bytes = test_file.read(1024)
            print(f"Successfully read {len(test_bytes)} bytes from file")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return
    
    # Prepare the file for upload with explicit content type
    try:
        file_handle = open(video_path, 'rb')
        files = {'file': (os.path.basename(video_path), file_handle, 'video/mp4')}
        print("File prepared for upload")
    except Exception as e:
        print(f"Error preparing file: {str(e)}")
        return
    
    try:
        # Set a longer timeout for the request
        print("Sending request to http://127.0.0.1:8000/detect-video/")
        start_time = time.time()
        response = requests.post('http://127.0.0.1:8000/detect-video/', files=files, timeout=300)
        end_time = time.time()
        
        # Print the response status and content
        print(f"Request took {end_time - start_time:.2f} seconds")
        print(f"Response status code: {response.status_code}")
        print(f"Response content type: {response.headers.get('content-type', 'unknown')}")
        
        # Save the response content to a file for inspection
        with open("response_content.html", "wb") as f:
            f.write(response.content)
        print("Response content saved to response_content.html")
        
        # If it's an error response, print the content
        if response.status_code >= 400:
            print("Error response content:")
            print(response.text)
        
    except requests.exceptions.Timeout:
        print("Request timed out after 300 seconds")
    except Exception as e:
        print(f"Error during request: {str(e)}")
    finally:
        # Make sure to close the file
        try:
            file_handle.close()
            print("File handle closed")
        except Exception as e:
            print(f"Error closing file: {str(e)}")

if __name__ == "__main__":
    test_upload()