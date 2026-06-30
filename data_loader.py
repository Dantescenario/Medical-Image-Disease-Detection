from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

train_dataset = datasets.ImageFolder(
    root= "dataset/chest_xray/train",
    transform= transform
)

val_dataset = datasets.ImageFolder(
    root= "dataset/chest_xray/val",
    transform=transform
)
test_dataset = datasets.ImageFolder(
    root= "dataset/chest_xray/test",
    transform=transform
)


train_loader = DataLoader(
    train_dataset,
    batch_size = 32,
    shuffle = True
)

val_loader = DataLoader(
    val_dataset,
    batch_size = 32,
    shuffle = False
)

test_loader = DataLoader(
    test_dataset,
    batch_size = 32,
    shuffle = False
)

print("Training images:", len(train_dataset))
print("Validation images:", len(val_dataset))
print("Test images:", len(test_dataset))