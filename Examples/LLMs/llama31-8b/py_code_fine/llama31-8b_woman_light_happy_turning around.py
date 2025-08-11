
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the points for the human body
points = np.array([
    [0, 0, 0],  # Head
    [-0.2, -0.2, 0],  # Left eye
    [0.2, -0.2, 0],  # Right eye
    [-0.2, 0, 0],  # Left ear
    [0.2, 0, 0],  # Right ear
    [-0.1, -0.1, 0.2],  # Left shoulder
    [0.1, -0.1, 0.2],  # Right shoulder
    [-0.1, 0.1, 0.2],  # Left hip
    [0.1, 0.1, 0.2],  # Right hip
    [-0.1, -0.1, 0.1],  # Left elbow
    [0.1, -0.1, 0.1],  # Right elbow
    [-0.1, 0.1, 0.1],  # Left knee
    [0.1, 0.1, 0.1],  # Right knee
    [-0.05, -0.05, 0.05],  # Left wrist
    [0.05, -0.05, 0.05],  # Right wrist
    [-0.05, 0.05, 0.05],  # Left ankle
    [0.05, 0.05, 0.05],  # Right ankle
])

# Define the rotation angles
theta = np.linspace(0, 2*np.pi, 100)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(-0.5, 0.5)
ax.set_facecolor('black')
ax.set_axis_off()

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_zlim(-0.5, 0.5)
    ax.set_facecolor('black')
    ax.set_axis_off()
    
    # Rotate the points
    rotation_matrix = np.array([
        [np.cos(theta[i]), -np.sin(theta[i]), 0],
        [np.sin(theta[i]), np.cos(theta[i]), 0],
        [0, 0, 1]
    ])
    
    rotated_points = np.dot(points, rotation_matrix)
    
    # Plot the points
    for j in range(15):
        ax.plot(rotated_points[j, 0], rotated_points[j, 1], rotated_points[j, 2], 'o', markersize=10, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
