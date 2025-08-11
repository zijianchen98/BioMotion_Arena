
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
time_steps = 60
frame_rate = 30
background_color = 'black'
point_light_color = 'white'

# Define the initial positions of the point lights
initial_positions = np.random.rand(num_points, 2)

# Define the function to update the positions of the point lights
def update(frame):
    # Clear the previous frame
    ax.clear()
    
    # Update the positions of the point lights based on the forward rolling motion
    new_positions = initial_positions + np.array([np.sin(2 * np.pi * frame / time_steps), -np.cos(2 * np.pi * frame / time_steps)])
    
    # Wrap around the positions if they go out of bounds
    new_positions[:, 0] %= 1
    new_positions[:, 1] %= 1
    
    # Plot the updated positions of the point lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color=point_light_color)
    
    # Set the limits of the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation using the update function
ani = FuncAnimation(fig, update, frames=time_steps, interval=int(1000 / frame_rate), blit=False)

# Show the animation
plt.show()
