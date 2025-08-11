
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject's walking motion parameters
num_points = 15
frames = 60
frame_rate = 30
time = np.linspace(0, frames / frame_rate, frames)
x_center = np.sin(time * 2 * np.pi / 4) * 0.5 + 0.5
y_center = np.cos(time * 2 * np.pi / 4) * 0.5 + 0.5
radius = 0.05
speed = 0.01

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point lights
point_lights = [plt.Circle((0, 0), radius, color='white') for _ in range(num_points)]
for light in point_lights:
    ax.add_artist(light)

def update(frame):
    for i, light in enumerate(point_lights):
        angle = (i / num_points + time[frame]) * 2 * np.pi
        x = x_center[frame] + np.cos(angle) * speed
        y = y_center[frame] + np.sin(angle) * speed
        light.center = (x, y)

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
