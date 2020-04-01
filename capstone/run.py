#! /usr/bin/env python3

import os
import requests

target_url = "http://[]/fruits"
description_directory = "supplier-data/descriptions"
files = os.listdir(description_directory)

descriptions = []

for file in files:
    full_path = os.path.join(description_directory, file)
    with open(full_path) as f:
        lines = f.readlines()

        description = {
            "name":lines[0].strip(),
            "weight":lines[1].strip(" lbs"),
            "description":lines[2].strip(),
            "image_name":file.replace("txt", "jpeg")
        }

        descriptions.append(description)

for description in descriptions:
    response = requests.post(target_url, json=description)

    if not response.ok:
        print("Unable to post the given description:\nResponse Code: {}\nReason:{}".format(response.status_code, response.reason))