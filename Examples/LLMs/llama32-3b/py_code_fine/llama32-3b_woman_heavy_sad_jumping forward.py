
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
    [100, 100],  # left shoulder
    [150, 100],  # left elbow
    [200, 100],  # left wrist
    [250, 100],  # left hand
    [300, 100],  # left hip
    [350, 100],  # left knee
    [400, 100],  # left ankle
    [450, 100],  # left foot
    [100, 200],  # right shoulder
    [150, 200],  # right elbow
    [200, 200],  # right wrist
    [250, 200],  # right hand
    [300, 200],  # right hip
    [350, 200],  # right knee
    [400, 200],  # right ankle
    [450, 200],  # right foot
])

# Define action parameters
action_duration = 10  # seconds
action_time = 0

# Main loop
while action_time < action_duration:
    # Clear the screen
    screen = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Draw lights
    for i in range(NUM_LIGHTS):
        x, y = light_positions[i]
        cv2.circle(screen, (x, y), 5, WHITE, -1)

    # Update animation
    if action_time < 3:
        # Initial jump phase
        for i in range(NUM_LIGHTS):
            x, y = light_positions[i]
            cv2.circle(screen, (x, y), 10, WHITE, -1)
    elif action_time < 6:
        # Ascending phase
        for i in range(NUM_LIGHTS):
            x, y = light_positions[i]
            cv2.circle(screen, (x, y), 15, WHITE, -1)
    elif action_time < 8:
        # Peak phase
        for i in range(NUM_LIGHTS):
            x, y = light_positions[i]
            cv2.circle(screen, (x, y), 20, WHITE, -1)
    elif action_time < 10:
        # Descending phase
        for i in range(NUM_LIGHTS):
            x, y = light_positions[i]
            cv2.circle(screen, (x, y), 15, WHITE, -1)

    # Display the screen
    cv2.imshow('Animation', screen)

    # Update time
    action_time += 0.1
    time.sleep(0.1)

# Close the window
cv2.destroyAllWindows()
