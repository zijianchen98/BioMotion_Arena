
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_sadman_bowing():
    """
    Generates a point-light animation of a sadman bowing.
    """

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_facecolor('black')
    ax.axis('off')

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(1, 3)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white', marker='o')

    def update(frame):
        """
        Updates the point positions for each frame of the animation.
        """
        for i, point in enumerate(points):
            x, y = point
            # Bowing motion simulation (simplified)
            dx = -0.02 * np.sin(frame * 0.1)
            dy = 0.03 * np.cos(frame * 0.1)
            points[i][0] += dx
            points[i][1] += dy

            # Keep points within the bounds
            points[i][0] = max(-20, min(20, points[i][0]))
            points[i][1] = max(-20, min(20, points[i][1]))

        scat.set_offsets(points)
        return scat

    ani = animation.FuncAnimation(fig, update, frames=30, interval=50, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_sadman_bowing()
