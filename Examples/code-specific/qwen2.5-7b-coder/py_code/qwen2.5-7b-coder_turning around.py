
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
num_lights = 15
lights = [plt.Circle((0, 0), 0.1, color='white') for _ in range(num_lights)]
for light in lights:
    ax.add_artist(light)

# Initialize the positions of the point lights
theta = np.linspace(0, 2 * np.pi, num_lights + 1)[:-1]
x = 8 * np.cos(theta)
y = 8 * np.sin(theta)
positions = np.vstack([x, y]).T

def update(frame):
    global positions
    # Update the positions based on the rotation angle
    rotation_angle = frame / 100.0
    new_positions = np.dot(positions, [[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                      [np.sin(rotation_angle), np.cos(rotation_angle)]])
    
    # Update the positions of the point lights
    for i, light in enumerate(lights):
        light.center = tuple(new_positions[i])

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 400), interval=50, blit=False)

# Show the animation
plt.show()
