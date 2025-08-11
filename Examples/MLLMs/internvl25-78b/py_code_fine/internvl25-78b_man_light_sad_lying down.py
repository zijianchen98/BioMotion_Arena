
import numpy as a
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Keyframe positions for the sadman lying down
positions = [
    [0, 5], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 6], [2, 7],
    [3, 3], [3, 4], [3, 6], [3, 7], [4, 4], [4, 5], [4, 6]
]

fig, ax = plt.subplots()
ax.set_xlim(-1, 6)
ax.set_ylim(2, 8)
scat = ax.scatter([], [], s=50, color='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    offset = positions[frame % len(positions)]
    scat.set_offsets(offset)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=60, init_func=init, blit=True, interval=100)

plt.axis('off')
plt.show()
