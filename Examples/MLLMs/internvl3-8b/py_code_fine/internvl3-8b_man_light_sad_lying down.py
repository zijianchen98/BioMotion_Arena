
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
N = 15

# Initial positions of points
positions = np.zeros((N, 2))

# Function to update the positions of the points
def update_positions(positions, step):
    return positions + step

# Create a figure with a black background
fig, ax = plt.subplots(facecolor='black')
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot with white points
sc = ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white', linewidths=1)

# Function to update the scatter plot
def update(frame):
    nonlocal positions
    step = np.array([-0.1, -0.1]) * (frame // (N * 5))
    positions = update_positions(positions, step)
    sc.set_offsets(positions)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=N*5, interval=100, blit=True)

# Show the animation
plt.show()
