
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_jump():
    """
    Generates an animation of a man jumping, represented by 15 moving point lights.

    The animation represents a simplified biomechanically plausible jump.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for _ in range(15):
        points.append(plt.Circle((0, 0), 0.2, color='white'))

    def update(frame):
        """
        Updates the positions of the point lights in each frame of the animation.
        """
        for i, point in enumerate(points):
            # Simulate jump trajectory - a parabola
            x = np.linspace(0, frame * 0.1, 100)  # Smoothness
            y = - (x**2) * 0.5 + 1  # Parabola for upward motion
            point.center = (x[49], y[49]) # Slightly delayed movement for realism

    ani = animation.FuncAnimation(fig, update, frames=60, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    animate_jump()
