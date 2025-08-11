
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
# Each point-light is represented by its x and y coordinates
point_lights = np.array([
    [0.0, 0.5],  # Head
    [-0.2, 0.6],  # Left shoulder
    [0.2, 0.6],  # Right shoulder
    [-0.3, 0.4],  # Left elbow
    [0.3, 0.4],  # Right elbow
    [-0.4, 0.2],  # Left wrist
    [0.4, 0.2],  # Right wrist
    [0.0, 0.0],  # Hip
    [-0.2, -0.2],  # Left knee
    [0.2, -0.2],  # Right knee
    [-0.3, -0.4],  # Left ankle
    [0.3, -0.4],  # Right ankle
    [-0.1, 0.3],  # Left breast
    [0.1, 0.3],  # Right breast
    [0.0, -0.1]  # Belly button
])

# Define the rotation angles for the turning around action
rotation_angles = np.linspace(0, np.pi, 100)

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Initialize the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Rotate the point-lights
    rotated_point_lights = np.copy(point_lights)
    for i in range(len(point_lights)):
        x, y = point_lights[i]
        rotated_x = x * np.cos(rotation_angles[frame]) - y * np.sin(rotation_angles[frame])
        rotated_y = x * np.sin(rotation_angles[frame]) + y * np.cos(rotation_angles[frame])
        rotated_point_lights[i] = [rotated_x, rotated_y]
    
    # Plot the rotated point-lights
    ax.scatter(rotated_point_lights[:, 0], rotated_point_lights[:, 1], c='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(rotation_angles), interval=50)

plt.show()
