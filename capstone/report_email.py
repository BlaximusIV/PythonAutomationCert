#!/usr/bin/env python3

import os
import datetime
import reports
import emails

description_directory = "supplier-data/descriptions"
pdf_path = "/tmp/processed.pdf"

def generate_email_pdf():
    date = datetime.datetime.today().strftime("%b %d, %Y")
    title = "Processed Update on {}".format(date)
    body = []

    files = os.listdir(description_directory)

    for file in files:
        with open(os.path.join(description_directory, file)) as f:
            lines = f.readlines()
            name = "name: {}".format(lines[0].strip())
            weight = "weight: {}".format(lines[1].strip())
            body.append(name + "\n" + weight)

    reports.generate_report(pdf_path, title, "<br/><br/>".join(body))

if __name__ == "__main__":
    generate_email_pdf()

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    email = emails.generate(sender, recipient, subject, body, pdf_path)
    emails.send(email)

