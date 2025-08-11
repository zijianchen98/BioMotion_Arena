
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_point_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.array([
    [-0.5, 0.5],  # head
    [-0.3, 0.4],  # shoulder
    [-0.1, 0.3],  # upper arm
    [0.1, 0.2],   # forearm
    [0.3, 0.1],   # hand
    [-0.5, -0.1], # hip
    [-0.3, -0.3], # upper leg
    [-0.1, -0.5], # lower leg
    [0.1, -0.7],  # foot
    [0.3, -0.5],  # other foot
    [-0.4, 0.2],  # upper body
    [-0.2, 0.1],  # body
    [0.0, 0.0],   # center of mass
    [-0.2, -0.2], # lower body
    [0.2, -0.2]   # other lower body
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the positions of the point-lights at the current frame
    positions = initial_positions.copy()
    for i in range(num_point_lights):
        # Simulate the forward rolling motion
        if i < 5:  # upper body
            positions[i, 0] += 0.01 * np.sin(frame / 10.0)
            positions[i, 1] -= 0.01 * np.cos(frame / 10.0)
        else:  # lower body
            positions[i, 0] -= 0.01 * np.sin(frame / 10.0)
            positions[i, 1] += 0.01 * np.cos(frame / 10.0)

    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
