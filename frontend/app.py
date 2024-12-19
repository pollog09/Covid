from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Define the model architecture
model = models.vgg16(pretrained=False)
model.classifier[6] = torch.nn.Linear(4096, 3)  # Assuming 3 classes: COVID, Pneumonia, Normal

# Load the model state dictionary
model.load_state_dict(torch.load('../models/vgg_canny.pth'))
model.eval()

# Image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        category, saliency_path, canny_path = classify_image(file_path)
        return render_template('result.html', category=category, filename=filename, saliency_path=saliency_path, canny_path=canny_path)

def classify_image(file_path):
    image = Image.open(file_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0)

    # Generate saliency map
    image_tensor.requires_grad_()
    output = model(image_tensor)
    _, predicted = torch.max(output, 1)
    categories = ["COVID", "Pneumonia", "Normal"]
    category = categories[predicted.item()]

    output[0, predicted.item()].backward()
    saliency, _ = torch.max(image_tensor.grad.data.abs(), dim=1)
    saliency = saliency.squeeze().cpu().numpy()

    # Save saliency map
    saliency_path = os.path.join(app.config['UPLOAD_FOLDER'], 'saliency_' + os.path.basename(file_path))
    plt.imsave(saliency_path, saliency, cmap='hot')

    # Generate Canny edge-filtered image
    image_np = np.array(image)
    canny_image = cv2.Canny(image_np, 100, 200)
    canny_path = os.path.join(app.config['UPLOAD_FOLDER'], 'canny_' + os.path.basename(file_path))
    cv2.imwrite(canny_path, canny_image)

    return category, saliency_path, canny_path

if __name__ == '__main__':
    app.run(debug=True)