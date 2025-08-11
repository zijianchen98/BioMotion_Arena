
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.4],
    [0.9, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8],
    [0.8, 0.7], [0.9, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7]
])

# Define the jump trajectory
jump_height = 0.2
jump_duration = 0.5
jump_speed = 0.1

# Create the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point-lights
ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)

# Animate the jump
for t in np.linspace(0, jump_duration, 100):
    # Calculate the new position based on the jump trajectory
    x = 0.5 + 0.1 * np.sin(2 * np.pi * t)
    y = 0.5 + jump_height * np.cos(2 * np.pi * t)
    
    # Update the point-lights' positions
    point_lights[:, 0] = x
    point_lights[:, 1] = y
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the updated point-lights
    ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.')
    
    # Update the plot
    fig.canvas.draw()

plt.show()
