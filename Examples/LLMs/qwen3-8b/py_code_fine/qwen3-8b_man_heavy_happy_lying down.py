
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions (indices correspond to body parts)
body_parts = {
    0: 'head',        1: 'neck',         2: 'shoulder_left',
    3: 'elbow_left',  4: 'wrist_left',    5: 'hand_left',
    6: 'shoulder_right', 7: 'elbow_right', 8: 'wrist_right',
    9: 'hand_right', 10: 'hip_left',     11: 'knee_left',
    12: 'ankle_left', 13: 'hip_right',   14: 'knee_right',
    15: 'ankle_right'
}

# Define a realistic motion path for a person lying down
def get_position(t, part):
    # Normalize time to [0, 1]
    t = t / 100  # Assume total animation time is 100 frames

    # Simulate a person lying down smoothly
    if part == 0:  # Head
        x = 0.2 * (1 - t)
        y = 0.4 * (1 - t)
    elif part == 1:  # Neck
        x = 0.2 * (1 - t)
        y = 0.3 * (1 - t)
    elif part == 2:  # Shoulder left
        x = -0.2 * (1 - t)
        y = 0.2 * (1 - t)
    elif part == 3:  # Elbow left
        x = -0.3 * (1 - t)
        y = 0.1 * (1 - t)
    elif part == 4:  # Wrist left
        x = -0.35 * (1 - t)
        y = 0.05 * (1 - t)
    elif part == 5:  # Hand left
        x = -0.4 * (1 - t)
        y = 0.02 * (1 - t)
    elif part == 6:  # Shoulder right
        x = 0.2 * (1 - t)
        y = 0.2 * (1 - t)
    elif part == 7:  # Elbow right
        x = 0.3 * (1 - t)
        y = 0.1 * (1 - t)
    elif part == 8:  # Wrist right
        x = 0.35 * (1 - t)
        y = 0.05 * (1 - t)
    elif part == 9:  # Hand right
        x = 0.4 * (1 - t)
        y = 0.02 * (1 - t)
    elif part == 10:  # Hip left
        x = -0.15 * (1 - t)
        y = -0.2 * (1 - t)
    elif part == 11:  # Knee left
        x = -0.18 * (1 - t)
        y = -0.3 * (1 - t)
    elif part == 12:  # Ankle left
        x = -0.2 * (1 - t)
        y = -0.4 * (1 - t)
    elif part == 13:  # Hip right
        x = 0.15 * (1 - t)
        y = -0.2 * (1 - t)
    elif part == 14:  # Knee right
        x = 0.18 * (1 - t)
        y = -0.3 * (1 - t)
    elif part == 15:  # Ankle right
        x = 0.2 * (1 - t)
        y = -0.4 * (1 - t)

    return (x, y)

# Create point lights
lights = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for light in lights:
    ax.add_patch(light)

# Animation function
def animate(t):
    for i, light in enumerate(lights):
        x, y = get_position(t, i)
        light.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
