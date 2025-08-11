
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim((-10, 10)
ax.set_ylim((-10, 10))
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points (15 white points on a circle
points = np.array([np.cos(np.linspace(0, 2*np.pi, 15)), np.sin(np.linspace(0, 2*np.pi, 15)]).T
points = points * 5 + 5 # Move points slightly outwards

# Function to update the positions of the points
def update_points(i):
    # Update positions to simulate waving hand motion
    # This is a simplified example, adjust the math to better represent waving motion
    points[:, 0] = np.cos(np.linspace(i/4, i/4 + 2*np.pi/15, 15))
    points[:, 1] = np.sin(np.linspace(i/4, i/4 + 2*np.pi/15, 15))
    
    return points

# Create the animation
animation = FuncAnimation(fig, update_points, frames=np.arange(0, 100, interval=20)

# Show the animation
plt.show()

