
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial coordinates of the points.  These will be adjusted
# according to a walking motion.  This is a simplified example.  For
# more realistic motion capture data would be needed.
# These are just initial values. They will be updated in the animate function.
points = np.array([
    [0.0, 2.0],  # head
    [-0.5, 1.5], # left shoulder
    [0.5, 1.5],  # right shoulder
    [-1.0, 1.0], # left elbow
    [1.0, 1.0],   # right elbow
    [-1.5, 0.5], # left hand
    [1.5, 0.5],  # right hand
    [-0.2, 1.0], # torso 1
    [0.2, 1.0],  # torso 2
    [0.0, 0.5],  # torso 3
    [-0.3, 0.0], # left hip
    [0.3, 0.0],  # right hip
    [-0.6, -0.5],# left knee
    [0.6, -0.5], # right knee
    [0.0, -1.0]  # feet position
])

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
plt.axis('off')


# Create the scatter plot
scat = ax.scatter([], [], s=20, c='white')

# Animation function
def animate(i):
    # Simulate the points moving like a person forward rolling
    # This is a very basic example.  More sophisticated motion capture data
    # would be needed for realistic animations.
    # This example just moves the points in a wave-like pattern.
    
    global points # Allows modification of points

    # Move the points
    for j in range(num_points):
        points[j, 0] += 0.01 * np.sin(i * 0.1 + j)  # Move horizontally
        points[j, 1] -= 0.01 * np.cos(i * 0.1 + j) # move down

    #Update point positions to simulate rolling
    theta = i * 0.05  #rotation angle
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    
    rotated_points = np.dot(points, rotation_matrix)

    scat.set_offsets(rotated_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

# Show the animation
plt.show()
