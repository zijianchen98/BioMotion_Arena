
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Initialize point lights
points, = ax.plot([], [], 'o', color='white')

# Define the initial positions and velocities of the points
positions = np.random.rand(15, 2)
velocities = np.random.randn(15, 2) * 0.01

def update(frame):
    # Update positions
    positions += velocities
    # Bounce off the walls
    for i in range(2):
        hit_left = positions[:, i] < 0
        hit_right = positions[:, i] > 1
        positions[hit_left, i] = -positions[hit_left, i]
        positions[hit_right, i] = 2 - positions[hit_right, i]
        velocities[hit_left, i] = -velocities[hit_left, i]
        velocities[hit_right, i] = -velocities[hit_right, i]
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show plot
plt.show()
