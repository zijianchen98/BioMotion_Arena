
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the subject's pose and action
POSE = {
    'x': 100,
    'y': 200,
    'z': 50,
    'angle': np.radians(30),
   'velocity': np.zeros(3)
}

# Define the action's pose and velocity
ACTION = {
    'x': 0,
    'y': 0,
    'z': 0,
    'angle': np.radians(90),
   'velocity': np.zeros(3)
}

# Define the light positions
LIGHTS = [
    {'x': 50, 'y': 50, 'z': 50},
    {'x': 150, 'y': 50, 'z': 50},
    {'x': 250, 'y': 50, 'z': 50},
    {'x': 350, 'y': 50, 'z': 50},
    {'x': 450, 'y': 50, 'z': 50},
    {'x': 500, 'y': 50, 'z': 50},
    {'x': 600, 'y': 50, 'z': 50},
    {'x': 650, 'y': 50, 'z': 50},
    {'x': 700, 'y': 50, 'z': 50},
    {'x': 750, 'y': 50, 'z': 50},
    {'x': 800, 'y': 50, 'z': 50}
]

def rotate_x(angle, x, y, z):
    """Rotate point (x, y, z) around x-axis by angle."""
    return x * np.cos(angle) - y * np.sin(angle), x * np.sin(angle) + y * np.cos(angle), z

def rotate_y(angle, x, y, z):
    """Rotate point (x, y, z) around y-axis by angle."""
    return x * np.cos(angle) + y * np.sin(angle), -x * np.sin(angle) + y * np.cos(angle), z

def rotate_z(angle, x, y, z):
    """Rotate point (x, y, z) around z-axis by angle."""
    return x * np.cos(angle) - y * np.sin(angle), x * np.sin(angle) + y * np.cos(angle), z

def create_point_light(position, color, intensity):
    """Create a point light at position with specified color and intensity."""
    light = {'x': position[0], 'y': position[1], 'z': position[2], 'color': color, 'intensity': intensity}
    return light

def animate(frame):
    globalPOSE, ACTION, LIGHTS

    # Update pose and velocity of subject
    POSE['x'] += ACTION['velocity'][0] * 0.01
    POSE['y'] += ACTION['velocity'][1] * 0.01
    POSE['z'] += ACTION['velocity'][2] * 0.01
    ACTION['x'] += POSE['velocity'][0] * 0.01
    ACTION['y'] += POSE['velocity'][1] * 0.01
    ACTION['z'] += POSE['velocity'][2] * 0.01

    # Update pose and velocity of subject
    POSE['x'] += 1
    POSE['y'] += 1
    POSE['z'] += 1

    # Update pose and velocity of subject
    POSE['x'] -= 1
    POSE['y'] -= 1
    POSE['z'] -= 1

    # Create point lights
    for light in LIGHTS:
        light['x'] = light['x'] + int(50 * np.sin(frame / 10))
        light['y'] = light['y'] + int(50 * np.cos(frame / 10))
        light['z'] = light['z'] + 50
        light['color'] = WHITE
        light['intensity'] = 100

    # Plot subject and point lights
    fig, ax = plt.subplots()
    ax.scatter(POSE['x'], POSE['y'], POSE['z'], color=WHITE, s=10)
    for light in LIGHTS:
        ax.scatter(light['x'], light['y'], light['z'], color=light['color'], s=5)
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_zlim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_aspect('equal')
    plt.show()

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=20)
plt.show()
