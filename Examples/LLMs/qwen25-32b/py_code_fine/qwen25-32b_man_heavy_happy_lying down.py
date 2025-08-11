
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights and frames
num_lights = 15
frames = 100

# Define the initial positions of the lights
positions = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6], [0.6, 0.6],  # Shoulders
    [0.3, 0.7], [0.7, 0.7],  # Elbows
    [0.2, 0.8], [0.8, 0.8],  # Hands
    [0.4, 0.4], [0.6, 0.4],  # Hips
    [0.3, 0.3], [0.7, 0.3],  # Knees
    [0.2, 0.2], [0.8, 0.2],  # Feet
    [0.5, 0.9],  # Chest
    [0.5, 0.1]   # Pelvis
])

# Define the movement trajectory
def update_positions(frame):
    t = frame / frames * 2 * np.pi
    positions[:, 1] = 0.5 + 0.1 * np.sin(t)
    positions[1:3, 0] += 0.01 * np.cos(t)
    positions[3:5, 0] += 0.02 * np.sin(t)
    positions[5:7, 0] += 0.01 * np.cos(t)
    positions[7:9, 0] -= 0.01 * np.sin(t)
    positions[9:11, 0] -= 0.02 * np.cos(t)
    positions[11:13, 0] -= 0.01 * np.sin(t)
    positions[13, 1] += 0.01 * np.sin(t)
    positions[14, 1] -= 0.01 * np.sin(t)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Update function for the animation
def animate(frame):
    update_positions(frame)
    scat.set_offsets(positions)

# Create the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=50, repeat=True)

plt.show()
