
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject and action
subject = 'sadwoman'
action = 'bowing'

# Define the number of points and their initial positions
num_points = 15
initial_positions = np.random.rand(num_points, 2) * 100

# Define the background color
background_color = (plt.cm.get_c('black')

# Define the function to update the animation frame
def update(frame):
    # Clear the previous frame
    ax.clear()
    
    # Update the positions of the points
    positions = np.clip(initial_positions + np.sin(frame / 10) * 10, 0, 100)
    
    # Draw the points on the plot
    for i, position in enumerate(positions):
        ax.scatter(*position, c=plt.cm.get_c('white'), s=100)
    
    # Set the background color
    ax.set_facecolor(background_color)
    
    # Set the title and labels the axes
    ax.set_title(f'{subject} {action}')
    ax.set_xlabel('X ')
    ax.set_ylabel(' Y ')
    ax.axis('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=20)

# Display the animation
plt.show()
