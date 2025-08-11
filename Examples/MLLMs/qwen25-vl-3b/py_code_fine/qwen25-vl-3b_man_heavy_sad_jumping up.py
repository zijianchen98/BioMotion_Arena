
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point lights
lights = np.array([
    [0.4, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7],
    [0.4, 0.4], [0.5, 0.5], [0.6, 0.6],
    [0.7, 0.7], [0.8, 0.8], [0.9, 0.9],
    [0.4, 0.2], [0.5, 0.3], [0.6, 0.4]
])

# Define the weights and height of the sadman
weights = np.array([0.5, 0.5])
height = 0.2

# Define the jump parameters
jump_height = 0.3
jump_speed = 0.1

# Initialize the position of the sadman
x = 0.5
y = height

# Create the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the sadman
ax.plot(x, y, 'o', markersize=10, color='white')

# Animate the sadman jumping
for t in range(10):
    # Calculate the new position based on the jump parameters
    y += jump_speed * t
    
    # Update the sadman's position
    x = 0.5
    y = height + jump_height * t
    
    # Plot the updated sadman
    ax.plot(x, y, 'o', markersize=10, color='white')
    
    # Update the plot
    fig.canvas.draw()
    fig.canvas.flush_events()

# Show the plot
plt.show()
