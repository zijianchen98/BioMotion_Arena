
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define constants
N_LIGHTS = 15
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor(BLACK)

# Initialize the lights
lights = []
for i in range(N_LIGHTS):
    # Calculate the position of the light
    x = np.random.uniform(0, WIDTH)
    y = np.random.uniform(0, HEIGHT)
    
    # Create a new circle to represent the light
    light = Circle((x, y), radius=5, color=WHITE, alpha=1.0)
    ax.add_patch(light)
    
    # Add the light to the list
    lights.append(light)

# Define the function to update the lights
def update(frame):
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor(BLACK)
    
    # Update the position of the lights
    for light in lights:
        # Calculate the new position of the light
        x = np.random.uniform(0, WIDTH)
        y = np.random.uniform(0, HEIGHT)
        
        # Update the position of the light
        light.center = (x, y)
        
        # Add the light to the list
        lights.append(light)
        
        # Remove the light if it's not in the list anymore
        if light not in lights:
            lights.remove(light)

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=50)

# Show the animation
plt.show()
