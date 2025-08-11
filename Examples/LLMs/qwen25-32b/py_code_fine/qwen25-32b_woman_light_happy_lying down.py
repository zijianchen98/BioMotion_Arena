
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.5, 0.5], [0.4, 0.6], [0.6, 0.6],  # Head
    [0.35, 0.7], [0.65, 0.7],             # Shoulders
    [0.3, 0.8], [0.7, 0.8],               # Elbows
    [0.2, 0.9], [0.8, 0.9],               # Wrists
    [0.4, 0.4], [0.6, 0.4],               # Hips
    [0.3, 0.3], [0.7, 0.3],               # Knees
    [0.2, 0.2], [0.8, 0.2]                # Ankles
])

# Define the amplitude and frequency of the oscillations for each joint
amplitudes = np.array([0]*2 + [0.05]*3 + [0.1]*2 + [0.15]*2 + [0]*2 + [0.1]*2 + [0.15]*2)
frequencies = np.array([0]*2 + [1]*3 + [1.2]*2 + [1.5]*2 + [0]*2 + [1.2]*2 + [1.5]*2)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

def update(frame):
    # Update the y-position of each point-light based on sine wave
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += amplitudes * np.sin(frequencies * frame / 10)
    scatter.set_offsets(updated_positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, repeat=True)

plt.show()
