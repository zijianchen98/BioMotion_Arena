
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
MAX_SPEED = 2

# Define subject and action
SUBJECT = (0, 0)
ACTION = (100, HEIGHT - 100)

# Define movement parameters
INITIAL_SPEED = 0.5
MAX_SPEED = 2
TIME_STEP = 0.02

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point lights
lights = []
for i in range(15):
    angle = np.radians(30 + i * 10)  # 30 degrees increments
    x = SUBJECT[0] + np.cos(angle) * 100
    y = SUBJECT[1] + np.sin(angle) * 100
    ax.add_patch(plt.Polygon([[x, y], [x + 10, y], [x + 20, y + 10]], facecolor=WHITE, alpha=0.5))
    lights.append(plt.Line2D([0, x], [0, y], color='white', linewidth=5, alpha=0.5, label=f'Light {i+1}'))

# Set axis limits
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Function to update the plot
def update(i):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    
    # Update the point lights
    for light in lights:
        light.set_xdata([light.get_xdata()[0] + i * TIME_STEP, light.get_xdata()[0] + i * TIME_STEP + 10])
        light.set_ydata([light.get_ydata()[0] + i * TIME_STEP, light.get_ydata()[0] + i * TIME_STEP + 10])
        light.set_alpha(1 - i / 15)
        light.set_color('white')
        light.set_linewidth(5)
        light.set_label(f'Light {i+1}')
    
    # Update the subject and action
    ax.add_patch(plt.Polygon([[SUBJECT[0], SUBJECT[1]], [SUBJECT[0] + 10, SUBJECT[1]], [SUBJECT[0] + 20, SUBJECT[1] + 10]], facecolor=BLACK, alpha=0.5))
    ax.add_patch(plt.Polygon([[ACTION[0], ACTION[1]], [ACTION[0] + 10, ACTION[1]], [ACTION[0] + 20, ACTION[1] + 10]], facecolor=BLACK, alpha=0.5))
    
    # Set axis limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    
    # Animate the plot
    plt.pause(TIME_STEP)

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=1000, interval=16, repeat=True)

plt.show()
