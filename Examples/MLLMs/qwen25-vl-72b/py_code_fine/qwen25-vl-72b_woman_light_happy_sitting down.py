
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.8, 0.4], [-0.6, 0.4], [-0.4, 0.4], [-0.2, 0.4], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [-0.3, 0.1], [0.3, 0.1]
])

# Define the target positions for sitting down
target_positions = np.array([
    [0, -1], [-0.5, -0.7], [0, -0.7], [0.5, -0.7],
    [-0.8, -0.4], [-0.6, -0.4], [-0.4, -0.4], [-0.2, -0.4], [0, -0.4], [0.2, -0.4], [0.4, -0.4], [0.6, -0.4], [0.8, -0.4],
    [-0.3, -0.1], [0.3, -0.1]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Create the points as scatter plot
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def update(frame):
    # Calculate the new positions using a simple linear interpolation
    new_positions = initial_positions + (target_positions - initial_positions) * frame / 100
    points.set_offsets(new_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()
