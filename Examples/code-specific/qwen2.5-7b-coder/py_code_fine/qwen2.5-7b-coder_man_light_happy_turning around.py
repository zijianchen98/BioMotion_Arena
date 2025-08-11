
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 60

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the positions of the points
positions = np.random.randn(num_points, 2)

# Function to update the positions of the points
def update(frame):
    # Clear the previous frame
    ax.clear()
    
    # Update the positions based on a simple rotation
    angle = frame * 2 * np.pi / frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    positions = np.dot(positions, rotation_matrix)
    
    # Normalize the positions to stay within the bounds [-1, 1]
    positions /= np.max(np.abs(positions))
    
    # Plot the updated positions
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)

# Show the animation
plt.show()
