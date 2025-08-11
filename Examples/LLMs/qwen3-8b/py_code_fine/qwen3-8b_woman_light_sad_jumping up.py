
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Define the body parts of a sad woman (simplified)
body_parts = {
    'head': np.array([0, 0.6]),
    'torso': np.array([0, 0.2]),
    'left_shoulder': np.array([-0.2, 0.2]),
    'right_shoulder': np.array([0.2, 0.2]),
    'left_hip': np.array([-0.2, -0.2]),
    'right_hip': np.array([0.2, -0.2]),
    'left_knee': np.array([-0.2, -0.4]),
    'right_knee': np.array([0.2, -0.4]),
    'left_ankle': np.array([-0.2, -0.6]),
    'right_ankle': np.array([0.2, -0.6]),
    'left_elbow': np.array([-0.2, 0.0]),
    'right_elbow': np.array([0.2, 0.0]),
    'left_wrist': np.array([-0.2, -0.1]),
    'right_wrist': np.array([0.2, -0.1]),
    'left_hand': np.array([-0.2, -0.2]),
    'right_hand': np.array([0.2, -0.2]),
}

# Define the joints for the skeleton
joints = [
    'head', 'left_shoulder', 'right_shoulder', 'torso', 'left_hip', 'right_hip',
    'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'left_hand', 'right_hand'
]

# Create circles for each point-light
point_lights = [Circle(body_parts[j], 0.03, color='white') for j in joints]
for light in point_lights:
    ax.add_patch(light)

# Define a function to animate the motion
def animate(frame):
    # Simulate a jumping motion with a sine wave for vertical movement
    vertical_offset = 0.2 * np.sin(2 * np.pi * frame / 30)
    # Apply a slight upward acceleration for the jump
    if frame < 60:
        vertical_offset += 0.05 * (frame / 60) ** 2
    else:
        vertical_offset -= 0.05 * ((frame - 60) / 30) ** 2

    # Apply a slight horizontal sway for realism
    horizontal_offset = 0.02 * np.sin(2 * np.pi * frame / 30)

    # Update each point-light position
    for i, j in enumerate(joints):
        body_parts[j] = body_parts[j] + np.array([horizontal_offset, vertical_offset])

    # Update the positions of the point-lights
    for light, pos in zip(point_lights, body_parts.values()):
        light.center = pos

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50, blit=False)

# Show the animation
plt.show()
