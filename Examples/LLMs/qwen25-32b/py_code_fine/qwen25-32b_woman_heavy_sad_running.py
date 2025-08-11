
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
num_frames = 100

# Define initial positions of the points
initial_positions = np.array([
    [0.5, 0.7], [0.4, 0.6], [0.6, 0.6],  # Head and shoulders
    [0.4, 0.4], [0.6, 0.4],               # Arms
    [0.35, 0.3], [0.45, 0.3],             # Left leg
    [0.55, 0.3], [0.65, 0.3],             # Right leg
    [0.3, 0.2], [0.4, 0.2], [0.5, 0.2],   # Feet
    [0.4, 0.5], [0.6, 0.5],               # Chest
    [0.5, 0.1]                            # Pelvis
])

# Define the amplitude and frequency of oscillation for each point
amplitudes = np.array([0.0]*3 + [0.1]*2 + [0.2]*2 + [0.2]*2 + [0.1]*3 + [0.1]*2 + [0.1])
frequencies = np.array([0.0]*3 + [1.0]*2 + [1.5]*2 + [1.5]*2 + [2.0]*3 + [1.0]*2 + [1.0])

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def update(frame):
    # Calculate new y positions based on sine wave
    new_y_positions = initial_positions[:, 1] + amplitudes * np.sin(frame * frequencies)
    
    # Update the scatter plot data
    scat.set_offsets(np.c_[initial_positions[:, 0], new_y_positions])

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, num_frames), repeat=True)

plt.show()
