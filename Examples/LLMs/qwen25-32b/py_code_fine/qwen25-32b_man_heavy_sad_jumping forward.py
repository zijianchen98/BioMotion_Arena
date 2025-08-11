
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights representing the sadman
initial_positions = {
    'head': [0, 0],
    'left_shoulder': [-1, -1],
    'right_shoulder': [1, -1],
    'left_elbow': [-2, -2],
    'right_elbow': [2, -2],
    'left_wrist': [-3, -3],
    'right_wrist': [3, -3],
    'left_hip': [-1, -4],
    'right_hip': [1, -4],
    'left_knee': [-2, -6],
    'right_knee': [2, -6],
    'left_ankle': [-3, -8],
    'right_ankle': [3, -8]
}

# Convert to numpy array for easier manipulation
positions = np.array(list(initial_positions.values()))

# Function to simulate jumping motion
def jump_motion(t):
    amplitude = 1.5
    frequency = 0.5
    offset = 2.0
    return amplitude * np.sin(2 * np.pi * frequency * t + offset)

# Function to update the positions of the point-lights
def update(frame):
    global positions
    
    # Update y-coordinates based on the jump motion function
    positions[:, 1] += jump_motion(frame)
    
    # Adjust the motion of the legs to simulate forward movement
    if frame % 4 == 0:
        positions[7][0] -= 0.1  # left hip
        positions[9][0] -= 0.2  # left knee
        positions[11][0] -= 0.3 # left ankle
    elif frame % 4 == 2:
        positions[8][0] += 0.1  # right hip
        positions[10][0] += 0.2 # right knee
        positions[12][0] += 0.3 # right ankle
    
    # Draw the points
    scat.set_offsets(positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 2)
ax.set_aspect('equal')
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
