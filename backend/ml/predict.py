import torch
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from torchvision import transforms

def number_to_image(n: int) -> torch.Tensor:
    """Convert number → 28x28 MNIST-style grayscale image"""
    img = Image.new("L", (28, 28), color=0)
    draw = ImageDraw.Draw(img)
    text = str(n % 10)  # last digit encodes parity
    draw.text((8, 4), text, fill=255)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    return transform(img).unsqueeze(0)  # (1, 1, 28, 28)

model = None

def predict(n: int) -> str:
    global model
    if model is None:
        from ml.train import EvenOddCNN
        model = EvenOddCNN()
        model.load_state_dict(torch.load("ml/model.pth",
                                          map_location="cpu"))
        model.eval()
    with torch.no_grad():
        img = number_to_image(n)
        out = model(img)
        pred = out.argmax(dim=1).item()
    return "ODD" if pred == 1 else "EVEN"