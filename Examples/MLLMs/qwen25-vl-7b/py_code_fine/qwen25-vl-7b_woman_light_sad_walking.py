
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0.5, 0.5], [0.7, 0.4], [0.8, 0.6], [0.9, 0.5],
    [0.6, 0.3], [0.8, 0.4], [0.9, 0.6], [0.7, 0.5],
    [0.5, 0.4], [0.6, 0.6], [0.7, 0.5], [0.8, 0.4],
    [0.6, 0.3], [0.7, 0.5], [0.8, 0.4]
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Smoothly move the points in a walking pattern
    for i in range(len(positions)):
        if i % 2 == 0:
            positions[i][0] += 0.01 * (-1 if frame % 2 == 0 else 1)
            positions[i][1] += 0.01 * (-1 if frame % 2 == 0 else 1)
        else:
            positions[i][0] += 0.01 * (1 if frame % 2 == 0 else -1)
            positions[i][1] += 0.01 * (1 if frame % 2 == 0 else -1)
    
    # Ensure points stay within a reasonable range
    for i in range(len(positions)):
        positions[i][0] = max(0, min(1, positions[i][0]))
        positions[i][1] = max(0, min(1, positions[i][1]))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, repeat=False)

plt.show()
