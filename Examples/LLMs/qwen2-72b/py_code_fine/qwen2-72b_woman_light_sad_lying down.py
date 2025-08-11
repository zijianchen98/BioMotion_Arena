
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.axis('off')

# Create data points
np.random.seed(42)
n_points = 15
points = np.random.rand(n_points, 2) * [10, 10]

# Define initial positions and velocities
positions = points.copy()
velocities = np.random.randn(n_points, 2)

# Function to update the animation frame
def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities * 0.1
    
    # Keep points within bounds
    positions[positions < 0] = 0
    positions[positions > 10] = 10
    
    # Plot points
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show animation
plt.show()
