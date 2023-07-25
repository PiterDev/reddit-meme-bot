from find_memes import get_hot_memes, get_images
from read_memes import read_image, is_readable
import cv2
import time
# 4/10 memes get read correctly
# Especially those with thick fonts and black captions on a white background

from read_memes import is_gibberish

print("Fetching memes...")
hot = get_hot_memes(5)
for meme in hot:
    image = meme.image
    print(meme.caption)
    # cv2.imshow("", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # if is_readable(image):
    #     print("Running OCR....")
    #     text = read_image(image)
    #     print("Caption: " + text)
    cv2.imwrite(f"{time.time()}.png", image)






