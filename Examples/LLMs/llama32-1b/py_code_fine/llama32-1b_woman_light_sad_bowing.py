
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
N_STEPS = 100
N_POINTS = 1000

# Define the parameters for the point-light stimulus
LIGHT_SIZE = 0.1
LIGHT_COLOR = (1, 1, 1)

# Define the parameters for the subject and action
SUBJECT_SIZE = 0.2
SUBJECT_COLOR = (0, 0, 0)
ACTION_COLOR = (1, 0, 0)

# Create a figure and axis object
fig, ax = plt.subplots()

# Initialize the axis with a solid black background
ax.set_facecolor('black')

# Initialize the point-light stimulus
light = plt.Line2D([], [], color=LIGHT_COLOR, lw=LIGHT_SIZE, zorder=10)
ax.add_artist(light)

# Initialize the subject and action
subject = plt.Line2D([], [], color=SUBJECT_COLOR, lw=SUBJECT_SIZE, zorder=10)
ax.add_artist(subject)

# Initialize the points for the subject and action
subject_points = np.zeros((N_POINTS, 2))
action_points = np.zeros((N_POINTS, 2))

# Initialize the animation
def animate(i):
    global subject_points, action_points

    # Move the subject and action points
    subject_points[:, 0] += 0.01 * np.random.uniform(-1, 1)
    subject_points[:, 1] += 0.01 * np.random.uniform(-1, 1)
    action_points[:, 0] += 0.01 * np.random.uniform(-1, 1)
    action_points[:, 1] += 0.01 * np.random.uniform(-1, 1)

    # Set the points to the current position
    subject_points[:, 0] = subject_points[:, 0] * 10 + 100
    subject_points[:, 1] = subject_points[:, 1] * 10 + 100
    action_points[:, 0] = action_points[:, 0] * 10 + 100
    action_points[:, 1] = action_points[:, 1] * 10 + 100

    # Clear the axis
    ax.clear()

    # Plot the points
    ax.scatter(subject_points[:, 0], subject_points[:, 1], color=SUBJECT_COLOR, zorder=10)
    ax.scatter(action_points[:, 0], action_points[:, 1], color=ACTION_COLOR, zorder=10)

    # Plot the point-light stimulus
    light.set_data([0, 0], [0, 0])
    light.set_color(LIGHT_COLOR)
    light.set_zorder(10)
    ax.add_artist(light)

    # Update the axis
    ax.set_facecolor('black')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')

ani = animation.FuncAnimation(fig, animate, frames=N_STEPS, interval=50, blit=True, save_count=True)

plt.show()
