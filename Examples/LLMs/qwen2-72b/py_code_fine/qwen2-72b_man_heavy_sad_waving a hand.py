
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Number of points
num_points = 15

# Initial positions and velocities
positions = np.random.rand(num_points, 2)
velocities = np.random.randn(num_points, 2)

# Create scatter plot for points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities * 0.1
    # Keep points within the plot area
    positions %= 1
    # Update scatter plot data
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)

# Show animation
plt.show()
