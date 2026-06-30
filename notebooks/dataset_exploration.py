from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader


transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

train_dataset = datasets.ImageFolder(
    root = "dataset/chest_xray/train",
    transform= transform
)


train_loader = DataLoader(
    train_dataset,
    batch_size = 32,
    shuffle = True
)


