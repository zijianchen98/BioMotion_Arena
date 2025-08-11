
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 30
light_radius = 0.2
jump_height = 1.0
jump_distance = 1.0
jump_duration = 1.0

# Initialize positions
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-jump_distance, jump_distance, num_lights)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-jump_distance - 1, jump_distance + 1)
ax.set_ylim(-1, jump_height + 1)

# Initialize lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], 0), light_radius, color='white')
    lights.append(light)
    ax.add_artist(light)

# Update function for each frame
def update(frame):
    t = frame / (num_frames - 1)
    for i in range(num_lights):
        y = jump_height * np.sin(t * np.pi)
        positions[i, 1] = y
        lights[i].center = (positions[i, 0], y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Set up plot
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Show the animation
plt.show()
