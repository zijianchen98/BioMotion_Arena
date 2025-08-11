
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-lights
num_points = 15
points = np.array([
    [0, 0],  # head
    [-0.2, 0.5],  # left shoulder
    [0.2, 0.5],  # right shoulder
    [-0.3, 0.2],  # left elbow
    [0.3, 0.2],  # right elbow
    [-0.4, -0.2],  # left hand
    [0.4, -0.2],  # right hand
    [0, 0.7],  # torso
    [0, 0.9],  # hip
    [-0.2, 1.1],  # left knee
    [0.2, 1.1],  # right knee
    [-0.3, 1.3],  # left ankle
    [0.3, 1.3],  # right ankle
    [-0.1, 1.5],  # left foot
    [0.1, 1.5],  # right foot
])

# Define the jumping motion
def jumping_motion(t):
    # Define the motion parameters
    jump_height = 0.5
    jump_duration = 1.0
    t_jump = t % jump_duration
    
    # Calculate the vertical displacement
    if t_jump < jump_duration / 2:
        displacement = jump_height * (t_jump / (jump_duration / 2)) ** 2
    else:
        displacement = jump_height * (1 - ((t_jump - jump_duration / 2) / (jump_duration / 2)) ** 2)
    
    # Update the point positions
    new_points = points.copy()
    new_points[:, 1] += displacement
    
    # Add some arm and leg movement
    new_points[3, 1] += 0.1 * np.sin(2 * np.pi * t_jump / jump_duration)
    new_points[4, 1] += 0.1 * np.sin(2 * np.pi * t_jump / jump_duration + np.pi)
    new_points[10, 1] += 0.1 * np.sin(2 * np.pi * t_jump / jump_duration)
    new_points[11, 1] += 0.1 * np.sin(2 * np.pi * t_jump / jump_duration + np.pi)
    
    return new_points

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create the point-light plot
points_plot = ax.scatter(points[:, 0], points[:, 1], c='white', s=10)

# Define the animation function
def animate(t):
    new_points = jumping_motion(t)
    points_plot.set_offsets(new_points)
    return points_plot,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 10, 0.1), interval=100, blit=True)

plt.show()
