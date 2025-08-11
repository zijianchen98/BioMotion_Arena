
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configure the animation figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1)
ax.set_facecolor('black')
ax.axis('off')

# Number of point-lights
num_points = 15

# Generate initial positions for the points (representing the human figure)
# These are simple relative coordinates for head, torso, arms, and legs.
initial_positions = np.array([
    [0, 0.9],  # Head
    [0, 0.6],  # Torso center
    [-0.2, 0.6], [0.2, 0.6],  # Shoulders
    [-0.4, 0.4], [-0.2, 0.4], [0.2, 0.4], [0.4, 0.4],  # Arms
    [-0.2, -0.2], [0.2, -0.2],  # Hips
    [-0.4, -0.6], [-0.2, -0.6], [0.2, -0.6], [0.4, -0.6],  # Legs
    [0, -1]  # Feet joint
])

points, = ax.plot([], [], 'wo')  # Initialize point lights (white dots)

# Bowing animation parameters
bow_rate = 0.05  # Control bowing speed
angle = np.pi / 6  # Maximum bow angle (30 degrees)
cycle = np.linspace(-angle, angle, 60)  # Bowing up and down full motion


def update(frame):
    """
    Update each frame for the animation.
    """
    bow_angle = cycle[frame % len(cycle)]

    # Generate biomechanical plausible rotation for bowing action
    rotated_positions = []
    for i, (x, y) in enumerate(initial_positions):
        if y >= 0.6:  # Rotate points for head and torso
            x_rotated = x * np.cos(bow_angle) - y * np.sin(bow_angle)
            y_rotated = x * np.sin(bow_angle) + y * np.cos(bow_angle)
        else:
            # Points representing legs and lower body remain mostly fixed
            x_rotated, y_rotated = x, y  
        rotated_positions.append([x_rotated, y_rotated])

    rotated_positions = np.array(rotated_positions)
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,


ani = animation.FuncAnimation(fig, update, frames=60, interval=100, blit=True)
plt.show()
