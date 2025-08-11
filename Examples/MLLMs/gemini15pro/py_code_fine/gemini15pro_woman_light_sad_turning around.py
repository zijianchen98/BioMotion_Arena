
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
# These positions are approximations based on the provided image
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
ax.set_xlim(-5, 5)  # Adjust limits as needed
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black

# Create the point light scatter plot
points = ax.scatter([], [], s=50, c='white')

def animate(i):
    # Calculate rotation angle based on frame number
    angle = (i / num_frames) * 2 * np.pi 

    # Apply rotation to the initial positions
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = initial_positions @ rotation_matrix

    # Update the point light positions
    points.set_offsets(rotated_positions)

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, blit=True)


# To save the animation, uncomment the following lines.
# writer = animation.PillowWriter(fps=30) # Or use other writers like FFmpegWriter
# ani.save('turning_around.gif', writer=writer)

plt.show()
