
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
LIGHT_RADIUS = 3
FPS = 60
DURATION = 5 # Duration in seconds
WALK_SPEED = 0.1
DIRECTION = [1, 1]

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim((-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Generate random positions for the lights
light_positions = np.random.uniform(-5, , size=(NUM_LIGHTS, 2))

# Function to update the position of each light
def update_light_positions(i):
    global light_positions
    for j in range(NUM_LIGHTS):
        # Update the position based on the walking speed and direction
        light_positions[j] += Direction * WALK_SPEED
        # Wrap around the edges
        light_positions[j] = light_positions[j] % 20
        # Ensure the lights stay within the plot boundaries
        if light_positions[j][0] > 0 or light_positions[j][0] < -0:
            Direction[0] *= -1
        if light_positions[j][1] > 0 or light_positions[j][1] < -0:
            Direction[1] *= -1
    return light_positions

# Create the animation
ani = animation.FuncAnimation(fig, update_light_positions, frames=np.arange(, interval=1000/FPS, blit=True)

# Show the animation
plt.show()

