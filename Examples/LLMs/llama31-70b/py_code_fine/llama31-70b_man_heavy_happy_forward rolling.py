
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the duration of the animation
duration = 5  # seconds

# Define the frame rate
fps = 60

# Define the time points for the animation
t = np.arange(0, duration, 1/fps)

# Define the motion parameters
# For a forward rolling motion, we'll use a combination of circular and linear motion
# The point-lights will move in a circle around the center of the body, while also moving forward
radius = 0.1  # radius of the circle
amplitude = 0.05  # amplitude of the linear motion
frequency = 1  # frequency of the circular motion

# Define the initial positions of the point-lights
# We'll use a random distribution of points around the center of the body
np.random.seed(0)
x0 = np.random.uniform(-0.5, 0.5, n_points)
y0 = np.random.uniform(-0.5, 0.5, n_points)

# Define the motion of the point-lights
x = np.zeros((len(t), n_points))
y = np.zeros((len(t), n_points))
for i in range(n_points):
    x[:, i] = x0[i] + radius * np.cos(2 * np.pi * frequency * t) + amplitude * np.sin(2 * np.pi * frequency * t)
    y[:, i] = y0[i] + radius * np.sin(2 * np.pi * frequency * t) + amplitude * np.cos(2 * np.pi * frequency * t)

    # Add some randomness to the motion to make it more natural
    x[:, i] += 0.01 * np.random.randn(len(t))
    y[:, i] += 0.01 * np.random.randn(len(t))

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Set the limits of the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the plot with the first frame
points, = ax.plot(x[0, :], y[0, :], 'wo', markersize=5)

# Animation function
def animate(i):
    points.set_data(x[i, :], y[i, :])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), blit=True, interval=1000/fps)

plt.show()
