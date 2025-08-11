
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the points
num_frames = 100
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 0.5], # Left Elbow
    [1.0, 0.5],  # Right Elbow
    [-1.5, -0.5],# Left Wrist
    [1.5, -0.5], # Right Wrist
    [-0.2, 0.75],# Spine 1
    [0.2, 0.75], # Spine 2
    [0.0, 0.0],  # Hip
    [-0.3, -1.0],# Left Knee
    [0.3, -1.0], # Right Knee
    [-0.6, -2.0],# Left Ankle
    [0.6, -2.0], # Right Ankle
    [0.0, -2.5]   # Foot
])

# Define the function to update the positions of the points
def update_points(frame_num):
    # Calculate the angle of rotation
    angle = np.sin(frame_num / 20) * np.pi / 4

    # Define the rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate the points around the origin
    rotated_positions = np.dot(initial_positions, rotation_matrix)

    # Update the positions of the points
    scat.set_offsets(rotated_positions)

    # Return the updated scatter plot
    return scat,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, blit=True, interval=25, repeat=True, frames=num_frames)

# Show the animation
plt.show()
