
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the parameters for the animation
num_points = 15
frames = 100
fall_height = 1.5
roll_distance = 3.0
gravity = 0.1

# Define the starting positions of the points
points = np.array([
    [0, 0.5],  # head
    [-0.2, 0.3], [0.2, 0.3],  # arms
    [-0.15, 0.1], [0.15, 0.1],  # elbow positions
    [-0.1, -0.2], [0.1, -0.2],  # knee positions
    [-0.2, -0.4], [0.2, -0.4],  # feet positions
    [-0.3, -0.7], [0.3, -0.7],  # extra feet points at end
    [-0.25, -0.6], [0.25, -0.6],  # mid-calf points
    [-0.05, -0.5], [0.05, -0.5],  # hand points
])

# Function to update the points for each frame
def update(frame):
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 1)
    ax.set_facecolor('black')

    # Calculate the movement of the points
    roll_angle = np.pi * (frame / frames)
    translation = [0, -gravity * frame * (frame / frames)]  # fall with gravity
    transformed_points = points.copy()

    # Apply forward roll transformation
    for i in range(len(transformed_points)):
        transformed_points[i, 0] += np.sin(roll_angle) * roll_distance
        transformed_points[i, 1] += translation[1]
    
    ax.scatter(transformed_points[:, 0], transformed_points[:, 1], color='white')
    return ax,

# Set up the figure and axis
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=False)

# Show the animation
plt.show()
