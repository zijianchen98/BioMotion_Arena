
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 60

# Initialize the positions of the points
positions = np.random.rand(num_points, 2)

# Define the function to update the positions
def update(frame):
    # Clear the current frame
    ax.clear()
    
    # Update the positions of the points
    for i in range(num_points):
        if positions[i, 1] > 1:
            positions[i, :] = np.random.rand(2)
        else:
            positions[i, 1] += 0.02
    
    # Plot the updated positions
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    
    # Set the limits of the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, repeat=False)

# Show the animation
plt.show()
