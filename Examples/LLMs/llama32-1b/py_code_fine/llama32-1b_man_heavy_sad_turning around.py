
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
SADMAN_X, SADMAN_Y = WIDTH // 2, HEIGHT // 2
ACTION_X, ACTION_Y = WIDTH // 2 - 50, HEIGHT // 2 - 50
TURNING_SPEED = 2

# Define point light positions
POINT_LIGHTS = [
    (SADMAN_X, SADMAN_Y, 100),
    (SADMAN_X - 100, SADMAN_Y, 100),
    (SADMAN_X - 200, SADMAN_Y, 100),
    (SADMAN_X, SADMAN_Y - 100, 100),
    (SADMAN_X + 100, SADMAN_Y - 100, 100),
    (SADMAN_X + 200, SADMAN_Y - 100, 100),
]

# Define point light angles
POINT_LIGHTAngles = np.linspace(0, 2 * np.pi, 15)

# Create a 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim(-WIDTH // 2, WIDTH // 2)
ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)
ax.set_zlim(-HEIGHT // 2, HEIGHT // 2)

# Initialize point light positions and angles
point_light_positions = np.zeros((len(POINT_LIGHTAngles), 3))
point_light_angles = np.zeros((len(POINT_LIGHTAngles), 3))

# Set initial point light positions
for i, angle in enumerate(POINT_LIGHTAngles):
    point_light_positions[i, 0] = SADMAN_X + np.cos(angle) * 100
    point_light_positions[i, 1] = SADMAN_Y + np.sin(angle) * 100
    point_light_positions[i, 2] = 100

# Animation loop
while True:
    # Clear previous frame
    ax.clear()

    # Set axis limits
    ax.set_xlim(-WIDTH // 2, WIDTH // 2)
    ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)
    ax.set_zlim(-HEIGHT // 2, HEIGHT // 2)

    # Plot point lights
    for i, (x, y, z) in enumerate(point_light_positions):
        ax.scatter(x, y, z, color=WHITE_COLOR, s=10)

    # Plot sadman
    ax.scatter(ACTION_X, ACTION_Y, 50, color=BLACK_COLOR, s=50)

    # Plot action
    ax.plot([ACTION_X, SADMAN_X], [ACTION_Y, SADMAN_Y], [0, 0], color=BLACK_COLOR, linewidth=2)

    # Update point light positions and angles
    point_light_positions[:, 0] += TURNING_SPEED
    point_light_angles[:, 0] += 0.01

    # Set point light positions and angles for next frame
    point_light_positions[:, 0] = np.clip(point_light_positions[:, 0], -WIDTH // 2, WIDTH // 2)
    point_light_angles[:, 0] = np.clip(point_light_angles[:, 0], 0, 2 * np.pi)

    # Display the animation
    plt.pause(0.02)
