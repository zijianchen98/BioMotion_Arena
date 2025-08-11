
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
frame_rate = 30
total_frames = 600
background_color = 'black'
point_color = 'white'

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor(background_color)

# Initialize the positions of the points
points = np.random.rand(num_points, 2) * 2 - 1
velocities = np.random.randn(num_points, 2) / 10

# Function to update the positions of the points
def update(frame):
    global points, velocities
    
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor(background_color)
    
    # Update the positions of the points
    points += velocities
    points %= 2  # Wrap around the edges of the screen
    
    # Draw the points
    ax.scatter(points[:, 0], points[:, 1], color=point_color, s=50)
    
    # Return the updated plot
    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(total_frames), interval=1000/frame_rate, blit=True)

# Show the animation
plt.show()
