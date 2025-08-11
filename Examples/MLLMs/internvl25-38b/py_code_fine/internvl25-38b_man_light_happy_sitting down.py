
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 lights
initial_positions = [
    (0.0, 1.0), (0.1, 0.8), (-0.1, 0.8),
    (0.2, 0.5), (-0.2, 0.5), (0.0, 0.3),
    (0.3, 0.0), (-0.3, 0.0), (0.15, 0.1),
    (-0.15, 0.1), (0.25, -0.1), (-0.25, -0.1),
    (0.0, -0.2), (0.1, -0.5), (-0.1, -0.5)
]

# Convert to numpy array for easier manipulation
positions = np.array(initial_positions)

# Define the movement for sitting down
def sit_down(t):
    positions[:, 1] = initial_positions[:, 1] - 0.1 * np.sin(2 * np.pi * t)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 1.0)
ax.set_facecolor('black')
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Animation function
def update(frame):
    t = frame / 60.0
    sit_down(t)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=30, blit=True)

# Show the plot
plt.show()
