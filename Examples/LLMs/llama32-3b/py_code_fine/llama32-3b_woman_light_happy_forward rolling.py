
import cv2
import numpy as np
import math

# Define the parameters
num_lights = 15
frame_rate = 30
fps = int(frame_rate * 2)
width, height = 640, 480
black_background = (0, 0, 0)
white_light = (255, 255, 255)

# Define the initial positions and velocities of the lights
light_positions = np.zeros((num_lights, 2))
light_velocities = np.zeros((num_lights, 2))

# Define the action (forward rolling)
action = "forward rolling"

# Define the animation parameters
num_frames = 120
time_step = 1 / fps

for i in range(num_frames):
    # Calculate the time
    t = i * time_step

    # Update the light positions and velocities
    if action == "forward rolling":
        for j in range(num_lights):
            # Update the light position
            light_positions[j, 0] += light_velocities[j, 0] * t
            light_positions[j, 1] += light_velocities[j, 1] * t

            # Update the light velocity
            if j < 5:  # top lights
                light_velocities[j, 0] += 0.01
                light_velocities[j, 1] -= 0.01
            elif j < 10:  # middle lights
                light_velocities[j, 0] += 0.01
                light_velocities[j, 1] += 0.01
            else:  # bottom lights
                light_velocities[j, 0] -= 0.01
                light_velocities[j, 1] += 0.01

            # Keep the light within the boundaries
            light_positions[j, 0] = max(0, min(light_positions[j, 0], width))
            light_positions[j, 1] = max(0, min(light_positions[j, 1], height))

    # Create a black background
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:] = black_background

    # Draw the lights
    for j in range(num_lights):
        # Calculate the light's position in the 2D space
        x = int(light_positions[j, 0])
        y = int(light_positions[j, 1])

        # Draw the light
        cv2.circle(frame, (x, y), 5, white_light, -1)

    # Display the frame
    cv2.imshow("Point Light Animation", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
