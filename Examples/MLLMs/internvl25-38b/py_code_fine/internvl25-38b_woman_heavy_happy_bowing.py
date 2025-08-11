
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    (0.5, 0.9),  # Head
    (0.45, 0.7), (0.55, 0.7),  # Shoulders
    (0.4, 0.6), (0.6, 0.6),  # Arms
    (0.5, 0.5),  # Torso
    (0.45, 0.3), (0.55, 0.3),  # Hips
    (0.4, 0.1), (0.45, 0.2), (0.55, 0.2), (0.6, 0.1),  # Legs and feet
    (0.5, 0.4),  # Center of mass
])

# Define the bowing motion functions
def bowing(t):
    amplitude = 0.08
    return amplitude * np.sin(2 * np.pi * t / 10)

def update_points(num):
    for i in range(points.shape[0]):
        if i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            points[i, 1] = points[i, 1] - bowing(num)

    scatter.set_offsets(points)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0, 100), interval=50)

plt.show()
