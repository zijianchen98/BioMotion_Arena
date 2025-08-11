
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Number of points
num_points = 15

# Create random initial positions and velocities
np.random.seed(0)
positions = np.random.rand(num_points, 2) * 100
velocities = np.random.randn(num_points, 2)

# Function to update the animation frame
def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities
    
    # Keep the points within the screen boundaries
    positions %= 100
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)
    
    # Set the axis limits
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
