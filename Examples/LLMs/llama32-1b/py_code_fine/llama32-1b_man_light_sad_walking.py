
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SADMAN_SIZE = 50
WALK_SPEED = 2

# Function to generate a random point in a 2D space
def random_point(x, y):
    return np.random.uniform(-WIDTH/2, WIDTH/2), np.random.uniform(-HEIGHT/2, HEIGHT/2)

# Create a new figure
fig, ax = plt.subplots()

# Initialize the point lights
light1 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light2 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light3 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light4 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light5 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light6 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light7 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light8 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light9 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light10 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light11 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light12 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light13 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light14 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)
light15 = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=2, alpha=0.8)

# Set the axis limits
ax.set_xlim(-WIDTH/2, WIDTH/2)
ax.set_ylim(-HEIGHT/2, HEIGHT/2)

# Function to update the point lights
def update(frame):
    global x, y
    x, y = random_point(WIDTH/2, HEIGHT/2)
    
    # Move the point lights to the current position
    light1.set_xdata([x, x])
    light1.set_ydata([y, y])
    light2.set_xdata([x, x])
    light2.set_ydata([y, y])
    light3.set_xdata([x, x])
    light3.set_ydata([y, y])
    light4.set_xdata([x, x])
    light4.set_ydata([y, y])
    light5.set_xdata([x, x])
    light5.set_ydata([y, y])
    light6.set_xdata([x, x])
    light6.set_ydata([y, y])
    light7.set_xdata([x, x])
    light7.set_ydata([y, y])
    light8.set_xdata([x, x])
    light8.set_ydata([y, y])
    light9.set_xdata([x, x])
    light9.set_ydata([y, y])
    light10.set_xdata([x, x])
    light10.set_ydata([y, y])
    light11.set_xdata([x, x])
    light11.set_ydata([y, y])
    light12.set_xdata([x, x])
    light12.set_ydata([y, y])
    light13.set_xdata([x, x])
    light13.set_ydata([y, y])
    light14.set_xdata([x, x])
    light14.set_ydata([y, y])
    light15.set_xdata([x, x])
    light15.set_ydata([y, y])
    
    # Update the axis limits
    ax.set_xlim(-WIDTH/2, WIDTH/2)
    ax.set_ylim(-HEIGHT/2, HEIGHT/2)
    
    return light1, light2, light3, light4, light5, light6, light7, light8, light9, light10, light11, light12, light13, light14, light15

# Animate the point lights
ani = animation.FuncAnimation(fig, update, interval=20, blit=True)

# Show the animation
plt.show()
