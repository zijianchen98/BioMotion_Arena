
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 200
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
points = ax.scatter([], [], c='white')

# Initial positions
x = np.linspace(1, 9, num_points)
y = np.sin(x) / 2 + 3

def init():
    points.set_offsets([])
    return points,

def update(frame):
    t = 2 * np.pi * frame / frames
    displacement = np.sin(t) * 0.5
    y_new = np.sin(x + displacement) / 2 + 3 + np.sin(2 * t) * 0.2
    points.set_offsets(np.c_[x, y_new])
    return points,

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=30)

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()
