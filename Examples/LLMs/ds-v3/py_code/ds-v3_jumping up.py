
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of points
num_points = 15

# Initialize point positions (x, y)
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Define key points for the stick figure (relative positions)
# Head, shoulders, elbows, hands, hips, knees, feet
# We'll model these points and animate them

def update(frame):
    t = frame * 0.1  # Time parameter
    
    # Jumping motion: vertical position follows a sine wave
    jump_height = 0.5
    vertical_offset = jump_height * np.sin(t * 2)  # Oscillate up and down
    
    # Body parts' relative positions
    head = np.array([0, 1.5 + vertical_offset])
    
    # Shoulders move slightly during jump
    shoulder_width = 0.3
    left_shoulder = np.array([-shoulder_width, 1.2 + vertical_offset])
    right_shoulder = np.array([shoulder_width, 1.2 + vertical_offset])
    
    # Arms move up and down
    arm_swing = 0.3 * np.sin(t * 4)
    left_elbow = np.array([-0.4, 1.0 + vertical_offset + arm_swing])
    right_elbow = np.array([0.4, 1.0 + vertical_offset + arm_swing])
    
    left_hand = np.array([-0.5, 0.8 + vertical_offset + arm_swing * 1.5])
    right_hand = np.array([0.5, 0.8 + vertical_offset + arm_swing * 1.5])
    
    # Hips
    hip_width = 0.2
    left_hip = np.array([-hip_width, 0.7 + vertical_offset])
    right_hip = np.array([hip_width, 0.7 + vertical_offset])
    
    # Legs bend during jump
    leg_bend = 0.2 * np.sin(t * 2 + np.pi/2)  # Offset phase for legs
    
    left_knee = np.array([-0.2, 0.3 + vertical_offset + leg_bend])
    right_knee = np.array([0.2, 0.3 + vertical_offset + leg_bend])
    
    left_foot = np.array([-0.2, 0.0 + max(0, vertical_offset)])
    right_foot = np.array([0.2, 0.0 + max(0, vertical_offset)])
    
    # Additional points for more natural motion (e.g., torso mid-points)
    torso_mid = np.array([0, 1.0 + vertical_offset])
    left_thigh_mid = (left_hip + left_knee) / 2
    right_thigh_mid = (right_hip + right_knee) / 2
    left_shin_mid = (left_knee + left_foot) / 2
    right_shin_mid = (right_knee + right_foot) / 2
    
    # Update all points
    points = np.array([
        head,
        left_shoulder, right_shoulder,
        left_elbow, right_elbow,
        left_hand, right_hand,
        torso_mid,
        left_hip, right_hip,
        left_knee, right_knee,
        left_thigh_mid, right_thigh_mid,
        left_foot, right_foot
    ])
    
    scatter.set_offsets(points[:15])  # Ensure only 15 points
    
    return scatter,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=100, interval=50, blit=True
)

plt.tight_layout()
plt.show()
