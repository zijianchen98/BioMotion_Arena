
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Define the subject's body position and velocity
subject_x, subject_y = 0, 0
subject_vx, subject_vy = 0, 0

# Define the action's body position and velocity
man_x, man_y = 300, 200
man_vx, man_vy = 0, 0

# Define the point lights
light1 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light2 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light3 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light4 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light5 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light6 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light7 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light8 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light9 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light10 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light11 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light12 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light13 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light14 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)
light15 = plt.Circle((0, 0), 0.1, color=WHITE, alpha=0.8)

# Define the figure and axis
fig, ax = plt.subplots()

# Draw the background
ax.add_patch(plt.Rectangle((0, 0), WIDTH, HEIGHT, color=BLACK, alpha=0.8))

# Draw the subject's body
ax.add_patch(plt.Circle((subject_x, subject_y), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((subject_x + 0.2, subject_y + 0.1), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((subject_x - 0.2, subject_y + 0.1), 0.1, color=WHITE, alpha=0.8))

# Draw the action's body
ax.add_patch(plt.Circle((man_x, man_y), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((man_x + 0.2, man_y + 0.1), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((man_x - 0.2, man_y + 0.1), 0.1, color=WHITE, alpha=0.8))

# Set the limits and aspect ratio
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Define the point light positions and colors
light_positions = [(0, 0), (0.2, 0), (0.4, 0), (0.6, 0), (0.8, 0), (1, 0), (1.2, 0), (1.4, 0), (1.6, 0), (1.8, 0), (2, 0), (2.2, 0), (2.4, 0), (2.6, 0), (2.8, 0), (3, 0), (3.2, 0), (3.4, 0), (3.6, 0), (3.8, 0), (4, 0), (4.2, 0), (4.4, 0), (4.6, 0), (4.8, 0), (5, 0), (5.2, 0), (5.4, 0), (5.6, 0), (5.8, 0), (6, 0), (6.2, 0), (6.4, 0), (6.6, 0), (6.8, 0), (7, 0), (7.2, 0), (7.4, 0), (7.6, 0), (7.8, 0), (8, 0), (8.2, 0), (8.4, 0), (8.6, 0), (8.8, 0), (9, 0), (9.2, 0), (9.4, 0), (9.6, 0), (9.8, 0), (10, 0), (10.2, 0), (10.4, 0), (10.6, 0), (10.8, 0), (11, 0), (11.2, 0), (11.4, 0), (11.6, 0), (11.8, 0), (12, 0), (12.2, 0), (12.4, 0), (12.6, 0), (12.8, 0), (13, 0), (13.2, 0), (13.4, 0), (13.6, 0), (13.8, 0), (14, 0), (14.2, 0), (14.4, 0), (14.6, 0), (14.8, 0), (15, 0)]

# Define the point light positions and colors
light_positions = [(0, 0), (0.2, 0), (0.4, 0), (0.6, 0), (0.8, 0), (1, 0), (1.2, 0), (1.4, 0), (1.6, 0), (1.8, 0), (2, 0), (2.2, 0), (2.4, 0), (2.6, 0), (2.8, 0), (3, 0), (3.2, 0), (3.4, 0), (3.6, 0), (3.8, 0), (4, 0), (4.2, 0), (4.4, 0), (4.6, 0), (4.8, 0), (5, 0), (5.2, 0), (5.4, 0), (5.6, 0), (5.8, 0), (6, 0), (6.2, 0), (6.4, 0), (6.6, 0), (6.8, 0), (7, 0), (7.2, 0), (7.4, 0), (7.6, 0), (7.8, 0), (8, 0), (8.2, 0), (8.4, 0), (8.6, 0), (8.8, 0), (9, 0), (9.2, 0), (9.4, 0), (9.6, 0), (9.8, 0), (10, 0), (10.2, 0), (10.4, 0), (10.6, 0), (10.8, 0), (11, 0), (11.2, 0), (11.4, 0), (11.6, 0), (11.8, 0), (12, 0), (12.2, 0), (12.4, 0), (12.6, 0), (12.8, 0), (13, 0), (13.2, 0), (13.4, 0), (13.6, 0), (13.8, 0), (14, 0)]

# Create the figure and axis
fig, ax = plt.subplots()

# Draw the background
ax.add_patch(plt.Rectangle((0, 0), WIDTH, HEIGHT, color=BLACK, alpha=0.8))

# Draw the subject's body
ax.add_patch(plt.Circle((subject_x, subject_y), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((subject_x + 0.2, subject_y + 0.1), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((subject_x - 0.2, subject_y + 0.1), 0.1, color=WHITE, alpha=0.8))

# Draw the action's body
ax.add_patch(plt.Circle((man_x, man_y), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((man_x + 0.2, man_y + 0.1), 0.1, color=WHITE, alpha=0.8))
ax.add_patch(plt.Circle((man_x - 0.2, man_y + 0.1), 0.1, color=WHITE, alpha=0.8))

# Draw the point lights
for pos, color in light_positions:
    ax.add_patch(plt.Circle(pos, 0.05, color=color, alpha=0.8))

# Define the animation function
def animate(i):
    global subject_x, subject_y, man_x, man_y
    subject_x += subject_vx * i / 60
    subject_y += subject_vy * i / 60
    man_x += man_vx * i / 60
    man_y += man_vy * i / 60

    # Keep the subject within the boundaries
    subject_x = max(0, min(subject_x, WIDTH - 0.1))
    subject_y = max(0, min(subject_y, HEIGHT - 0.1))
    man_x = max(0, min(man_x, WIDTH - 0.1))
    man_y = max(0, min(man_y, HEIGHT - 0.1))

    # Update the point lights
    for pos, color in light_positions:
        ax.add_patch(plt.Circle(pos, 0.05, color=color, alpha=0.8))

    # Update the subject and action positions
    subject_vx, subject_vy = subject_vx * 2, subject_vy * 2
    man_vx, man_vy = man_vx * 2, man_vy * 2

    # Limit the animation speed
    if i % 10 == 0:
        subject_vx *= 0.9
        subject_vy *= 0.9
        man_vx *= 0.9
        man_vy *= 0.9

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=10, blit=True)

# Show the animation
plt.show()
