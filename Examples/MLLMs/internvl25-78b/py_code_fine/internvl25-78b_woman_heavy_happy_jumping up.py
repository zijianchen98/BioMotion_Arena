
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Number of points
num_points = 15
points = np.random.rand(num_points, 2)

# Initial positions
positions = np.array([
    [0.45, 0.40],
    [0.55, 0.40],
    [0.40, 0.45],
    [0.60, 0.45],
    [0.45, 0.50],
    [0.55, 0.50],
    [0.40, 0.55],
    [0.60, 0.55],
    [0.45, 0.60],
    [0.55, 0.60],
    [0.50, 0.65],
    [0.40, 0.70],
    [0.60, 0.70],
    [0.45, 0.75],
    [0.55, 0.75]
])

scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

def update(frame):
    amplitude = 0.05
    offset = 0.02
    phase_shift = frame * 0.1

    # Update positions to simulate jumping
    positions[:, 1] = positions[:, 1] + amplitude * np.sin(frame * 0.1 + phase_shift) + offset

    # Boundary conditions
    positions[:, 1] = np.clip(positions[:, 1], 0.4, 0.8)

    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
