from find_memes import get_hot_memes
import cv2
import time

print("Fetching memes...")
hot = get_hot_memes(5)
for meme in hot:
    image = meme.image
    cv2.imwrite(f"{time.time()}.png", image)






