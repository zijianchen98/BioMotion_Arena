
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Number of points representing the happyman
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions of the points
points[0] = [0.5, 0.2]  # Head
points[1] = [0.45, 0.3]  # Left shoulder
points[2] = [0.55, 0.3]  # Right shoulder
points[3] = [0.4, 0.4]  # Left elbow
points[4] = [0.6, 0.4]  # Right elbow
points[5] = [0.4, 0.5]  # Left hand
points[6] = [0.6, 0.5]  # Right hand
points[7] = [0.45, 0.5]  # Left hip
points[8] = [0.55, 0.5]  # Right hip
points[9] = [0.4, 0.6]  # Left knee
points[10] = [0.6, 0.6]  # Right knee
points[11] = [0.35, 0.7]  # Left foot
points[12] = [0.65, 0.7]  # Right foot
points[13] = [0.45, 0.4]  # Chest
points[14] = [0.55, 0.4]  # Back

# Scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=10)

# Time variable for the animation
t = 0
dt = 0.1

def update(frame):
    global t
    # Update y-position of each point based on sine wave for jumping motion
    for i in range(num_points):
        points[i, 1] = 0.2 + 0.1 * np.sin(t + i * dt)
    scat.set_offsets(points)
    t += dt
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
