
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_SIZE = 2

# Define the happyman's pose
happyman_pose = {
    'x': WIDTH / 2,
    'y': HEIGHT / 2,
    'z': 0,
    'angle': np.pi / 4,
   'velocity': np.zeros(3)
}

# Define the action
action = {
    'x': 200,
    'y': 300,
    'z': 0,
    'angle': np.pi / 2,
   'velocity': np.zeros(3)
}

# Define the animation function
def animate(frame):
    global happyman_pose, action
    global happyman_x, happyman_y, happyman_z, action_x, action_y, action_z, action_angle, action_velocity

    # Update the happyman's pose
    happyman_pose['x'] += action['velocity'][0] * 0.01
    happyman_pose['y'] += action['velocity'][1] * 0.01
    happyman_pose['z'] += action['velocity'][2] * 0.01

    # Update the action
    action['x'] += action['velocity'][0] * 0.01
    action['y'] += action['velocity'][1] * 0.01
    action['z'] += action['velocity'][2] * 0.01

    # Update the happyman's angle
    action_angle += action['angle'] * 0.01

    # Update the happyman's velocity
    action_velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])

    # Ensure the action stays within the bounds of the screen
    action['x'] = max(0, min(action['x'], WIDTH))
    action['y'] = max(0, min(action['y'], HEIGHT))
    action['z'] = max(0, min(action['z'], HEIGHT))

    # Update the happyman's position
    happyman_x = happyman_pose['x'] + action['x']
    happyman_y = happyman_pose['y'] + action['y']
    happyman_z = happyman_pose['z'] + action['z']

    # Ensure the happyman stays within the bounds of the screen
    happyman_x = max(0, min(happyman_x, WIDTH))
    happyman_y = max(0, min(happyman_y, HEIGHT))
    happyman_z = max(0, min(happyman_z, HEIGHT))

    # Draw the point-lights
    fig, ax = plt.subplots()
    points = np.array([[happyman_x + POINT_SIZE * np.cos(action_angle), happyman_y + POINT_SIZE * np.sin(action_angle)],
                       [happyman_x + POINT_SIZE * np.cos(action_angle + np.pi / 2), happyman_y + POINT_SIZE * np.sin(action_angle + np.pi / 2)],
                       [happyman_x + POINT_SIZE * np.cos(action_angle + np.pi), happyman_y + POINT_SIZE * np.sin(action_angle + np.pi)]])
    ax.scatter(points[:, 0], points[:, 1], s=POINT_SIZE, c='w', alpha=0.5, zorder=0)
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_zlim(0, HEIGHT)
    ax.set_axis_off()

    # Clear the previous frame
    ax.clear()

    return ax,

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=100, interval=16)

# Show the animation
plt.show()
