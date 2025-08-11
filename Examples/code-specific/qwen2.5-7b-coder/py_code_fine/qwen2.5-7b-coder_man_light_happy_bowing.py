
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2)

# Define the target position for the bowing motion
target_position = np.array([0.5, 0.5])

# Define the speed of the point lights
speed = 0.05

# Define the function to update the positions of the point lights
def update(frame):
    global initial_positions
    
    # Calculate the distance between each point light and the target position
    distances = np.linalg.norm(initial_positions - target_position, axis=1)
    
    # Update the positions of the point lights towards the target position
    initial_positions -= speed * (initial_positions - target_position) / distances[:, np.newaxis]
    
    # Wrap around the edges of the screen
    initial_positions %= 1
    
    # Clear the previous frame
    ax.clear()
    
    # Draw the point lights
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
    
    # Set the limits of the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Create the figure and axis for the plot
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, repeat=False)

# Show the animation
plt.show()
