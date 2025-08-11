
import cv2
import numpy as np

# Define the position of the points (this is a simplified example)
points_positions = [
    [620, 150],
    [540, 195], [610, 195], [680, 195], [750, 195],
    [470, 240], [540, 240], [610, 240], [680, 240], [750, 240],
    [540, 285], [610, 285], [680, 285], [750, 285],
    [540, 380], [610, 380], [680, 380]
]

# Setup the parameters for the animation
img_w, img_h = 1000, 800
video_duration = 5  # Duration of the video in seconds
frame_rate = 24  # Number of frames per second
num_frames = video_duration * frame_rate

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('biological_motion.mp4', fourcc, frame_rate, (img_w, img_h), False)

# Generate the animation
for i in range(num_frames):
    black_background = np.zeros((img_h, img_w), dtype=np.uint8)

    # Move the points
    for point in points_positions:
        point[0] = int(point[0] + 2 * np.sin(i * 0.5))
        point[1] = int(point[1] + 2 * np.cos(i * 0.5))
        cv2.circle(black_background, (point[0], point[1]), 5, (255), -1)

    video_writer.write(black_background)

video_writer.release()
