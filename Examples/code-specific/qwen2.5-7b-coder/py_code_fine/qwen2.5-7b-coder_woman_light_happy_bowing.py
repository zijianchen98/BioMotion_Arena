
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 60

# Define the initial positions of the points
positions = np.random.rand(num_points, 2)

# Define the velocity vectors for each point
velocities = np.random.randn(num_points, 2)
velocities /= np.linalg.norm(velocities, axis=1, keepdims=True)

# Define the acceleration vector for gravity
gravity = np.array([0, -0.1])

# Define the function to update the positions
def update(frame):
    global positions
    # Apply gravity
    velocities += gravity
    # Update positions
    positions += velocities
    # Wrap around the edges
    positions %= 1
    # Draw the points
    scatter.set_offsets(positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter([], [], color='white', s=10)

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
