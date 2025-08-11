
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the subject's position and velocity
SUBJECT_X, SUBJECT_Y = WIDTH // 2, HEIGHT // 2
SUBJECT_VX, SUBJECT_VY = 0, 0

# Define the action's position and velocity
ACTION_X, ACTION_Y = 200, 200
ACTION_VX, ACTION_VY = 0, 0

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the figure with a solid black background
ax.set_facecolor(BLACK)

# Initialize the point-lights
point_lights = []
for i in range(15):
    angle = np.linspace(0, 2 * np.pi, 100)
    x = SUBJECT_X + SUBJECT_VX * i + 50 * np.cos(angle)
    y = SUBJECT_Y + SUBJECT_VY * i + 50 * np.sin(angle)
    point_lights.append(ax.add_patch(plt.Circle((x, y), 2, edgecolor='black', facecolor='white', alpha=0.5)))

# Function to update the plot
def update(frame):
    global SUBJECT_VX, SUBJECT_VY, ACTION_VX, ACTION_VY
    SUBJECT_VX += 0.01
    SUBJECT_VY += 0.01
    ACTION_VX += 0.01
    ACTION_VY += 0.01

    # Update the point-lights
    for i, point in enumerate(point_lights):
        x = SUBJECT_X + SUBJECT_VX * i + 50 * np.cos(frame * 2 * np.pi / 100)
        y = SUBJECT_Y + SUBJECT_VY * i + 50 * np.sin(frame * 2 * np.pi / 100)
        point.center = (x, y)
        point.set_alpha(0.5)

    # Update the action's position and velocity
    ACTION_VX += 0.01
    ACTION_VY += 0.01
    if ACTION_VX > 10 or ACTION_VX < -10:
        ACTION_VX *= -1
    if ACTION_VY > 10 or ACTION_VY < -10:
        ACTION_VY *= -1

    # Clear the previous frame
    ax.clear()

    # Draw the point-lights
    ax.add_patch(plt.Circle((SUBJECT_X, SUBJECT_Y), 2, edgecolor='black', facecolor='white', alpha=0.5))
    ax.add_patch(plt.Circle((ACTION_X, ACTION_Y), 2, edgecolor='black', facecolor='white', alpha=0.5))

    # Update the plot
    plt.draw()
    plt.pause(0.01)

# Animate the subject and action
ani = animation.FuncAnimation(fig, update, frames=100, interval=16, repeat=True)

plt.show()
