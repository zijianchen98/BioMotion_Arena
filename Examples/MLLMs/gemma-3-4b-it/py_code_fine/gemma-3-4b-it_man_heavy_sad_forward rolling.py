
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_forward_roll():
    """
    Generates a point-light animation of a sadman performing a forward roll.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    points = 15
    lights = []
    for _ in range(points):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.3, 0.7)
        lights.append([radius * np.cos(angle), radius * np.sin(angle)])

    light_circles = []
    for light in lights:
        circle = plt.Circle(light, radius=0.03, color='white')
        light_circles.append(circle)
        ax.add_patch(circle)

    def animate(frame):
        """
        Animation function to update the position of the lights.
        """
        for i, light in enumerate(lights):
            # Simulate motion based on a simple rolling pattern
            x, y = light
            x_new = x + 0.01 * np.cos(frame * 5 + np.pi/2)
            y_new = y + 0.01 * np.sin(frame * 5 + np.pi/2)
            lights[i] = [x_new, y_new]

            # Update the circle's position
            light_circles[i].center = (lights[i][0], lights[i][1])

        return light_circles

    ani = animation.FuncAnimation(fig, animate, frames=100, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    sadman_forward_roll()
