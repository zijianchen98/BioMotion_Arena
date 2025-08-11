
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a lying down woman
# Based on a simplified biomechanical model
initial_positions = np.array([
    [0, 0],    # Head
    [0.5, 0.5], [0.5, -0.5],  # Shoulders
    [1, 1], [1, -1],  # Elbows
    [1.5, 1.5], [1.5, -1.5],  # Wrists
    [0, 2],    # Hip
    [0.5, 2.5], [0.5, 1.5],  # Knees
    [1, 3], [1, 2],  # Ankles
    [1.5, 3.5], [1.5, 2.5],  # Toes
    [-0.5, 2],  # Other hip
    [-0.5, 2.5]  # Other knee
]) * 0.1  # Scaling factor for visibility

# Define motion parameters for natural lying down movement (slight breathing and shifting)
frames = 100
t = np.linspace(0, 2 * np.pi, frames)
amplitude = 0.02  # Small amplitude for breathing motion
shift = 0.01      # Slight body shift

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.2, 0.2)
ax.set_ylim(-0.2, 0.3)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter([], [], c='white', s=50)

def update(frame):
    # Calculate new positions with breathing and slight shifting
    positions = initial_positions.copy()
    positions[:, 1] += amplitude * np.sin(t[frame])  # Breathing motion (vertical)
    positions[:, 0] += shift * np.cos(t[frame] / 2)  # Slight horizontal shift
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
