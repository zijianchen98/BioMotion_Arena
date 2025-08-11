
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
lights = np.random.rand(num_lights, 2) * 2 - 1

# Define the movement parameters
angle = 0
radius = 1

# Function to update the positions of the point lights
def update(frame):
    global angle, radius, lights
    angle += 0.01
    radius = 1 + 0.1 * np.sin(angle)
    
    # Update the positions of the point lights
    x = radius * np.cos(angle + np.linspace(0, 2*np.pi, num_lights))
    y = radius * np.sin(angle + np.linspace(0, 2*np.pi, num_lights))
    
    # Update the positions of the point lights
    lights[:, 0] = x
    lights[:, 1] = y
    
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the point lights
    ax.scatter(lights[:, 0], lights[:, 1], s=100, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20)

# Display the animation
plt.show()
