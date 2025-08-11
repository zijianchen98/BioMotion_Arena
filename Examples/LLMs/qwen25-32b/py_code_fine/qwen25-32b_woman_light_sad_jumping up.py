
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing the sadwoman
initial_positions = {
    'left_ankle': np.array([-0.1, -0.2]),
    'right_ankle': np.array([0.1, -0.2]),
    'left_knee': np.array([-0.1, 0.0]),
    'right_knee': np.array([0.1, 0.0]),
    'left_hip': np.array([-0.1, 0.2]),
    'right_hip': np.array([0.1, 0.2]),
    'waist': np.array([0.0, 0.4]),
    'chest': np.array([0.0, 0.6]),
    'neck': np.array([0.0, 0.8]),
    'head': np.array([0.0, 1.0]),
    'left_wrist': np.array([-0.3, 0.7]),
    'right_wrist': np.array([0.3, 0.7]),
    'left_elbow': np.array([-0.2, 0.5]),
    'right_elbow': np.array([0.2, 0.5]),
    'shoulders': np.array([0.0, 0.4])
}

# Convert the dictionary to a list of positions
positions = np.array(list(initial_positions.values()))

# Constants for the jumping motion
AMPLITUDE = 0.1
FREQUENCY = 0.05
TIME = np.linspace(0, 2 * np.pi / FREQUENCY, 100)

# Function to update the position of the points based on time
def update(frame):
    y_offset = AMPLITUDE * np.sin(FREQUENCY * TIME[frame])
    new_positions = positions.copy()
    new_positions[:, 1] += y_offset
    scat.set_offsets(new_positions)
    return scat,

# Set up the plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(len(TIME)), blit=True, interval=50)

plt.show()
