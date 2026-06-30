import torch
import torch.nn as nn
from torch.optim import Adam

from models.model import model
from data_loader import train_loader, val_loader


# ======================================================
# Device
# ======================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


# ======================================================
# Class Weights (Handle Class Imbalance)
# NORMAL = 1341
# PNEUMONIA = 3875
# ======================================================
class_counts = torch.tensor([1341, 3875], dtype=torch.float32)

class_weights = class_counts.sum() / (2 * class_counts)
class_weights = class_weights.to(device)


# ======================================================
# Loss Function
# ======================================================
criterion = nn.CrossEntropyLoss(weight=class_weights)


# ======================================================
# Optimizer
# ======================================================
optimizer = Adam(
    model.parameters(),
    lr=0.001
)


# ======================================================
# Learning Rate Scheduler
# Reduce LR after every 3 epochs
# ======================================================
scheduler = torch.optim.lr_scheduler.StepLR(
    optimizer,
    step_size=3,
    gamma=0.1
)


# ======================================================
# Training Settings
# ======================================================
num_epochs = 5
best_val_acc = 0.0

train_losses = []
val_losses = []
val_accuracies = []


# ======================================================
# Training Loop
# ======================================================
for epoch in range(num_epochs):

    # ----------------------------
    # Training
    # ----------------------------
    model.train()

    running_loss = 0.0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    train_loss = running_loss / len(train_loader)
    train_losses.append(train_loss)


    # ----------------------------
    # Validation
    # ----------------------------
    model.eval()

    val_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = criterion(outputs, labels)

            val_loss += loss.item()

            predictions = outputs.argmax(dim=1)

            correct += (predictions == labels).sum().item()
            total += labels.size(0)

    val_loss /= len(val_loader)
    val_acc = correct / total

    val_losses.append(val_loss)
    val_accuracies.append(val_acc)


    # ----------------------------
    # Save Best Model
    # ----------------------------
    if val_acc > best_val_acc:

        best_val_acc = val_acc

        torch.save(
            model.state_dict(),
            "outputs/best_model.pth"
        )

        print("✅ Best model saved!")


    # ----------------------------
    # Step Learning Rate Scheduler
    # ----------------------------
    scheduler.step()

    current_lr = optimizer.param_groups[0]["lr"]


    # ----------------------------
    # Epoch Summary
    # ----------------------------
    print(
        f"Epoch [{epoch+1}/{num_epochs}] | "
        f"Train Loss: {train_loss:.4f} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Acc: {val_acc:.4f} | "
        f"LR: {current_lr:.6f}"
    )


print("\n========================================")
print("Training Complete!")
print(f"Best Validation Accuracy: {best_val_acc:.4f}")
print("========================================")