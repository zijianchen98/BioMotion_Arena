
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SPEED = 1.0
JUMP_SPEED = 10.0
JUMP_HEIGHT = 20.0

# Initialize figure and axis
fig, ax = plt.subplots()

# Set axis limits and aspect ratio
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Initialize point-lights
light_positions = []
light_colors = []
for i in range(15):
    x = i * 50 + 100
    y = HEIGHT // 2
    light_positions.append((x, y))
    light_colors.append(WHITE)

# Initialize figure
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Function to update light positions
def update(frame):
    global light_positions, light_colors
    for i in range(15):
        x = light_positions[i][0]
        y = light_positions[i][1]
        light_colors[i] = WHITE
        light_positions[i] = (x + LIGHT_SPEED * frame, y)
        ax.clear()
        ax.set_xlim(0, WIDTH)
        ax.set_ylim(0, HEIGHT)
        ax.set_aspect('equal')
        ax.add_patch(plt.Circle((x, y), 2, color=light_colors[i]))
        plt.draw()

# Animate
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=16)

plt.show()
