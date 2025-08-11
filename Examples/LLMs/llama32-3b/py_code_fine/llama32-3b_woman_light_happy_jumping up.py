
import cv2
import numpy as np
import time

# Define constants
WIDTH, HEIGHT = 640, 480
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
JUMP_HEIGHT = HEIGHT // 2
JUMP_DURATION = 2  # seconds

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define camera parameters
CAMERA_FOV = np.pi / 2  # 90 degrees

# Define animation parameters
ANIMATION_DURATION = 2  # seconds
FPS = 30

# Define lighting positions and velocities
light_positions = np.random.rand(NUM_LIGHTS, 2) * (WIDTH, HEIGHT)
light_velocities = np.random.rand(NUM_LIGHTS, 2) * 2 - 1  # random velocities between -1 and 1

def create_frame():
    # Create a black background
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    frame[:] = BLACK

    # Draw point lights
    for i in range(NUM_LIGHTS):
        x, y = int(light_positions[i, 0]), int(light_positions[i, 1])
        cv2.circle(frame, (x, y), LIGHT_RADIUS, WHITE, -1)

    return frame

def animate():
    global light_positions, light_velocities

    # Jump animation
    if ANIMATION_DURATION > 0:
        ANIMATION_DURATION -= 1 / FPS

        # Update lighting positions
        light_positions += light_velocities * ANIMATION_DURATION

        # Keep lighting positions within the camera view
        light_positions[:, 0] = np.clip(light_positions[:, 0], 0, WIDTH)
        light_positions[:, 1] = np.clip(light_positions[:, 1], 0, HEIGHT)

        # Draw updated frame
        frame = create_frame()
        cv2.imshow('Point-Light Stimulus Animation', frame)

        # Check for quit event
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Jump completed
    else:
        # Reset lighting positions and velocities
        light_positions = np.random.rand(NUM_LIGHTS, 2) * (WIDTH, HEIGHT)
        light_velocities = np.random.rand(NUM_LIGHTS, 2) * 2 - 1

        # Draw final frame
        frame = create_frame()
        cv2.imshow('Point-Light Stimulus Animation', frame)

        # Wait for animation to complete
        time.sleep(1)

    # Check for quit event
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

# Start animation
animate()

# Wait for user input
cv2.waitKey(0)
