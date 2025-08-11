
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the figure and axis
fig, ax = plt.subplots()

# Set the background to black
ax.set_facecolor('#000000')

# Number of point-lights
num_points = 15

# Starting positions for the points
points = np.random.rand(num_points, 2)

# Set the maximum displacement (range) for the motion
max_displacement = 0.05

# Set the velocity for the motion
velocity = 0.01

# Function to initialize the animation
def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return

# Function to update the animation
def update(frame):
    # Update the position of each point
    for i in range(num_points):
        points[i, 0] += velocity * np.cos(np.pi * frame / 50)
        points[i, 1] += velocity * np.sin(np.pi * frame / 50)
    
    # Clear the axis
    ax.cla()
    
    # Set the new axis limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], s=20, c='white')
    
    # Hide axis
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 1000, 10), init_func=init, blit=True)

# Display the animation
plt.show()
