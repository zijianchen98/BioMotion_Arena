
import numpy as np
import matplotlib.pyplot as plt

# Define the positions and movements of the point-lights
num_lights = 15
positions = np.array([
    [10, 20], [15, 15], [25, 15], [35, 20], [40, 15],
    [45, 20], [35, 10], [25, 10], [15, 10],
    [5, 5], [15, 5], [25, 5], [35, 5], [45, 5], [55, 5]
])
times = np.linspace(0, 2 * np.pi, 1000, endpoint=False)
motion = np.column_stack([np.sin(times) * 5, np.cos(times) * 5])

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)

# Plot the initial positions as small red circles
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=50, c='red', alpha=1)

# Define the update function for the animation
def update(frame):
    scatter.set_offsets(positions + motion * frame)
    return scatter,

# Animate the figure
ani = matplotlib.animation.FuncAnimation(fig, update, frames=times, blit=True, interval=50)
plt.show()
