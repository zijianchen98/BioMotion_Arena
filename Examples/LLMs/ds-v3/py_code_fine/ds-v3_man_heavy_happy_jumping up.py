
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Parameters
num_points = 15
fps = 30
duration = 2  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.1, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key points for the stick figure (relative positions)
# Head, shoulders, elbows, hands, hips, knees, feet
# We'll model the points in a hierarchical manner (parent-child relationships)
joint_positions = np.zeros((total_frames, num_points, 2))

# Body proportions (relative lengths)
head_radius = 0.2
torso_length = 0.5
upper_arm_length = 0.3
lower_arm_length = 0.25
upper_leg_length = 0.4
lower_leg_length = 0.4
foot_length = 0.2

# Key frames for jumping motion
for t in range(total_frames):
    time = t / fps
    
    # Vertical position (jumping motion)
    jump_height = 1.5
    # Simple harmonic motion for up and down
    if time < 0.5:
        # Crouching down
        y_offset = -0.5 * time
    elif time < 1.0:
        # Jumping up
        y_offset = -0.25 + jump_height * (time - 0.5) - 4.9 * (time - 0.5)**2
    else:
        # Landing
        y_offset = max(-0.5 * (time - 1.0), 0)
    
    # Body angle (leaning forward during jump)
    if time < 0.5:
        body_angle = 0
    elif time < 0.7:
        body_angle = -0.3 * (time - 0.5) / 0.2
    else:
        body_angle = -0.3 * (1 - (time - 0.7) / 0.3)
    
    # Head (0)
    joint_positions[t, 0, 0] = 0
    joint_positions[t, 0, 1] = y_offset + torso_length + head_radius
    
    # Shoulders (1)
    joint_positions[t, 1, 0] = 0
    joint_positions[t, 1, 1] = y_offset + torso_length
    
    # Elbows (2, 3)
    arm_angle = 0.5 * math.sin(2 * math.pi * time * 2)
    joint_positions[t, 2, 0] = -upper_arm_length * math.sin(arm_angle + body_angle)
    joint_positions[t, 2, 1] = y_offset + torso_length - upper_arm_length * math.cos(arm_angle + body_angle)
    
    joint_positions[t, 3, 0] = upper_arm_length * math.sin(arm_angle + body_angle)
    joint_positions[t, 3, 1] = y_offset + torso_length - upper_arm_length * math.cos(arm_angle + body_angle)
    
    # Hands (4, 5)
    hand_angle = arm_angle + 0.3
    joint_positions[t, 4, 0] = joint_positions[t, 2, 0] - lower_arm_length * math.sin(hand_angle + body_angle)
    joint_positions[t, 4, 1] = joint_positions[t, 2, 1] - lower_arm_length * math.cos(hand_angle + body_angle)
    
    joint_positions[t, 5, 0] = joint_positions[t, 3, 0] + lower_arm_length * math.sin(hand_angle + body_angle)
    joint_positions[t, 5, 1] = joint_positions[t, 3, 1] - lower_arm_length * math.cos(hand_angle + body_angle)
    
    # Hips (6)
    joint_positions[t, 6, 0] = 0
    joint_positions[t, 6, 1] = y_offset
    
    # Knees (7, 8)
    if time < 0.5:
        # Crouching
        leg_angle = -0.5
    elif time < 0.7:
        # Jumping
        leg_angle = -0.5 + 1.5 * (time - 0.5) / 0.2
    else:
        # Landing
        leg_angle = 1.0 - 1.5 * (time - 0.7) / 0.3
    
    joint_positions[t, 7, 0] = -0.2
    joint_positions[t, 7, 1] = y_offset - upper_leg_length * math.cos(leg_angle)
    
    joint_positions[t, 8, 0] = 0.2
    joint_positions[t, 8, 1] = y_offset - upper_leg_length * math.cos(leg_angle)
    
    # Feet (9, 10)
    foot_angle = leg_angle - 0.3
    joint_positions[t, 9, 0] = joint_positions[t, 7, 0] - lower_leg_length * math.sin(foot_angle)
    joint_positions[t, 9, 1] = joint_positions[t, 7, 1] - lower_leg_length * math.cos(foot_angle)
    
    joint_positions[t, 10, 0] = joint_positions[t, 8, 0] + lower_leg_length * math.sin(foot_angle)
    joint_positions[t, 10, 1] = joint_positions[t, 8, 1] - lower_leg_length * math.cos(foot_angle)
    
    # Additional points for more natural motion (e.g., torso, waist)
    # Torso middle (11)
    joint_positions[t, 11, 0] = 0
    joint_positions[t, 11, 1] = y_offset + torso_length / 2
    
    # Waist sides (12, 13)
    joint_positions[t, 12, 0] = -0.15
    joint_positions[t, 12, 1] = y_offset + 0.1
    
    joint_positions[t, 13, 0] = 0.15
    joint_positions[t, 13, 1] = y_offset + 0.1
    
    # Toes (14, 15)
    joint_positions[t, 14, 0] = joint_positions[t, 9, 0] - foot_length * math.cos(foot_angle)
    joint_positions[t, 14, 1] = joint_positions[t, 9, 1] + foot_length * math.sin(foot_angle)
    
    joint_positions[t, 15 - 1, 0] = joint_positions[t, 10, 0] + foot_length * math.cos(foot_angle)
    joint_positions[t, 15 - 1, 1] = joint_positions[t, 10, 1] + foot_length * math.sin(foot_angle)

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        point.center = (joint_positions[frame, i, 0], joint_positions[frame, i, 1])
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
