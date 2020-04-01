#!/usr/bin/python3

import sys
import os
from PIL import Image

# Width, Height
image_size = (600, 400)
image_directory = 'supplier-data/images'

images = []
for file in os.listdir(image_directory):
    if file.endswith('tiff'):
        images.append(file)

for image in images:
    im = Image.open(os.path.join(image_directory, image))
    new_im = im.resize(image_size).convert('RGB')

    try:
        new_im.save(os.path.join(image_directory, image.replace('tiff', 'jpeg')))
    except Exception as ex:
        print("Unable to save image {} \n{}".format(image, ex))