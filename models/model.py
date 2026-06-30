import torch.nn as nn
from torchvision.models import resnet18

#loading the pretrained Resnet 18
model = resnet18(weights = "DEFAULT")

#replacing the final classification layer

model.fc = nn.Linear(
    in_features=model.fc.in_features,
    out_features=2
)

print(model.fc)