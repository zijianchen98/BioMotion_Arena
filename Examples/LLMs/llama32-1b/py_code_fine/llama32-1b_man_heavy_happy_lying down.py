
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1.0, 1.0, 1.0)
BLACK_COLOR = (0.0, 0.0, 0.0)
HUMAN_SIZE = 50
MAN_SIZE = 100

# Create a new figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the point light source
def point_light(x, y, z, intensity):
    return np.array([x, y, z]) + np.array([0, 0, 0]) * intensity

# Define the human pose
def human_pose(x, y, z):
    return np.array([x, y, z]) - np.array([MAN_SIZE // 2, MAN_SIZE // 2, MAN_SIZE // 2])

# Define the animation function
def animate(frame):
    global ax
    ax.clear()

    # Define the human pose at each frame
    pose = human_pose(WIDTH / 2, HEIGHT / 2, 0)

    # Calculate the position of the point light source
    light_position = point_light(pose[0], pose[1], pose[2], 0.5)

    # Draw the human pose
    ax.scatter(pose[0], pose[1], pose[2], color=WHITE_COLOR, s=10, c='b')

    # Draw the point light source
    ax.scatter(light_position[0], light_position[1], light_position[2], color=WHITE_COLOR, s=100, c='w')

    # Animate the point light source
    ax.set_xlim(-WIDTH // 2, WIDTH // 2)
    ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)
    ax.set_zlim(-HEIGHT // 2, HEIGHT // 2)
    ax.set_axis_off()

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
