
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RUNNING_SPEED = 0.5

# Define subject and action
SUBJECT = patches.Circle((WIDTH / 2, HEIGHT / 2), 20, edgecolor='black', facecolor='white', lw=2)
ACTION = patches.Circle((WIDTH / 2 + 100, HEIGHT / 2 + 100), 30, edgecolor='black', facecolor='white', lw=2)
RUNNING = patches.Poly3D([SUBJECT, ACTION], [(-100, 100), (-150, 150), (-200, 200), (100, 100)], color='white', alpha=0.5)

# Define camera
CAMERA = patches.Arc((WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + 200, HEIGHT / 2 + 200), 20, 0, 2 * np.pi, color='black', lw=2)

# Define point lights
LIGHTS = [patches.PointLight(100, 50, 50), patches.PointLight(300, 150, 150)]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')
ax.set_axis_off()

# Function to update the plot
def update(frame):
    global RUNNING, LIGHTS
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Update subject and action
    SUBJECT.center = (WIDTH / 2, HEIGHT / 2)
    ACTION.center = (WIDTH / 2 + 100, HEIGHT / 2 + 100)
    RUNNING.center = (WIDTH / 2 + 150, HEIGHT / 2 + 150)
    RUNNING.angle = np.random.uniform(0, 2 * np.pi, 1)[0]

    # Update point lights
    for light in LIGHTS:
        light.position = (light.position.x + RUNNING.angle * 0.1, light.position.y + RUNNING.angle * 0.1)
        light.size = 1

    # Draw axis
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)

    # Draw camera
    CAMERA.center = (WIDTH / 2, HEIGHT / 2)
    CAMERA.angle = np.random.uniform(0, 2 * np.pi, 1)[0]

    # Draw background
    ax.set_facecolor(BLACK)
    ax.add_patch(patches.Rectangle((0, 0), WIDTH, HEIGHT, facecolor='black', alpha=0.5))

    # Draw point lights
    for light in LIGHTS:
        light.set_color('white')
        light.set_alpha(RUNNING.angle * 0.1)

    # Draw subject and action
    ax.add_patch(SUBJECT)
    ax.add_patch(ACTION)
    ax.add_patch(RUNNING)

    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    return ax,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(360), interval=50)

plt.show()
