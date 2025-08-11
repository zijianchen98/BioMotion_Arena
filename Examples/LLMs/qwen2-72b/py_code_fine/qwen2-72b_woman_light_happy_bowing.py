
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the initial positions and velocities of the 15 point-lights
np.random.seed(0)
positions = np.random.uniform(-1, 1, (15, 2))
velocities = np.random.uniform(-0.05, 0.05, (15, 2))

# Function to update the positions of the points for each frame
def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities
    # Ensure the points remain within the bounds
    positions = np.clip(positions, -1, 1)
    # Update the scatter plot
    scat.set_offsets(positions)
    return scat,

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')  # Set background color to black
plt.axis('off')  # Hide axes

# Create a scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True, interval=40)

# Show the animation
plt.show()
