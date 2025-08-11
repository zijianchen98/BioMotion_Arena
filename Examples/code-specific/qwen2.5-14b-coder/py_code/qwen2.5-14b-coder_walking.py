
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.array([
    [0.1, 0.1], [0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1],
    [0.5, 0.2], [0.5, 0.3], [0.5, 0.4], [0.5, 0.5],
    [0.6, 0.5], [0.7, 0.5], [0.8, 0.5], [0.9, 0.5],
    [0.9, 0.4], [0.9, 0.3]
])

# Define the function to update the positions of the point lights
def update(frame):
    # Calculate the angle of rotation based on the frame number
    angle = frame * 0.05
    
    # Calculate the rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply the rotation matrix to each point light's position
    new_positions = np.dot(initial_positions, rotation_matrix)
    
    # Update the scatter plot with the new positions
    scatter.set_offsets(new_positions)
    
    return scatter,

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
