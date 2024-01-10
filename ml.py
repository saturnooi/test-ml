from PIL import Image
import numpy as np
import os

def load_images(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"): 
            img = Image.open(os.path.join(folder, filename))
            img = img.resize((128, 128))  # ปรับขนาดภาพ
            img = img.convert('RGB')
            img_array = np.array(img)
            images.append(img_array)
            labels.append(label)
    return images, labels
