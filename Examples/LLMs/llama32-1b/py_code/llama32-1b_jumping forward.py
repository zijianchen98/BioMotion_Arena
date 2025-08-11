
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAN_SIZE = 20
MAN_SPEED = 0.05

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the points
points = np.zeros((100, 2))
for i in range(100):
    points[i, 0] = i * MAN_SIZE
    points[i, 1] = i * MAN_SIZE

# Initialize the line
line, = ax.plot([], [], 'o-', markersize=10, color=WHITE)

# Initialize the axis
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    
    # Update the points
    points = np.zeros((100, 2))
    for i in range(100):
        points[i, 0] = i * MAN_SIZE
        points[i, 1] = i * MAN_SIZE
    line.set_data(points[:, 0], points[:, 1])
    
    # Draw the axis
    ax.set_axis_off()
    
    # Draw the point lights
    for i in range(15):
        angle = np.linspace(0, 2*np.pi, 100, endpoint=False)
        x = WIDTH / 2 + MAN_SIZE / 2 * np.cos(angle)
        y = HEIGHT / 2 + MAN_SIZE / 2 * np.sin(angle)
        ax.plot([x, x], [y, y], color=WHITE, lw=1)
    
    # Set the limits of the plot
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    plt.draw()
    plt.pause(0.01)

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=16)

plt.show()
