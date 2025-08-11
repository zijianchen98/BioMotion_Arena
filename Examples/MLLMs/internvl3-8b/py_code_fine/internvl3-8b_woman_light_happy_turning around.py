
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the initial positions of the 15 circles
num_circles = 15
circle_radii = np.array([0.1]*num_circles)
initial_positions = np.zeros((num_circles, 2))

# Set the x, y bounds for the animation
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Function to update the animation at each frame
def update(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    
    for i, (x, y) in enumerate(initial_positions):
        # Simulate some simple cyclical motion for each circle
        x += 0.2 * np.cos(frame * 0.1 + 2 * np.pi * i / num_circles)
        y += 0.2 * np.sin(frame * 0.1 + 2 * np.pi * i / num_circles)
        
        # Ensure circles stay within bounds
        x = max(min(x, x_max), x_min)
        y = max(min(y, y_max), y_min)
        
        # Add the circle to the plot
        circle = Circle((x, y), radius=circle_radii[i], color='white')
        ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=False)

# Show the animation
plt.show()
