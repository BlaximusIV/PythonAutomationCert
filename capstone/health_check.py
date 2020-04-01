#!/usr/bin/env python3

import os
import emails
import shutil
import psutil

def send_email(error_message):
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Error - {}".format(error_message)
    body = "Please check your system and resolve the issue as soon as possible"

    email = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(email)

def check_health():
    cpu_usage = psutil.cpu_percent(1)
    disk_usage = shutil.disk_usage('/')
    memory_usage = psutil.virtual_memory()
    can_resolve_localhost = (os.system("ping -c 1 127.0.0.1") == 0)

    if cpu_usage > 80:
        send_email("CPU usage is over 80%")
    if (disk_usage.free / disk_usage.total) < .2:
        send_email("Available disk space is less than 20%")
    if (memory_usage.available << 20) < 500:
        send_email("Available memory is less than 500MB")
    if not can_resolve_localhost:
        send_email("localhost cannot be resolved to 127.0.0.1")

if __name__ == "__main__":
    check_health()


