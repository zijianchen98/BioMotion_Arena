
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Define the initial positions of the points
def init_positions():
    positions = [
        [0, 1.5], [-0.5, 1], [0.5, 1], [-1, 0.5], [1, 0.5],
        [-0.5, 0.5], [0.5, 0.5], [-0.25, 0], [0.25, 0], [0, -0.5],
        [-0.75, -1], [0.75, -1], [-0.5, -1.5], [0.5, -1.5], [-0.25, -2], [0.25, -2]
    ]
    return np.array(positions)

# Update the positions to simulate running
def update_positions(positions, frame):
    speed = 0.05  # Adjust for a light weight feeling
    cycle_length = 120  # Length of the running cycle

    t = (frame % cycle_length) / cycle_length  # Normalized time

    # Adjust positions to create a running motion
    positions[0] += [speed, -0.1 * np.sin(t * 2 * np.pi)]  # Head
    positions[1:3] += [speed, -0.1 * np.sin(t * 2 * np.pi)]  # Shoulders
    positions[3:5] += [speed, -0.1 * np.cos(t * 2 * np.pi)]  # Hips
    positions[5:7] += [speed, -0.1 * np.sin(t * 2 * np.pi)]  # Arms
    positions[7:9] += [speed, -0.1 * np.cos(t * 2 * np.pi)]  # Waist
    positions[9] += [speed, -0.1 * np.sin(t * 2 * np.pi)]  # Lower body

    # Legs movement
    positions[10:12] += [speed, 0.1 * np.sin(t * 2 * np.pi)]  # Upper legs
    positions[12:14] += [speed, 0.1 * np.cos(t * 2 * np.pi)]  # Lower legs
    positions[14:15] += [speed, 0.1 * np.sin(t * 2 * np.pi)]  # Feet

# Animation update function
def animate(frame):
    update_positions(positions, frame)
    ax.clear()
    ax.set_facecolor('black')
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-3, 2)
    ax.axis('off')

# Initialize the positions
positions = init_positions()

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=240, interval=50)

plt.show()
