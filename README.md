🩺 Medical Image Disease Detection

An AI-powered web application that detects Pneumonia from chest X-ray images using Deep Learning (ResNet18) and provides model explainability through Grad-CAM visualizations.

The application includes a complete machine learning pipeline, a FastAPI backend, and a React frontend that allows users to upload an X-ray image and receive an instant prediction with confidence score and visual explanation.

📸 Demo

Add screenshots or a GIF here after deployment.

Home Page

docs/home.jpeg

Prediction Result

docs/result.jpeg

Grad-CAM Visualization

docs/gradcam.png

✨ Features
Chest X-ray classification
Detects NORMAL and PNEUMONIA
Confidence score for each prediction
Grad-CAM heatmap for model explainability
React frontend for image upload
FastAPI REST API
PyTorch implementation using transfer learning
Evaluation metrics including Accuracy, Precision, Recall, F1-score and Confusion Matrix
🏗️ Project Architecture
                React Frontend
                       │
                       │ HTTP Request
                       ▼
                 FastAPI Backend
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     ResNet18 Model          Grad-CAM Generator
          │                         │
          └────────────┬────────────┘
                       ▼
               Prediction + Heatmap
📂 Project Structure
Medical-Image-Disease-Detection
│
├── app/
│   ├── backend/
│   └── frontend/
│
├── dataset/
│
├── models/
│
├── notebooks/
│
├── outputs/
│
├── scripts/
│
├── data_loader.py
├── requirements.txt
└── README.md
🧠 Model

Architecture

ResNet18
Transfer Learning
Pretrained ImageNet weights

Loss Function

CrossEntropyLoss
Class weighting for imbalanced dataset

Optimizer

Adam

Input Size

224 × 224 × 3

Classes

NORMAL
PNEUMONIA
📊 Model Performance
Metric	Score
Accuracy	81%
Precision	78%
Recall	95%
F1 Score	86%

Example Classification Report

              precision    recall    f1-score

NORMAL          0.88        0.56      0.69
PNEUMONIA       0.78        0.95      0.86

Accuracy                              0.81
🔥 Grad-CAM Explainability

The project integrates Grad-CAM to visualize the regions of the chest X-ray that contributed most to the model's prediction.

This improves interpretability by highlighting important areas used by the neural network during inference.

🚀 Installation
Clone Repository
git clone https://github.com/YOUR_USERNAME/Medical-Image-Disease-Detection.git
cd Medical-Image-Disease-Detection
Install Python Dependencies
pip install -r requirements.txt
Install Frontend Dependencies
cd app/frontend

npm install
▶️ Running the Project
Start Backend
uvicorn app.backend.main:app --reload

Backend:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
Start Frontend
cd app/frontend

npm run dev

Frontend:

http://localhost:5173
📡 API Endpoint
POST /predict

Upload a chest X-ray image.

Returns

{
    "prediction": "PNEUMONIA",
    "confidence": 99.63,
    "heatmap": "outputs/gradcam_api.png"
}
🛠️ Tech Stack
Machine Learning
PyTorch
TorchVision
Scikit-learn
NumPy
Pillow
Backend
FastAPI
Uvicorn
Frontend
React
Vite
Axios
Tailwind CSS
🎯 Future Improvements
Multi-class disease detection
Support for additional medical imaging modalities
Docker deployment
Cloud deployment
User authentication
Batch image prediction
Model versioning
👨‍💻 Author

Developed by Rishabh Bhardwaj

If you found this project useful, consider giving it a ⭐ on GitHub.