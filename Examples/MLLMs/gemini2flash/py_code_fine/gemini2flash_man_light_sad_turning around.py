
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial coordinates of the 15 points
initial_coords = np.array([
    [0, 2],   # head
    [-0.5, 1.5],  # left shoulder
    [0.5, 1.5],   # right shoulder
    [-1, 1],   # left elbow
    [1, 1],    # right elbow
    [-1.5, 0.5],  # left wrist
    [1.5, 0.5],   # right wrist
    [-0.2, 0.8],  # left hip
    [0.2, 0.8],   # right hip
    [-0.7, 0.3],  # left knee
    [0.7, 0.3],   # right knee
    [-0.8, -0.2],  # left ankle
    [0.8, -0.2],  # right ankle
    [-0.6, -0.7],  # left foot
    [0.6, -0.7]   # right foot
])

# Define the rotation matrix
def rotation_matrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])

# Define the movement of the points for each frame
def update_points(frame_num):
    # Define the angle of rotation for the current frame
    angle = np.sin(frame_num / num_frames * 2 * np.pi) * np.pi / 4

    # Apply the rotation matrix to the initial coordinates
    rotated_coords = np.zeros_like(initial_coords)
    for i in range(len(initial_coords)):
        rotated_coords[i] = np.dot(initial_coords[i], rotation_matrix(angle))

    # Apply the translation to the coordinates
    x = rotated_coords[:, 0]
    y = rotated_coords[:, 1]

    # Update the scatter plot data
    scatter.set_offsets(np.c_[x, y])

    # Return the updated scatter plot
    return scatter,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2.5)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Remove ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot
scatter = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], color='white', s=20)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
