import torch
from PIL import Image
from torchvision import transforms

from models.model import model


# ======================================================
# Device
# ======================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

model.load_state_dict(
    torch.load(
        "outputs/best_model.pth",
        map_location=device
    )
)

model.eval()


# ======================================================
# Transform
# ======================================================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


classes = ["NORMAL", "PNEUMONIA"]


# ======================================================
# Prediction Function
# ======================================================
def predict(image: Image.Image):

    image = image.convert("RGB")

    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(input_tensor)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, prediction = torch.max(probabilities, dim=1)

    return {
        "prediction": classes[prediction.item()],
        "confidence": round(confidence.item() * 100, 2)
    }