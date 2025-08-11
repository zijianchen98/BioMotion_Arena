
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Define initial positions and velocities for the points
num_points = 15
points = np.random.rand(num_points, 2)
velocities = np.random.uniform(-0.01, 0.01, size=(num_points, 2))

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    global points, velocities
    # Update positions based on velocities
    points += velocities
    # Keep points within the plot boundaries
    points[points > 1] -= 1
    points[points < 0] += 1
    # Update scatter plot data
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
