#!/home/simon/.pyenv/versions/learning-celeri/bin/python
"""
Download images with Celery
"""
# pylint: disable=invalid-name
from os import getenv
from celery import Celery
import requests
from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")
CELERY_BACKEND_URL = getenv("CELERY_BACKEND_URL")


app = Celery(
    "app",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)


@app.task
def download_image(n):
    """DL image"""

    url = "https://picsum.photos/200/300"
    image = requests.get(url, timeout=5)

    image_path = f"./images/{n}.jpg"
    with open(image_path, "wb") as f_out:
        f_out.write(image.content)

    return image_path
