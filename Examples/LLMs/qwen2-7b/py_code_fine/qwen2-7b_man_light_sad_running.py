
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_running():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    # Create 15 white point-lights
    points = [(np.random.uniform(-9, 1), np.random.uniform(-9, 1)) for _ in range( (15)]
    scat = ax.scatter(*zip(*points), color='white', s=100)

    def update(frame):
        global points
        for i, ( in enumerate(points):
            dx = np.sin(np.pi * frame / 40)
            dy = np.cos(np.pi * frame / 40)
            points[i] = (points[i][0] + dx, points[i][1] + dy
        scat.set_offsets(points)
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=np.arange((0, 800),
                                   interval=50, blit=True)
    plt.show()

if __name__ == "__main__":
    sadman_running()
