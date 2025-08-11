import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of animation frames
FRAMES = 60

# Create figure and axes with black background
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot for 15 white points
points = ax.scatter([], [], c='white', s=50)

def bow_angle(f):
    # Smoothly vary angle for bowing: 0 -> 45 deg -> 0 -> -5 deg (small up posture) -> 0 ...
    # Using a sine wave scaled and shifted for a repeating bow cycle
    return 20 * np.sin(2 * np.pi * f / FRAMES)

def joint_positions(frame):
    """
    Return 15 (x,y) positions representing a simplified human figure performing a bow.
    Joints index:
        0 pelvis
        1 chest
        2 head
        3 right_shoulder
        4 right_elbow
        5 right_wrist
        6 left_shoulder
        7 left_elbow
        8 left_wrist
        9 right_hip
        10 right_knee
        11 right_ankle
        12 left_hip
        13 left_knee
        14 left_ankle
    """
    # Bow angle
    a = np.radians(bow_angle(frame))
    
    # Base pelvis coordinates with a simple vertical bob
    pelvis_y = 1 + 0.05 * np.sin(2 * np.pi * frame / FRAMES)
    pelvis = np.array([0.0, pelvis_y])
    
    # Torso lengths
    torso_length = 0.4
    neck_length = 0.3  # chest to head
    shoulder_offset = 0.2
    upper_arm_length = 0.3
    forearm_length = 0.3
    upper_leg_length = 0.5
    lower_leg_length = 0.5

    # Rotate torso for bow
    # Chest
    chest = pelvis + np.array([0, torso_length]) @ np.array([[np.cos(a), -np.sin(a)],
                                                             [np.sin(a),  np.cos(a)]])
    
    # Head
    head = chest + np.array([0, neck_length]) @ np.array([[np.cos(a), -np.sin(a)],
                                                          [np.sin(a),  np.cos(a)]])
    
    # Shoulders
    right_shoulder = chest + np.array([ shoulder_offset, 0]) @ np.array([[np.cos(a), -np.sin(a)],
                                                                        [np.sin(a),  np.cos(a)]])
    left_shoulder  = chest + np.array([-shoulder_offset, 0]) @ np.array([[np.cos(a), -np.sin(a)],
                                                                        [np.sin(a),  np.cos(a)]])
    
    # Arms bend slightly more when bowing
    arm_bend_angle = a * 1.5
    
    # Right arm
    right_elbow = right_shoulder + np.array([ upper_arm_length, 0]) @ np.array([[np.cos(arm_bend_angle), -np.sin(arm_bend_angle)],
                                                                               [np.sin(arm_bend_angle),  np.cos(arm_bend_angle)]])
    right_wrist = right_elbow + np.array([ forearm_length, 0]) @ np.array([[np.cos(arm_bend_angle), -np.sin(arm_bend_angle)],
                                                                          [np.sin(arm_bend_angle),  np.cos(arm_bend_angle)]])
    
    # Left arm
    left_elbow = left_shoulder + np.array([-upper_arm_length, 0]) @ np.array([[np.cos(arm_bend_angle), -np.sin(arm_bend_angle)],
                                                                             [np.sin(arm_bend_angle),  np.cos(arm_bend_angle)]])
    left_wrist = left_elbow + np.array([-forearm_length, 0]) @ np.array([[np.cos(arm_bend_angle), -np.sin(arm_bend_angle)],
                                                                        [np.sin(arm_bend_angle),  np.cos(arm_bend_angle)]])
    
    # Hips (slight offset from pelvis)
    hip_offset = 0.1
    right_hip = pelvis + np.array([ hip_offset, 0])
    left_hip  = pelvis + np.array([-hip_offset, 0])
    
    # Legs bend slightly to support bow
    leg_bend = 0.2 * np.sin(a)  # small bend correlated with torso angle
    # Right leg
    right_knee = right_hip + np.array([0, -upper_leg_length * (1 - abs(leg_bend))])
    right_ankle = right_knee + np.array([0, -lower_leg_length * (1 - abs(leg_bend))])
    # Left leg
    left_knee = left_hip + np.array([0, -upper_leg_length * (1 - abs(leg_bend))])
    left_ankle = left_knee + np.array([0, -lower_leg_length * (1 - abs(leg_bend))])

    # Combine all into array
    return np.array([
        pelvis, chest, head,
        right_shoulder, right_elbow, right_wrist,
        left_shoulder, left_elbow, left_wrist,
        right_hip, right_knee, right_ankle,
        left_hip, left_knee, left_ankle
    ])

def update(frame):
    coords = joint_positions(frame)
    points.set_offsets(coords)
    return [points]

ani = FuncAnimation(fig, update, frames=FRAMES, interval=50, blit=True, repeat=True)

plt.show()