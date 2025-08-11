
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 7)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define initial positions of the point-lights representing a man
# This setup represents positions at rest
points = np.array([
    [0, 6],  # Head
    [-1, 5], [1, 5],  # Shoulders
    [-1, 4], [1, 4],  # Elbows
    [0, 3],  # Chest
    [-1, 2], [1, 2],  # Hips
    [0, 1],  # Knees
    [-1, 0], [1, 0],  # Feet
    [0, -1],  # Ankle
])

# Create specks for point-lights
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

# Function to update the animation
def update(frame):
    # Simple jumping motion
    jump_height = np.sin(frame / 10.0)  # Create a smooth jumping motion
    # Modify y position of points to simulate the jump
    new_y = points[:, 1] + jump_height
    scat.set_offsets(points[:, 0], new_y)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
