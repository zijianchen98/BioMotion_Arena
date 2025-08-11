
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_lying_down():
    """
    Generates an animation of a happy woman lying down, represented by 15 white point lights.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = []
    for _ in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.3, 0.7)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

    def update(frame):
        """Updates the positions of the points for each frame."""
        for i in range(len(points)):
            angle = (frame / 20) % (2 * np.pi)  # Varying angle over time
            radius = 0.5 + 0.2 * np.sin(frame / 10) #Varying radius over time
            points[i][0] = radius * np.cos(angle)
            points[i][1] = radius * np.sin(angle)
            scat.set_offsets(points)
        return scat

    ani = animation.FuncAnimation(fig, update, frames=50, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_lying_down()
