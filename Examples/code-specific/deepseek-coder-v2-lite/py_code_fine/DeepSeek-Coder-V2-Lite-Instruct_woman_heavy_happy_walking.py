
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

# Animation function
def animate(frame):
    for i in range(num_lights):
        positions[i, 1] -= 0.05  # Move lights down
        if positions[i, 1] < -1:
            positions[i, 1] = 1

    scat.set_offsets(positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*100, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
