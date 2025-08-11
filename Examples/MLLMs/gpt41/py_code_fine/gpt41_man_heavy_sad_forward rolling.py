
# Biological motion Point-Light "Forward Roll" animation (Sadman carrying weight)
# 15 points on black background, in the style of the example image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dot indices:
# 0 - Head
# 1,2 - Shoulders (L/R)
# 3,4 - Elbows (L/R)
# 5,6 - Wrists (L/R)
# 7,8 - Hips (L/R)
# 9,10 - Knees (L/R)
# 11,12 - Ankles (L/R)
# 13,14 - Heavy weight (Each 'hand' holds one side)

# Skeleton segment lengths (all units arbitrary, relative to head at [0,0])
L_head = 1.0
L_neck = 0.6
L_shoulder = 0.8
L_upperarm = 1.1
L_forearm = 1.0
L_torso = 2.2
L_hip = 0.7
L_thigh = 1.4
L_shin = 1.3
L_foot = 0.3
L_weight = 0.8  # distance of weight from wrist

# Body point connections (not used for drawing, but for position calculations)
# Left = 0, Right = 1 in pairs

def sadman_forward_roll_pose(t, cycle_len=2.0, roll_radius=3.0, weightdown=0.3):
    """
    Generate a frame of body marker coordinates for a sadman performing a forward roll.
    t: time (seconds)
    cycle_len: time for one complete roll cycle (seconds)
    roll_radius: radius of the roll circle
    weightdown: how much the weight drags the body downward
    Returns: np.array shape [15,2] (x,y) coords of each point
    """
    # Phase of roll (0~2pi for each cycle)
    omega = 2*np.pi/cycle_len
    phase = omega * t

    # Sadman: hunched, carrying weight
    # For rolling: the whole body center moves along a circular trajectory
    # The body rotates around its center as it moves

    # Center of "roll": to roll forward horizontally
    roll_x = roll_radius * np.sin(phase)
    roll_y = -roll_radius * np.cos(phase) + roll_radius + 3

    # For sadness: crouched, rounded back, head is closer to chest, arms lower
    # For carrying weight: arms and hands tugged down, wrists below shoulders, holding 'weight' below wrists

    # Body orientation: angle tangent to circle (the roll), + pi/2
    body_angle = phase + np.pi/2

    # Crouched position, all segments compressed
    L_torso_c = L_torso * 0.82
    L_thigh_c = L_thigh * 0.83
    L_shin_c = L_shin * 0.90

    # Head
    # Offset from center: (0, torso/2 + neck + head)
    head_offset = np.array([0, L_torso_c*0.43 + L_neck + L_head])

    # Shoulders
    shoulder_center = np.array([0, L_torso_c*0.43 + L_neck])
    shoulder_offset = np.array([
        [-L_shoulder/2, 0],
        [ L_shoulder/2, 0]
    ])

    # Hips (pelvis): (0, -torso/2)
    hip_center = np.array([0, -L_torso_c*0.57])
    hip_offset = np.array([
        [-L_hip/2, 0],
        [ L_hip/2, 0]
    ])

    # Arms: angle downward/slightly in front (sad, carrying weight)
    arm_theta = np.deg2rad(120) # from horizontal (downward & forward)
    arm_dir = [np.array([np.cos(arm_theta), -np.sin(arm_theta)]),   # left arm
               np.array([np.cos(-arm_theta), -np.sin(-arm_theta)])] # right arm

    # Wrists and elbows (arms bent "sadly", shoulders slumped forward)
    elbow_offset = [0.47, 0.47] # fractional for upper arm
    for i in range(2):
        if i == 0:  # left
            sign = -1
        else:
            sign = 1

        # Shoulders to elbow: upper arm, bent out
        elbow_angle = arm_theta + sign*np.deg2rad(19)
        arm_dir[i] = np.array([np.cos(elbow_angle), -np.sin(elbow_angle)])

    # For each shoulder, find elbow/wrist positions
    elbows = []
    wrists = []
    weights = []
    for side in range(2):
        # Shoulder pos
        shoulder = shoulder_center + shoulder_offset[side]
        # Elbow pos
        elbow = shoulder + arm_dir[side] * L_upperarm * elbow_offset[side]
        # Wrist pos
        # Forearm slightly downward
        forearm_theta = arm_theta + (-1 if side==0 else 1)*np.deg2rad(9) + np.deg2rad(15) # arms hang
        forearm_dir = np.array([np.cos(forearm_theta), -np.sin(forearm_theta)])
        wrist = elbow + forearm_dir * L_forearm*0.94
        # Wrist y is pulled down (weight "drags")
        wrist[1] -= weightdown
        # Weight marker below wrist
        weight = wrist + np.array([0, -L_weight])
        elbows.append(elbow)
        wrists.append(wrist)
        weights.append(weight)

    # Knees and ankles: crouched, feet under hips
    knees = []
    ankles = []
    for side in range(2):
        # Hip pos
        hip = hip_center + hip_offset[side]
        # Thigh slopes down and slightly inward (crouched)
        thigh_angle = np.deg2rad(105 + 14*side) # thighs not symmetric
        thigh_vec = np.array([np.cos(thigh_angle)*0.7, -np.abs(np.sin(thigh_angle))])
        thigh_vec = thigh_vec / np.linalg.norm(thigh_vec)
        knee = hip + thigh_vec * L_thigh_c
        # Shin, nearly vertical, slightly backward
        shin_angle = np.deg2rad(269 + 7*side)
        shin_vec = np.array([np.cos(shin_angle), -np.sin(shin_angle)])
        shin_vec = shin_vec / np.linalg.norm(shin_vec)
        ankle = knee + shin_vec * L_shin_c
        knees.append(knee)
        ankles.append(ankle)

    # Assemble all points in torso reference frame
    points = []
    points.append(head_offset)              # 0 head
    points.append(shoulder_center + shoulder_offset[0]) # 1 L shoulder
    points.append(shoulder_center + shoulder_offset[1]) # 2 R shoulder
    points.append(elbows[0])                # 3 L elbow
    points.append(elbows[1])                # 4 R elbow
    points.append(wrists[0])                # 5 L wrist
    points.append(wrists[1])                # 6 R wrist
    points.append(hip_center + hip_offset[0]) # 7 L hip
    points.append(hip_center + hip_offset[1]) # 8 R hip
    points.append(knees[0])                 # 9 L knee
    points.append(knees[1])                 # 10 R knee
    points.append(ankles[0])                # 11 L ankle
    points.append(ankles[1])                # 12 R ankle
    points.append(weights[0])               # 13 heavy weight (L)
    points.append(weights[1])               # 14 heavy weight (R)

    # Stack shape: [15,2]
    points = np.stack(points, axis=0)

    # Rotate body and translate according to rolling trajectory
    rot = np.array([
        [np.cos(body_angle), -np.sin(body_angle)],
        [np.sin(body_angle),  np.cos(body_angle)]
    ])
    points = points @ rot.T
    points[:,0] += roll_x
    points[:,1] += roll_y

    return points

# Animation setup
fig, ax = plt.subplots(figsize=(4,7))
ax.set_aspect('equal')
plt.axis('off')
ax.set_facecolor('black')
# Frame limits
ax.set_xlim(-6, 6)
ax.set_ylim(-1, 11)

# Start with empty scatter plot for 15 points
scatter = ax.scatter([], [], s=49, color='white') # s is dot size

# Animation function
def animate(frame):
    n_frames = 120
    t_total = 2.0
    t = frame / n_frames * t_total
    pts = sadman_forward_roll_pose(t, cycle_len=t_total)
    scatter.set_offsets(pts)
    return scatter,

# Run animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=1000/60, blit=True)

plt.show()
