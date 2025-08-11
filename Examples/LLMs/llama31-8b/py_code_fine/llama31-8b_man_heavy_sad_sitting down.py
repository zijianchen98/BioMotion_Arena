
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')  # Set the background color to black

# Define the point-light stimulus
num_lights = 15
light_positions = np.zeros((num_lights, 2))

# Define the movement of each point-light
# Sitting down motion is approximated by a parabolic curve
t = np.linspace(0, 2, 100)  # Time array
x = 0.5 * t**2  # x-coordinate of the point-light
y = -1.5 * t + 1.5  # y-coordinate of the point-light

# Initialize the point-light positions
light_positions[:, 0] = x
light_positions[:, 1] = y

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')  # Set the background color to black
    ax.set_xlim(-1, 1)  # Set the x-axis limits
    ax.set_ylim(-1, 1)  # Set the y-axis limits
    
    # Update the point-light positions
    for j in range(num_lights):
        light_positions[j, 0] = x[i % len(x)]  # Update the x-coordinate
        light_positions[j, 1] = y[i % len(y)]  # Update the y-coordinate
        
    # Plot the point-lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], s=100, color='white')
    
    # Add a static sadman image
    sadman_image = plt.imread('sadman_image.png')  # Replace with your sadman image
    ax.imshow(sadman_image, extent=[-1, 1, -1, 1])  # Display the sadman image
    
    # Add a heavy weight image
    weight_image = plt.imread('weight_image.png')  # Replace with your weight image
    ax.imshow(weight_image, extent=[-0.5, 0.5, -0.5, 0.5])  # Display the weight image

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=20)

# Show the animation
plt.show()
