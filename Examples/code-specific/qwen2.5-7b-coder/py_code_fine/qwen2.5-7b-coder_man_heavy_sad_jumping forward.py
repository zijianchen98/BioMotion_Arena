
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Initialize the positions of the point lights
positions = np.random.rand(num_lights, 2)

# Define the speed of each light
speeds = np.random.rand(num_lights, 2) * 0.01

# Define the function to update the positions of the point lights
def update(frame):
    global positions
    # Update the positions of the point lights
    positions += speeds
    # Wrap around the edges of the screen
    positions %= 1
    # Clear the previous frame
    ax.clear()
    # Set the face color of the axis to black
    ax.set_facecolor('black')
    # Draw the point lights
    ax.scatter(positions[:, 0], positions[:, 1], s=10, c='white')
    return []

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
