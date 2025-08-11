
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, 0],  # Right elbow
    [0, -1],  # Right wrist
    [-2, 0],  # Left elbow
    [0, -2],  # Left wrist
    [1, 1],  # Right hip
    [-1, 1],  # Left hip
    [2, 1],  # Right knee
    [0, 2],  # Right ankle
    [-2, 1],  # Left knee
    [0, 3],  # Left ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a wave-like motion for the hand
    positions[6][1] += 0.1 * np.sin(frame / 10)
    positions[7][1] += 0.1 * np.sin(frame / 10)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
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
ani = FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
