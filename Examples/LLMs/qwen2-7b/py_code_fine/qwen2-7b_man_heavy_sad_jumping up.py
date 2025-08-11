
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
WHITE = (255, 255, 255
BLACK = (0, 0, 0
NUM_POINTS = 15
FPS = 30
DURATION_SECONDS = 5

# Animation function
def animate(i):
    # Clear the plot
    ax.clear()
    
    # Generate random positions for the points
    positions = np.random.rand(NUM_POINTS, 2)
    positions[:, 0] *= (4 * D / 2 - d / 2
    positions[:, 1] *= 4
    
    # Set the color for each point
    colors = np.linspace(0, 1, NUM_POINTS
    colors = np.sin(np.linspace 0, , NUM_POINTS) / 2 + 0.55
    
    # Draw the points
    for j in range(NUM_POINTS):
        circle = plt.Circle(positions[j], radius=0.05, color=color[j], fill=True)
        ax.add_artist(circle)
        
    # Set the background color
    ax.set_facecolor(BLACK)
    
    # Set the axis limits
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 5)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=FPS * DURATION_SECONDS, interval=1000 // FPS)

# Show the animation
plt.show()
