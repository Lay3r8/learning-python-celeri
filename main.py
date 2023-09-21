#!/home/simon/.pyenv/versions/learning-celeri/bin/python
"""
Download images with Celery
"""
# pylint: disable=invalid-name
from time import time
from app import download_image


def download_images(n):
    """DL images"""

    tasks = []
    for i in range(n):
        task = download_image.delay(i)
        tasks.append(task)

    r = []
    for task in tasks:
        r.append(task.get())

    return r


start_time = time()
results = download_images(100)
print(f"Total exec time: {time() - start_time} seconds")
