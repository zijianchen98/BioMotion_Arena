
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
# These are approximate coordinates based on the provided image
initial_positions = np.array([
    [0, 4], [-1, 3], [1, 3],
    [-1, 2], [0, 2], [1, 2],
    [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1],
    [-1, 0], [1, 0],
    [-1, -2], [1, -2]
])

# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)  # Adjust limits as needed
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black
points, = ax.plot([], [], 'wo', markersize=5)  # White dots

# Function to update the positions of the points for each frame
def animate(i):
    angle = (i / num_frames) * 2 * np.pi  # Rotate over one full circle

    # Apply rotation to the initial positions
    rotated_positions = np.dot(initial_positions, np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ]))


    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, blit=True)



plt.show()


