
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

# Define the forward rolling motion
def forward_rolling(t):
    theta = np.pi / 4 * np.sin(np.pi / 10 * t)
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return np.dot(positions, R.T)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

# Update function for the animation
def update(frame):
    for i, light in enumerate(lights):
        pos = forward_rolling(frame + i)
        light.center = (pos[0], pos[1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), repeat=True)

# Show the animation
plt.show()
