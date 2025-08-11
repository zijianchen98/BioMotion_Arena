
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Each point-light represents a joint in the body (e.g. head, shoulders, elbows, etc.)
# The positions are defined in a 2D space, with the x-axis representing the horizontal direction and the y-axis representing the vertical direction
initial_positions = np.array([
    [0.0, 0.5],  # Head
    [-0.1, 0.4],  # Left shoulder
    [0.1, 0.4],  # Right shoulder
    [-0.2, 0.3],  # Left elbow
    [0.2, 0.3],  # Right elbow
    [-0.1, 0.2],  # Left hand
    [0.1, 0.2],  # Right hand
    [0.0, 0.1],  # Hips
    [-0.1, 0.0],  # Left knee
    [0.1, 0.0],  # Right knee
    [-0.2, -0.1],  # Left ankle
    [0.2, -0.1],  # Right ankle
    [-0.1, -0.2],  # Left foot
    [0.1, -0.2],  # Right foot
    [0.0, -0.3]  # Weight
])

# Define the movement patterns for each point-light
# Each movement pattern is a 2D array, where the first column represents the horizontal movement and the second column represents the vertical movement
# The movements are defined in terms of the initial position, so the values represent the change in position over time
movement_patterns = np.array([
    [[0.0, 0.05], [0.0, 0.0], [0.0, -0.05], [0.0, 0.0]],  # Head
    [[-0.02, 0.02], [-0.01, 0.01], [0.02, -0.02], [0.01, -0.01]],  # Left shoulder
    [[0.02, -0.02], [0.01, -0.01], [-0.02, 0.02], [-0.01, 0.01]],  # Right shoulder
    [[-0.05, 0.05], [-0.03, 0.03], [0.05, -0.05], [0.03, -0.03]],  # Left elbow
    [[0.05, -0.05], [0.03, -0.03], [-0.05, 0.05], [-0.03, 0.03]],  # Right elbow
    [[-0.03, 0.03], [-0.02, 0.02], [0.03, -0.03], [0.02, -0.02]],  # Left hand
    [[0.03, -0.03], [0.02, -0.02], [-0.03, 0.03], [-0.02, 0.02]],  # Right hand
    [[0.0, 0.02], [0.0, 0.01], [0.0, -0.02], [0.0, -0.01]],  # Hips
    [[-0.02, 0.02], [-0.01, 0.01], [0.02, -0.02], [0.01, -0.01]],  # Left knee
    [[0.02, -0.02], [0.01, -0.01], [-0.02, 0.02], [-0.01, 0.01]],  # Right knee
    [[-0.05, 0.05], [-0.03, 0.03], [0.05, -0.05], [0.03, -0.03]],  # Left ankle
    [[0.05, -0.05], [0.03, -0.03], [-0.05, 0.05], [-0.03, 0.03]],  # Right ankle
    [[-0.03, 0.03], [-0.02, 0.02], [0.03, -0.03], [0.02, -0.02]],  # Left foot
    [[0.03, -0.03], [0.02, -0.02], [-0.03, 0.03], [-0.02, 0.02]],  # Right foot
    [[0.0, 0.05], [0.0, 0.03], [0.0, -0.05], [0.0, -0.03]]  # Weight
])

# Define the number of frames in the animation
num_frames = 100

# Create a new figure and axis
fig, ax = plt.subplots()

# Initialize the positions of the point-lights
positions = initial_positions.copy()

# Function to update the positions of the point-lights for each frame
def update(frame):
    global positions
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    for i in range(len(positions)):
        positions[i] = initial_positions[i] + movement_patterns[i][frame % 4]
        ax.plot(positions[i, 0], positions[i, 1], 'o', markersize=5, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
