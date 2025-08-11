
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights and the number of frames in the animation
num_lights = 15
num_frames = 100

# Initialize the positions of the point-lights in a simple pattern that suggests jumping
# Each point-light is represented by its (x, y) position
light_positions = np.array([[[0, 0]] * num_lights for _ in range(num_frames)])

# Calculate the general jump motion for each frame
# Assuming the jump starts at (0, 0), goes up and forward, and then comes back down
for i in range(num_frames):
    t = i / (num_frames - 1)  # Normalize time to the range [0, 1]
    # Calculate a parabolic jump with some forward movement
    jump_height = 4 * np.sin(np.pi * t)
    forward_jump = 6 * t
    for j in range(num_lights):
        angle = 2 * np.pi * j / num_lights  # Spread lights around in a circle
        light_positions[i][j] = [forward_jump * np.cos(angle), jump_height]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 10)
ax.set_facecolor('black')  # Set background color to black
ax.set_xticks([])
ax.set_yticks([])  # Hide axes ticks

# Create scatter plot for the point-lights
scatter = ax.scatter(light_positions[0][:, 0], light_positions[0][:, 1], c='white', s=30)

# Animation update function
def update(frame):
    scatter.set_offsets(light_positions[frame])
    return scatter,

# Create the animation by calling FuncAnimation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
