
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights
num_lights = 15

# Define the initial positions of the lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each frame
def target_positions(frame):
    angle = np.radians(frame * 2)  # Rotate around the center
    x_offset = np.cos(angle)
    y_offset = np.sin(angle)
    return np.array([[x + x_offset, y + y_offset] for x, y in initial_positions])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the scatter plot for the lights
lights, = ax.plot([], [], 'o', color='white', markersize=5)

# Update function for the animation
def update(frame):
    positions = target_positions(frame)
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
sad_woman_animation = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50, blit=True)

# Show the animation
plt.show()
