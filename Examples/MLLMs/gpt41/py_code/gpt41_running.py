
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Kinematic parameters (biologically plausible, simplified 2D)
# Each point: [shoulder, elbow, wrist, hip, knee, ankle, head, chest]
# We'll use 15 markers: head, neck, r_shoulder, r_elbow, r_wrist, l_shoulder, l_elbow, l_wrist,
# r_hip, r_knee, r_ankle, l_hip, l_knee, l_ankle, chest

# Marker order:
MARKER_LABELS = [
    "head", "neck",
    "r_shoulder", "r_elbow", "r_wrist",
    "l_shoulder", "l_elbow", "l_wrist",
    "chest",
    "r_hip", "r_knee", "r_ankle",
    "l_hip", "l_knee", "l_ankle",
]

# Skeleton topology (for internal joints reference, not for drawing lines)
# Key joint positions (2D, stand-in model, unit arbitrary)
# We'll use a model based on biomechanical studies (cf. Johansson figures)
# All lengths relative

def running_gait_markers(phase, stride_length=2.5, amplitude=0.20):
    """
    Returns 2D coordinates (x, y) for the 15 markers at a given running phase (0..2*pi).
    Origin is pelvis midpoint; man runs from left to right.
    """
    # Parameters
    hip_height = 1.0         # height of hips
    spine_length = 0.6       # hip -> shoulder (trunk)
    neck_length = 0.18
    head_radius = 0.15
    shoulder_width = 0.38
    pelvis_width = 0.28
    upper_arm = 0.33
    lower_arm = 0.30
    upper_leg = 0.42
    lower_leg = 0.43
    shoulder_to_chest = 0.14

    # Running step timing
    # Phase: 0 = right foot contact, pi = left foot contact
    # For "biological" appearance, use sinusoidal swing + phase offsets

    # Hips (center), progressing horizontally
    x0 = stride_length * phase/(2*np.pi)  # advance over time
    y0 = hip_height + amplitude * np.sin(2*phase) * 0.10

    # Lateral sway (running has minor lateral movement)
    sway = amplitude * np.sin(phase) * 0.04

    # Hip positions
    pelvis = np.array([
        [x0 - pelvis_width/2, y0 + sway],   # r_hip
        [x0 + pelvis_width/2, y0 - sway],   # l_hip
    ])

    # Knee trajectories: large ellipses for swing, mirrored for each leg
    leg_phase_r = phase
    leg_phase_l = phase + np.pi

    def foot_pos(pelvis_xy, phase_leg, side):
        # Elliptical trajectory for ankle (realistic, with flex)
        dy = -np.abs(np.sin(phase_leg)) * lower_leg - upper_leg
        lx = stride_length/2 * np.sin(phase_leg)
        if side == 'left':
            lx *= 1.04  # Slight asymmetry
        return pelvis_xy + np.array([lx, dy])

    # Knees
    def knee_pos(hip_xy, ankle_xy):
        # Place knee using law of cosines, maintaining thigh/lower lengths
        # Assume straight leg (fully extended) at contact, flexed in swing
        v = ankle_xy - hip_xy
        L = np.linalg.norm(v)
        L = np.clip(L, 0.2, upper_leg + lower_leg - 0.02)
        # Compute knee position
        # Triangle: hip -- upper -- knee -- lower -- ankle
        # Place knee "above" the line, with flex proportional to phase
        theta_knee = np.pi - np.arccos(
            (upper_leg**2 + lower_leg**2 - L**2) / (2*upper_leg*lower_leg)
        )
        ratio = upper_leg/(upper_leg+lower_leg)
        knee = hip_xy + (ankle_xy-hip_xy)*ratio
        # Offset laterally (outward) for knee flex -- approx
        norm = np.array([-v[1], v[0]])
        norm = norm / np.linalg.norm(norm) if np.linalg.norm(norm) > 0 else norm
        knee += norm * 0.05 * np.sin(phase)/2
        return knee

    # Ankles
    r_ankle = foot_pos(pelvis[0], leg_phase_r, 'right')
    l_ankle = foot_pos(pelvis[1], leg_phase_l, 'left')
    # Knees
    r_knee = knee_pos(pelvis[0], r_ankle)
    l_knee = knee_pos(pelvis[1], l_ankle)

    # Chest/shoulder height
    chest_y = y0 + spine_length
    chest = np.array([x0, chest_y])

    # Chest sway
    chest_x = x0 + 0.03*np.sin(2*phase)

    # Shoulders
    shoulder_y = chest_y + shoulder_to_chest
    r_shoulder = np.array([chest_x - shoulder_width/2, shoulder_y])
    l_shoulder = np.array([chest_x + shoulder_width/2, shoulder_y])

    # Neck and head
    neck = np.array([chest_x, shoulder_y + neck_length])
    head = neck + np.array([0, head_radius*1.15])

    # Arms: swing forward/back in counter-phase to legs for realism
    arm_phase_r = leg_phase_l + 0.23  # right arm swings with left leg
    arm_phase_l = leg_phase_r + 0.20

    def arm_joints(shoulder, phase_arm, side):
        arm_angle = np.pi/8 * np.sin(phase_arm)  # pendulum
        if side == 'left':
            arm_angle += 0.10
        else:
            arm_angle -= 0.10
        # Elbow flexes in running (dynamic), more flexed when arm is back
        elbow_angle = np.pi/2 + 0.3*np.sin(phase_arm + np.pi/2)
        # Elbow position
        r = np.array([
            upper_arm*np.cos(arm_angle),
            -upper_arm*np.sin(arm_angle)
        ])
        elbow = shoulder + r
        # Wrist
        r2 = np.array([
            lower_arm*np.cos(arm_angle-elbow_angle),
            -lower_arm*np.sin(arm_angle-elbow_angle)
        ])
        wrist = elbow + r2
        return elbow, wrist

    r_elbow, r_wrist = arm_joints(r_shoulder, arm_phase_r, 'right')
    l_elbow, l_wrist = arm_joints(l_shoulder, arm_phase_l, 'left')

    # Assemble marker array [x, y] shape (15, 2), order per MARKER_LABELS
    markers = np.stack([
        head,           # head
        neck,           # neck
        r_shoulder,     # r_shoulder
        r_elbow,        # r_elbow
        r_wrist,        # r_wrist
        l_shoulder,     # l_shoulder
        l_elbow,        # l_elbow
        l_wrist,        # l_wrist
        chest,          # chest
        pelvis[0],      # r_hip
        r_knee,         # r_knee
        r_ankle,        # r_ankle
        pelvis[1],      # l_hip
        l_knee,         # l_knee
        l_ankle,        # l_ankle
    ])
    return markers

# --- Animation code ---

fig, ax = plt.subplots(figsize=(4, 8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# For a 2.5 stride, keep figure centered and within frame
padding = 0.7
xlim = [-padding, 2.5 + padding]
ylim = [-1.1, 2.0]

ax.set_xlim(*xlim)
ax.set_ylim(*ylim)

# Draw initial
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    frames = 60
    # phase goes from 0 to 2*pi
    phi = 2*np.pi * (i%frames)/frames
    markers = running_gait_markers(phi)
    x, y = markers[:,0], markers[:,1]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(
    fig, animate,
    frames=60, init_func=init,
    interval=33, blit=True
)

plt.show()
