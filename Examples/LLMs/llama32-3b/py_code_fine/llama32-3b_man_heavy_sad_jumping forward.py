
import cv2
import numpy as np
import math

# Define constants
WIDTH, HEIGHT = 800, 600
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Define the action parameters
action = 'jumping'
angle = 0
duration = 100  # in milliseconds

# Create a black background
bg = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
bg[:, :, 0] = BG_COLOR[0]
bg[:, :, 1] = BG_COLOR[1]
bg[:, :, 2] = BG_COLOR[2]

# Define the lights
lights = []
for i in range(NUM_LIGHTS):
    x = int(WIDTH / 2 + math.cos(i * math.pi / 10) * 200)
    y = int(HEIGHT / 2 + math.sin(i * math.pi / 10) * 200)
    lights.append((x, y))

# Define the animation function
def animate(angle):
    global lights
    global bg
    global action

    # Clear the background
    bg = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    bg[:, :, 0] = BG_COLOR[0]
    bg[:, :, 1] = BG_COLOR[1]
    bg[:, :, 2] = BG_COLOR[2]

    # Update the lights
    for i in range(NUM_LIGHTS):
        x, y = lights[i]
        if action == 'jumping' and angle > 0:
            dx = int(WIDTH / 2 + math.cos((i + angle) * math.pi / 100) * 200)
            dy = int(HEIGHT / 2 + math.sin((i + angle) * math.pi / 100) * 200)
            lights[i] = (dx, dy)
        elif action == 'jumping' and angle <= 0:
            dx = int(WIDTH / 2 + math.cos(i * math.pi / 10) * 200)
            dy = int(HEIGHT / 2 + math.sin(i * math.pi / 10) * 200)
            lights[i] = (dx, dy)

    # Draw the lights
    for x, y in lights:
        cv2.circle(bg, (x, y), LIGHT_RADIUS, LIGHT_COLOR, -1)

    # Display the frame
    cv2.imshow('Point-Light Stimulus', bg)
    cv2.waitKey(16)  # 16 milliseconds = 60 FPS
    if cv2.waitKey(16) & 0xFF == ord('q'):
        break

# Define the main function
def main():
    global angle

    # Initialize the animation
    cv2.namedWindow('Point-Light Stimulus')
    cv2.setMouseCallback('Point-Light Stimulus', lambda x, y, z: print(f'Mouse clicked at ({x}, {y}, {z})'))
    animate(0)

    # Wait for the animation to finish
    cv2.waitKey(duration)
    cv2.destroyAllWindows()

# Call the main function
if __name__ == '__main__':
    main()
