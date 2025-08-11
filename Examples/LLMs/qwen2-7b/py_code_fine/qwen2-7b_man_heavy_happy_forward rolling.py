
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def forward_rolling_animation():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Define the initial position of the points
    points = np.array([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
                        [4-1, 1], [4-2, 2], [4-3, 3], [4-4, 4],
                        [4-5, 4], [4-4, 3], [4-3, 2], [4-2, 1], [4-1, 0]])

    def update(frame):
        global points
        for i in range(len(points)):
            points[i][0] += 0.1 * np.sin(((i+frame)/20)
            points[i][1] += 0.1 * np.cos(((i+frame)/20))

        # Remove the first point if it goes out of bounds
        if points[0][0] > 10 or points[0][0] < -10:
            points = np.delete(points, 0, axis=0)

        ax.clear()
        ax.plot(points[:, 0], points[:, 1], 'o', color='white')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
        ax.set_facecolor('black')

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 400), interval=20, repeat=False)
    plt.show()

forward_rolling_animation()
