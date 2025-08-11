
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.5, 0.9], [0.6, 0.8], [0.7, 0.7], [0.8, 0.6], [0.9, 0.5],
    [0.4, 0.5], [0.3, 0.6], [0.2, 0.7], [0.1, 0.8], [0.0, 0.9],
    [0.3, 0.4], [0.4, 0.3], [0.5, 0.2], [0.6, 0.1], [0.7, 0.0]
])

# Define the target positions for each point-light
target_positions = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.2], [0.9, 0.1],
    [0.4, 0.1], [0.3, 0.2], [0.2, 0.3], [0.1, 0.4], [0.0, 0.5],
    [0.3, 0.2], [0.4, 0.3], [0.5, 0.4], [0.6, 0.5], [0.7, 0.6]
])

# Define the time steps
time_steps = 100

# Define the animation function
def animate(frame):
    # Calculate the current positions of the point-lights
    current_positions = (1 - frame / time_steps) * initial_positions + (frame / time_steps) * target_positions
    
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the point-lights
    ax.scatter(current_positions[:, 0], current_positions[:, 1], color='white', s=10)
    
    # Set the limits of the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Remove the axes
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, animate, frames=time_steps, interval=50)

# Show the animation
plt.show()
