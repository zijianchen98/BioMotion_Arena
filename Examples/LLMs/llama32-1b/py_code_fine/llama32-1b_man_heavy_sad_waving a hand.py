
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HUMAN_SIZE = 0.5  # in pixels

# Define human pose parameters
POSE = {
    'head': {'x': 0, 'y': 0},
    'torso': {'x': 200, 'y': 0, 'z': 200},
    'left_arm': {'x': 100, 'y': 0, 'z': 200, 'w': 0.5},
    'right_arm': {'x': 400, 'y': 0, 'z': 200, 'w': -0.5},
    'left_leg': {'x': 200, 'y': 200, 'z': 100, 'w': 0.5},
    'right_leg': {'x': 400, 'y': 200, 'z': 100, 'w': -0.5},
    'left_hand': {'x': 200, 'y': 300, 'z': 100, 'w': 0.5},
    'right_hand': {'x': 400, 'y': 300, 'z': 100, 'w': -0.5}
}

# Define camera parameters
CAMERA = {
    'x': 0,
    'y': 0,
    'z': 200,
    'w': 0,
    'h': 1
}

# Define animation parameters
ANIMATION = {
    'frames': 15,
    'duration': 30,
    'fps': 30
}

# Define lighting parameters
LIGHTING = {
    'intensity': 1,
    'color': WHITE
}

# Function to calculate the position of the point light at time t
def calculate_light_position(t):
    return LIGHTING['x'] + t * LIGHTING['w'], LIGHTING['y'] + t * LIGHTING['h'], LIGHTING['z'] + t * LIGHTING['z']

# Function to calculate the direction of the point light at time t
def calculate_light_direction(t):
    return np.array([LIGHTING['x'] - LIGHTING['x'], LIGHTING['y'] - LIGHTING['y'], LIGHTING['z'] - LIGHTING['z']]) / LIGHTING['w']

# Function to update the plot
def update(frame):
    global pose, camera, lighting, animation, light_position, light_direction

    # Calculate the position of the point light at time t
    t = frame / ANIMATION['duration']
    light_position = calculate_light_position(t)

    # Calculate the direction of the point light at time t
    light_direction = calculate_light_direction(t)

    # Update the plot
    fig.clear()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*pose['head']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['torso']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['left_arm']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['right_arm']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['left_leg']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['right_leg']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['left_hand']['x:z'], s=100, color=BLACK)
    ax.scatter(*POSE['right_hand']['x:z'], s=100, color=BLACK)

    # Update the camera position
    camera['x'] = WIDTH / 2
    camera['y'] = HEIGHT / 2

    # Update the lighting parameters
    light_position = calculate_light_position(frame)
    light_direction = calculate_light_direction(frame)

    # Update the plot
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    ax.set_zlim(-HEIGHT / 2, HEIGHT / 2)
    ax.view_init(elev=45, azim=0)

    return ax,

# Create the plot
fig, ax = plt.subplots()

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=ANIMATION['frames'], interval=ANIMATION['duration'] / 1000, blit=True)

# Show the plot
plt.show()
