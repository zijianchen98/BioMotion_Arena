
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
    [0, -3],  # Left foot
    [-2, -2],  # Right knee
    [0, -4],  # Right foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a smooth movement of the points
    for i in range(len(positions)):
        positions[i][0] += np.random.normal(0, 0.1)
        positions[i][1] += np.random.normal(0, 0.1)
    
    # Ensure the points stay within a reasonable range
    for i in range(len(positions)):
        if positions[i][0] > 3:
            positions[i][0] = 3
        elif positions[i][0] < -3:
            positions[i][0] = -3
        if positions[i][1] > 3:
            positions[i][1] = 3
        elif positions[i][1] < -3:
            positions[i][1] = -3

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
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
