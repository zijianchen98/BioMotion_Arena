
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initial positions of the point lights (representing a happy woman lifting a heavy weight)
# The positions will be adjusted to simulate turning around
initial_positions = np.array([
    [0, 5], [1, 6], [-1, 6], [2, 7], [-2, 7], # Top cluster
    [0, 4], [1, 5], [-1, 5], [2, 6], [-2, 6], # Upper middle cluster
    [0, 3], [1, 4], [-1, 4], [2, 5], [-2, 5], # Lower middle cluster
    [0, 2]  # Bottom point
])

# Create a figure and an axes
fig, ax = plt.subplots()

# Set the limits and background color
ax.set_xlim(-4, 4)
ax.set_ylim(0, 8)
ax.set_facecolor('black')

# Turn off the axes
ax.axis('off')

# Create points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Update function for animation
def update(frame):
    # Angle of rotation
    angle = frame * np.pi / 30  # Adjust speed here
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    # Rotate points around the center point (0, 4) to simulate turning around
    rotated_positions = initial_positions @ rotation_matrix + np.array([0, 4])
    
    # Update points
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=1000/30, blit=True)

# Show the animation
plt.show()
