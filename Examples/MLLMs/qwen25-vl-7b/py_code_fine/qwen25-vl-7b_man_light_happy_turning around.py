
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
    # Rotate the body parts around the head
    angle = frame * 2 * np.pi / 15  # 24 degrees per frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    new_positions = []
    for pos in positions:
        new_pos = np.dot(rotation_matrix, pos)
        new_positions.append(new_pos)
    positions = new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the positions
update(0)

# Animation function
def animate(frame):
    update(frame)
    points.set_data(*zip(*positions))
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=range(15), interval=100, blit=True)

# Show the animation
plt.show()
