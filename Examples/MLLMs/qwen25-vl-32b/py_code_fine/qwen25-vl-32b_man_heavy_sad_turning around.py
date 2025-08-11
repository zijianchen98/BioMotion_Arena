
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1],
    'left_shoulder': [-0.5, 0],
    'right_shoulder': [0.5, 0],
    'left_elbow': [-1, -0.5],
    'right_elbow': [1, -0.5],
    'left_wrist': [-1.5, -1],
    'right_wrist': [1.5, -1],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3],
    'right_ankle': [1.5, -3],
}

# Convert the dictionary to a list of positions
positions = np.array(list(initial_positions.values()))

# Define the range of motion for turning around
angle_range = np.linspace(0, 2 * np.pi, 100)  # Full rotation in 100 frames

# Function to update the positions based on the angle
def update_positions(angle):
    # Apply rotation matrix to each point
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate all points around the origin
    rotated_positions = np.dot(positions, rotation_matrix.T)
    
    # Add a slight sagging effect to simulate heavy weight
    sag_factor = 0.1
    rotated_positions[:, 1] += sag_factor * np.abs(rotated_positions[:, 0])
    
    return rotated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    angle = angle_range[frame]
    updated_positions = update_positions(angle)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=len(angle_range), interval=50, blit=True
)

# Display the animation
plt.show()
