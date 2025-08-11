
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject and action parameters
subject = 'happyman'
action = 'jumping up'

# Set the number of points and their initial positions
num_points = 15
points = np.random.rand(num_points, 2) * 100

# Set the background color
background_color = 'black'

# Define the initial positions and velocities for each point
initial_positions = points[:, :2]
velocities = np.zeros((num_points, 2))

# Set the gravity force (adjust this value to control the speed of the animation
gravity_force = 0.5

# Define the function to update the positions and velocities
def update(frame):
    global points, velocities
    
    # Update velocities due to gravity
    velocities += gravity_force * np.array([0, -1])  # gravity in y-direction
    
    # Update positions based on velocities
    points += velocities
    
    # Ensure points stay within the plot boundaries
    points = np.clip(points, 0, 99)
    
    # Clear the axes and draw new points
    ax.clear()
    ax.set_facecolor(background_color)
    ax.scatter(*points.T, s=50, c='white')
    
    return ax,

# Create the figure and axis for the animation
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()

