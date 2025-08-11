
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axes

# Creating the points' initial positions
num_points = 15
# Positions represent the body points in a lying down position (x, y)
positions = np.array([
    (5, 8),  # Head
    (4.5, 7), (5.5, 7),  # Shoulders
    (4, 6), (5, 6), (6, 6),  # Arms
    (4, 5), (6, 5),  # Elbows
    (4, 4), (5, 4), (6, 4),  # Hands
    (4, 3), (5, 3), (6, 3),  # Hips
    (4, 2), (6, 2)   # Knees
])

# Create a scatter plot for point-lights
points = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Animation update function
def update(frame):
    # Simulating movement by shifting the y-coordinates
    movement = np.sin(frame / 10) * 0.1  # Movement for realism
    new_positions = positions.copy()
    new_positions[:, 1] -= movement  # Move downwards
    points.set_offsets(new_positions)

    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# Display the animation
plt.show()
