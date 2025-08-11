
from moviepy import pyimageio
from moviepy.video.writing_utils import concatenate_videoclips
from moviepy.video.clip import ImageClip
import numpy as np
import random

# Define white point lights
white_point_lights = np.array([[140, 140], [150, 136], [152, 152], [154, 152], [154, 154],
                               [152, 180], [154, 168], [156, 176], [158, 168], [158, 164],
                               [154, 156], [144, 164], [148, 174], [142, 172],
                               [140, 172]], dtype=np.uint8)

# Function to create a single frame clip with a specific position
def create_bow_frame(light_positions):
    # Black background
    background = np.full((240, 240), 0)
    
    # Plot the white dots on the black background
    for (x, y) in light_positions:
        background[y, x] = 255
    
    return ImageClip(background, size=(240, 240))

# Create a list of frames
frames = [create_bow_frame(white_point_lights)]

# Create a video from the frames
clip = concatenate_videoclips(frames, method="compose")

# Export the video
clip.write_videofile("bowing_point_lights.mp4", fps=10, codec="mpeg4")

print("Animation saved as 'bowing_point_lights.mp4'")
