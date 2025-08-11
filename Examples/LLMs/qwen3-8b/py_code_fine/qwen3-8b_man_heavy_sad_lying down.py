
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions (simplified for a lying-down sad man)
body_parts = {
    'head': np.array([0.0, 0.6]),
    'neck': np.array([0.0, 0.5]),
    'torso': np.array([0.0, 0.3]),
    'pelvis': np.array([0.0, 0.1]),
    'left_shoulder': np.array([-0.2, 0.4]),
    'left_elbow': np.array([-0.3, 0.2]),
    'left_wrist': np.array([-0.3, 0.0]),
    'right_shoulder': np.array([0.2, 0.4]),
    'right_elbow': np.array([0.3, 0.2]),
    'right_wrist': np.array([0.3, 0.0]),
    'left_hip': np.array([-0.1, 0.0]),
    'left_knee': np.array([-0.2, -0.2]),
    'left_ankle': np.array([-0.2, -0.4]),
    'right_hip': np.array([0.1, 0.0]),
    'right_knee': np.array([0.2, -0.2]),
    'right_ankle': np.array([0.2, -0.4]),
}

# Define the point-light positions (initial positions)
point_lights = {
    'head': np.array([0.0, 0.6]),
    'neck': np.array([0.0, 0.5]),
    'torso': np.array([0.0, 0.3]),
    'pelvis': np.array([0.0, 0.1]),
    'left_shoulder': np.array([-0.2, 0.4]),
    'left_elbow': np.array([-0.3, 0.2]),
    'left_wrist': np.array([-0.3, 0.0]),
    'right_shoulder': np.array([0.2, 0.4]),
    'right_elbow': np.array([0.3, 0.2]),
    'right_wrist': np.array([0.3, 0.0]),
    'left_hip': np.array([-0.1, 0.0]),
    'left_knee': np.array([-0.2, -0.2]),
    'left_ankle': np.array([-0.2, -0.4]),
    'right_hip': np.array([0.1, 0.0]),
    'right_knee': np.array([0.2, -0.2]),
    'right_ankle': np.array([0.2, -0.4]),
}

# Create point-light circles
point_light_circles = []
for part in point_lights:
    circle = plt.Circle(point_lights[part], 0.02, color='white')
    ax.add_patch(circle)
    point_light_circles.append(circle)

# Define the motion parameters for each point-light
motion_params = {
    'head': {'amplitude': 0.05, 'frequency': 0.05, 'phase': 0.0},
    'neck': {'amplitude': 0.04, 'frequency': 0.04, 'phase': 0.1},
    'torso': {'amplitude': 0.03, 'frequency': 0.03, 'phase': 0.2},
    'pelvis': {'amplitude': 0.02, 'frequency': 0.02, 'phase': 0.3},
    'left_shoulder': {'amplitude': 0.03, 'frequency': 0.03, 'phase': 0.4},
    'left_elbow': {'amplitude': 0.02, 'frequency': 0.02, 'phase': 0.5},
    'left_wrist': {'amplitude': 0.01, 'frequency': 0.01, 'phase': 0.6},
    'right_shoulder': {'amplitude': 0.03, 'frequency': 0.03, 'phase': 0.7},
    'right_elbow': {'amplitude': 0.02, 'frequency': 0.02, 'phase': 0.8},
    'right_wrist': {'amplitude': 0.01, 'frequency': 0.01, 'phase': 0.9},
    'left_hip': {'amplitude': 0.02, 'frequency': 0.02, 'phase': 1.0},
    'left_knee': {'amplitude': 0.01, 'frequency': 0.01, 'phase': 1.1},
    'left_ankle': {'amplitude': 0.005, 'frequency': 0.005, 'phase': 1.2},
    'right_hip': {'amplitude': 0.02, 'frequency': 0.02, 'phase': 1.3},
    'right_knee': {'amplitude': 0.01, 'frequency': 0.01, 'phase': 1.4},
    'right_ankle': {'amplitude': 0.005, 'frequency': 0.005, 'phase': 1.5},
}

# Animation function
def animate(frame):
    for part in point_lights:
        params = motion_params[part]
        x = point_lights[part][0] + params['amplitude'] * np.sin(2 * np.pi * params['frequency'] * frame + params['phase'])
        y = point_lights[part][1] + params['amplitude'] * np.cos(2 * np.pi * params['frequency'] * frame + params['phase'])
        point_light_circles[point_light_circles.index(part)] = plt.Circle((x, y), 0.02, color='white')
        ax.add_patch(point_light_circles[point_light_circles.index(part)])
        point_light_circles[point_light_circles.index(part)].set_center((x, y))

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
