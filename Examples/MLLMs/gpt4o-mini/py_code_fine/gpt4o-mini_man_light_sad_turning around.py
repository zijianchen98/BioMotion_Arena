
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Generate initial positions for the point lights
num_points = 15
points = np.zeros((num_points, 2))
# Defining positions based on a rough skeletal outline of a sad man turning around
# Skeleton coordinates for pointlights mapped to a sadman model
# Here we will only place points for the turning motion.
points[:, 0] = np.array([0, 0, -0.5, 0.5, 0, 0, -0.5, 0.5, -0.3, 0.3, -0.1, 0.1, 0, 0])
points[:, 1] = np.array([-3, -1, -1.5, -1.5, 0, 0, 0.5, 0.5, 1, 1, 2, 2, 3, 3, 4])

# Create a point collection
points_scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def update(frame):
    # Rotation angle
    angle = np.deg2rad(frame)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    rotated_points = points @ rotation_matrix.T
    points_scat.set_offsets(rotated_points)
    return points_scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), blit=True, interval=50)

# Show the animation
plt.show()
