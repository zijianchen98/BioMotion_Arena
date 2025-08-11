
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
duration = 200  # milliseconds
y_down_position = -2
y_up_position = 0

# Initialize point-light positions for the 'happy man'
# A simple structure using y-coordinates and fixed x-coordinates for the points
x_coordinates = [0] * num_points
y_coordinates = np.linspace(y_up_position, y_down_position, num_points)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation function
def init():
    points.set_data([], [])
    return points,

def animate(frame):
    # Simulate downward motion of a happy man sitting down
    # Adjust y-coordinates in a smooth manner
    movement = np.interp(frame, [0, frames//2, frames], [y_up_position, y_down_position, y_down_position])
    updated_y = [movement + i for i in np.linspace(0, 1, num_points)]
    points.set_data(x_coordinates, updated_y)
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=duration/frames, blit=True)

# Show the animation
plt.show()
