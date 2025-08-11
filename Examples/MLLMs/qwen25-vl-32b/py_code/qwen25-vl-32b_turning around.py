
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.75],
    'right_elbow': [1, 0.75],
    'left_hand': [-1.5, 0.5],
    'right_hand': [1.5, 0.5],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5]
}

# Convert to numpy array for easier manipulation
positions = np.array(list(initial_positions.values()))

# Define the range of angles for rotation
angle_range = np.linspace(0, 2 * np.pi, 180)  # Full circle in 180 frames

# Function to update the positions based on the angle
def update_positions(angle):
    # Rotation matrix for 2D
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation to each point
    new_positions = np.dot(positions, rotation_matrix)
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def update(frame):
    angle = angle_range[frame]
    new_positions = update_positions(angle)
    scatter.set_offsets(new_positions)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(angle_range), interval=50, blit=True)

# Show the animation
plt.show()
