
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial positions of the point lights
initial_positions = np.array([
    [0, 3], [1, 3], [2, 3], [3, 3], [4, 3],
    [1, 2], [2, 2], [3, 2], [4, 2],
    [1, 1], [2, 1], [3, 1],
    [1, 0], [2, 0], [3, 0]
])

fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', ms=8)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    positions = initial_positions.copy()
    positions[:, 1] -= frame / 10.0  # Simulate lying down motion
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=30, init_func=init, blit=True, interval=50)

plt.axis('off')
plt.show()
