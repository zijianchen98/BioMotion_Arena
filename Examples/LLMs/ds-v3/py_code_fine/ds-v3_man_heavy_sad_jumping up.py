
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [Circle((0, 0), 0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key points for the sad man jumping
# Points are ordered as: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), and torso (1)
def get_jump_position(t):
    # Time parameters for the jump cycle
    # The jump consists of crouching, ascending, peak, and descending phases
    period = 5.0  # total time for one jump cycle
    t = t % period
    
    # Vertical motion (parabolic for jump)
    if t < 1.0:
        # Crouching phase
        y_offset = -0.2 * t
    elif t < 2.0:
        # Ascending phase
        y_offset = -0.2 + 1.5 * (t - 1.0)
    elif t < 3.0:
        # Peak phase
        y_offset = 1.3 - 0.3 * (t - 2.0)
    else:
        # Descending phase
        y_offset = 1.0 - 1.2 * (t - 3.0)
    
    # Arm motion (moving up and down)
    arm_angle = 0.5 * math.pi * math.sin(2 * math.pi * t / period)
    
    # Leg motion (bending during crouch and jump)
    leg_angle = 0.3 * math.pi * math.sin(2 * math.pi * t / period + math.pi/2)
    
    # Head position
    head_x = 0
    head_y = 1.7 + y_offset
    
    # Shoulders
    shoulder_y = 1.5 + y_offset
    left_shoulder_x = -0.3
    right_shoulder_x = 0.3
    
    # Elbows (relative to shoulders)
    elbow_left_x = left_shoulder_x - 0.3 * math.cos(arm_angle)
    elbow_left_y = shoulder_y - 0.3 * math.sin(arm_angle)
    elbow_right_x = right_shoulder_x + 0.3 * math.cos(arm_angle)
    elbow_right_y = shoulder_y - 0.3 * math.sin(arm_angle)
    
    # Hands (relative to elbows)
    hand_left_x = elbow_left_x - 0.25 * math.cos(arm_angle - 0.2)
    hand_left_y = elbow_left_y - 0.25 * math.sin(arm_angle - 0.2)
    hand_right_x = elbow_right_x + 0.25 * math.cos(arm_angle - 0.2)
    hand_right_y = elbow_right_y - 0.25 * math.sin(arm_angle - 0.2)
    
    # Hips
    hip_y = 1.0 + y_offset
    left_hip_x = -0.2
    right_hip_x = 0.2
    
    # Knees (relative to hips)
    knee_left_x = left_hip_x - 0.2 * math.sin(leg_angle)
    knee_left_y = hip_y - 0.4 * math.cos(leg_angle)
    knee_right_x = right_hip_x + 0.2 * math.sin(leg_angle)
    knee_right_y = hip_y - 0.4 * math.cos(leg_angle)
    
    # Feet (relative to knees)
    foot_left_x = knee_left_x - 0.2 * math.sin(leg_angle + 0.2)
    foot_left_y = knee_left_y - 0.3 * math.cos(leg_angle + 0.2)
    foot_right_x = knee_right_x + 0.2 * math.sin(leg_angle + 0.2)
    foot_right_y = knee_right_y - 0.3 * math.cos(leg_angle + 0.2)
    
    # Torso point (midpoint between shoulders and hips)
    torso_x = 0
    torso_y = (shoulder_y + hip_y) / 2
    
    # Return all points in order: head, shoulders, elbows, hands, hips, knees, feet, torso
    return [
        (head_x, head_y),  # head
        (left_shoulder_x, shoulder_y), (right_shoulder_x, shoulder_y),  # shoulders
        (elbow_left_x, elbow_left_y), (elbow_right_x, elbow_right_y),  # elbows
        (hand_left_x, hand_left_y), (hand_right_x, hand_right_y),  # hands
        (left_hip_x, hip_y), (right_hip_x, hip_y),  # hips
        (knee_left_x, knee_left_y), (knee_right_x, knee_right_y),  # knees
        (foot_left_x, foot_left_y), (foot_right_x, foot_right_y),  # feet
        (torso_x, torso_y)  # torso
    ]

# Update function for animation
def update(t):
    positions = get_jump_position(t)
    for i in range(num_points):
        points[i].center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 5, 100), interval=50, blit=True)

plt.tight_layout()
plt.show()
