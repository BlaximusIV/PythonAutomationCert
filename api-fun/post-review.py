#! /usr/bin/env python3

import os
import requests
import json

def upload_feedback(directory):
    reviews = []
    files = os.listdir(directory)

    # Convert each file to a json string to append to a body
    for file in files:
        with open(os.path.join(directory, file)) as f:
            lines = f.readlines()

            review = {
                "title":lines[0].strip(),
                "name":lines[1].strip(),
                "date":lines[2].strip(),
                "feedback":lines[3].strip()
            }

            review_json = json.dumps(review)
            reviews.append(review_json)
    
    # Post review to service
    for review in reviews:
        headers = { "Content-Type":"application/json" }
        response = requests.post("http://35.222.235.179/feedback/", data=review, headers=headers)
        
        if not response.ok:
            print("Unable to post the given review. Response Code: {} Response Message: {}".format(response.status_code, response.reason))
        
    upload_feedback("/data/feedback")