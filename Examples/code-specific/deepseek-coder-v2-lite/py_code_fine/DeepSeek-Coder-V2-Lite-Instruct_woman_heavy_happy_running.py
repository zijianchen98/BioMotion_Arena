
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-1, 1, num_lights)
positions[:, 1] = 1

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    # Update positions
    positions[:, 1] -= 0.05  # Move all lights down
    if positions[0, 1] < -1:  # Reset positions when lights go out of view
        positions[:, 1] = 1
        positions[:, 0] = np.linspace(-1, 1, num_lights)

    # Update the data
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
