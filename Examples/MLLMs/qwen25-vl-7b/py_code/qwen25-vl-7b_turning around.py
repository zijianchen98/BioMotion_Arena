
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [-1, -1],  # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -2],  # Left hip
    [2, -2],  # Right hip
    [-3, -3],  # Left knee
    [3, -3],  # Right knee
    [-4, -4],  # Left ankle
    [4, -4],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate rotation by adjusting the angles
    angle = frame * 2 * np.pi / 15  # 2pi/15 radians per frame
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    
    new_positions = []
    for pos in positions:
        x, y = pos
        new_x = x * cos_angle - y * sin_angle
        new_y = x * sin_angle + y * cos_angle
        new_positions.append([new_x, new_y])
    
    positions = new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Animation function
ani = FuncAnimation(fig, update, frames=range(15), interval=100)

plt.show()
