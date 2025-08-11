
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
# These positions are placeholders and should be replaced with actual keyframe data
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each frame (placeholder data)
target_positions = np.random.rand(num_lights, 2)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create point-light objects
lights = [ax.plot([], [], 'o', color='white', markersize=5)[0] for _ in range(num_lights)]

# Update function for the animation
def update(frame):
    # Interpolate between initial and target positions
    current_positions = (1 - frame / 100) * initial_positions + (frame / 100) * target_positions
    for i, light in enumerate(lights):
        light.set_data(current_positions[i, 0], current_positions[i, 1])
    return lights

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
