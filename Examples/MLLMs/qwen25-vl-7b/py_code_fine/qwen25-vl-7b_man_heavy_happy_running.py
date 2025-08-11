
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happyman running
positions = [
    [0.5, 0.5], [0.4, 0.6], [0.6, 0.6], [0.7, 0.5], [0.8, 0.4],
    [0.9, 0.5], [0.8, 0.6], [0.7, 0.7], [0.6, 0.6], [0.5, 0.5],
    [0.5, 0.4], [0.6, 0.3], [0.7, 0.4], [0.8, 0.3], [0.9, 0.4]
]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Plot the initial position of the points
points, = ax.plot(*zip(*positions), 'o', color='white')

def update(frame):
    # Update the positions of the points
    positions[frame % len(positions)] = [np.random.uniform(0.4, 0.6), np.random.uniform(0.3, 0.5)]
    points.set_data(*zip(*positions))
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Save the animation as a GIF
ani.save('happyman_running.gif', writer='imagemagick')
plt.show()
