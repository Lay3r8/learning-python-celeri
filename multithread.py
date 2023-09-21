#!/home/simon/.pyenv/versions/learning-celeri/bin/python
"""
Download images with multithreading.

(Yes I know it's not real multithreading)
"""
from time import time
from concurrent.futures import ThreadPoolExecutor
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

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(download_image, i) for i in range(REPETITIONS)]

        for future in futures:
            future.result()

    print(f"Total exec time: {time() - start_time} seconds")
