
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the happy man
point_lights = np.array([
    [0, 10],  # Head
    [-5, 8],  # Left shoulder
    [5, 8],   # Right shoulder
    [-10, 5], # Left elbow
    [10, 5],  # Right elbow
    [-15, 0], # Left hand
    [15, 0],  # Right hand
    [0, -5],  # Waist
    [-3, -10],# Left hip
    [3, -10], # Right hip
    [-8, -15],# Left knee
    [8, -15], # Right knee
    [-12, -20],# Left ankle
    [12, -20], # Right ankle
    [0, -25]   # Feet
])

# Define the rotation angles for the point-lights
rotation_angles = np.linspace(0, 2*np.pi, 128)

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-20, 20)
ax.set_ylim(-30, 15)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-30, 15)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Rotate the point-lights
    rotated_point_lights = np.copy(point_lights)
    for i in range(len(rotated_point_lights)):
        if i in [1, 2, 3, 4, 5, 6]:  # Upper body
            rotated_point_lights[i, 0] = point_lights[i, 0] * np.cos(rotation_angles[frame]) - point_lights[i, 1] * np.sin(rotation_angles[frame])
            rotated_point_lights[i, 1] = point_lights[i, 0] * np.sin(rotation_angles[frame]) + point_lights[i, 1] * np.cos(rotation_angles[frame])
        elif i in [7, 8, 9, 10, 11, 12, 13, 14]:  # Lower body
            rotated_point_lights[i, 0] = point_lights[i, 0] * np.cos(rotation_angles[frame]) - point_lights[i, 1] * np.sin(rotation_angles[frame])
            rotated_point_lights[i, 1] = point_lights[i, 0] * np.sin(rotation_angles[frame]) + point_lights[i, 1] * np.cos(rotation_angles[frame])

    # Plot the rotated point-lights
    ax.scatter(rotated_point_lights[:, 0], rotated_point_lights[:, 1], color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(rotation_angles), interval=50)

plt.show()
