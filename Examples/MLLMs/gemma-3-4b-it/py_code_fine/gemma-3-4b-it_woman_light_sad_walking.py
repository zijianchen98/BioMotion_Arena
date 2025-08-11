
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 500  # Frames
fps = 30
dt = 1 / fps

# Define the walking motion parameters
amplitude = 0.2
frequency = 3
phase = 0

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((0, 0), 0.03, color='white', alpha=0.8)
    lights.append(light)
    ax.add_light(light)

# Animation function
def animate(frame):
    for light in lights:
        light.set_data(np.sin(2 * np.pi * frequency * frame / duration) * amplitude * np.cos(phase),
                       np.sin(2 * np.pi * frequency * frame / duration) * amplitude * np.sin(phase))
        phase += dt
        if phase > 2 * np.pi:
            phase -= 2 * np.pi

    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation
ani.save('walking_sadwoman.gif', writer='pillow', fps=fps)

plt.show()
