
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights and the total frames
num_lights = 15
total_frames = 100

# Define the initial positions of the lights
positions = np.random.rand(num_lights, 2)

# Define the target positions for each light
target_positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    # Distribute the lights along a curved path to simulate lying down
    angle = np.linspace(0, 2 * np.pi, num_lights)[i]
    radius = 0.4 + 0.1 * np.sin(angle)
    target_positions[i] = [radius * np.cos(angle), radius * np.sin(angle)]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the lights
lights = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

# Define the update function for the animation
def update(frame):
    # Interpolate between the current and target positions
    alpha = frame / total_frames
    positions = (1 - alpha) * positions + alpha * target_positions
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=50, blit=True)

# Show the animation
plt.show()
