
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SADMAN_X, SADMAN_Y = 400, 300
ACTION_X, ACTION_Y = 200, 300

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point lights
light1 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light2 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light3 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light4 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light5 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light6 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light7 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light8 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light9 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light10 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light11 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light12 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light13 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light14 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)
light15 = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=0.5)

# Function to update the plot
def update(frame):
    global SADMAN_X, SADMAN_Y, ACTION_X, ACTION_Y
    SADMAN_X += 0.01
    SADMAN_Y += 0.01
    ACTION_X += 0.01
    ACTION_Y += 0.01

    # Update the point lights
    light1.set_xdata([SADMAN_X, SADMAN_X + 10])
    light1.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light2.set_xdata([SADMAN_X, SADMAN_X + 10])
    light2.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light3.set_xdata([SADMAN_X, SADMAN_X + 10])
    light3.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light4.set_xdata([SADMAN_X, SADMAN_X + 10])
    light4.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light5.set_xdata([SADMAN_X, SADMAN_X + 10])
    light5.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light6.set_xdata([SADMAN_X, SADMAN_X + 10])
    light6.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light7.set_xdata([SADMAN_X, SADMAN_X + 10])
    light7.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light8.set_xdata([SADMAN_X, SADMAN_X + 10])
    light8.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light9.set_xdata([SADMAN_X, SADMAN_X + 10])
    light9.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light10.set_xdata([SADMAN_X, SADMAN_X + 10])
    light10.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light11.set_xdata([SADMAN_X, SADMAN_X + 10])
    light11.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light12.set_xdata([SADMAN_X, SADMAN_X + 10])
    light12.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light13.set_xdata([SADMAN_X, SADMAN_X + 10])
    light13.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light14.set_xdata([SADMAN_X, SADMAN_X + 10])
    light14.set_ydata([SADMAN_Y, SADMAN_Y + 10])
    light15.set_xdata([SADMAN_X, SADMAN_X + 10])
    light15.set_ydata([SADMAN_Y, SADMAN_Y + 10])

    # Update the plot
    ax.clear()
    ax.set_xlim(-WIDTH, WIDTH)
    ax.set_ylim(-HEIGHT, HEIGHT)
    ax.set_aspect('equal')
    ax.add_patch(plt.Rectangle((SADMAN_X, SADMAN_Y), 10, 10, fill=False, color=WHITE))
    ax.add_patch(plt.Rectangle((ACTION_X, ACTION_Y), 10, 10, fill=False, color=WHITE))
    ax.add_patch(plt.Rectangle((SADMAN_X - 10, SADMAN_Y - 10), 10, 10, fill=False, color=WHITE))
    ax.add_patch(plt.Rectangle((SADMAN_X + 10, SADMAN_Y - 10), 10, 10, fill=False, color=WHITE))
    ax.add_patch(plt.Rectangle((ACTION_X + 10, ACTION_Y - 10), 10, 10, fill=False, color=WHITE))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=16)

# Display the animation
plt.show()
