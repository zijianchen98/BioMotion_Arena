
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 50
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [0, 4],  # Head
    [-0.5, 3.5], # Left shoulder
    [0.5, 3.5],  # Right shoulder
    [-1, 3],   # Left elbow
    [1, 3],    # Right elbow
    [-1.5, 2.5], # Left wrist
    [1.5, 2.5],  # Right wrist
    [-0.2, 2.5],  # Torso-top
    [0.2, 2.5], # Torso-top
    [0, 2],  # Torso-bottom
    [-0.3, 1],   # Left hip
    [0.3, 1],    # Right hip
    [-0.8, 0],   # Left knee
    [0.8, 0],    # Right knee
    [0, -1]    # Foot
])

# Define the range of motion for each point during the jump
motion_ranges = np.array([
    [0, 0.2],  # Head
    [-0.1, 0.1], # Left shoulder
    [0.1, -0.1],  # Right shoulder
    [-0.2, 0.2],   # Left elbow
    [0.2, -0.2],    # Right elbow
    [-0.3, 0.3], # Left wrist
    [0.3, -0.3],  # Right wrist
    [-0.2, 0.2],  # Torso-top
    [0.2, -0.2], # Torso-top
    [0, 0.5],  # Torso-bottom
    [-0.1, 0.1],   # Left hip
    [0.1, -0.1],    # Right hip
    [-0.2, 0.2],   # Left knee
    [0.2, -0.2],    # Right knee
    [0, 0.4]    # Foot
])


# Generate the animation data
def generate_data():
    data = np.zeros((num_frames, num_points, 2))
    for i in range(num_frames):
        phase = np.sin(2 * np.pi * i / num_frames)
        for j in range(num_points):
            data[i, j, 0] = initial_positions[j, 0] + motion_ranges[j, 0] * phase
            data[i, j, 1] = initial_positions[j, 1] + motion_ranges[j, 1] * phase
    return data

data = generate_data()

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 5)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scatter = ax.scatter(data[0, :, 0], data[0, :, 1], c='white', s=20)

# Update function for the animation
def update(frame):
    scatter.set_offsets(data[frame, :, :])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True)

# Show the animation
plt.show()
