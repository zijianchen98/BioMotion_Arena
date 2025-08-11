
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 1], [1, 1], [-1, 1], [0.5, 0.5], [-0.5, 0.5],
    [1, 0], [-1, 0], [0, 0], [0.5, -0.5], [-0.5, -0.5],
    [1, -1], [-1, -1], [0, -2], [0.5, -1.5], [-0.5, -1.5]
])

# Normalize positions for the size of the plot
initial_positions *= 0.1

# Create scatter plot of point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Define the movement path
def movement(t):
    return np.sin(t), np.cos(t)

# Animation update function
def update(frame):
    t = frame / 10.0
    dx, dy = movement(t)
    new_positions = initial_positions.copy()
    new_positions[:, 0] += dx * 0.05
    new_positions[:, 1] += dy * 0.05
    
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 200), interval=30, blit=True)

# Show the animation
plt.show()
