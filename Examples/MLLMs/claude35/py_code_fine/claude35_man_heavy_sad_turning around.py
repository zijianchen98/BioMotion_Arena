
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize point-lights positions
points = np.zeros((num_points, 2))

# Define initial positions for the point-lights to represent upper body
upper_body_indices = np.array([0, 1, 2, 3, 4, 5, 6])
lower_body_indices = np.array([7, 8, 9, 10, 11, 12, 13, 14])

# Create the point-light objects
point_lights, = ax.plot(points[:, 0], points[:, 1], 'o', color='white', markersize=10)

# Function to update the animation
def update(frame):
    # Parameters for the sad man turning around
    angle = np.radians(frame)  # Convert frame count to radians
    weight_sway = 0.2 * np.sin(np.radians(frame))  # Simulate weight sway
    
    # Update positions of upper body
    points[upper_body_indices, 0] = np.array([-0.5, 0, 0.5, -0.5, 0, 0.5, 0]) * np.cos(angle)  # X coordinates
    points[upper_body_indices, 1] = np.array([1, 0.5, 1, 1.5, 1.5, 1.5, 1]) + weight_sway  # Y coordinates
    
    # Update positions of lower body
    points[lower_body_indices, 0] = np.array([-0.25, 0, 0.25, -0.25, 0.25, 0, 0]) * np.cos(angle)  # X coordinates
    points[lower_body_indices, 1] = np.array([0, -0.5, -0.5, -1, -1, -1, -1.5]) + weight_sway  # Y coordinates

    # Update point-light objects
    point_lights.set_data(points[:, 0], points[:, 1])
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=100, blit=True)

# Display the plot
plt.show()
