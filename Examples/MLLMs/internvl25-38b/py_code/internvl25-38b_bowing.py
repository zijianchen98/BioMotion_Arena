
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

dots, = ax.plot([], [], 'wo', markersize=5)


def init():
    dots.set_data([], [])
    return dots,


def update(frame):
    points = [
        (0.5, 0.95),

        (0.45, 0.85), (0.55, 0.85),
        
        (0.4, 0.75), (0.5, 0.75), (0.6, 0.75),
        
        (0.475, 0.65), (0.525, 0.65),
        
        (0.4, 0.55), (0.5, 0.55), (0.6, 0.55),
        
        (0.45, 0.45), (0.55, 0.45),
        
        (0.5, 0.35),
    ]

    y_offset = np.sin(frame / 10.0) * 0.05

    new_points = [(x, y + y_offset) for x, y in points]
    x_data, y_data = zip(*new_points)
    dots.set_data(x_data, y_data)
    return dots,


ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=40)
plt.show()
