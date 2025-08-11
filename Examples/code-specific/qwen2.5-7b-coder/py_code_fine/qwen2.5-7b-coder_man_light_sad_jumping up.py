
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points
num_points = 15
points = np.random.rand(num_points, 2) * 20 - 10

# Define the jump function
def jump(t):
    # Simple harmonic motion parameters
    amplitude = 4
    frequency = 0.5
    phase = t * frequency
    return amplitude * np.sin(phase)

# Update function for the animation
def update(frame):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Update the positions of the points
    for i in range(num_points):
        points[i, 1] += jump(frame / 100)
        if points[i, 1] > 10:
            points[i, 1] = -10
    
    # Draw the points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 2000), interval=50, blit=False)

# Show the animation
plt.show()
