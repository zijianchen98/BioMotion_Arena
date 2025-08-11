
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 body points (approximate human body joints)
body_points = [
    (0.0, 0.0),    # Pelvis
    (0.2, 0.1),    # Right hip
    (-0.2, 0.1),   # Left hip
    (0.3, 0.2),    # Right knee
    (-0.3, 0.2),   # Left knee
    (0.4, 0.3),    # Right ankle
    (-0.4, 0.3),   # Left ankle
    (0.0, 0.6),    # Torso
    (0.15, 0.7),   # Right shoulder
    (-0.15, 0.7),  # Left shoulder
    (0.2, 0.85),   # Right elbow
    (-0.2, 0.85),  # Left elbow
    (0.1, 0.95),   # Right wrist
    (-0.1, 0.95),  # Left wrist
    (0.0, 1.0)     # Head
]

# Create circles for the point lights
circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Define a realistic motion function for a man lying down
def update(frame):
    # Simulate a man lying down from upright to lying position
    t = frame / 100.0  # Normalize time

    # Define position functions for each body part
    positions = []
    for i, (x, y) in enumerate(body_points):
        if i == 0:  # Pelvis
            # Move pelvis down as the body lies
            new_y = y - t * 0.6
            positions.append((x, new_y))
        elif i == 1 or i == 2:  # Hips
            # Move hips down and slightly back
            new_y = y - t * 0.6
            new_x = x - t * 0.1
            positions.append((new_x, new_y))
        elif i == 3 or i == 4:  # Knees
            # Knees move down and forward
            new_y = y - t * 0.6
            new_x = x + t * 0.1
            positions.append((new_x, new_y))
        elif i == 5 or i == 6:  # Ankles
            # Ankles move down and forward
            new_y = y - t * 0.6
            new_x = x + t * 0.1
            positions.append((new_x, new_y))
        elif i == 7:  # Torso
            # Torso moves down and slightly back
            new_y = y - t * 0.6
            new_x = x - t * 0.1
            positions.append((new_x, new_y))
        elif i == 8 or i == 9:  # Shoulders
            # Shoulders move down and slightly back
            new_y = y - t * 0.6
            new_x = x - t * 0.1
            positions.append((new_x, new_y))
        elif i == 10 or i == 11:  # Elbows
            # Elbows move down and slightly back
            new_y = y - t * 0.6
            new_x = x - t * 0.1
            positions.append((new_x, new_y))
        elif i == 12 or i == 13:  # Wrists
            # Wrists move down and slightly back
            new_y = y - t * 0.6
            new_x = x - t * 0.1
            positions.append((new_x, new_y))
        elif i == 14:  # Head
            # Head moves down slightly
            new_y = y - t * 0.4
            positions.append((x, new_y))

    # Update positions of the circles
    for circle, (x, y) in zip(circles, positions):
        circle.set_center((x, y))

    return circles

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
