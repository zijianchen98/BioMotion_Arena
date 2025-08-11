
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each point-light
target_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.8, 0.1],
    [0.7, 0.2], [0.6, 0.3], [0.5, 0.4], [0.4, 0.5], [0.3, 0.6]
])

# Define the animation function
def animate(frame):
    # Update the positions of the point-lights
    positions = initial_positions + (target_positions - initial_positions) * frame / 100
    scat.set_offsets(positions)
    return scat,

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create a scatter plot of the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
