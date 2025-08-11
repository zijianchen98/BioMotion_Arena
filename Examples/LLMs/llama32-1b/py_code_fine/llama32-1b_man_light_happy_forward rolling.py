
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)  # White
MAN_SIZE = 20
MAN_SPEED = 2

# Define the happyman's body parts
BODY_PARTS = ['head', 'torso', 'left_arm', 'right_arm', 'left_leg', 'right_leg']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Define the point lights
lights = []
for i in range(15):
    light = plt.Line2D([0, WIDTH], [0, HEIGHT], color=LIGHT_COLOR, lw=1, alpha=0.5)
    ax.add_line(light)
    lights.append(light)

# Define the happyman's body parts
body_parts = [plt.Line2D([0, 0], [0, 0], color=WHITE, lw=5, alpha=0.5) for _ in range(6)]
body_parts.append(plt.Line2D([WIDTH, 0], [WIDTH, 0], color=WHITE, lw=5, alpha=0.5))
body_parts.append(plt.Line2D([WIDTH, 0], [WIDTH, HEIGHT], color=WHITE, lw=5, alpha=0.5))

# Set the axis limits and aspect ratio
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Define the happyman's body movement
def move_body(part, angle):
    if part == 'head':
        ax.text(0.5, 0.8, 'HEAD', ha='center', va='center', size=20)
    elif part == 'torso':
        ax.text(WIDTH / 2, 0.8, 'TORSO', ha='center', va='center', size=20)
    elif part == 'left_arm':
        ax.text(0.5, 0.2, 'ARM', ha='center', va='center', size=20)
    elif part == 'right_arm':
        ax.text(WIDTH / 2, 0.2, 'ARM', ha='center', va='center', size=20)
    elif part == 'left_leg':
        ax.text(WIDTH / 2, -0.2, 'LEG', ha='center', va='center', size=20)
    elif part == 'right_leg':
        ax.text(0.5, -0.2, 'LEG', ha='center', va='center', size=20)

# Define the happyman's movement
def move_man(angle):
    for part in BODY_PARTS:
        move_body(part, angle)
    move_man_speed = 0.1 * angle
    for light in lights:
        light.set_x(0)
        light.set_y(0)
        light.set_width(MAN_SPEED * move_man_speed)
        light.set_alpha(0)
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    move_man(angle)

# Animate the happyman's movement
ani = animation.FuncAnimation(fig, move_man, frames=np.arange(0, 360, 1), interval=10)

plt.show()
