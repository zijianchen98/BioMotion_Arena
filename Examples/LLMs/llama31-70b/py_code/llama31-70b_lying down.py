
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the number of frames in the animation
n_frames = 100

# Define the time points for each frame
t = np.linspace(0, 2 * np.pi, n_frames)

# Define the x and y coordinates of the point-lights at each frame
# Each point-light will represent a joint in the body (e.g. head, shoulders, elbows, etc.)
# The coordinates are based on a simple sinusoidal motion to represent a lying down action
x = np.zeros((n_points, n_frames))
y = np.zeros((n_points, n_frames))

# Head
x[0, :] = np.cos(t) + 0.5
y[0, :] = np.sin(t) + 0.5

# Shoulders
x[1, :] = np.cos(t) + 0.2
y[1, :] = np.sin(t) + 0.3
x[2, :] = np.cos(t) - 0.2
y[2, :] = np.sin(t) + 0.3

# Elbows
x[3, :] = np.cos(t) + 0.2
y[3, :] = np.sin(t) + 0.1
x[4, :] = np.cos(t) - 0.2
y[4, :] = np.sin(t) + 0.1

# Hands
x[5, :] = np.cos(t) + 0.1
y[5, :] = np.sin(t) + 0.0
x[6, :] = np.cos(t) - 0.1
y[6, :] = np.sin(t) + 0.0

# Hips
x[7, :] = np.cos(t) + 0.0
y[7, :] = np.sin(t) - 0.2
x[8, :] = np.cos(t) - 0.0
y[8, :] = np.sin(t) - 0.2

# Knees
x[9, :] = np.cos(t) + 0.0
y[9, :] = np.sin(t) - 0.4
x[10, :] = np.cos(t) - 0.0
y[10, :] = np.sin(t) - 0.4

# Ankles
x[11, :] = np.cos(t) + 0.0
y[11, :] = np.sin(t) - 0.6
x[12, :] = np.cos(t) - 0.0
y[12, :] = np.sin(t) - 0.6

# Feet
x[13, :] = np.cos(t) + 0.0
y[13, :] = np.sin(t) - 0.7
x[14, :] = np.cos(t) - 0.0
y[14, :] = np.sin(t) - 0.7

# Create a new figure
fig, ax = plt.subplots()

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Set the limits of the plot to the size of the animation
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Remove the axes
ax.set_axis_off()

# Initialize the plot with the first frame
scatter = ax.scatter(x[:, 0], y[:, 0], s=50, c='w')

# Set the background color to black
fig.patch.set_facecolor('black')
ax.patch.set_facecolor('black')

# Function to update the plot for each frame
def update(i):
    scatter.set_offsets(np.column_stack((x[:, i], y[:, i])))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50)

plt.show()
