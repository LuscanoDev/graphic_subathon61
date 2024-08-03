import os
from moviepy.editor import ImageSequenceClip
import re

image_folder = 'images'

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else -1

images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")],
                key=lambda x: extract_number(x))

clip = ImageSequenceClip(images, fps=30)

clip.write_videofile('output_video.mp4', codec='libx264')
