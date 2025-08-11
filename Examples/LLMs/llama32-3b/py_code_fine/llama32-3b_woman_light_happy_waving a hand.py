
import cv2
import numpy as np
import math

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15
LIGHT_RADIUS = 10
LIGHT_SPACING = 100

# Define the hand and arm positions
hand_position = [WIDTH // 2, HEIGHT // 2]
arm_position = [WIDTH // 2, HEIGHT // 2 + LIGHT_SPACING]

# Define the angles of the hand and arm
hand_angle = 0
arm_angle = 0

# Define the time parameters
frame_rate = 30
duration = 10  # seconds

# Create a video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = frame_rate
out = cv2.VideoWriter('animation.mp4', fourcc, fps, (WIDTH, HEIGHT))

# Define the light positions
lights = []
for i in range(NUM_LIGHTS):
    light_x = arm_position[0] + math.cos(i * 2 * math.pi / NUM_LIGHTS) * LIGHT_SPACING
    light_y = arm_position[1] + math.sin(i * 2 * math.pi / NUM_LIGHTS) * LIGHT_SPACING
    lights.append((light_x, light_y))

# Define the animation parameters
t = 0
while t < duration:
    # Draw the background
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    frame[:] = BLACK

    # Draw the lights
    for i, (light_x, light_y) in enumerate(lights):
        light_x = int(light_x)
        light_y = int(light_y)
        cv2.circle(frame, (light_x, light_y), LIGHT_RADIUS, WHITE, -1)

    # Draw the hand and arm
    cv2.line(frame, (hand_position[0], hand_position[1]), (arm_position[0], arm_position[1]), WHITE, 2)
    cv2.line(frame, (arm_position[0], arm_position[1]), (arm_position[0] + math.cos(arm_angle) * LIGHT_SPACING, arm_position[1] + math.sin(arm_angle) * LIGHT_SPACING), WHITE, 2)

    # Update the hand and arm positions
    hand_angle += 0.1
    arm_angle += 0.1

    # Update the light positions
    for i, (light_x, light_y) in enumerate(lights):
        light_x += math.cos(i * 2 * math.pi / NUM_LIGHTS) * 0.1
        light_y += math.sin(i * 2 * math.pi / NUM_LIGHTS) * 0.1
        lights[i] = (light_x, light_y)

    # Write the frame to the video
    out.write(frame)

    # Increment the time
    t += 1 / frame_rate

# Release the video writer
out.release()
