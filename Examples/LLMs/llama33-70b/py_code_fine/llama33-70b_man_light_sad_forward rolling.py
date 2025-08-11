
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sad man
point_lights = np.array([
    [0, 0],  # head
    [-0.2, 0.2],  # left shoulder
    [0.2, 0.2],  # right shoulder
    [-0.2, -0.2],  # left hip
    [0.2, -0.2],  # right hip
    [-0.1, 0.4],  # left elbow
    [0.1, 0.4],  # right elbow
    [-0.3, 0.1],  # left hand
    [0.3, 0.1],  # right hand
    [-0.1, -0.4],  # left knee
    [0.1, -0.4],  # right knee
    [-0.2, -0.6],  # left foot
    [0.2, -0.6],  # right foot
    [0, 0.6],  # top of head
    [0, -0.8]  # bottom of body
])

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Calculate the new positions of the point-lights for the forward rolling action
    new_point_lights = point_lights.copy()
    new_point_lights[:, 0] += np.sin(i / 10.0) * 0.1
    new_point_lights[:, 1] -= np.cos(i / 10.0) * 0.1
    
    # Plot the point-lights
    ax.scatter(new_point_lights[:, 0], new_point_lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
