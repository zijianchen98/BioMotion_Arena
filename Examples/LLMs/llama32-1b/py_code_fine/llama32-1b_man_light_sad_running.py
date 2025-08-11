
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)

# Define point light parameters
LIGHT_SIZE = 10
LIGHT_COLOR = WHITE_COLOR
LIGHT_SPEED = 0.01

# Define parameters for the happyman's motion
MAN_SIZE = 50
MAN_SPEED = 2
MAN_SPEED_VEL = 2

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize point light positions
lights = []
for i in range(15):
    angle = np.radians(i * 360 / 14)
    x = WIDTH / 2 + 20 * np.cos(angle)
    y = HEIGHT / 2 + 20 * np.sin(angle)
    ax.add_patch(plt.Circle((x, y), LIGHT_SIZE, edgecolor='black', facecolor=WHITE_COLOR, lw=2))
    lights.append((x, y))

# Initialize happyman's position and velocity
man_x, man_y = WIDTH / 2, HEIGHT / 2
man_vel_x, man_vel_y = 0, 0

# Function to update the happyman's position
def update(frame):
    global man_x, man_y, man_vel_x, man_vel_y
    
    # Update happyman's position
    man_x += man_vel_x * MAN_SPEED_VEL
    man_y += man_vel_y * MAN_SPEED_VEL
    
    # Ensure happyman stays within the boundaries
    man_x = max(0, man_x)
    man_x = min(WIDTH - MAN_SIZE, man_x)
    man_y = max(0, man_y)
    man_y = min(HEIGHT - MAN_SIZE, man_y)
    
    # Update happyman's velocity
    man_vel_x += (man_x - man_x) * LIGHT_SPEED / 1000
    man_vel_y += (man_y - man_y) * LIGHT_SPEED / 1000
    
    # Limit velocity to prevent animation from moving too fast
    if man_vel_x > 0.01:
        man_vel_x = 0.01
    elif man_vel_x < -0.01:
        man_vel_x = -0.01
    
    if man_vel_y > 0.01:
        man_vel_y = 0.01
    elif man_vel_y < -0.01:
        man_vel_y = -0.01
    
    # Draw the happyman and point lights
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.add_patch(plt.Circle((man_x, man_y), MAN_SIZE, edgecolor='black', facecolor=WHITE_COLOR, lw=2))
    for light_x, light_y in lights:
        ax.add_patch(plt.Circle((light_x, light_y), LIGHT_SIZE, edgecolor='black', facecolor=WHITE_COLOR, lw=2))
    
    # Update the happyman's position and velocity
    man_x += man_vel_x
    man_y += man_vel_y
    
    # Update the plot
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    plt.pause(0.01)

# Animate the happyman and point lights
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=16)

plt.show()
