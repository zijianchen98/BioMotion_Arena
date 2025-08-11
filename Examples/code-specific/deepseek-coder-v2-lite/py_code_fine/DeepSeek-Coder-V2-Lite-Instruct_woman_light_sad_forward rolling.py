
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-1, 1, num_lights)
positions[:, 1] = 1

# Define the animation function
def animate(frame):
    # Update positions for forward rolling
    for i in range(num_lights):
        positions[i, 1] -= 0.05  # Move down
        positions[i, 0] += 0.02  # Move slightly forward
        if positions[i, 1] < -1:
            positions[i, 1] = 1
            positions[i, 0] = np.linspace(-1, 1, num_lights)[i]

    # Clear the plot
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Plot the lights
    for pos in positions:
        circle = plt.Circle(pos, light_radius, color='white')
        ax.add_artist(circle)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
