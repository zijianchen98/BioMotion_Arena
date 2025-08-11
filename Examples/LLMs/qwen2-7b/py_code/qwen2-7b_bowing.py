
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_bow():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_title('Biological Motion Animation: Man Bowing')
    ax.set_facecolor('black')

    # Create 15 white points
    points = np.random.rand((15, 2) * 20 - 10
    points = np.round(points).astype(int)

    def update(frame):
        for i in range(15):
            points[i] += [np.sin(frame * 0.1 + i * 0.02), np.cos(frame * 0.1 + i * 0.02)]
            points[i] %= 20
            points[i] -= np.floor(points[i])
            if frame % 5 == 0:
                ax.plot(points[i][0], points[i][1], 'w.')
        return []

    ani = animation.FuncAnimation(fig, update, frames=range( (60), interval=50, blit=True)
    plt.show()

animate_bow()
