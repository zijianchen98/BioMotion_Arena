
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 100
# Define the size of the figure
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights representing the happyman
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, -0.5], [0.5, -0.5],  # Shoulders
    [-1, -1.5], [1, -1.5],     # Hips
    [-1.5, -2.5], [-0.5, -2.5],  # Left leg
    [1.5, -2.5], [0.5, -2.5],   # Right leg
    [-1, -0.5], [-1.5, -1],     # Left arm
    [1, -0.5], [1.5, -1],       # Right arm
    [-0.5, -1.5], [0.5, -1.5]   # Hands
])

# Create scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=10)

def update(frame):
    # Define the rotation angle based on the frame
    angle = np.radians(frame * 360 / num_frames)
    
    # Rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply the rotation to each point
    rotated_positions = np.dot(initial_positions, rotation_matrix.T)
    
    # Update the scatter plot data
    scatter.set_offsets(rotated_positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

plt.show()
