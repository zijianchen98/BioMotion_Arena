
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

# Define the 15 point-light positions (representing joints)
# These positions are based on a simplified human body with a sad woman jumping forward
# Coordinates are normalized to [-1, 1] for the plot

# Define joint indices and their positions (approximate)
joints = {
    'head': (0, 0.8),
    'neck': (0, 0.6),
    'torso': (0, 0.4),
    'upper_left_arm': (-0.2, 0.4),
    'lower_left_arm': (-0.4, 0.3),
    'upper_right_arm': (0.2, 0.4),
    'lower_right_arm': (0.4, 0.3),
    'left_hip': (-0.3, 0.1),
    'left_knee': (-0.4, 0.05),
    'left_ankle': (-0.5, -0.05),
    'right_hip': (0.3, 0.1),
    'right_knee': (0.4, 0.05),
    'right_ankle': (0.5, -0.05),
    'left_shoulder': (-0.2, 0.4),
    'right_shoulder': (0.2, 0.4)
}

# Create circles for point-lights
points = {}
for name, (x, y) in joints.items():
    points[name] = Circle((x, y), 0.02, color='white', zorder=5)

# Add point-lights to the plot
for p in points.values():
    ax.add_patch(p)

# Define motion parameters (simplified)
# These are approximate positions for a jumping motion
def get_position(t, frame, total_frames=100):
    # t is time from 0 to 1
    # frame is the current frame (0 to total_frames)
    # total_frames is the total number of frames in the animation

    # Jumping motion: up and down
    jump_height = 0.3
    jump_duration = 50
    jump_phase = (frame / total_frames) * 2 * np.pi
    y_jump = jump_height * np.sin(jump_phase)

    # Forward motion: forward and backward
    forward_duration = 50
    forward_phase = (frame / total_frames) * 2 * np.pi
    x_forward = 0.5 * np.sin(forward_phase)

    # Combine x and y motion
    x = x_forward
    y = y_jump

    return x, y

# Update function for the animation
def update(frame):
    for name, (x, y) in joints.items():
        # Get the current position for the joint
        current_x, current_y = get_position(0, frame, total_frames=100)
        # Apply joint-specific motion (adjust based on body part)
        if name == 'head':
            current_x += 0.05 * np.sin(frame / 10)
            current_y += 0.05 * np.cos(frame / 10)
        elif name == 'torso':
            current_y += 0.05 * np.sin(frame / 10)
        elif name == 'left_hip':
            current_x += 0.02 * np.sin(frame / 10)
        elif name == 'right_hip':
            current_x -= 0.02 * np.sin(frame / 10)
        elif name == 'left_knee':
            current_y += 0.01 * np.sin(frame / 10)
        elif name == 'right_knee':
            current_y += 0.01 * np.sin(frame / 10)
        elif name == 'left_ankle':
            current_y -= 0.01 * np.sin(frame / 10)
        elif name == 'right_ankle':
            current_y -= 0.01 * np.sin(frame / 10)
        elif name == 'left_shoulder':
            current_x -= 0.02 * np.sin(frame / 10)
        elif name == 'right_shoulder':
            current_x += 0.02 * np.sin(frame / 10)
        elif name == 'upper_left_arm':
            current_y += 0.01 * np.sin(frame / 10)
        elif name == 'lower_left_arm':
            current_y += 0.01 * np.sin(frame / 10)
        elif name == 'upper_right_arm':
            current_y += 0.01 * np.sin(frame / 10)
        elif name == 'lower_right_arm':
            current_y += 0.01 * np.sin(frame / 10)

        # Update the position of the point-light
        points[name].center = (current_x, current_y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
