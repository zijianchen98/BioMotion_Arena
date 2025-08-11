
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Define the initial positions of the points
initial_positions = np.random.rand(num_points, 2)

# Define the speed and direction of each point
speeds = np.random.uniform(0.1, 0.5, num_points)
directions = np.random.uniform(-np.pi, np.pi, num_points)

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot for the points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

def update(frame):
    # Update the positions of the points based on their speeds and directions
    initial_positions += speeds * np.array([np.cos(directions), np.sin(directions)])
    
    # Wrap around the edges of the screen
    initial_positions %= 1
    
    # Update the scatter plot
    points.set_offsets(initial_positions)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
