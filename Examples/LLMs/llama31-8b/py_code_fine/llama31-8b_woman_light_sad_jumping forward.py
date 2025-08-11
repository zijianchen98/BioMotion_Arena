
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the positions of the points
positions = np.zeros((num_points, 2))

# Define the movement parameters
jump_height = 0.5
jump_width = 1.0
duration = 2.0

# Define the animation function
def animate(i):
    global positions
    # Update the positions of the points
    positions[:, 0] = np.sin((i / duration) * np.pi * 2) * jump_width
    positions[:, 1] = np.sin((i / duration) * np.pi * 2) * jump_height * np.sin((i / duration) * np.pi)

    # Clear the axes
    ax.clear()

    # Plot the points
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_axis_off()
    ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white')

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * 60), interval=16)

# Show the animation
plt.show()
