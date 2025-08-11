
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the coordinates of the points over time
# This is a simplified example and would need to be adjusted for realistic motion
def point_coordinates(t):
    # Base pose
    x = np.array([0, -1, 1, -2, 2, -1, 1, -0.5, 0.5, -2, 2, -1, 1, -0.5, 0.5])
    y = np.array([4, 3, 3, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, -2, -2])

    # Wave motion for right hand (points 4, 9, 13)
    wave_angle = np.sin(t * 2 * np.pi / 10)  # Adjust frequency as needed
    x[4] += wave_angle
    x[9] += wave_angle * 0.7
    x[13] += wave_angle * 0.7

    return x, y

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 5])
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')


# Update function for the animation
def update(frame):
    x, y = point_coordinates(frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# To save the animation as a gif (requires imagemagick)
# ani.save('biological_motion.gif', writer='imagemagick')

plt.show()

