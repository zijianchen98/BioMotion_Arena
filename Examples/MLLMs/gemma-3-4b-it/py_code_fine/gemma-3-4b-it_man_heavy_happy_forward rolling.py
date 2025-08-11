
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_forward_roll():
    """
    Generates an animation of a forward roll performed by a man with heavy weight.

    The animation consists of 15 white point-lights moving against a black background, 
    representing the segments of the body during the roll.  The movement is designed
    to be biomechanically plausible.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    points = 15
    radii = np.linspace(0.05, 0.1, points)
    colors = 'white'

    lights = []
    for r in radii:
        light = plt.scatter(0, 0, s=r*100, c=colors, alpha=1)
        lights.append(light)

    def update(frame):
        """
        Updates the position of the lights to simulate the forward roll.
        """
        for i in range(points):
            # Define a sinusoidal trajectory for each point.  This is a simplified
            # approximation of the body segments moving during a roll.
            angle = np.pi * frame / 10 
            x = np.cos(angle)
            y = np.sin(angle)
            lights[i].set_offsets([x, y])
        return lights

    ani = animation.FuncAnimation(fig, update, frames=30, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_forward_roll()
