
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights
num_points = 15

# Define the body parts and their positions relative to the center of the body
body_parts = {
    'head': (0, 0.5),
    'torso': (0, 0),
    'left_shoulder': (-0.2, 0.2),
    'right_shoulder': (0.2, 0.2),
    'left_elbow': (-0.4, 0.1),
    'right_elbow': (0.4, 0.1),
    'left_hand': (-0.6, 0.05),
    'right_hand': (0.6, 0.05),
    'left_hip': (-0.3, -0.3),
    'right_hip': (0.3, -0.3),
    'left_knee': (-0.5, -0.5),
    'right_knee': (0.5, -0.5),
    'left_foot': (-0.7, -0.7),
    'right_foot': (0.7, -0.7),
    'pelvis': (0, -0.3)
}

# Define the positions of the point lights
point_light_positions = {
    'head': (0, 0.5),
    'left_shoulder': (-0.2, 0.2),
    'right_shoulder': (0.2, 0.2),
    'left_elbow': (-0.4, 0.1),
    'right_elbow': (0.4, 0.1),
    'left_hand': (-0.6, 0.05),
    'right_hand': (0.6, 0.05),
    'left_hip': (-0.3, -0.3),
    'right_hip': (0.3, -0.3),
    'left_knee': (-0.5, -0.5),
    'right_knee': (0.5, -0.5),
    'left_foot': (-0.7, -0.7),
    'right_foot': (0.7, -0.7),
    'pelvis': (0, -0.3),
    'neck': (0, 0.4),
    'spine': (0, 0.2),
    'waist': (0, -0.2)
}

# Define a function to simulate a walking motion
def walk_position(t, amplitude=0.1, frequency=0.1, phase=0):
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Define the animation function
def animate(frame):
    # Create a list of point light positions
    points = []
    for name, pos in point_light_positions.items():
        x, y = pos

        # Add walking motion to the torso and pelvis
        if name == 'pelvis':
            y += walk_position(frame, amplitude=0.1, frequency=0.1, phase=0)
        elif name == 'spine':
            y += walk_position(frame, amplitude=0.1, frequency=0.1, phase=0.5)

        # Add small oscillations to simulate natural movement
        if name in ['left_hip', 'right_hip']:
            y += walk_position(frame, amplitude=0.05, frequency=0.15, phase=0)
        elif name in ['left_knee', 'right_knee']:
            y += walk_position(frame, amplitude=0.05, frequency=0.2, phase=0.5)
        elif name in ['left_foot', 'right_foot']:
            y += walk_position(frame, amplitude=0.05, frequency=0.25, phase=0.75)

        # Add small oscillations to simulate arm movement
        if name in ['left_hand', 'right_hand']:
            y += walk_position(frame, amplitude=0.05, frequency=0.2, phase=0.5)
        elif name in ['left_elbow', 'right_elbow']:
            y += walk_position(frame, amplitude=0.05, frequency=0.15, phase=0.75)
        elif name in ['left_shoulder', 'right_shoulder']:
            y += walk_position(frame, amplitude=0.05, frequency=0.1, phase=0.9)

        # Scale the position to fit within the plot
        x *= 1.2
        y *= 1.2

        points.append((x, y))

    # Update the points
    for i, point in enumerate(points):
        points[i] = (point[0], point[1])

    # Clear the previous points
    for point in points_list:
        point.remove()

    # Add new points
    points_list.clear()
    for x, y in points:
        circle = Circle((x, y), 0.02, color='white')
        ax.add_patch(circle)
        points_list.append(circle)

    return points_list

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the list of point lights
points_list = []

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
