
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Initialize positions
positions = np.random.rand(num_points, 2)

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Update function for animation
def update(frame):
    # Generate new random positions for each point
    new_positions = np.random.rand(num_points, 2)
    
    # Update the scatter plot
    scatter.set_offsets(new_positions)
    
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(100), interval=50, blit=True)

# Show the animation
plt.show()
