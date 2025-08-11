
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights representing a lying down sadman
initial_positions = {
    'head': [0.5, 0.2],
    'torso': [0.5, 0.4],
    'left_shoulder': [0.4, 0.4],
    'right_shoulder': [0.6, 0.4],
    'left_elbow': [0.3, 0.4],
    'right_elbow': [0.7, 0.4],
    'left_wrist': [0.2, 0.4],
    'right_wrist': [0.8, 0.4],
    'left_hip': [0.4, 0.6],
    'right_hip': [0.6, 0.6],
    'left_knee': [0.4, 0.8],
    'right_knee': [0.6, 0.8],
    'left_ankle': [0.4, 1.0],
    'right_ankle': [0.6, 1.0],
    'feet_center': [0.5, 1.1]
}

# Convert dictionary to list of positions
positions = np.array(list(initial_positions.values()))

# Create figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Function to update the position of the points
def update(frame):
    global positions
    
    # Simulate a lying down motion with slight oscillation
    amplitude = 0.05
    frequency = 0.05 * frame
    positions[:, 1] += amplitude * np.sin(frequency * np.arange(len(positions)))
    
    # Ensure the head stays at the top
    positions[0][1] = 0.2
    
    # Update the scatter plot
    scat.set_offsets(positions)

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Set the background color to black
fig.patch.set_facecolor('black')
plt.show()
