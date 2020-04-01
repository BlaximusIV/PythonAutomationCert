#!/usr/bin/python3

import sys
import os
from PIL import Image

# Width, Height
image_size = (600, 400)
image_directory = 'supplier-data/images'

images = []
for file in os.listdir(image_directory):
    images.append(file)

for image in images:
    im = Image.open(image)
    new_im = im.resize(image_size).convert('RGB')

    try:
        new_im.save(os.path.join(image_directory, image + ".jpeg"))
    except Exception as ex:
        print("Unable to save image {} \n{}".format(image, ex))