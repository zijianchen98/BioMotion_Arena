
import cv2
import numpy as np
import math

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHTS = 15
ANGLE_STEP = 2 * math.pi / POINT_LIGHTS

# Create a black background
background = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8) * BLACK

# Define the positions and angles of the point lights
light_positions = [
    (WIDTH // 2, HEIGHT // 2),
    (WIDTH // 4, HEIGHT // 4),
    (WIDTH * 3 // 4, HEIGHT // 4),
    (WIDTH // 2, HEIGHT * 3 // 4),
    (WIDTH // 4, HEIGHT * 3 // 4),
    (WIDTH * 3 // 4, HEIGHT * 3 // 4),
    (WIDTH // 4, HEIGHT * 5 // 8),
    (WIDTH * 3 // 4, HEIGHT * 5 // 8),
    (WIDTH // 2, HEIGHT * 7 // 8),
    (WIDTH // 4, HEIGHT * 7 // 8),
    (WIDTH * 3 // 4, HEIGHT * 7 // 8),
    (WIDTH // 2, HEIGHT * 9 // 16),
    (WIDTH // 4, HEIGHT * 9 // 16),
    (WIDTH * 3 // 4, HEIGHT * 9 // 16)
]

light_angles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# Animation loop
for frame in range(100):
    # Clear the background
    background = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8) * BLACK

    # Draw the point lights
    for i in range(POINT_LIGHTS):
        angle = light_angles[i] + frame * ANGLE_STEP
        x = int(WIDTH / 2 + light_positions[i][0] * math.cos(angle) - light_positions[i][1] * math.sin(angle))
        y = int(HEIGHT / 2 + light_positions[i][0] * math.sin(angle) + light_positions[i][1] * math.cos(angle))
        cv2.circle(background, (x, y), 2, WHITE, -1)

    # Display the output
    cv2.imshow('Point Light Stimulus', background)
    cv2.waitKey(100 // 60)
    cv2.destroyAllWindows()

    # Update the light angles to create a smooth rotation
    for i in range(POINT_LIGHTS):
        light_angles[i] = (light_angles[i] + 1) % (2 * math.pi)

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
