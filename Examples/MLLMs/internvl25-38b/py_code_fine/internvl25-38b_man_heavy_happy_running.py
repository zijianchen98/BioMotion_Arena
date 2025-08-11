
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the figure and axis
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initial positions for the 15 point-lights
points = np.array([
    [0.5, 0.8], [0.45, 0.7], [0.55, 0.7],
    [0.5, 0.6], [0.4, 0.5], [0.6, 0.5],
    [0.45, 0.4], [0.55, 0.4], [0.4, 0.3],
    [0.6, 0.3], [0.45, 0.2], [0.55, 0.2],
    [0.5, 0.1], [0.4, 0.15], [0.6, 0.15]
])

# Scatter plot for point-lights
scat = ax.scatter(points[:, 0], points[:, 1], s=50, color='white')

# Function to update the position of point-lights
def update(frame):
    global points
    shift = np.sin(frame / 10.0 * np.pi) / 20.0
    points[:, 0] += shift
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=40)

# Display the animation
plt.show()
