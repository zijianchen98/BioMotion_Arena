
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the point lights
lights = []
for i in range(15):
    light = patches.Circle((0, 0), 0.05, edgecolor='white', facecolor='white')
    lights.append(light)

# Define the initial positions of the point lights
positions = np.array([
    [-0.25, -0.2], [-0.2, -0.2], [-0.2, -0.15], [-0.2, -0.1], [-0.2, -0.05],
    [-0.2, 0], [-0.2, 0.05], [-0.2, 0.1], [-0.2, 0.15], [-0.2, 0.2],
    [0, -0.2], [0, -0.15], [0, -0.1], [0, -0.05], [0, 0]
])

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    
    # Update the positions of the point lights
    for j in range(15):
        x = positions[j, 0] + np.sin(i / 10 + j / 5) * 0.1
        y = positions[j, 1] + np.cos(i / 10 + j / 5) * 0.1
        lights[j].center = (x, y)
        ax.add_patch(lights[j])
        
    # Set the limits of the axis
    ax.set_xlim(-0.3, 0.3)
    ax.set_ylim(-0.25, 0.25)
    
    # Remove the axis ticks and frames
    ax.set_xticks([])
    ax.set_yticks([])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
