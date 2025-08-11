
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the number of frames in the animation
n_frames = 100

# Define the initial positions of the point-lights
# These positions represent the key points of the woman's body
# (head, shoulders, elbows, wrists, hips, knees, ankles)
initial_positions = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.3, 0.7],  # left elbow
    [0.7, 0.7],  # right elbow
    [0.2, 0.8],  # left wrist
    [0.8, 0.8],  # right wrist
    [0.5, 0.4],  # left hip
    [0.5, 0.4],  # right hip
    [0.4, 0.3],  # left knee
    [0.6, 0.3],  # right knee
    [0.3, 0.2],  # left ankle
    [0.7, 0.2],  # right ankle
    [0.5, 0.9],  # left hand (waving)
    [0.5, 0.1]   # right hand
])

# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Calculate the positions of the point-lights at the current frame
    positions = initial_positions.copy()
    # Simulate the waving motion
    positions[13, 0] = 0.5 + 0.1 * np.sin(frame / 10.0)
    positions[13, 1] = 0.9 + 0.1 * np.cos(frame / 10.0)

    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='w', s=50)

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

# Show the animation
plt.show()
