
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the points representing the sadwoman turning around
initial_positions = {
    'head': [0, 0],
    'left_shoulder': [-0.5, -0.5],
    'right_shoulder': [0.5, -0.5],
    'left_elbow': [-1.0, -1.0],
    'right_elbow': [1.0, -1.0],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-0.75, -2.0],
    'right_knee': [0.75, -2.0],
    'left_ankle': [-0.75, -2.5],
    'right_ankle': [0.75, -2.5]
}

# Convert to a list of positions
positions = list(initial_positions.values())

# Function to update the position of the points
def update_points(frame):
    angle = np.radians(frame * 4)  # Rotate 4 degrees per frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Apply the rotation matrix to each point
    new_positions = []
    for pos in positions:
        new_pos = np.dot(rotation_matrix, pos)
        new_positions.append(new_pos)
        
    scatter.set_offsets(new_positions)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')  # Hide axes for a cleaner look
scatter = ax.scatter(*zip(*positions), color='white')

# Create the animation
animation = FuncAnimation(fig, update_points, frames=90, interval=50, repeat=True)

plt.show()
