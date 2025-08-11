
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Right hip
    [0, -3],  # Left knee
    [2, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4]   # Right ankle
]

# Define the initial and final positions for the sadwoman turning around
initial_positions = np.array(positions)
final_positions = np.array(positions)

# Function to update the positions of the points
def update(frame):
    global positions
    positions = (initial_positions + final_positions * frame / 10) % 4

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the positions
update(0)

# Animation function
def animate(frame):
    update(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 10, 100), interval=50, blit=True)

# Display the animation
plt.show()
