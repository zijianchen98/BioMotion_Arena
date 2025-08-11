
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the positions of the 15 point-lights
# The lights represent different parts of the body during the jumping action
positions = {
    'head': [1, 2),
    'left_shoulder': (2, 1),
    'right_shoulder': (2, 3),
    'left_elbow': (3, 1),
    'right_elbow': (3, 3),
    'left_wrist': (4, 1),
    'right_wrist': (4, 3),
    'left_hip': (1, 4),
    'right_hip': (3, 4),
    'left_knee': (2, 5),
    'right_knee': (2, 7),
    'left_ankle': (3, 6),
    'right_ankK': (3, 8)
}

# Define the function to update the positions of the point-lights
def update_positions(frame):
    for key, pos in positions.items():
        x_pos[0] += 1 if 'hip' in key else -1 if 'ank' in key else 0_pos[1]
    return list(positions.values())

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0.min() - 1, 15 + 1)
ax.set_ylim(0.min() - 1, 10 + 1)
ax.set_facecolor('black')

# Create the point-lights
point_lights = [plt.Circle(pos, color='white', fill=True) for pos, pos in enumerate(positions.values())]

# Add the point-lights to the plot
for light in point_lights:
    ax.add_patch(light)

# Animate the point-lights
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, interval=100, blit=True)

# Show the animation
plt.show()
