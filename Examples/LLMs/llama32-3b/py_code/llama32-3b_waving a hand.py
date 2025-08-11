
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import matplotlib.animation as animation

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Define the point lights
lights = [
    patches.Circle((0.1, 0.1), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.2, 0.2), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.3, 0.3), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.4, 0.4), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.5, 0.5), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.6, 0.6), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.7, 0.7), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.8, 0.8), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.9, 0.9), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((1.0, 0.9), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.9, 1.0), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.8, 1.0), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.7, 1.0), 0.01, edgecolor='white', facecolor='white', lw=2),
    patches.Circle((0.6, 0.9), 0.01, edgecolor='white', facecolor='white', lw=2),
]

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Set the aspect ratio to be equal
    ax.set_aspect('equal')
    
    # Set the x and y limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Set the aspect ratio to be equal
    ax.set_aspect('equal')
    
    # Draw the point lights
    for light in lights:
        ax.add_patch(light)
        light.set_edgecolor('white')
        light.set_facecolor('white')
        light.set_alpha(0.5)
    
    # Animate the movement of the point lights
    x = np.linspace(0.1, 1.0, 15)
    y = np.linspace(0.9, 0.1, 15)
    x, y = np.meshgrid(x, y)
    x = x + i * 0.01
    y = y + i * -0.01
    
    for j in range(15):
        for k in range(15):
            if j % 3 == 0 and k % 3 == 0:
                lights[j * 3 + k].center = (x[j, k], y[j, k])
                lights[j * 3 + k].set_edgecolor('white')
                lights[j * 3 + k].set_facecolor('white')
                lights[j * 3 + k].set_alpha(0.5)

# Create the animation
ani = FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
