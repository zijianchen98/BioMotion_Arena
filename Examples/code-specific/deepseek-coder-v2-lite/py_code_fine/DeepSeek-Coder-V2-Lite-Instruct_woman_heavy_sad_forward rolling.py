
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
    # Update positions for the next frame
    for i in range(num_lights):
        positions[i, 1] -= 0.05  # Move down
        positions[i, 0] += 0.02  # Slight horizontal movement

    # Scatter plot for the lights
    scat.set_offsets(positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis

# Create the scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*100, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
