
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
light_positions = np.random.rand(num_lights, 2) * 10

# Define the target position of the point lights
target_position = np.array([10, 10])

# Define the velocity of the point lights
velocity = np.random.rand(num_lights, 2) * 0.1

# Define the animation function
def animate(i):
    global light_positions

    # Update the position of each point light
    for j in range(num_lights):
        light_positions[j] += velocity[j]

        # Keep the point light within the boundaries
        light_positions[j] = np.clip(light_positions[j], 0, 10)

    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Plot the point lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], color='white')

    # Plot the target position
    ax.scatter(target_position[0], target_position[1], color='red', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=16)

# Show the animation
plt.show()
