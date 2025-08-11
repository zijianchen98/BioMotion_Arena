
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
positions = np.random.rand(num_lights, 2)

# Define the speed of each point light
speeds = np.random.uniform(0.1, 0.3, num_lights)

# Define the direction of each point light
directions = np.random.randn(num_lights, 2)
directions /= np.linalg.norm(directions, axis=1, keepdims=True)

# Define the figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot for the point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=10)

def update(frame):
    global positions
    
    # Update the positions of the point lights
    positions += speeds * directions
    
    # Wrap around the edges of the screen
    positions %= 1
    
    # Set the data for the scatter plot
    scatter.set_offsets(positions)
    
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
