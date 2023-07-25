import io
import sys

import cv2
import numpy
import praw
import requests
from PIL import Image

from read_memes import read_image, is_readable, is_gibberish
from meme import Meme

reddit = praw.Reddit(
    client_id="O6XsiMhigeat8w",
    client_secret="U5vLklqzNaxkEkRxOIXo3HD9EsIosQ",
    user_agent="firefox:me.piterdev.memereader:v0.0.1 (by u/PewolfP)",
)

sub = reddit.subreddit("memes")


def get_hot_memes(amount: int) -> list:
    memes = []
    submissions = sub.hot()
    memes_found = 0
    print("AAAA")
    log_submissions_checked = 0
    while memes_found < amount:
        log_submissions_checked += 1
        submission = next(submissions)

        is_image = submission.url.endswith(".png") or submission.url.endswith(".jpg")
        if "url" in vars(submission) and not submission.over_18 and is_image:
            # Now let's check if it's worthy of reading
            image = get_image(submission.url)
            if is_readable(image):
                caption = read_image(image)
                if caption and not is_gibberish(caption):
                    memes_found += 1
                    print(f"{memes_found}/{amount}")
                    memes.append(Meme(image, caption, submission.author.name))
    print(f"Memes grabbed. Submissions fetched: {log_submissions_checked} ")
    return memes


def get_image(url) -> numpy.array:
    data = requests.get(url).content
    pil_image = Image.open(io.BytesIO(data)).convert('RGB')
    cv_image = numpy.array(pil_image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
    return cv_image


def get_images(submissions: list) -> list:
    images = []
    for submission in submissions:
        url = submission.url
        cv_image = get_image(url)
        # data = requests.get(url).content
        # pil_image = Image.open(io.BytesIO(data)).convert('RGB')
        # cv_image = numpy.array(pil_image)
        # cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

        images.append(cv_image)
    return images

# cv2.imshow("Meme Viewer free trial", get_images(get_hot_submissions(1))[0])
# cv2.waitKey(0)
