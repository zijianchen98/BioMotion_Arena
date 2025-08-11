
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent the major joints of the human body
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.7],  # Left elbow
    [0.6, 0.7],  # Right elbow
    [0.4, 0.6],  # Left hand
    [0.6, 0.6],  # Right hand
    [0.5, 0.5],  # Hip
    [0.4, 0.4],  # Left knee
    [0.6, 0.4],  # Right knee
    [0.4, 0.3],  # Left ankle
    [0.6, 0.3],  # Right ankle
    [0.5, 0.7],  # Left ear
    [0.5, 0.3],  # Left foot toe
    [0.5, 0.1]   # Right foot toe
])

# Define the key frames of the animation
# Each key frame is a 2D array where each row represents the position of a point-light
key_frames = [
    initial_positions,
    np.array([
        [0.5, 0.8],  # Head
        [0.4, 0.7],  # Left shoulder
        [0.6, 0.7],  # Right shoulder
        [0.4, 0.6],  # Left elbow
        [0.6, 0.6],  # Right elbow
        [0.4, 0.5],  # Left hand
        [0.6, 0.5],  # Right hand
        [0.5, 0.4],  # Hip
        [0.4, 0.3],  # Left knee
        [0.6, 0.3],  # Right knee
        [0.4, 0.2],  # Left ankle
        [0.6, 0.2],  # Right ankle
        [0.5, 0.6],  # Left ear
        [0.5, 0.2],  # Left foot toe
        [0.5, 0.0]   # Right foot toe
    ]),
    np.array([
        [0.5, 0.7],  # Head
        [0.4, 0.6],  # Left shoulder
        [0.6, 0.6],  # Right shoulder
        [0.4, 0.5],  # Left elbow
        [0.6, 0.5],  # Right elbow
        [0.4, 0.4],  # Left hand
        [0.6, 0.4],  # Right hand
        [0.5, 0.3],  # Hip
        [0.4, 0.2],  # Left knee
        [0.6, 0.2],  # Right knee
        [0.4, 0.1],  # Left ankle
        [0.6, 0.1],  # Right ankle
        [0.5, 0.5],  # Left ear
        [0.5, 0.1],  # Left foot toe
        [0.5, -0.1]  # Right foot toe
    ]),
    np.array([
        [0.5, 0.6],  # Head
        [0.4, 0.5],  # Left shoulder
        [0.6, 0.5],  # Right shoulder
        [0.4, 0.4],  # Left elbow
        [0.6, 0.4],  # Right elbow
        [0.4, 0.3],  # Left hand
        [0.6, 0.3],  # Right hand
        [0.5, 0.2],  # Hip
        [0.4, 0.1],  # Left knee
        [0.6, 0.1],  # Right knee
        [0.4, 0.0],  # Left ankle
        [0.6, 0.0],  # Right ankle
        [0.5, 0.4],  # Left ear
        [0.5, 0.0],  # Left foot toe
        [0.5, -0.2]  # Right foot toe
    ])
]

# Define the interpolation function
def interpolate(key_frames, frame_num, total_frames):
    if frame_num < total_frames // 2:
        t = frame_num / (total_frames // 2)
        return (1 - t) * key_frames[0] + t * key_frames[1]
    else:
        t = (frame_num - total_frames // 2) / (total_frames // 2)
        return (1 - t) * key_frames[1] + t * key_frames[2]

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Create a list to store the point-light plots
plots = []

# Function to update the plot at each frame
def update(frame_num):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, 1)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    
    # Interpolate the positions of the point-lights
    positions = interpolate(key_frames, frame_num, 100)
    
    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
