
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the background color
ax.set_facecolor('black')

# Define the point lights
lights = [
    patches.Circle((0.2, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.3, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.4, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.5, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.6, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.7, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.8, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.9, 0.5), 0.05, facecolor='white'),
    patches.Circle((0.1, 0.6), 0.05, facecolor='white'),
    patches.Circle((0.2, 0.6), 0.05, facecolor='white'),
    patches.Circle((0.3, 0.6), 0.05, facecolor='white'),
    patches.Circle((0.4, 0.6), 0.05, facecolor='white'),
    patches.Circle((0.5, 0.6), 0.05, facecolor='white'),
    patches.Circle((0.6, 0.6), 0.05, facecolor='white'),
]

# Initialize the light positions
light_positions = np.array([
    [0.2, 0.5],
    [0.3, 0.5],
    [0.4, 0.5],
    [0.5, 0.5],
    [0.6, 0.5],
    [0.7, 0.5],
    [0.8, 0.5],
    [0.9, 0.5],
    [0.1, 0.6],
    [0.2, 0.6],
    [0.3, 0.6],
    [0.4, 0.6],
    [0.5, 0.6],
    [0.6, 0.6],
    [0.7, 0.6],
])

# Define the animation function
def animate(i):
    # Update the light positions
    light_positions[:, 0] = np.sin(i * 0.1) + 0.5
    light_positions[:, 1] = np.sin(i * 0.1) + 0.5
    
    # Update the light patches
    for j, light in enumerate(lights):
        light.center = light_positions[j]
    
    # Clear the previous frame
    ax.clear()
    
    # Set the background color
    ax.set_facecolor('black')
    
    # Draw the lights
    for light in lights:
        ax.add_patch(light)
    
    # Set the limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Set the aspect ratio
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=False, interval=20)

# Show the animation
plt.show()
