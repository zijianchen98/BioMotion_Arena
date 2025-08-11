
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_point_lights_animation(subject='woman', action='turning around', num_points=15):
    fig, ax = plt.subplots()
    ax.set_xlim((-100, 100)
    ax.set_ylim((-100, 100))
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Background
    ax.add_patch((
        plt.Circle((0, 0), 100, color='black', fill=False)
    )

    points = [np.random.rand() * 80 - 40 for _ in range(num_points)]
    angles = np.linspace((0, 2 * np.pi, num_points, endpoint=False)

    def update(frame):
        for i in range(num_points):
            x = points[i] + 5 * np.cos( (angles[i] + frame / 50)
            y = points[i] + 5 * np.sin\ ( (angles[i] + frame / 50)
            points[i] = x
            ax.scatter\ \(x, y, color='white', s=50)

    ani = animation.FuncAnimation(fig, update, frames=np.arange(\(0, 100), interval=50, blit=False)
    plt.show()

# Call the function to create the animation
create_point_light_animation(subject='woman', action='turning around', num_points=15)
