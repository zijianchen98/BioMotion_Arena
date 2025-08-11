
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
frames = 60
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
plt.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a bowing person
def update(frame):
    # Head and torso
    t = frame / frames
    bow_angle = np.sin(t * np.pi) * 0.5  # Bowing motion
    
    # Head (1 point)
    head_x = 0
    head_y = 1.5 - 0.5 * bow_angle
    
    # Shoulders (2 points)
    shoulder_y = 1.2 - 0.4 * bow_angle
    shoulder_left_x = -0.3
    shoulder_right_x = 0.3
    
    # Elbows (2 points)
    elbow_left_x = -0.4
    elbow_right_x = 0.4
    elbow_y = 1.0 - 0.3 * bow_angle
    
    # Hands (2 points)
    hand_left_x = -0.5
    hand_right_x = 0.5
    hand_y = 0.8 - 0.2 * bow_angle
    
    # Hips (2 points)
    hip_left_x = -0.2
    hip_right_x = 0.2
    hip_y = 0.6 - 0.1 * bow_angle
    
    # Knees (2 points)
    knee_left_x = -0.2
    knee_right_x = 0.2
    knee_y = 0.3 - 0.05 * bow_angle
    
    # Feet (2 points)
    foot_left_x = -0.2
    foot_right_x = 0.2
    foot_y = 0.0
    
    # Additional points for smoother motion (e.g., spine, mid-limbs)
    spine_x = 0
    spine_y = 0.9 - 0.25 * bow_angle
    
    mid_arm_left_x = -0.35
    mid_arm_right_x = 0.35
    mid_arm_y = 0.9 - 0.25 * bow_angle
    
    mid_leg_left_x = -0.2
    mid_leg_right_x = 0.2
    mid_leg_y = 0.15 - 0.025 * bow_angle
    
    # Assign positions to points
    positions = [
        (head_x, head_y),  # head
        (shoulder_left_x, shoulder_y),  # left shoulder
        (shoulder_right_x, shoulder_y),  # right shoulder
        (elbow_left_x, elbow_y),  # left elbow
        (elbow_right_x, elbow_y),  # right elbow
        (hand_left_x, hand_y),  # left hand
        (hand_right_x, hand_y),  # right hand
        (hip_left_x, hip_y),  # left hip
        (hip_right_x, hip_y),  # right hip
        (knee_left_x, knee_y),  # left knee
        (knee_right_x, knee_y),  # right knee
        (foot_left_x, foot_y),  # left foot
        (foot_right_x, foot_y),  # right foot
        (spine_x, spine_y),  # spine
        (0, 0.45 - 0.075 * bow_angle)  # mid-torso
    ]
    
    for i, point in enumerate(points):
        point.center = positions[i]
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)
plt.show()
