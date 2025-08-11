
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
light_radius = 0.2
jump_height = 1.0
jump_duration = 1.0  # seconds
num_frames = 60

# Create a time array for the animation
time = np.linspace(0, jump_duration, num_frames)

# Initialize the positions of the lights
positions = np.zeros((num_lights, 2, num_frames))

# Define the motion of the lights
for i in range(num_lights):
    # Time-varying position for each light
    t = time / jump_duration
    positions[i, 0, :] = np.interp(t, [0, 0.5, 1], [0, 0, 1])
    positions[i, 1, :] = np.interp(t, [0, 0.5, 1], [i - num_lights / 2, num_lights / 2, i - num_lights / 2])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-num_lights / 2, num_lights / 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((0, i - num_lights / 2), light_radius, color='white')
    lights.append(light)
    ax.add_artist(light)

# Animation function
def animate(frame):
    for i in range(num_lights):
        lights[i].center = (positions[i, 0, frame], positions[i, 1, frame])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/30, repeat=False)

# Show the animation
plt.show()
