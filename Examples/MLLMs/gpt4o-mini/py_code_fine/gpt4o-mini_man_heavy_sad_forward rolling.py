
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the number of point-lights
num_points = 15

# Initial positions of the point-lights creating a sad man carrying a weight
points = np.array([[0, 0.5], [-0.2, 0.3], [0.2, 0.3], [-0.4, 0.1],
                   [0.4, 0.1], [-0.5, -0.1], [0.5, -0.1], [0, -0.3],
                   [-0.2, -0.4], [0.2, -0.4], [0, -0.6], 
                   [-0.25, -0.5], [0.25, -0.5], [-0.1, -0.6], [0.1, -0.6]])

# Create scatter plot for point-lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Calculate new positions for the point-lights to simulate forward rolling
    angle = frame * 0.1
    # Apply rotation and translation
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    transformed_points = points @ rotation_matrix.T
    
    # Update the positions of the point-lights
    scat.set_offsets(transformed_points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
