
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
HUMAN_WIDTH, HUMAN_HEIGHT = 100, 50
HAND_WIDTH, HAND_HEIGHT = 20, 10

# Create a new figure
fig, ax = plt.subplots()

# Define the subject and action parameters
SUBJECT_X, SUBJECT_Y = WIDTH / 2, HEIGHT / 2
ACTION_X, ACTION_Y = 0, 0

# Define the parameters for the point lights
LIGHTS = []
for i in range(15):
    LIGHTS.append([i, SUBJECT_X + np.random.uniform(-HUMAN_WIDTH / 2, HUMAN_WIDTH / 2),
                    i, SUBJECT_Y + np.random.uniform(-HUMAN_HEIGHT / 2, HUMAN_HEIGHT / 2)])

# Define the parameters for the animation
ANIMATION_SPEED = 0.01
TICKS = np.arange(0, 100, ANIMATION_SPEED)

# Initialize the point lights
def init():
    for light in LIGHTS:
        ax.add_patch(plt.Line2D([light[1], light[1]], [light[2], light[2]], color=WHITE, linewidth=1))
    return ax

# Update the point lights
def update(i):
    for light in LIGHTS:
        light[1] += ANIMATION_SPEED * i
        light[2] += ANIMATION_SPEED * i
        if light[1] < 0 or light[1] > WIDTH or light[2] < 0 or light[2] > HEIGHT:
            light[1] = WIDTH / 2
            light[2] = HEIGHT / 2
    return ax

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=TICKS, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
