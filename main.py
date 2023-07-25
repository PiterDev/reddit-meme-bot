from find_memes import get_hot_memes
import cv2
import time

from make_video import say_meme

print("Fetching memes...")
hot = get_hot_memes(1)
for meme in hot:
    image = meme.image

    max_height = 300
    aspect_ratio = float(max_height) / image.shape[0]
    dimensions = (int(image.shape[1] * aspect_ratio), max_height)
    # perform the resizing
    resized = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

    say_meme(meme)
    cv2.imwrite(f"Resources/Images/{meme.id}.png", image)







