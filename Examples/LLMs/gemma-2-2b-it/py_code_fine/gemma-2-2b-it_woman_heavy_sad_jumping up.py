
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Define the position of the point lights
positions = np.array([
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0],
    [9, 0],
    [10, 0],
    [11, 0],
    [12, 0],
    [13, 0],
    [14, 0],
    [15, 0],
])

# Define the initial position of the point lights
initial_positions = positions

# Define the animation function
def animate(i):
    # Update the positions of the point lights
    for j in range(num_lights):
        positions[j] = positions[j] + np.array([0, 0.1 * np.sin(i * 0.05 * j)])

    # Update the plot
    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
