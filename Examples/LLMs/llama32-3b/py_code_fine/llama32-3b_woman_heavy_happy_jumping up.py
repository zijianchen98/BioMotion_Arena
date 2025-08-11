
import cv2
import numpy as np
import time

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15

# Define light positions
light_positions = np.array([
    [WIDTH // 2, HEIGHT // 2 + i * 50],
    [WIDTH // 2 + i * 50, HEIGHT // 2],
    [WIDTH // 2 + i * 50, HEIGHT // 2 - i * 50],
    [WIDTH // 2 + i * 75, HEIGHT // 2],
    [WIDTH // 2 + i * 50, HEIGHT // 2 + i * 75],
    [WIDTH // 2 + i * 50, HEIGHT // 2 - i * 75],
    [WIDTH // 2 + i * 100, HEIGHT // 2],
    [WIDTH // 2 + i * 75, HEIGHT // 2 + i * 100],
    [WIDTH // 2 + i * 50, HEIGHT // 2 - i * 100],
    [WIDTH // 2 + i * 125, HEIGHT // 2],
    [WIDTH // 2 + i * 100, HEIGHT // 2 + i * 125],
    [WIDTH // 2 + i * 50, HEIGHT // 2 - i * 125],
    [WIDTH // 2 + i * 150, HEIGHT // 2],
    [WIDTH // 2 + i * 125, HEIGHT // 2 + i * 150],
    [WIDTH // 2 + i * 50, HEIGHT // 2 - i * 150]
])

# Define action duration
action_duration = 10

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
out = cv2.VideoWriter('animation.mp4', fourcc, fps, (WIDTH, HEIGHT))

# Define animation frames
for i in range(action_duration * fps):
    # Clear frame
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Draw lights
    for j, (x, y) in enumerate(light_positions):
        cv2.circle(frame, (x, y), 5, WHITE, -1)

    # Draw happy woman
    cv2.line(frame, (WIDTH // 2, HEIGHT // 2 - 50), (WIDTH // 2, HEIGHT // 2 + 50), WHITE, 2)
    cv2.line(frame, (WIDTH // 2 - 50, HEIGHT // 2 + 50), (WIDTH // 2 + 50, HEIGHT // 2 + 50), WHITE, 2)
    cv2.line(frame, (WIDTH // 2 + 50, HEIGHT // 2 + 50), (WIDTH // 2 + 50, HEIGHT // 2 - 50), WHITE, 2)

    # Add motion
    for j, (x, y) in enumerate(light_positions):
        if i % (action_duration * fps // NUM_LIGHTS) < 100:
            x += (x - light_positions[j, 0]) / 100
            y += (y - light_positions[j, 1]) / 100

    # Draw woman motion
    cv2.line(frame, (WIDTH // 2, HEIGHT // 2 - 50 + int((i / (action_duration * fps)) * 50)), (WIDTH // 2, HEIGHT // 2 + 50 - int((i / (action_duration * fps)) * 50)), WHITE, 2)
    cv2.line(frame, (WIDTH // 2 - 50 + int((i / (action_duration * fps)) * 50), HEIGHT // 2 + 50 - int((i / (action_duration * fps)) * 50)), (WIDTH // 2 + 50 - int((i / (action_duration * fps)) * 50), HEIGHT // 2 + 50 - int((i / (action_duration * fps)) * 50)), WHITE, 2)
    cv2.line(frame, (WIDTH // 2 + 50 - int((i / (action_duration * fps)) * 50), HEIGHT // 2 + 50 - int((i / (action_duration * fps)) * 50)), (WIDTH // 2 + 50 - int((i / (action_duration * fps)) * 50), HEIGHT // 2 - 50 + int((i / (action_duration * fps)) * 50)), WHITE, 2)

    # Write frame
    out.write(frame)

# Release video writer
out.release()
