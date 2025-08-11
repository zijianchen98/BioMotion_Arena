
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
point_lights = np.array([
    [0.0, 0.5],  # head
    [-0.2, 0.4],  # left shoulder
    [0.2, 0.4],  # right shoulder
    [-0.3, 0.2],  # left elbow
    [0.3, 0.2],  # right elbow
    [-0.4, 0.1],  # left wrist
    [0.4, 0.1],  # right wrist
    [0.0, 0.3],  # chest
    [-0.1, 0.2],  # left hip
    [0.1, 0.2],  # right hip
    [-0.2, 0.0],  # left knee
    [0.2, 0.0],  # right knee
    [-0.3, -0.1],  # left ankle
    [0.3, -0.1],  # right ankle
    [0.0, -0.2]  # bottom
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the new positions of the point-lights based on the frame number
    new_positions = point_lights.copy()
    new_positions[0, 1] = 0.5 - frame / 100.0  # head
    new_positions[1, 1] = 0.4 - frame / 100.0  # left shoulder
    new_positions[2, 1] = 0.4 - frame / 100.0  # right shoulder
    new_positions[3, 1] = 0.2 - frame / 100.0  # left elbow
    new_positions[4, 1] = 0.2 - frame / 100.0  # right elbow
    new_positions[5, 1] = 0.1 - frame / 100.0  # left wrist
    new_positions[6, 1] = 0.1 - frame / 100.0  # right wrist
    new_positions[7, 1] = 0.3 - frame / 100.0  # chest
    new_positions[8, 1] = 0.2 - frame / 100.0  # left hip
    new_positions[9, 1] = 0.2 - frame / 100.0  # right hip
    new_positions[10, 1] = 0.0 - frame / 100.0  # left knee
    new_positions[11, 1] = 0.0 - frame / 100.0  # right knee
    new_positions[12, 1] = -0.1 - frame / 100.0  # left ankle
    new_positions[13, 1] = -0.1 - frame / 100.0  # right ankle
    new_positions[14, 1] = -0.2 - frame / 100.0  # bottom

    # Plot the point-lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
