
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
num_frames = 100
background_color = 'black'
point_color = 'white'

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor(background_color)
ax.axis('off')

# Initialize the scatter plot
sc = ax.scatter([], [], s=50, color=point_color)

# Define the jumping motion parameters
peak_height = 5
cycle_length = 2 * np.pi
weight = 1.5

# Function to update the scatter plot for each frame
def update(frame):
    t = frame / num_frames * cycle_length
    
    # Calculate the x and y positions for the points
    x_positions = np.linspace(0, 10, num_points)
    
    # Create a jumping motion for each point
    y_positions = peak_height * np.sin(t) / weight + 5
    
    # Update the scatter plot
    sc.set_offsets(np.column_stack((x_positions, y_positions)))
    return sc,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

# Display the animation
plt.show()
