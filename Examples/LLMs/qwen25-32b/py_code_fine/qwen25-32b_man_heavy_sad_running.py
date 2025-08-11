
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing the sadman
initial_positions = {
    'left_ankle': np.array([-0.5, -0.5]),
    'right_ankle': np.array([0.5, -0.5]),
    'left_knee': np.array([-0.5, 0.0]),
    'right_knee': np.array([0.5, 0.0]),
    'left_hip': np.array([-0.5, 0.5]),
    'right_hip': np.array([0.5, 0.5]),
    'waist': np.array([0.0, 0.75]),
    'chest': np.array([0.0, 1.0]),
    'neck': np.array([0.0, 1.25]),
    'head': np.array([0.0, 1.5]),
    'left_shoulder': np.array([-0.5, 1.25]),
    'right_shoulder': np.array([0.5, 1.25]),
    'left_elbow': np.array([-1.0, 1.0]),
    'right_elbow': np.array([1.0, 1.0]),
    'left_wrist': np.array([-1.5, 0.75]),
    'right_wrist': np.array([1.5, 0.75])
}

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide the axes

# Initialize the scatter plot
scat = ax.scatter([], [], color='white')

# Function to update the position of each point-light
def update(frame):
    positions = initial_positions.copy()
    
    # Simulate running motion
    for i in range(16):
        if frame % 32 == i:
            positions['left_ankle'] += np.array([0, 0.1])
            positions['right_ankle'] -= np.array([0, 0.1])
        elif frame % 32 == i + 16:
            positions['left_ankle'] -= np.array([0, 0.1])
            positions['right_ankle'] += np.array([0, 0.1])
    
    # Update the scatter plot data
    x = [pos[0] for pos in positions.values()]
    y = [pos[1] for pos in positions.values()]
    scat.set_offsets(np.c_[x, y])

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

plt.show()
