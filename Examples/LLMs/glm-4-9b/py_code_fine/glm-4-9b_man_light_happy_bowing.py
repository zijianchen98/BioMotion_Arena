
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
background_color = (0, 0, 0)
light_color = (1, 1, 1)
light_size = 50  # Size of the point lights
animation_interval = 50  # milliseconds between frames
total_frames = 200

# Generate initial positions and velocities for the point lights
np.random.seed(42)
positions = np.random.rand(num_lights, 2) * 0.8 + 0.1  # Initial positions within a 90% of the display
velocities = (np.random.rand(num_lights, 2) - 0.5) * 0.004  # Random initial velocities

# Function to simulate bowing motion
def bowing(positions, frame):
    """Simulate bowing by moving points vertically and having a slight horizontal sway."""
    bow_angle = np.sin(frame / 20) * 0.1
    sway = np.sin(frame / 30) * 0.01
    positions[:, 0] += sway
    positions[:, 1] = 0.5 - np.sqrt((positions[:, 0] - 0.5) ** 2 + (0.5 - np.sin(bow_angle)) ** 2) * 0.8

    # Add some randomness to simulate more natural movement
    positions += (np.random.rand(num_lights, 2) - 0.5) * 0.005
    # Keep points within the display area
    positions = np.clip(positions, 0.1, 0.9)

# Setup the figure and axis for animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor(background_color)
ax.axis('off')

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=light_size, color=light_color)

# Animation update function
def update(frame):
    global positions
    bowing(positions, frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=animation_interval, blit=True)

# plt.show() to display the animation in a window, or save the animation using:
ani.save('biological_motion_animation.gif', writer='imagemagick', dpi=80)
