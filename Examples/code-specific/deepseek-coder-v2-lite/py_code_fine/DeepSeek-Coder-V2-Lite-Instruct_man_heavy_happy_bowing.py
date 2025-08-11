
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

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Plot the lights
points, = ax.plot([], [], 'wo', markersize=light_radius*50)

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Call the animate function for each frame
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
