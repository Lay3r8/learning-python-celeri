#!/home/simon/.pyenv/versions/learning-celeri/bin/python
"""
Download images, single thread example
"""
from time import time
import requests


REPETITIONS = 100


def download_image(n):
    """DL image"""

    url = "https://picsum.photos/200/300"
    image = requests.get(url, timeout=5)

    image_path = f"./images/{n}.jpg"
    with open(image_path, "wb") as f_out:
        f_out.write(image.content)

    return image_path


if __name__ == "__main__":
    start_time = time()
    for i in range(REPETITIONS):
        download_image(i)
    print(f"Total exec time: {time() - start_time} seconds")
