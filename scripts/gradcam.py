import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from torchvision import transforms

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

from models.model import model


# ======================================================
# Device
# ======================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


# ======================================================
# Load Trained Model
# ======================================================
model.load_state_dict(
    torch.load(
        "outputs/best_model.pth",
        map_location=device
    )
)

model.eval()


# ======================================================
# Image Path
# Change this to test another image
# ======================================================
image_path = r"D:\Medical-Image-Disease-Detection\dataset\chest_xray\test\PNEUMONIA\person1_virus_7.jpeg"


# ======================================================
# Image Transform
# ======================================================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


# ======================================================
# Load Image
# ======================================================
image = Image.open(image_path).convert("RGB")

input_tensor = transform(image).unsqueeze(0).to(device)


# ======================================================
# Model Prediction
# ======================================================
outputs = model(input_tensor)

probabilities = torch.softmax(outputs, dim=1)

confidence, prediction = torch.max(probabilities, dim=1)

classes = ["NORMAL", "PNEUMONIA"]

predicted_class = classes[prediction.item()]


# ======================================================
# Print Results
# ======================================================
print("=" * 50)
print("Chest X-ray Analysis")
print("=" * 50)
print(f"Prediction : {predicted_class}")
print(f"Confidence : {confidence.item()*100:.2f}%")
print(f"Image Path : {image_path}")
print("=" * 50)


# ======================================================
# Grad-CAM
# ======================================================
target_layer = model.layer4[-1]

cam = GradCAM(
    model=model,
    target_layers=[target_layer]
)

grayscale_cam = cam(
    input_tensor=input_tensor
)[0]


# ======================================================
# Prepare Original Image
# ======================================================
rgb_image = image.resize((224, 224))

rgb_image = np.array(rgb_image).astype(np.float32) / 255.0


# ======================================================
# Overlay Heatmap
# ======================================================
visualization = show_cam_on_image(
    rgb_image,
    grayscale_cam,
    use_rgb=True
)


# ======================================================
# Save Heatmap Image
# ======================================================
cv2.imwrite(
    "outputs/gradcam_result.png",
    cv2.cvtColor(
        visualization,
        cv2.COLOR_RGB2BGR
    )
)


# ======================================================
# Display Results
# ======================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image)
axes[0].set_title("Original X-ray")
axes[0].axis("off")

axes[1].imshow(visualization)
axes[1].set_title(
    f"{predicted_class}\nConfidence: {confidence.item()*100:.2f}%"
)
axes[1].axis("off")

plt.tight_layout()

plt.savefig(
    "outputs/gradcam_result.png",
    dpi=300
)

plt.show()


print("\n✅ Grad-CAM visualization saved to outputs/gradcam_result.png")