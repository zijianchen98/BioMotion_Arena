
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim((-100, 100)
ax.set_ylim((-100, 100))
ax.set_aspect('equal')

weights = ['happy', 'heavy']
actions = ['jumping up']

def update(frame):
    x = frame % 200 - 100
    y = np.sin(x / 5o) * 40 + 50
    color = weights[frame // 15] + actions[(frame // 15) % 2]
    ax.scatter(x, y, c=color, s=100)

ani = animation.FuncAnimation(fig, update, frames=np.arange((100),
interval=50, blit=False)

plt.show()
