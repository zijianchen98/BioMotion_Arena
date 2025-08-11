
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_positions(frame):
    positions = np.array([
        [0.0, 0.7],
        [-0.3, 0.5],
        [0.3, 0.5],
        [-0.5, 0.3],
        [0.5, 0.3],
        [-0.7, 0.1],
        [0.0, 0.1],
        [0.7, 0.1],
        [-0.5, -0.1],
        [0.0, -0.1],
        [0.5, -0.1],
        [-0.3, -0.3],
        [0.0, -0.3],
        [0.3, -0.3],
        [0.0, -0.5],
        [0.0, -0.7]
    ])

    amplitude = 0.1
    if frame % 2 == 0:
        positions[:, 1] += amplitude * np.sin(frame / 10)

    return positions

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
scat = ax.scatter([], [], s=100, color='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    positions = generate_positions(frame)
    scat.set_offsets(positions)
    return scat,

ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)
plt.show()
