
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters
N_POINTS = 1000
N_LIGHTS = 15
WIDTH, HEIGHT = 800, 600

# Define the subject's parameters
SUBJECT_X, SUBJECT_Y = 100, 100
SUBJECT_Z = 50

# Define the action parameters
ACTION_X, ACTION_Y = 300, 300
ACTION_Z = 150

# Define the movement parameters
MOVEMENT_SPEED = 0.1

# Define the point-light parameters
LIGHT_SPAWN_RATE = 10
LIGHT_SPEED = 2
LIGHT_COUNT = LIGHT_SPAWN_RATE * 10

# Create a 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Initialize the point-lights
light_positions = np.random.rand(N_LIGHTS, 3)
light_colors = np.random.rand(N_LIGHTS, 3)

# Initialize the subject's position
subject_position = np.array([SUBJECT_X, SUBJECT_Y, SUBJECT_Z])

# Initialize the action's position
action_position = np.array([ACTION_X, ACTION_Y, ACTION_Z])

# Initialize the movement
movement = np.zeros((N_POINTS, 3))

# Initialize the animation
def animate(i):
    global movement
    global light_positions
    global light_colors
    global subject_position
    global action_position
    
    # Update the subject's position
    subject_position[0] += MOVEMENT_SPEED * i
    if subject_position[0] > WIDTH:
        subject_position[0] = WIDTH
        subject_position[1] = HEIGHT
    
    # Update the action's position
    action_position[0] += MOVEMENT_SPEED * i
    if action_position[0] > WIDTH:
        action_position[0] = WIDTH
        action_position[1] = HEIGHT
    
    # Update the light positions
    light_positions = np.random.rand(N_LIGHTS, 3)
    light_colors = np.random.rand(N_LIGHTS, 3)
    
    # Update the movement
    movement = np.zeros((N_POINTS, 3))
    for i in range(N_POINTS):
        movement[i] = np.array([np.random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED), np.random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED), np.random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)])
        movement[i] += np.array([MOVEMENT_SPEED, MOVEMENT_SPEED, MOVEMENT_SPEED]) * i / (N_POINTS - 1)
    
    # Update the light positions
    light_positions = np.roll(light_positions, -1, axis=0)
    light_positions = np.vstack((light_positions, light_positions[1:]))
    light_positions = light_positions[:N_LIGHTS]
    
    # Update the light colors
    light_colors = np.roll(light_colors, -1, axis=0)
    light_colors = np.vstack((light_colors, light_colors[1:]))
    light_colors = light_colors[:N_LIGHTS]
    
    # Plot the scene
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_zlim(0, HEIGHT)
    ax.set_title(f'Subject: {SUBJECT_X}, {SUBJECT_Y}, {SUBJECT_Z}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Plot the subject
    ax.scatter(subject_position[0], subject_position[1], subject_position[2], c='r', s=10, alpha=0.5)
    
    # Plot the action
    ax.scatter(action_position[0], action_position[1], action_position[2], c='g', s=10, alpha=0.5)
    
    # Plot the lights
    for i in range(N_LIGHTS):
        light = plt.Line2D([0, WIDTH], [0, HEIGHT], color=light_colors[i, :3], alpha=0.1, label=f'Light {i+1}')
        ax.plot([light_positions[i, 0], light_positions[i+1, 0]], [light_positions[i, 1], light_positions[i+1, 1]], [light_positions[i, 2], light_positions[i+1, 2]], color=light_colors[i, :3], lw=1)
    
    plt.legend()
    plt.show()
    
ani = animation.FuncAnimation(fig, animate, interval=10)

plt.show()
