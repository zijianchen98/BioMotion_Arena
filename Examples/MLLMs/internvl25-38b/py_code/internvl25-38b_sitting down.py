
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the frames for the sitting down motion
frames = [
    [3, 1, 0, 7, 8, 0, 9, 10, 11, 12, 13, 14],
    [2, 2, 0, 6, 9, 1, 8, 11, 12, 13, 14, 15],
    [1, 3, 0, 5, 10, 2, 7, 12, 13, 14, 15, 16],
    [0, 4, 1, 4, 11, 3, 6, 13, 14, 15, 16, 17],
    [0, 5, 2, 3, 12, 4, 5, 14, 15, 16, 17, 18],
    [0, 6, 3, 2, 13, 5, 4, 15, 16, 17, 18, 19],
    [0, 7, 4, 1, 14, 6, 3, 16, 17, 18, 19, 20],
    [0, 8, 5, 0, 15, 7, 2, 17, 18, 19, 20, 21],
    [0, 9, 6, 1, 16, 8, 1, 18, 19, 20, 21, 22],
    [0, 10, 7, 2, 17, 9, 0, 19, 20, 21, 22, 23],
    [0, 11, 8, 3, 18, 10, 1, 20, 21, 22, 23, 24],
    [0, 12, 9, 4, 19, 11, 2, 21, 22, 23, 24, 25],
    [0, 13, 10, 5, 20, 12, 3, 22, 23, 24, 25, 26],
    [0, 14, 11, 6, 21, 13, 4, 23, 24, 25, 26, 27],
    [0, 15, 12, 7, 22, 14, 5, 24, 25, 26, 27, 28],
    [0, 16, 13, 8, 23, 15, 6, 25, 26, 27, 28, 29],
]

fig, ax = plt.subplots()
ax.set_xlim(0, 25)
ax.set_ylim(0, 25)
ax.set_facecolor('black')

points, = ax.plot([], [], 'wo')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    x = frame[:12]
    y = frame[12:]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, repeat=True, interval=100)

plt.show()
