import os
from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from PIL import Image

from app.backend.predictor import predict

from app.backend.gradcam import generate_gradcam
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Medical Image Disease Detection API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in os.getenv(
        "CORS_ORIGINS", "http://localhost:5173"
    ).split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

app.mount(
    "/outputs",
    StaticFiles(directory=OUTPUT_DIR),
    name="outputs"
)

@app.get("/")
def home():

    return {
        "message": "Medical Image Disease Detection API"
    }


@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):

    image = Image.open(file.file)

    result = predict(image)

    heatmap_path = generate_gradcam(image)

    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "heatmap": heatmap_path
    }
