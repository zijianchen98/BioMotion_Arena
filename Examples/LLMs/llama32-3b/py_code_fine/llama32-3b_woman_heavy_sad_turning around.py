
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
num_lights = 15
light_positions = np.random.rand(num_lights, 3) * 2 - 1  # Random position between -1 and 1
light_sizes = np.random.rand(num_lights) * 0.1 + 0.05  # Random size between 0.05 and 0.15
light_colors = np.random.rand(num_lights, 3)  # Random color
action = 'turning around'  # Action

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the lights
lights = ax.scatter(light_positions[:, 0], light_positions[:, 1], light_positions[:, 2], s=light_sizes*100, c=light_colors, marker='o', alpha=0.8)

# Define the rotation angles
angle_x = 0
angle_y = 0

# Animation function
def animate(i):
    global angle_x, angle_y
    
    # Rotate the lights
    rotation_matrix = np.array([[np.cos(angle_x), -np.sin(angle_x), 0],
                                 [np.sin(angle_x), np.cos(angle_x), 0],
                                 [0, 0, 1]])
    rotation_matrix = np.dot(rotation_matrix, np.array([[np.cos(angle_y), 0, 0],
                                                         [0, np.cos(angle_y), 0],
                                                         [0, 0, 1]]))
    
    ax.clear()
    ax.set_facecolor('black')
    
    lights = ax.scatter(light_positions[:, 0]*rotation_matrix[0, 0] + light_positions[:, 1]*rotation_matrix[1, 0] + light_positions[:, 2]*rotation_matrix[2, 0],
                        light_positions[:, 0]*rotation_matrix[0, 1] + light_positions[:, 1]*rotation_matrix[1, 1] + light_positions[:, 2]*rotation_matrix[2, 1],
                        light_positions[:, 0]*rotation_matrix[0, 2] + light_positions[:, 1]*rotation_matrix[1, 2] + light_positions[:, 2]*rotation_matrix[2, 2],
                        s=light_sizes*100, c=light_colors, marker='o', alpha=0.8)
    
    # Update the rotation angles
    angle_x += 0.01
    angle_y += 0.01
    
    # Set the limits of the axis
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

# Animate the lights
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
