
import cv2
import numpy as np
import math

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPACING = 50

# Define the sad woman's body parts
BODY_PARTS = {
    "head": (WIDTH // 2, HEIGHT // 2),
    "torso": (WIDTH // 2, HEIGHT // 2),
    "left_arm": (BODY_PARTS["torso"][0] - 100, BODY_PARTS["torso"][1] + 50),
    "right_arm": (BODY_PARTS["torso"][0] + 100, BODY_PARTS["torso"][1] + 50),
    "left_leg": (BODY_PARTS["torso"][0] - 50, BODY_PARTS["torso"][1] + 150),
    "right_leg": (BODY_PARTS["torso"][0] + 50, BODY_PARTS["torso"][1] + 150),
}

# Define the animation
def animate(frame):
    # Create a black background
    frame.fill(BLACK)

    # Draw the point-lights
    for i in range(NUM_LIGHTS):
        # Calculate the position of the light
        angle = i * 2 * math.pi / NUM_LIGHTS
        radius = LIGHT_SPACING + (LIGHT_RADIUS * math.sin(angle))
        x = int(BODY_PARTS["torso"][0] + radius * math.cos(angle))
        y = int(BODY_PARTS["torso"][1] + radius * math.sin(angle))

        # Draw the light
        cv2.circle(frame, (x, y), LIGHT_RADIUS, WHITE, -1)

    # Return the frame
    return frame

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 30
frame_size = (WIDTH, HEIGHT)
video_writer = cv2.VideoWriter("sad_woman_jumping.mp4", fourcc, fps, frame_size)

# Create the frames
for i in range(100):
    frame = animate(i)
    video_writer.write(frame)

# Release the video writer
video_writer.release()
