from flask import Flask, request, Response
import time
from torchvision.io import decode_image
from torchvision import datasets, transforms
from torchvision.models import mnasnet0_5, MNASNet0_5_Weights
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from PIL import Image

CLASS_NAMES = [
    "E1",
    "E2",
    "E3",
    "E40",
    "E5H",
    "E6",
    "E8",
    "EHRB"
]
weights = MNASNet0_5_Weights.DEFAULT

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
model = mnasnet0_5()
model.classifier = nn.Sequential(
    nn.Flatten(),
    nn.Dropout(0.5),
    nn.Linear(1280, 128),
    nn.ReLU(),
    nn.Dropout(0.25),
    nn.Linear(128, 8),  # 8 Classes in DOES
    nn.Softmax(dim=1))

model.load_state_dict(torch.load("best_model_no_resize.pth",map_location=device,weights_only=True)["model_state_dict"])
model.to(device)
model.eval()
preprocess = weights.transforms()

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./image_frontend.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():



    i = request.files['image']  # get the image
    img = Image.open(i.stream).convert("RGB") # Open the file stream

# Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        logits = model(batch)

        probs = torch.softmax(logits, dim=1)

        class_id = probs.argmax(dim=1).item()

        score = probs[0][class_id].item()

    category_name = CLASS_NAMES[class_id]

    return Response(
        f"Prediction: {category_name} ({score:.4f})",
        mimetype="text/plain"
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')