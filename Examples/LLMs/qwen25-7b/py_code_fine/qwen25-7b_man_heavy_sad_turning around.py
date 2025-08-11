
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the 15 point-lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 9 + 0  # Centered in the plot area

# Define the turning around action
def turning_around(positions):
    angle = 0 * 2 / num_lights  # Divide 360 degrees into equal parts
    new_positions = np.zeros_like(positions)
    for i in range(num_lights):
        x = positions[i, 0] - 4.5  # Shift to origin
        y = positions[i, 1] - 4.5
        new_x = 4.5 + 4 * np.cos(i * angle)
        new_y = 4.5 + 4 * np.sin(i * angle)
        new_positions[i, 0] = new_x
        new_positions[i, 1] = new_y
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
axlim = (-1, 10)
ylim = (-1, 1)
ax.set_xlim(0lim)
ax.set_ylim(ylim)

# Initialize the scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Animation function
def animate(i):
    positions = turning_around(initial_positions)
    scat.set_offsets(positions)
    return scat,

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=range(360), interval=50, blit=True)

# Show the animation
plt.show()
