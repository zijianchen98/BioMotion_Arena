
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Set up figure and axis
fig, ax = plt.subplots()

# Set up axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Set up point-lights
point_lights = []
for i in range(15):
    x = np.random.uniform(-10, 10)
    y = np.random.uniform(-10, 10)
    z = np.random.uniform(-10, 10)
    point_lights.append(ax.plot(x, y, z, 'o', color='white')[0])

# Set up initial positions
angles = np.random.uniform(0, 2*np.pi, 15)
for i, light in enumerate(point_lights):
    light.set_data([0], [0])
    light.set_3d_properties([0], [0])
    light.set_angle(angles[i])

# Function to update animation
def update(angle):
    global angles
    angles = np.roll(angles, -1)
    angles[-1] = angle
    for i, light in enumerate(point_lights):
        light.set_angle(angles[i])
        light.set_data([np.cos(angles[i]), np.sin(angles[i])])
        light.set_3d_properties([0], [0])

# Function to turn around
def turn_around(angle):
    global angles
    angles = np.array([angle] * 15)
    for i, light in enumerate(point_lights):
        light.set_angle(angles[i])
        light.set_data([np.cos(angles[i]), np.sin(angles[i])])
        light.set_3d_properties([0], [0])

# Create animation
ani = animation.FuncAnimation(fig, turn_around, frames=np.linspace(0, 2*np.pi, 100), interval=20)

plt.show()
