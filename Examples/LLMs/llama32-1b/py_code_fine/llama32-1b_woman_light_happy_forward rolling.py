
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

# Define the subject's pose
pose = {
    'x': 100,
    'y': 100,
    'z': 100,
    'roll': 0,
    'pitch': 0,
    'yaw': 0
}

# Define the action
action = {
    'forward': 0.5,
    'roll': 0.2,
    'pitch': 0.1,
    'yaw': 0.1
}

def create_point_light(position, color):
    """Create a point light at the specified position with the given color."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(position[0], position[1], position[2], c=color, s=10, alpha=0.5)
    return fig, ax

def animate(frame):
    global pose, action
    pose['x'] += action['roll'] * 0.01
    pose['y'] += action['pitch'] * 0.01
    pose['z'] += action['yaw'] * 0.01
    ax.clear()
    fig, ax = create_point_light((pose['x'], pose['y'], pose['z']), WHITE)
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_zlim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.draw()
    plt.pause(0.01)

ani = animation.FuncAnimation(WIDTH, HEIGHT, frame=animate, interval=16)

plt.show()
