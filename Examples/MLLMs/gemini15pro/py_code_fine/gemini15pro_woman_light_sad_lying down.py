
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# The data represents the lying down pose across several frames
num_frames = 20
num_points = 15

x = np.random.rand(num_frames, num_points) * 2 - 1  # Range: -1 to 1
y = np.random.rand(num_frames, num_points) * 2 - 1  # Range: -1 to 1

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5]) # adjust according to x values, similarly for y
ax.set_ylim([-1.5, 1.5])
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')

# Update function for the animation
def update(frame):
    points.set_data(x[frame], y[frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(num_frames), blit=True, interval = 100)

#To save as a gif
#ani.save('lying_down.gif', writer='pillow')
plt.show()

