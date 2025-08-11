
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Left knee
    [0, -3],  # Left ankle
    [-2, -2],  # Right knee
    [0, -4],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate walking by slightly adjusting the positions
    for i in range(len(positions)):
        if i == 0:  # Head
            positions[i][1] += 0.05 * (-1 if frame % 2 == 0 else 1)
        elif i == 1 or i == 2:  # Shoulders
            positions[i][1] += 0.05 * (-1 if frame % 2 == 0 else 1)
        elif i == 3 or i == 6:  # Hips
            positions[i][1] += 0.05 * (-1 if frame % 2 == 0 else 1)
        elif i == 4 or i == 7:  # Knees
            positions[i][1] += 0.05 * (-1 if frame % 2 == 0 else 1)
        elif i == 5 or i == 8:  # Ankles
            positions[i][1] += 0.05 * (-1 if frame % 2 == 0 else 1)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 0)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Animation function
def animate(frame):
    update(frame)
    points.set_data(*zip(*positions))
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
