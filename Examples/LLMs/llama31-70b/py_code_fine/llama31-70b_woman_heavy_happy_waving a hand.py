
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are based on the typical positions of joints in a human body
# The positions are in a 2D space with x and y coordinates
initial_positions = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.8],  # left wrist
    [0.6, 0.8],  # right wrist
    [0.5, 0.4],  # torso
    [0.5, 0.3],  # hip
    [0.4, 0.2],  # left knee
    [0.6, 0.2],  # right knee
    [0.4, 0.1],  # left ankle
    [0.6, 0.1],  # right ankle
    [0.4, 0.9],  # left hand
    [0.6, 0.9]   # right hand
])

# Define the movement of each point-light over time
# This is based on the typical movement of a person waving their hand
# The movement is a simple sinusoidal function
def move_points(time):
    positions = initial_positions.copy()
    # Move the head slightly
    positions[0, 0] += 0.05 * np.sin(time)
    positions[0, 1] += 0.05 * np.sin(time)
    # Move the shoulders
    positions[1, 0] += 0.1 * np.sin(time)
    positions[1, 1] += 0.1 * np.sin(time)
    positions[2, 0] -= 0.1 * np.sin(time)
    positions[2, 1] += 0.1 * np.sin(time)
    # Move the elbows
    positions[3, 0] += 0.2 * np.sin(time)
    positions[3, 1] += 0.2 * np.sin(time)
    positions[4, 0] -= 0.2 * np.sin(time)
    positions[4, 1] += 0.2 * np.sin(time)
    # Move the wrists
    positions[5, 0] += 0.3 * np.sin(time)
    positions[5, 1] += 0.3 * np.sin(time)
    positions[6, 0] -= 0.3 * np.sin(time)
    positions[6, 1] += 0.3 * np.sin(time)
    # Move the hands
    positions[13, 0] += 0.4 * np.sin(time)
    positions[13, 1] += 0.4 * np.sin(time)
    positions[14, 0] -= 0.4 * np.sin(time)
    positions[14, 1] += 0.4 * np.sin(time)
    return positions

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the initial positions
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Set the background color to black
ax.set_facecolor('black')

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Remove the axis
ax.axis('off')

# Define the animation function
def animate(time):
    positions = move_points(time)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 10, 0.1), interval=50)

plt.show()
