
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Radius of each point-light
radius = 0.5

# Define the initial positions (x, y) of point-lights
initial_positions = np.random.rand(num_points, 2)

# Define the paths of motion (theta angle: 0 to 2*pi radians)
theta = np.linspace(0, 2 * np.pi, 60)

# Velocity of point-lights (adjustable to simulate different speeds)
velocity = 0.4

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_axis_off()

# Create scatter plot for initial positions
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=radius, c='white')

def update(frame):
    # Compute the new positions
    new_positions = initial_positions - velocity * np.sin(theta[frame % len(theta)])
    initial_positions = new_positions

    # Update the scatter plot positions
    scat.set_offsets(initial_positions)

    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
