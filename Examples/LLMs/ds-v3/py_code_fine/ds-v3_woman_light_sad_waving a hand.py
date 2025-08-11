
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframe positions for a waving hand motion
def get_keyframe(frame):
    t = frame / num_frames * 2 * np.pi
    
    # Body points (torso, head, legs)
    body_x = np.zeros(5)
    body_y = np.linspace(-1, 0.5, 5)
    
    # Arm points (right arm waving)
    arm_angle = 0.5 * np.sin(2 * t)  # Waving motion
    arm_x = np.linspace(0, 0.5 * np.cos(arm_angle + np.pi/4), 3)
    arm_y = np.linspace(0.2, 0.5 * np.sin(arm_angle + np.pi/4) + 0.2, 3)
    
    # Left arm (static)
    left_arm_x = np.linspace(0, -0.3, 2)
    left_arm_y = np.linspace(0.2, 0.1, 2)
    
    # Legs (slightly moving to balance)
    leg_angle = 0.1 * np.sin(t)
    right_leg_x = np.linspace(0, 0.2 * np.cos(leg_angle), 2)
    right_leg_y = np.linspace(-0.5, -1, 2)
    left_leg_x = np.linspace(0, -0.2 * np.cos(leg_angle), 2)
    left_leg_y = np.linspace(-0.5, -1, 2)
    
    # Combine all points
    x = np.concatenate([
        [0],            # head
        body_x[1:],     # torso
        arm_x,          # right arm
        left_arm_x,     # left arm
        right_leg_x,    # right leg
        left_leg_x      # left leg
    ])
    y = np.concatenate([
        [0.7],          # head
        body_y[1:],     # torso
        arm_y,          # right arm
        left_arm_y,     # left arm
        right_leg_y,    # right leg
        left_leg_y      # left leg
    ])
    
    return x, y

# Update function for animation
def update(frame):
    x, y = get_keyframe(frame)
    for i, point in enumerate(points):
        point.center = (x[i], y[i])
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
