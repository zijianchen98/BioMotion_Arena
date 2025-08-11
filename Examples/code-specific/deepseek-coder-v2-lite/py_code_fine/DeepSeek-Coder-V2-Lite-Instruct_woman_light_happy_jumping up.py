
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 30
radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2, num_frames))
positions[:, 0, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1, 0] = 0.1

# Animation function
def animate(frame):
    for i in range(num_lights):
        positions[i, 1, frame] = positions[i, 1, frame - 1] + 0.03 * (1 if frame % 2 == 0 else -1)
        if positions[i, 1, frame] > 0.9:
            positions[i, 1, frame] = 0.9
            positions[i, 1, frame - 1] = 0.1
        elif positions[i, 1, frame] < 0.1:
            positions[i, 1, frame] = 0.1
            positions[i, 1, frame - 1] = 0.9

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0, 0], positions[i, 1, 0]), radius, color='white')
    lights.append(light)
    ax.add_artist(light)

# Animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=100, repeat=False)

plt.show()
