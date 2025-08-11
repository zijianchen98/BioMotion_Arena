
import numpy as hnp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points' initial positions
positions = hnp.array([
    [0, 3], [0.5, 2.5], [1, 2], [1.5, 2.5], [2, 3],
    [0.5, 1.5], [1, 1], [1.5, 1.5], [1.25, 0.5],
    [1, 0], [1, -1], [0, -2], [2, -2], [0.5, -1.5], [1.5, -1.5]
])

fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-3, 4)
ax.set_facecolor('black')
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

def update(frame):
    # Create a motion for sitting down
    offset = frame / 50.0
    new_positions = positions.copy()
    new_positions[:, 1] -= offset
    if frame > 50:
        new_positions[:, 1] = positions[:, 1] - 1
        new_positions[[4, 8, 11, 12], 1] -= (frame - 50) / 50.0
    scat.set_offsets(new_positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.axis('off')
plt.show()
