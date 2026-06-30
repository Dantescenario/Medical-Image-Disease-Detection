import torch
import cv2
import numpy as np

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

model.load_state_dict(
    torch.load(
        "outputs/best_model.pth",
        map_location=device
    )
)

model.eval()


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


def generate_gradcam(image: Image.Image):

    image = image.convert("RGB")

    input_tensor = transform(image).unsqueeze(0).to(device)

    target_layer = model.layer4[-1]

    cam = GradCAM(
        model=model,
        target_layers=[target_layer]
    )

    grayscale_cam = cam(input_tensor=input_tensor)[0]

    rgb_image = image.resize((224, 224))
    rgb_image = np.array(rgb_image).astype(np.float32) / 255.0

    visualization = show_cam_on_image(
        rgb_image,
        grayscale_cam,
        use_rgb=True
    )

    output_path = "outputs/gradcam_api.png"

    cv2.imwrite(
        output_path,
        cv2.cvtColor(
            visualization,
            cv2.COLOR_RGB2BGR
        )
    )

    return output_path