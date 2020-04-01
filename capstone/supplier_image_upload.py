#!/usr/bin/env python3
import requests
import os

# The script was written for execution on a vm that was running django
url = "http://localhost/upload/"
image_directory = "supplier-data/images"
image_files = os.listdir(image_directory)
jpeg_images = [image for image in image_files if image.endswith(".jpeg")]

for image in jpeg_images:
    image_path = os.path.join(image_directory, image)
    with open(image_path) as image_file:
        response = requests.post(url, files={'file': image_file})
        if not response.ok:
            print("Unable to post the given image:\n{}\n{}".format(response.status_code, response.reason))