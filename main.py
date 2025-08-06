 from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
from detect import detect_video

app = FastAPI()

# Setup required directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)
os.makedirs("weights", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount templates and static
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/detect-video/", response_class=HTMLResponse)
async def detect_from_video(request: Request, file: UploadFile = File(...)):
    try:
        input_path = f"uploads/{file.filename}"
        with open(input_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        output_video_path = detect_video(weights="weights/best.pt", source=input_path)

        static_output_path = "static/output.mp4"
        if os.path.exists(static_output_path):
            os.remove(static_output_path)
        shutil.copy(output_video_path, static_output_path)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "video_url": "/static/output.mp4"
        })
    except Exception as e:
        import traceback
        print("ERROR during detection:", traceback.format_exc())
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })
