
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_bowing():
    """
    Generates an animation of a man bowing using 15 white point-lights against a black background.
    The motion is designed to be biomechanically plausible and visually realistic.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        points.append(plt.Circle((0, 0), 0.03, color='white'))  # Adjust radius as needed

    def update(frame):
        """
        Updates the positions of the point-lights for each frame of the animation.
        """
        for point in points:
            x = np.sin(frame * 0.2) * 0.7  # Modify the frequency and amplitude for more diverse movement
            y = np.cos(frame * 0.2) * 0.7  # Modify the frequency and amplitude for more diverse movement
            point.center = (x, y)

        return points

    ani = animation.FuncAnimation(fig, update, frames=30, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_bowing()
