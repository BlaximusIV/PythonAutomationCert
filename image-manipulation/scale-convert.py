#!/usr/bin/python3

import sys
import os
from PIL import Image

#If given image names
def scale_convert_images(images, rotation, width, height, target_dir):
    for image in images:
        # Get the image at the given location
        im = Image.open(image)

        # Apply processing
        new_im = im.rotate(rotation).resize((width, height))
        try:    
            new_im.save(os.path.join(target_dir, image))
        except:
            print("Unable to save image {}".format(image))
        

#if given image directory
def scale_convert_directory(directory, rotation, width, height, target_dir):
    images = []
    for file in os.listdir(directory):
        if file.endswith(".jpg"):
            images.append(file)
    
    for image in images:
        # Get the image at the given location
        im = Image.open(image)

        # Apply processing
        new_im = im.rotate(rotation).resize((width, height))
        try:    
            new_im.save(os.path.join(target_dir, image))
        except:
            print("Unable to save image {}".format(image))

if __name__ == "__main__":
    scale_convert_directory("/images", 90, 240, 240, "/clean_images")