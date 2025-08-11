
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
n_points = 15

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define the initial positions of the points (body joints)
points = np.zeros((n_points, 2))

# Positions for a simple human figure representation
# Head, shoulders, elbows, hips, knees, and feet
points[0] = [0, 6]    # Head
points[1] = [0, 5]    # Neck
points[2] = [-0.5, 4] # Left shoulder
points[3] = [0.5, 4]  # Right shoulder
points[4] = [-0.7, 3] # Left elbow
points[5] = [0.7, 3]  # Right elbow
points[6] = [0, 3]    # Torso
points[7] = [-0.5, 2] # Left hip
points[8] = [0.5, 2]  # Right hip
points[9] = [-0.3, 1] # Left knee
points[10] = [0.3, 1] # Right knee
points[11] = [-0.3, 0]# Left foot
points[12] = [0.3, 0] # Right foot
points[13] = [-1, 4]  # Weight left
points[14] = [1, 4]   # Weight right

# Create a scatter plot for the points
point_lights = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Animation function
def update(frame):
    # Clear the points
    points[:, 1] = points[:, 1] * (1 - 0.05) + (np.sin(frame / 10) + 1) * 0.1  # vertical motion
    points[:, 0] += 0.1  # horizontal motion to the right

    # Update positions for a jumping motion
    points[0, 1] += np.sin(frame / 10) * 0.5  # head bobbing
    points[1, 1] += np.sin(frame / 10) * 0.5
    points[2:6, 1] += np.sin(frame / 10) * 0.3

    # Update the scatter plot with the new points
    point_lights.set_offsets(points)
    return point_lights,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
