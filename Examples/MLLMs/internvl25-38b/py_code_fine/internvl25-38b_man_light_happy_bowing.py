
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the happyman bowing pose
def bowing():
    points = np.array([
        [0.0, 1.0],  # Head
        [-0.2, 0.8], [0.2, 0.8],  # Shoulders
        [-0.3, 0.6], [-0.1, 0.6], [0.1, 0.6], [0.3, 0.6],  # Chest
        [-0.4, 0.4], [0.4, 0.4],  # Hips
        [-0.5, 0.2], [-0.3, 0.2], [-0.1, 0.2], [0.1, 0.2], [0.3, 0.2], [0.5, 0.2]  # Legs
    ])
    points[:, 1] -= 0.5  # Bowing effect
    return points

# Create Figure and Axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], c='white', s=50)

# Animation function
def animate(frame):
    if frame % 2 == 0:
        points = bowing()
        scat.set_offsets(points)
        return [scat]

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=2, interval=500, blit=True)

# Show plot
plt.show()
