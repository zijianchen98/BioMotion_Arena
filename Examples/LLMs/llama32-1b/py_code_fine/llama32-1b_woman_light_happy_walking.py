
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
LIGHT_COLOR = WHITE.copy()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Initialize the axis with a solid black background
ax.set_facecolor(BLACK)

# Function to update the plot for each frame
def update(frame):
    global LIGHT_COLOR
    
    # Calculate the position of the light source
    angle = frame / 100
    x = WIDTH / 2 + WIDTH / 2 * np.cos(angle)
    y = HEIGHT / 2 + HEIGHT / 2 * np.sin(angle)
    
    # Update the color of the light source
    LIGHT_COLOR = WHITE.copy()
    LIGHT_COLOR[0] = int(255 * (1 - angle / 100))
    LIGHT_COLOR[1] = int(255 * (1 - angle / 100))
    LIGHT_COLOR[2] = int(255 * (1 - angle / 100))
    
    # Plot the light source
    ax.scatter(x, y, s=50, c=LIGHT_COLOR, alpha=0.5)
    
    # Return the updated plot
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20)

# Show the animation
plt.show()
