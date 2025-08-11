
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the point light positions (example positions)
def init_positions():
    # Define 15 points in 3 columns for x, y coordinates
    return np.array([
        [-0.5, 1.0], [0.0, 1.0], [0.5, 1.0],
        [-1.0, 0.0], [-0.5, 0.0], [0.0, 0.0], [0.5, 0.0], [1.0, 0.0],
        [-0.75, -1.0], [-0.5, -0.5], [-0.25, -1.0], [0.25, -1.0], [0.5, -0.5], [0.75, -1.0],
        [0.0, -1.5]
    ])

# Update function to animate the points
def update(frame, points, scat):
    # Simple sinusoidal motion for demonstration
    y = np.sin(np.pi * frame / 50)
    x = points[:, 0] + np.cos(np.pi * frame / 50)
    y_positions = points[:, 1] + y

    scat.set_offsets(np.c_[x, y_positions])

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
scat = ax.scatter([], [], color='white', s=100)

# Initialize points
points = init_positions()

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=30, blit=False, fargs=(points, scat))

# Display the animation
plt.show()
