
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial positions and velocities for the point-lights
positions = np.array([
    [0.3, 0.1], [0.6, 0.1], [0.45, 0.2], [0.55, 0.2],
    [0.4, 0.3], [0.45, 0.4], [0.55, 0.4], [0.5, 0.5],
    [0.35, 0.6], [0.45, 0.6], [0.55, 0.6], [0.65, 0.6],
    [0.3, 0.8], [0.6, 0.8], [0.45, 0.9]
])
velocities = np.random.uniform(-0.005, 0.005, positions.shape)

# Function to update the positions
def update(num):
    global positions, velocities
    positions += velocities
    positions[positions < 0] -= 2 * positions[positions < 0]
    positions[positions > 1] -= 2 * (positions[positions > 1] - 1)
    scat.set_offsets(positions)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
plt.axis('off')

# Create scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50)

plt.show()
