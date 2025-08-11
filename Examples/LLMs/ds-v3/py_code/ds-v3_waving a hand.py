
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Number of point-lights
num_points = 15

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the waving motion
def update(frame):
    # Time parameter
    t = frame * 0.1
    
    # Body points (relative positions)
    # Head
    head_x = 0
    head_y = 1.0 + 0.05 * np.sin(t * 2)
    
    # Shoulders
    shoulder_x = 0
    shoulder_y = 0.8
    
    # Torso and hips
    torso_x = 0
    torso_y = 0.5
    hip_x = 0
    hip_y = 0.2
    
    # Left arm (non-waving arm)
    left_upper_arm_x = -0.3
    left_upper_arm_y = 0.7
    left_lower_arm_x = -0.4
    left_lower_arm_y = 0.4
    
    # Right arm (waving arm)
    wave_amplitude = 0.5
    wave_freq = 2.0
    right_upper_arm_x = 0.3
    right_upper_arm_y = 0.7 + 0.05 * np.sin(t)
    right_elbow_x = 0.6 + 0.1 * np.sin(t * wave_freq)
    right_elbow_y = 0.6 + wave_amplitude * np.sin(t * wave_freq)
    right_hand_x = 0.8 + 0.1 * np.sin(t * wave_freq + 0.5)
    right_hand_y = 0.5 + wave_amplitude * np.sin(t * wave_freq + 1.0)
    
    # Legs
    left_upper_leg_x = -0.2
    left_upper_leg_y = 0.0
    left_lower_leg_x = -0.2
    left_lower_leg_y = -0.4
    left_foot_x = -0.2
    left_foot_y = -0.8
    
    right_upper_leg_x = 0.2
    right_upper_leg_y = 0.0
    right_lower_leg_x = 0.2
    right_lower_leg_y = -0.4
    right_foot_x = 0.2
    right_foot_y = -0.8
    
    # Update point positions
    point_positions = [
        (head_x, head_y),  # 0: Head
        (shoulder_x, shoulder_y),  # 1: Shoulder
        (torso_x, torso_y),  # 2: Torso
        (hip_x, hip_y),  # 3: Hip
        (left_upper_arm_x, left_upper_arm_y),  # 4: Left upper arm
        (left_lower_arm_x, left_lower_arm_y),  # 5: Left lower arm
        (right_upper_arm_x, right_upper_arm_y),  # 6: Right upper arm
        (right_elbow_x, right_elbow_y),  # 7: Right elbow
        (right_hand_x, right_hand_y),  # 8: Right hand
        (left_upper_leg_x, left_upper_leg_y),  # 9: Left upper leg
        (left_lower_leg_x, left_lower_leg_y),  # 10: Left lower leg
        (left_foot_x, left_foot_y),  # 11: Left foot
        (right_upper_leg_x, right_upper_leg_y),  # 12: Right upper leg
        (right_lower_leg_x, right_lower_leg_y),  # 13: Right lower leg
        (right_foot_x, right_foot_y)  # 14: Right foot
    ]
    
    for i, point in enumerate(points):
        point.center = point_positions[i]
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.title('Biological Motion: Waving Hand', color='white')
plt.tight_layout()
plt.show()
