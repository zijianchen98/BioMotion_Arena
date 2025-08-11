
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the coordinates of the 15 points representing the sad woman
num_points = 15
points = np.zeros((num_points, 2))

# Set up the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def init():
    """Initialize the animation."""
    scat.set_offsets(points)
    return scat,

def update(frame):
    """Update function for each frame of the animation."""
    angle = np.radians(frame * 4)  # Rotate 4 degrees per frame
    
    # Simple rotation matrix
    c, s = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array(((c, -s), (s, c)))
    
    # Apply rotation to the points
    points_rotated = np.dot(points, rotation_matrix.T)
    scat.set_offsets(points_rotated)
    
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 90), init_func=init, blit=True)

plt.show()
