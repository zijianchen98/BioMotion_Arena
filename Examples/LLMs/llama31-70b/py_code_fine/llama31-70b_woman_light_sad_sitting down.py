
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent the major joints of the human body
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.5, 0.8],  # Neck
    [0.4, 0.7],  # Left shoulder
    [0.6, 0.7],  # Right shoulder
    [0.4, 0.6],  # Left elbow
    [0.6, 0.6],  # Right elbow
    [0.4, 0.5],  # Left hand
    [0.6, 0.5],  # Right hand
    [0.5, 0.5],  # Torso
    [0.5, 0.4],  # Hip
    [0.4, 0.3],  # Left knee
    [0.6, 0.3],  # Right knee
    [0.4, 0.2],  # Left ankle
    [0.6, 0.2],  # Right ankle
    [0.5, 0.1],  # Bottom of torso
])

# Define the key frames of the animation
# These key frames represent the major poses of the action
key_frames = np.array([
    # Initial pose (standing)
    initial_positions,
    # Start sitting down
    initial_positions + np.array([
        [0, 0],
        [0, 0],
        [0, -0.1],
        [0, -0.1],
        [0, -0.2],
        [0, -0.2],
        [0, -0.3],
        [0, -0.3],
        [0, -0.1],
        [0, -0.2],
        [0, -0.3],
        [0, -0.3],
        [0, -0.4],
        [0, -0.4],
        [0, -0.2],
    ]),
    # Continue sitting down
    initial_positions + np.array([
        [0, 0],
        [0, 0],
        [0, -0.2],
        [0, -0.2],
        [0, -0.4],
        [0, -0.4],
        [0, -0.5],
        [0, -0.5],
        [0, -0.2],
        [0, -0.4],
        [0, -0.5],
        [0, -0.5],
        [0, -0.6],
        [0, -0.6],
        [0, -0.4],
    ]),
    # Final pose (sitting down)
    initial_positions + np.array([
        [0, 0],
        [0, 0],
        [0, -0.3],
        [0, -0.3],
        [0, -0.5],
        [0, -0.5],
        [0, -0.6],
        [0, -0.6],
        [0, -0.3],
        [0, -0.5],
        [0, -0.6],
        [0, -0.6],
        [0, -0.7],
        [0, -0.7],
        [0, -0.5],
    ]),
])

# Define the animation function
def animate(i):
    # Clear the current frame
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Calculate the current pose based on the key frames
    t = i / (len(key_frames) - 1)
    pose = (1 - t) * key_frames[0] + t * key_frames[-1]

    # Draw the current pose
    ax.scatter(pose[:, 0], pose[:, 1], c='w', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(key_frames), interval=1000, repeat=True)

# Show the animation
plt.show()
