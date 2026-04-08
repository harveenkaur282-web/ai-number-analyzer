import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

# CNN definition (overkill for even/odd but that's the point)
class EvenOddCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 128), nn.ReLU(),
            nn.Linear(128, 2)   # 0=even, 1=odd
        )

    def forward(self, x):
        return self.fc(self.conv(x))

def train():
    transform = transforms.Compose([transforms.ToTensor()])
    mnist = datasets.MNIST('./data', download=True, transform=transform)

    # Remap labels: 0=even (0,2,4,6,8), 1=odd (1,3,5,7,9)
    mnist.targets = (mnist.targets % 2)
    loader = DataLoader(mnist, batch_size=64, shuffle=True)

    model = EvenOddCNN()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()

    for epoch in range(3):  # 3 epochs is plenty for mod 2
        for imgs, labels in loader:
            opt.zero_grad()
            loss = loss_fn(model(imgs), labels)
            loss.backward(); opt.step()
        print(f"Epoch {epoch+1} complete")

    torch.save(model.state_dict(), "model.pth")
    print("Model saved. Used 3 data centers for this.")

if __name__ == "__main__":
    train()