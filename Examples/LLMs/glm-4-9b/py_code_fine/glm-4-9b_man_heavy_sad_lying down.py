
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Parameters
num lights = 15
duration = 10
fps = 30
frames = duration * fps
background_color = 'black'

# Define the sadman's body parts (each part is a point-light)
# The positions are initially randomly positioned around a central body
body_parts = np.random.rand(num lights, 2) * 0.8 - 0.4
body_parts[:, 0] *= 2
body_parts[:, 1] *= 4

# Define the animation function
def update(frame, lights, artists):
    t = frame / frames * np.pi * 2
    # Animate sadman's body parts (e.g., a smooth oscillation)
    angles = t + np.linspace(0, 2*np.pi, num lights, endpoint=False)
    body_parts[:, 0] = np.sin(angles) * 0.5
    body_parts[:, 1] = np.cos(angles) * 2 + np.sin(t) * 0.5

    # Update light positions
    for i, light in enumerate(lights):
        light.set_center(body_parts[i])
    
    return artists

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 5)
ax.set_facecolor(background_color)
ax.axis('off')

# Create point-lights
lights = [ax.add_patch(patches.Circle(body_parts[i], radius=0.1, color='white')) for i in range(num lights)]

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, fargs=(lights, lights), interval=1000/fps, blit=True)

plt.show()
