
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off the axis

# Number of points
num_points = 15

# Initial coordinates for the "happy man" lying down
# Configure the positions (x, y) of the point lights
positions = np.array([
    [0, 0.1],   # head
    [0.1, 0],   # right shoulder
    [-0.1, 0],  # left shoulder
    [0.22, -0.4],# right hand
    [-0.22, -0.4],# left hand
    [0.1, -0.3], # right hip
    [-0.1, -0.3],# left hip
    [0.2, -0.7], # right knee
    [-0.2, -0.7],# left knee
    [0.1, -0.9], # right foot
    [-0.1, -0.9],# left foot
    [0, -0.5],   # center of body
    [0.2, -0.1], # right side of the body
    [-0.2, -0.1],# left side of the body
    [0, -0.2]    # torso
]).T

# Create scatter points
points = ax.scatter(positions[0], positions[1], color='white')

def init():
    points.set_offsets(np.zeros((num_points, 2)))  # Initialize points
    return points,

def update(frame):
    # Update the y positions for a smooth, natural motion
    y_motion = np.sin(np.linspace(0, 3*np.pi, num_points)) * 0.05
    new_positions = positions.copy()
    new_positions[1] += y_motion * np.cos(frame * 0.1)  # Variate the y position
    
    points.set_offsets(new_positions.T)  # Set new coordinates
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
