
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Function to update positions for bowing motion
def update_positions(frame_number):
    angle = (frame_number / num_frames) * np.pi
    amplitude = 0.1
    for i in range(num_lights):
        positions[i, 1] = 0.5 + amplitude * np.sin(angle + i * (2 * np.pi / num_lights))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights as scatter plot
lights, = ax.plot([], [], 'wo', markersize=10)

# Set up the animation
def init():
    lights.set_data([], [])
    return lights,

def animate(frame_number):
    update_positions(frame_number)
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
