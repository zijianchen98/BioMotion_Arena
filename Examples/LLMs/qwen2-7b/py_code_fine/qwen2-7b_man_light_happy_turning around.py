
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    # Clear previous frame
    ax.clear()

    # Set up the scene
    ax.set_xlim((-40, 40)
    ax.set_ylim((-40, 40))
    ax.set_title('Happy Man Animation')
    ax.set_facecolor('#000000')  # Black background

    # Happy Man's
    happy_man = [(10, 10), (-10, 10), (-10, -10), (10, -10)]
    for point in happy_man:
        ax.scatter(point[0], point[1], c='white', s=100)

    # Action: Turning around
    angle = i * 2 * np.pi / 15
    happy_man_rotated = [(np.cos(angle) * x + np.sin(angle) * y,
                          -np.sin(angle) * x + np.cos(angle) * y)
                         for x, y in happy_man]
    for point in happy_man_rotated:
        ax.scatter(point[0], point[1], c='white', s=100)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=15, interval=50)
plt.show()
