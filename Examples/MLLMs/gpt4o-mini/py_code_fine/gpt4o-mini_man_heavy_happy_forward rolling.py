
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
plt.axis('off')

# Properties
num_points = 15
points = np.zeros((num_points, 2))

# Define initial positions of the point lights
# The positions form a rough human shape (head, shoulders, etc.)
initial_positions = np.array([[0, 1], [-0.5, 0.5], [0.5, 0.5], [-0.5, 0], [0.5, 0], 
                              [-0.5, -0.5], [0.5, -0.5], [-0.5, -1], [0.5, -1], 
                              [0, 1], [0, 0.5], [0, 0], [0, -0.5], [0, -1], [0, -1.5]])

# Set initial position
points = initial_positions.copy()

# Animation function
def update(frame):
    # Clear previous points
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_facecolor('black')
    plt.axis('off')
    
    # Forward rolling motion (simple translation with a slight rotation effect)
    rotation_angle = np.radians(frame) * 0.05
    rolling_shift = 0.05 * np.sin(np.radians(frame))

    # Update positions for rolling motion
    for i in range(num_points):
        x_shift = initial_positions[i, 0] + rolling_shift
        y_shift = initial_positions[i, 1] + (-frame * 0.05 + (i // 3) * 0.2)
        points[i] = [x_shift, y_shift]

    # Draw current points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create animation
anim = FuncAnimation(fig, update, frames=300, interval=20)
plt.show()
