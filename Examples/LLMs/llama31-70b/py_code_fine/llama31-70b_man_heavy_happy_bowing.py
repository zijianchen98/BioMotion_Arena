
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
# Happyman with heavy weight bowing
lights = np.array([
    [0, 0],  # Head
    [-0.2, 0.1], [-0.1, 0.1], [0.1, 0.1], [0.2, 0.1],  # Shoulders
    [-0.3, 0], [-0.2, 0], [-0.1, 0], [0.1, 0], [0.2, 0], [0.3, 0],  # Arms
    [-0.1, -0.2], [0.1, -0.2],  # Hands
    [0, -0.3],  # Torso
    [0, -0.5],  # Hips
    [-0.1, -0.6], [0.1, -0.6],  # Legs
])

# Define the movement of the point-lights
def move_lights(frame):
    # Bending motion
    angle = np.pi / 2 * np.sin(frame / 50.0)
    lights_bent = lights.copy()
    lights_bent[1:6, 1] += np.sin(angle) * 0.1  # Shoulders
    lights_bent[6:12, 1] += np.sin(angle) * 0.2  # Arms
    lights_bent[12, 1] += np.sin(angle) * 0.1  # Torso
    lights_bent[13, 1] += np.sin(angle) * 0.2  # Hips
    lights_bent[14:, 1] += np.sin(angle) * 0.3  # Legs

    # Swaying motion
    angle = np.pi / 2 * np.cos(frame / 50.0)
    lights_bent[1:6, 0] += np.cos(angle) * 0.05  # Shoulders
    lights_bent[6:12, 0] += np.cos(angle) * 0.1  # Arms
    lights_bent[12, 0] += np.cos(angle) * 0.05  # Torso
    lights_bent[13, 0] += np.cos(angle) * 0.1  # Hips
    lights_bent[14:, 0] += np.cos(angle) * 0.15  # Legs

    return lights_bent

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the initial positions of the point-lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], color='white', s=50)

# Animation function
def animate(frame):
    lights_bent = move_lights(frame)
    scatter.set_offsets(lights_bent)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
