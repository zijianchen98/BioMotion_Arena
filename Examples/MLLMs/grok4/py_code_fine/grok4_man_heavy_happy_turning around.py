
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Define initial positions for the point-lights representing the happy man's joints
# Format: (x, y)
joint_positions = np.array([
    [0, 6],  # Head
    [-1, 5], [1, 5],  # Shoulders
    [-1, 4], [1, 4],  # Elbows
    [-1, 3], [1, 3],  # Hands
    [0, 4],  # Torso
    [0, 2],  # Hips
    [-1, 1], [1, 1],  # Knees
    [-1, 0], [1, 0],  # Feet
])

# Weight position (as an additional point)
weight_position = np.array([0, 3])

# Function to update the positions for each frame
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-10, 10)
    plt.ylim(-5, 7)
    plt.gca().set_facecolor('black')
    
    # Calculate rotation angle in radians
    theta = np.deg2rad(frame * 10)  # Adjust the speed of rotation

    # Rotate joints around the y-axis
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    
    # Apply rotation to joint positions
    rotated_positions = joint_positions @ rotation_matrix

    # Draw the joint positions
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], c='white', s=100)  # Joints
    plt.scatter(*weight_position, c='gray', s=150)  # Weight
    
    # Set aspect of the plot to equal
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')  # Hide the axes

# Create the animation
fig = plt.figure()
anim = animation.FuncAnimation(fig, update, frames=np.arange(0, 36), interval=100)

# Show the animation
plt.show()
