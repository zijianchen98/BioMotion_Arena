
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

# Define the body parts and their positions (simplified for a running woman)
body_parts = {
    'hips': np.array([0.0, -0.5]),
    'left_knee': np.array([0.2, -0.3]),
    'right_knee': np.array([-0.2, -0.3]),
    'left_ankle': np.array([0.3, -0.1]),
    'right_ankle': np.array([-0.3, -0.1]),
    'left_shoulder': np.array([0.2, 0.3]),
    'right_shoulder': np.array([-0.2, 0.3]),
    'left_elbow': np.array([0.3, 0.1]),
    'right_elbow': np.array([-0.3, 0.1]),
    'left_wrist': np.array([0.4, 0.0]),
    'right_wrist': np.array([-0.4, 0.0]),
    'head': np.array([0.0, 0.5]),
    'left_hip_joint': np.array([0.0, -0.5]),
    'right_hip_joint': np.array([0.0, -0.5]),
}

# Define the point-light positions (15 points)
point_lights = [
    'hips', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle',
    'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'head', 'left_hip_joint', 'right_hip_joint', 'left_shoulder'
]

# Create circles for point lights
point_circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in point_circles:
    ax.add_patch(circle)

# Define a function to update the animation
def update(frame):
    # Define a running motion pattern (simplified)
    t = frame / 50.0
    sin_t = np.sin(t)
    cos_t = np.cos(t)

    # Define a function to animate body parts
    def animate_body_parts(part, base, offset):
        if part == 'hips':
            return base + np.array([0.0, -0.5]) + np.array([0.0, 0.2 * sin_t])
        elif part == 'left_knee':
            return base + np.array([0.2, -0.3]) + np.array([0.1 * sin_t, 0.1 * cos_t])
        elif part == 'right_knee':
            return base + np.array([-0.2, -0.3]) + np.array([-0.1 * sin_t, 0.1 * cos_t])
        elif part == 'left_ankle':
            return base + np.array([0.3, -0.1]) + np.array([0.1 * sin_t, 0.1 * cos_t])
        elif part == 'right_ankle':
            return base + np.array([-0.3, -0.1]) + np.array([-0.1 * sin_t, 0.1 * cos_t])
        elif part == 'left_shoulder':
            return base + np.array([0.2, 0.3]) + np.array([0.1 * sin_t, 0.1 * cos_t])
        elif part == 'right_shoulder':
            return base + np.array([-0.2, 0.3]) + np.array([-0.1 * sin_t, 0.1 * cos_t])
        elif part == 'left_elbow':
            return base + np.array([0.3, 0.1]) + np.array([0.1 * sin_t, 0.1 * cos_t])
        elif part == 'right_elbow':
            return base + np.array([-0.3, 0.1]) + np.array([-0.1 * sin_t, 0.1 * cos_t])
        elif part == 'left_wrist':
            return base + np.array([0.4, 0.0]) + np.array([0.1 * sin_t, 0.1 * cos_t])
        elif part == 'right_wrist':
            return base + np.array([-0.4, 0.0]) + np.array([-0.1 * sin_t, 0.1 * cos_t])
        elif part == 'head':
            return base + np.array([0.0, 0.5]) + np.array([0.0, 0.1 * sin_t])
        elif part == 'left_hip_joint':
            return base + np.array([0.0, -0.5]) + np.array([0.0, 0.2 * sin_t])
        elif part == 'right_hip_joint':
            return base + np.array([0.0, -0.5]) + np.array([0.0, 0.2 * sin_t])
        else:
            return base

    # Update each point light position
    for i, part in enumerate(point_lights):
        pos = animate_body_parts(part, body_parts[part], 0)
        point_circles[i].center = pos

    return point_circles

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
