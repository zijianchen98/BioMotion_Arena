
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of point lights
num_lights = 15

# Define the colors of the point lights
colors = [(1, 1, 1)] * num_lights  # white

# Define the positions of the point lights
positions = np.random.rand(num_lights, 3) * 2 - 1  # random positions between -1 and 1

# Define the target positions of the point lights
target_positions = np.zeros((num_lights, 3))
target_positions[0, 0] = 1
target_positions[0, 1] = 0.5
target_positions[0, 2] = 0.5

target_positions[1, 0] = 1
target_positions[1, 1] = 0.5
target_positions[1, 2] = -0.5

target_positions[2, 0] = 1
target_positions[2, 1] = -0.5
target_positions[2, 2] = -0.5

target_positions[3, 0] = 0.5
target_positions[3, 1] = -0.5
target_positions[3, 2] = -0.5

target_positions[4, 0] = 0.5
target_positions[4, 1] = -0.5
target_positions[4, 2] = 0.5

target_positions[5, 0] = 0.5
target_positions[5, 1] = 0.5
target_positions[5, 2] = 0.5

target_positions[6, 0] = -0.5
target_positions[6, 1] = 0.5
target_positions[6, 2] = 0.5

target_positions[7, 0] = -0.5
target_positions[7, 1]  = 0.5
target_positions[7, 2] = -0.5

target_positions[8, 0] = -0.5
target_positions[8, 1]  = -0.5
target_positions[8, 2] = -0.5

target_positions[9, 0] = -0.5
target_positions[9, 1]  = -0.5
target_positions[9, 2] = 0.5

target_positions[10, 0] = -0.5
target_positions[10, 1]  = 0.5
target_positions[10, 2] = 0.5

target_positions[11, 0] = -0.5
target_positions[11, 1]  = 0.5
target_positions[11, 2] = -0.5

target_positions[12, 0] = 0.5
target_positions[12, 1]  = 0.5
target_positions[12, 2] = -0.5

target_positions[13, 0] = 0.5
target_positions[13, 1]  = -0.5
target_positions[13, 2] = -0.5

target_positions[14, 0] = 0.5
target_positions[14, 1]  = -0.5
target_positions[14, 2] = 0.5

# Define the velocity of the point lights
velocities = np.zeros((num_lights, 3))
velocities[0, 0] = 0.05
velocities[0, 1] = 0.05
velocities[0, 2] = 0.05

velocities[1, 0] = -0.05
velocities[1, 1] = 0.05
velocities[1, 2] = 0.05

velocities[2, 0] = -0.05
velocities[2, 1] = -0.05
velocities[2, 2] = 0.05

velocities[3, 0] = -0.05
velocities[3, 1] = -0.05
velocities[3, 2] = -0.05

velocities[4, 0] = 0.05
velocities[4, 1] = -0.05
velocities[4, 2] = -0.05

velocities[5, 0] = 0.05
velocities[5, 1] = -0.05
velocities[5, 2] = 0.05

velocities[6, 0] = 0.05
velocities[6, 1] = 0.05
velocities[6, 2] = -0.05

velocities[7, 0] = 0.05
velocities[7, 1]  = 0.05
velocities[7, 2] = 0.05

velocities[8, 0] = 0.05
velocities[8, 1]  = 0.05
velocities[8, 2] = -0.05

velocities[9, 0] = 0.05
velocities[9, 1]  = -0.05
velocities[9, 2] = -0.05

velocities[10, 0] = -0.05
velocities[10, 1]  = 0.05
velocities[10, 2] = 0.05

velocities[11, 0] = -0.05
velocities[11, 1]  = 0.05
velocities[11, 2] = -0.05

velocities[12, 0] = -0.05
velocities[12, 1]  = 0.05
velocities[12, 2] = -0.05

velocities[13, 0] = -0.05
velocities[13, 1]  = -0.05
velocities[13, 2] = -0.05

velocities[14, 0] = -0.05
velocities[14, 1]  = -0.05
velocities[14, 2] = 0.05

# Define the figure
fig = plt.figure(figsize=(6, 6))

# Define the axis
ax = fig.add_subplot(111, projection='3d')

# Define the point lights
lights = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c=colors, s=50)

# Define the target positions of the point lights
target_positions = ax.scatter(target_positions[:, 0], target_positions[:, 1], target_positions[:, 2], c='r', s=50)

# Define the velocities of the point lights
velocities = ax.quiver(positions[:, 0], positions[:, 1], positions[:, 2], velocities[:, 0], velocities[:, 1], velocities[:, 2], color='r', length=0.1)

# Define the animation function
def animate(i):
    global positions, velocities
    
    # Update the positions of the point lights
    positions = positions + velocities * 0.01
    
    # Update the velocities of the point lights
    velocities = velocities * 0.99
    
    # Update the positions of the target point lights
    target_positions = target_positions + 0.01
    
    # Update the positions of the point lights towards the target positions
    for j in range(num_lights):
        positions[j, :] = positions[j, :] + (target_positions[j, :] - positions[j, :]) * 0.01
    
    # Clear the axis
    ax.clear()
    
    # Plot the point lights
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c=colors, s=50)
    
    # Plot the target positions of the point lights
    ax.scatter(target_positions[:, 0], target_positions[:, 1], target_positions[:, 2], c='r', s=50)
    
    # Plot the velocities of the point lights
    ax.quiver(positions[:, 0], positions[:, 1], positions[:, 2], velocities[:, 0], velocities[:, 1], velocities[:, 2], color='r', length=0.1)

# Define the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Display the animation
plt.show()
