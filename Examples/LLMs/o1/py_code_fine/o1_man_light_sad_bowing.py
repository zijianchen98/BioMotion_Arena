import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of animation frames
FRAMES = 60

# Number of points
N_POINTS = 15

def get_sadman_coordinates(frame):
    """
    Returns an (N_POINTS x 2) array representing the (x, y) coordinates
    of the 15 white point-lights for a 'sadman' bowing at a given frame.
    """
    # Normalize frame to [0, 1]
    t = frame / (FRAMES - 1)
    # Bow angle in radians (0 to ~60 degrees forward, then back up)
    # Forward half-bow for first half of frames, return for second half
    if t <= 0.5:
        bow_angle = np.radians(60.0 * (t / 0.5))
    else:
        bow_angle = np.radians(60.0 * (1.0 - (t - 0.5) / 0.5))

    # Body segment lengths (rough approximate in 2D)
    head_to_neck = 0.15
    neck_to_chest = 0.2
    chest_to_pelvis = 0.25
    shoulder_offset = 0.15
    upper_arm = 0.2
    forearm = 0.2
    pelvis_to_hip = 0.15
    thigh = 0.25
    shin = 0.25

    # Slight droop for a "sad" posture: shift arms, head downward
    sad_head_drop = 0.05

    # Base position (pelvis) in 2D
    pelvis_x, pelvis_y = (0.0, 0.0)

    # Chest rotates forward by bow_angle around pelvis
    chest_x = pelvis_x
    chest_y = pelvis_y + chest_to_pelvis
    # Neck position
    neck_x = chest_x
    neck_y = chest_y + neck_to_chest
    # Head
    head_x = neck_x
    head_y = neck_y + head_to_neck - sad_head_drop
    
    # Apply the forward bow rotation around the pelvis for trunk (chest, neck, head)
    # A basic rotation about pelvis = (pelvis_x, pelvis_y)
    def rotate_point(px, py, cx, cy, angle):
        # Rotate px, py around cx, cy by angle
        s = np.sin(angle)
        c = np.cos(angle)
        px -= cx
        py -= cy
        xnew = px * c - py * s
        ynew = px * s + py * c
        px = xnew + cx
        py = ynew + cy
        return px, py

    # Rotate chest
    chest_x, chest_y = rotate_point(chest_x, chest_y, pelvis_x, pelvis_y, bow_angle)
    # Rotate neck
    neck_x, neck_y = rotate_point(neck_x, neck_y, pelvis_x, pelvis_y, bow_angle)
    # Rotate head
    head_x, head_y = rotate_point(head_x, head_y, pelvis_x, pelvis_y, bow_angle)

    # Shoulders (around neck)
    r_shoulder_x = neck_x + shoulder_offset
    r_shoulder_y = neck_y
    l_shoulder_x = neck_x - shoulder_offset
    l_shoulder_y = neck_y
    # Rotate shoulders around neck by a small droop angle
    shoulder_droop = np.radians(15)
    r_shoulder_x, r_shoulder_y = rotate_point(r_shoulder_x, r_shoulder_y, neck_x, neck_y, bow_angle + shoulder_droop)
    l_shoulder_x, l_shoulder_y = rotate_point(l_shoulder_x, l_shoulder_y, neck_x, neck_y, bow_angle - shoulder_droop)

    # Right arm (elbow, hand)
    r_elbow_x = r_shoulder_x
    r_elbow_y = r_shoulder_y - upper_arm
    r_hand_x = r_elbow_x
    r_hand_y = r_elbow_y - forearm

    # Left arm (elbow, hand)
    l_elbow_x = l_shoulder_x
    l_elbow_y = l_shoulder_y - upper_arm
    l_hand_x = l_elbow_x
    l_hand_y = l_elbow_y - forearm

    # Hips (around pelvis)
    r_hip_x = pelvis_x + pelvis_to_hip
    r_hip_y = pelvis_y
    l_hip_x = pelvis_x - pelvis_to_hip
    l_hip_y = pelvis_y

    # Right leg (knee, foot)
    r_knee_x = r_hip_x
    r_knee_y = r_hip_y - thigh
    r_foot_x = r_knee_x
    r_foot_y = r_knee_y - shin

    # Left leg (knee, foot)
    l_knee_x = l_hip_x
    l_knee_y = l_hip_y - thigh
    l_foot_x = l_knee_x
    l_foot_y = l_knee_y - shin

    # Collect all points in order
    points = np.array([
        [head_x, head_y],          # 0: Head
        [neck_x, neck_y],          # 1: Neck
        [r_shoulder_x, r_shoulder_y],  # 2: Right Shoulder
        [r_elbow_x, r_elbow_y],    # 3: Right Elbow
        [r_hand_x, r_hand_y],      # 4: Right Hand
        [l_shoulder_x, l_shoulder_y],  # 5: Left Shoulder
        [l_elbow_x, l_elbow_y],    # 6: Left Elbow
        [l_hand_x, l_hand_y],      # 7: Left Hand
        [chest_x, chest_y],        # 8: Chest
        [r_hip_x, r_hip_y],        # 9: Right Hip
        [r_knee_x, r_knee_y],      # 10: Right Knee
        [r_foot_x, r_foot_y],      # 11: Right Foot
        [l_hip_x, l_hip_y],        # 12: Left Hip
        [l_knee_x, l_knee_y],      # 13: Left Knee
        [l_foot_x, l_foot_y],      # 14: Left Foot
    ])

    return points

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1)
ax.axis('off')

# Initialize scatter plot
initial_positions = get_sadman_coordinates(0)
scatter = ax.scatter(initial_positions[:, 0],
                     initial_positions[:, 1],
                     c='white', s=20)

def update(frame):
    coords = get_sadman_coordinates(frame)
    scatter.set_offsets(coords)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=100, blit=True)
plt.show()