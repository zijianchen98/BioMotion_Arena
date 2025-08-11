
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
WIDTH = 10
HEIGHT = 10
DOT_SIZES = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
INITIAL_ANGLE = 0
ANGLE_OFFSETS = np.array([0, 90, 180, 270, 0, 90, 180, 270, 0, 90, 180, 270, 0, 90, 180])
VELOCITY = 1

def init():
    """Initialize the animation."""
    return []

def animate(angle):
    """Update the animation for each frame."""
    angle = angle % 360
    
    # Convert degree angles to radians
    radians = np.deg2rad(angle + ANGLE_OFFSETS)
    
    # Calculate dot positions
    x_coords = WIDTH / 2 + DOT_SIZES * np.cos(radians) * VELOCITY
    y_coords = HEIGHT / 2 + DOT_SIZES * np.sin(radians) * VELOCITY
    
    # Clear the plot
    plt.cla()
    
    # Create a figure with black background
    plt.figure(facecolor='black')
    
    # Plot the white dots
    plt.scatter(x_coords, y_coords, c='white', s=50)
    
    # Set plot limits
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    
    # Turn off axis
    plt.axis('off')
    
    return []

# Setup plot and animation
fig = plt.figure(facecolor='black')
anim = animation.FuncAnimation(fig, animate, frames=np.linspace(INITIAL_ANGLE, INITIAL_ANGLE + 360, 100), init_func=init, blit=True)

# Show the animation
plt.show()
