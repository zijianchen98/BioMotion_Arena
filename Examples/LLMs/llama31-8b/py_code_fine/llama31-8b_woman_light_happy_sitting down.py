
import cv2
import numpy as np
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions
NUM_LIGHTS = 15
LIGHT_RADIUS = 2
LIGHT_COLOR = (255, 255, 255)

# Sitting down action parameters
ACTION_DUR = 5  # seconds
CYCLE_FRAMES = int(30 * ACTION_DUR)  # 30 FPS

# Initial and final joint positions (approximate)
INIT_JOINTS = [
    [WIDTH / 2, HEIGHT / 2],  # head
    [WIDTH / 2 - 50, HEIGHT / 2 + 50],  # left shoulder
    [WIDTH / 2 + 50, HEIGHT / 2 + 50],  # right shoulder
    [WIDTH / 2 - 100, HEIGHT / 2 + 150],  # left elbow
    [WIDTH / 2 + 100, HEIGHT / 2 + 150],  # right elbow
    [WIDTH / 2 - 150, HEIGHT / 2 + 250],  # left wrist
    [WIDTH / 2 + 150, HEIGHT / 2 + 250],  # right wrist
    [WIDTH / 2 - 200, HEIGHT / 2 + 350],  # left hand
    [WIDTH / 2 + 200, HEIGHT / 2 + 350],  # right hand
    [WIDTH / 2 - 50, HEIGHT / 2 + 450],  # left hip
    [WIDTH / 2 + 50, HEIGHT / 2 + 450],  # right hip
    [WIDTH / 2 - 100, HEIGHT / 2 + 550],  # left knee
    [WIDTH / 2 + 100, HEIGHT / 2 + 550],  # right knee
    [WIDTH / 2 - 150, HEIGHT / 2 + 650],  # left ankle
    [WIDTH / 2 + 150, HEIGHT / 2 + 650],  # right ankle
]

FINAL_JOINTS = [
    [WIDTH / 2, HEIGHT / 2 + 200],  # head
    [WIDTH / 2 - 50, HEIGHT / 2 + 250],  # left shoulder
    [WIDTH / 2 + 50, HEIGHT / 2 + 250],  # right shoulder
    [WIDTH / 2 - 100, HEIGHT / 2 + 350],  # left elbow
    [WIDTH / 2 + 100, HEIGHT / 2 + 350],  # right elbow
    [WIDTH / 2 - 150, HEIGHT / 2 + 450],  # left wrist
    [WIDTH / 2 + 150, HEIGHT / 2 + 450],  # right wrist
    [WIDTH / 2 - 200, HEIGHT / 2 + 550],  # left hand
    [WIDTH / 2 + 200, HEIGHT / 2 + 550],  # right hand
    [WIDTH / 2 - 50, HEIGHT / 2 + 600],  # left hip
    [WIDTH / 2 + 50, HEIGHT / 2 + 600],  # right hip
    [WIDTH / 2 - 100, HEIGHT / 2 + 700],  # left knee
    [WIDTH / 2 + 100, HEIGHT / 2 + 700],  # right knee
    [WIDTH / 2 - 150, HEIGHT / 2 + 800],  # left ankle
    [WIDTH / 2 + 150, HEIGHT / 2 + 800],  # right ankle
]

# Function to calculate the distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to interpolate between two points
def interpolate(p1, p2, t):
    return [int(p1[0] + (p2[0] - p1[0]) * t), int(p1[1] + (p2[1] - p1[1]) * t)]

# Create a window
cv2.namedWindow('Point-Light Stimulus', cv2.WINDOW_NORMAL)

# Create a black background
background = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# Set up the frame loop
for frame in range(CYCLE_FRAMES):
    # Calculate the interpolation factor
    t = frame / CYCLE_FRAMES

    # Clear the background
    cv2.imshow('Point-Light Stimulus', background)

    # Draw the point-lights
    for i in range(NUM_LIGHTS):
        p1 = INIT_JOINTS[i]
        p2 = FINAL_JOINTS[i]
        p = interpolate(p1, p2, t)
        cv2.circle(background, p, LIGHT_RADIUS, LIGHT_COLOR, -1)

    # Update the display
    cv2.waitKey(1)

# Close the window
cv2.destroyAllWindows()
