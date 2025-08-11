
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_animation():
    """Generates a point-light animation of a man lying down."""

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for i in range(15):
        # Create random starting positions
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-0.8, 0.8)
        z = 0  # Start at the ground

        # Define the movement trajectory - this is crucial for biomechanical plausibility
        # Simulate lying down movement.  Simple example.
        theta = 2 * np.pi * i / 15  # Rotate around a vertical axis
        r = 0.6 + 0.2 * np.sin(2 * np.pi * i / 10) # Radius varies slightly
        points.append([x, y, z])
    
    light = plt.PointCollection(points, markersize=10, color='white')
    ax.add_collection(light)

    def animate(i):
        light.set_offsets(points[i:])
        return light,

    ani = animation.FuncAnimation(fig, animate, frames=15, repeat=True, blit=True)
    plt.show()

if __name__ == '__main__':
    generate_motion_animation()
