import numpy as np
from os import listdir
from moviepy.editor import *

image_clips = []
for file in listdir("Resources/Images"):
    image_clips.append(ImageClip(f"Resources/Images/{file}").set_duration(5)) # TODO: Get audio length

video = concatenate(image_clips, method="compose")
video.write_videofile('test.mp4', fps=24)
