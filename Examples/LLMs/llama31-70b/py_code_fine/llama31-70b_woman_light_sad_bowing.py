
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the number of frames in the animation
n_frames = 100

# Define the time array
time = np.linspace(0, 2 * np.pi, n_frames)

# Define the x and y coordinates of the point-lights
# The coordinates are defined to represent a sad woman bowing
x = np.zeros((n_points, n_frames))
y = np.zeros((n_points, n_frames))

# Define the initial positions of the point-lights
# The initial positions are defined to represent a standing person
x[:, 0] = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 0.5, 0.3, 0.1, 0.5, 0.7, 0.9, 0.5, 0.3, 0.1, 0.5])
y[:, 0] = np.array([0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1])

# Define the motion of the point-lights
# The motion is defined to represent a bowing action
for i in range(1, n_frames):
    x[:, i] = x[:, 0] + np.sin(time[i]) * np.array([0.1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.2, 0.3, 0.2, 0.1])
    y[:, i] = y[:, 0] - np.sin(time[i]) * np.array([0.1, 0.2, 0.3, 0.2, 0.1, 0.3, 0.2, 0.1, 0.2, 0.3, 0.2, 0.1, 0.2, 0.3, 0.2])

# Create a new figure
fig, ax = plt.subplots()

# Set the aspect ratio of the plot to 'equal' to ensure the animation is not distorted
ax.set_aspect('equal')

# Set the background color to black
ax.set_facecolor('black')

# Initialize the plot with the initial positions of the point-lights
scatter = ax.scatter(x[:, 0], y[:, 0], s=10, c='white')

# Set the limits of the plot to the range of the point-lights
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)

# Define the animation function
def animate(i):
    scatter.set_offsets(np.column_stack((x[:, i], y[:, i])))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

# Display the animation
plt.show()
