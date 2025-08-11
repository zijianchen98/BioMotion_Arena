
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Define the frames for the animation
angle, position = np.mgrid[
    np.linspace(0, np.pi / 2, 180)
, np.linspace(0, 2 * np.pi, 200)
]

# Create the animation function
def update(frame):
    # Calculate the position of each light in the current frame
    angles = 0.1 * (frame - 10) * 2 * np.pi
    points = np.array([
        np.cos(angle - angles) * np.sin(position) * (1 + np.sin((angle - angles) / 10)),
        np.sin(angle - angles) * np.sin(position) * (1 + np.sin((angle - angles) / 10))
    ])

    # Clear the current plot
    line.set_data(points[0], points[1])
    return line,

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_axis_off()

# Create the line plot object
line, = ax.plot([], [])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
