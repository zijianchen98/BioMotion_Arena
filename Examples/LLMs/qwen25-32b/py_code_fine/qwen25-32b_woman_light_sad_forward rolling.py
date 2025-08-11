
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes

# Create a scatter plot for the points
scat = ax.scatter([], [], color='white')

# Define the initial positions of the points
positions = np.zeros((num_points, 2))

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate forward rolling motion
    t = frame / 100.0  # Time in seconds
    # Update positions based on some biomechanically plausible motion
    for i in range(num_points):
        positions[i][0] = 5 + 2 * np.sin(t * 10 + i * 2 * np.pi / num_points)
        positions[i][1] = 5 + 2 * np.cos(t * 10 + i * 2 * np.pi / num_points)
    
    scat.set_offsets(positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
