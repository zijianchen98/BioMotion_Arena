
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and the walking path
num_lights = 15
path_length = 100
frame_count = 100

# Create a set of points representing the lights in a walking configuration
# Initial positions (in a normalized way)
initial_positions = np.array([
    [0, 1],  # head
    [-0.5, 0.5], [0.5, 0.5],  # shoulders
    [-0.5, 0], [0.5, 0],  # arms
    [-0.5, -0.5], [0.5, -0.5],  # hips
    [-0.3, -1], [0.3, -1],  # knees
    [-0.2, -2], [0.2, -2],  # feet
    [-0.2, -2.5], [0.2, -2.5],  # heels
    [-0.5, -1.5], [0.5, -1.5],  # mid thigh
    [0, -3]  # center of the body
])

# Create a walking motion for each point
def create_walking_motion(frame_count):
    # Generate the y positions for walking
    y_positions = np.zeros((frame_count, num_lights))
    for i in range(frame_count):
        y_positions[i] = initial_positions[:, 1] + (0.1 * np.sin(np.linspace(0, 2 * np.pi, num_lights) + i * 0.1))
    # Add walking effect by modifying x positions
        x_shift = (0.5 * np.sin(i * 0.2))
        y_positions[i] += x_shift

    return y_positions

# Get the points motions
walking_motion = create_walking_motion(frame_count)

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 1)
ax.axis('off')  # Hide the axes

# Points that will be animated
points, = ax.plot([], [], 'wo', markersize=10)

# Update function for the animation
def update(frame):
    x_data = initial_positions[:, 0]
    y_data = walking_motion[frame]
    points.set_data(x_data, y_data)
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frame_count, blit=True, interval=50)

# Display the animation
plt.show()
