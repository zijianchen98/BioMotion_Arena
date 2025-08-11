
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(0, 2)
scatter = ax.scatter([], [], color='white', s=10)

standing_pos = [
    (0, 1.6), (0, 1.4), (-0.2, 1.4), (-0.15, 1.0), (-0.15, 0.6),
    (0.2, 1.4), (0.15, 1.0), (0.15, 0.6), (0, 1.0), (-0.1, 0.8),
    (-0.1, 0.4), (-0.1, 0.0), (0.1, 0.8), (0.1, 0.4), (0.1, 0.0)
]

tucked_pos = [
    (0, 0.8), (0, 1.0), (-0.2, 1.0), (-0.25, 0.8), (-0.25, 0.6),
    (0.2, 1.0), (0.25, 0.8), (0.25, 0.6), (0, 0.8), (-0.1, 0.6),
    (-0.1, 0.8), (-0.1, 1.0), (0.1, 0.6), (0.1, 0.8), (0.1, 1.0)
]

T = 2.0
v = 1.6 / T

def x(t):
    return v * t

def update(t):
    c = (np.sin(np.pi * t / T)) ** 2
    world_pos = []
    for i in range(15):
        bx = (1 - c) * standing_pos[i][0] + c * tucked_pos[i][0]
        by = (1 - c) * standing_pos[i][1] + c * tucked_pos[i][1]
        theta = 2 * np.pi * t / T
        rx = bx * np.cos(theta) - (by - 1.0) * np.sin(theta)
        ry = bx * np.sin(theta) + (by - 1.0) * np.cos(theta)
        wx = rx + x(t)
        wy = ry + 1.0
        world_pos.append((wx, wy))
    scatter.set_offsets(world_pos)
    return scatter,

ani = FuncAnimation(fig, update, frames=np.linspace(0, T, 60), interval=1000/30, blit=True)
plt.show()
