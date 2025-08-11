
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
x = np.array([0, -20, 20, -20, 20, -10, 0, 10, -5, 5, -15, 15, -5, 5, 0])
y = np.array([100, 70, 70, 40, 40, 40, 40, 40, 10, 10, -20, -20, -50, -50, -80])

# Define the number of frames in the animation
num_frames = 36

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-50, 50])
ax.set_ylim([-100, 120])
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=5)

# Define the animation function
def animate(i):
    angle = i * 10 * np.pi / 180  # Rotate by 10 degrees per frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(rotation_matrix, np.vstack((x, y)))
    points.set_data(rotated_points[0], rotated_points[1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation 
plt.show()


