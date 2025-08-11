
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_RADIUS = 2
WHITE_COLOR = WHITE

# Define the subject and action
SUBJECT_X, SUBJECT_Y = 50, 50
SUBJECT_SPEED = 5
ACTION_X, ACTION_Y = 200, 100
ACTION_SPEED = 2

# Define the parameters
NUM_POINT_LIGHTS = 15
WHITE_COLOR_SATURATION = 0.5
WHITE_COLOR_LUMINANCE = 0.8

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize the axis
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Initialize the point lights
point_lights = []
for i in range(NUM_POINT_LIGHTS):
    angle = np.radians(i * 10)  # Convert angle to radians
    x = SUBJECT_X + np.cos(angle) * 150
    y = SUBJECT_Y + np.sin(angle) * 150
    ax.add_patch(plt.Circle((x, y), POINT_LIGHT_RADIUS, edgecolor=POINT_LIGHT_COLOR, facecolor=POINT_LIGHT_COLOR, alpha=0.8))
    point_lights.append(plt.Line2D([x, x], [y, y], color=POINT_LIGHT_COLOR, alpha=0.8, lw=2))

# Define the action
def animate(i):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    
    # Update the point lights
    for light in point_lights:
        light.set_xy((SUBJECT_X + np.cos(np.radians(i * 10)) * 150, 
                     SUBJECT_Y + np.sin(np.radians(i * 10)) * 150))
    
    # Update the subject
    ax.add_patch(plt.Circle((SUBJECT_X, SUBJECT_Y), POINT_LIGHT_RADIUS, edgecolor=POINT_LIGHT_COLOR, facecolor=POINT_LIGHT_COLOR, alpha=WHITE_COLOR_SATURATION))
    ax.add_patch(plt.Circle((ACTION_X, ACTION_Y), POINT_LIGHT_RADIUS, edgecolor=POINT_LIGHT_COLOR, facecolor=POINT_LIGHT_COLOR, alpha=WHITE_COLOR_SATURATION))
    
    # Update the action
    ax.add_patch(plt.Circle((ACTION_X, ACTION_Y), POINT_LIGHT_RADIUS, edgecolor=WHITE, facecolor=WHITE, alpha=WHITE_COLOR_LUMINANCE))
    
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')

ani = animation.FuncAnimation(fig, animate, frames=range(NUM_POINT_LIGHTS), interval=10)

plt.show()
