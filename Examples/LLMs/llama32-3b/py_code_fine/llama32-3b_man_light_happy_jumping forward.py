
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of point lights and their positions
num_lights = 15
light_positions = np.random.rand(num_lights, 3) * 10 - 5

# Define the animation function
def animate(i):
    # Clear the previous frame
    fig.clear()
    
    # Set the axis limits
    fig.set_xlim(-10, 10)
    fig.set_ylim(-10, 10)
    fig.set_zlim(-10, 10)
    
    # Create the black background
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Create the point lights
    lights = []
    for light in light_positions:
        # Rotate the light position to simulate the action
        rotated_light = np.array([
            light[0] + 0.1 * np.sin(i * 0.1),
            light[1] + 0.1 * np.cos(i * 0.1),
            light[2]
        ])
        
        # Add the light to the list
        lights.append(plt.scatter(rotated_light[0], rotated_light[1], rotated_light[2], s=10, c='white'))
    
    # Add the lights to the axes
    for light in lights:
        ax.add_artist(light)
    
    # Return the axes
    return ax

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Display the animation
plt.show()
