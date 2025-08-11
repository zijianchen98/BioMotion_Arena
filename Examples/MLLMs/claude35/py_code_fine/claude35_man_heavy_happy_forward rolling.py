
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100  # Total number of frames in the animation
width, height = 10, 10  # Size of the background

# Point positions (initial configuration)
def initial_positions():
    # Create a point-light configuration mimicking a happy man
    return np.array([[0, 3], [2, 5], [0, 7], [-2, 5], 
                     [0, 1], [1, 0], [-1, 0], [2, -1],
                     [-2, -1], [1, -2], [-1, -2],
                     [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]])

# Function to update point positions for rolling motion
def update_positions(frame, points, line):
    # Simple forward rolling motion parameters 
    # Create a rolling effect by shifting the y-position
    y_shift = np.sin(np.linspace(0, 4*np.pi, frames) + frame/10) * 0.4
    points[:, 1] -= y_shift
    points[:, 0] += 0.01  # Simulate the forward motion
    line.set_data(points[:, 0], points[:, 1])
    return line,

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-width, width)
ax.set_ylim(-height, height)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initial points
points = initial_positions()
line, = ax.plot(points[:, 0], points[:, 1], 'wo', markersize=10)  # 'wo' means white color

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames, fargs=(points, line),
                              interval=50, blit=True)

# Show the animation
plt.show()
