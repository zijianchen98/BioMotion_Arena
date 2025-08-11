
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Body joint indices
# 0: Head
# 1: Neck
# 2: RShoulder
# 3: LShoulder
# 4: RElbow
# 5: LElbow
# 6: RWrist
# 7: LWrist
# 8: Torso
# 9: RHip
# 10: LHip
# 11: RKnee
# 12: LKnee
# 13: RAnkle
# 14: LAnkle

def skeleton_pose(t, heavy_weight=True):
    '''
    Generate a sad figure with 15 points, right hand waving ("sad" = hunched, limp, slow swing, heavier look).
    '''
    # Main body parameters
    body_x = 0
    body_y = 0
    scale = 1.0

    # Lengths in arbitrary units
    shoulders_width = 0.36 * scale
    upperarm = 0.31 * scale
    forearm = 0.27 * scale
    upperleg = 0.38 * scale
    lowerleg = 0.38 * scale
    hip_width = 0.19 * scale
    head_height = 0.16 * scale

    # Spine points
    head = np.array([body_x, body_y + 1.47 * scale])
    neck = np.array([body_x, body_y + 1.37 * scale])
    shoulder_center = np.array([body_x, body_y + 1.32 * scale])
    chest = np.array([body_x, body_y + 1.12 * scale])
    hips_center = np.array([body_x, body_y + 0.91 * scale])

    # Shoulders
    R_shoulder = shoulder_center + np.array([shoulders_width / 2, 0])
    L_shoulder = shoulder_center - np.array([shoulders_width / 2, 0])

    # Hips
    R_hip = hips_center + np.array([hip_width / 2, 0])
    L_hip = hips_center - np.array([hip_width / 2, 0])

    # "Sad" posture: slouch body forward and drop head/shoulders a bit
    forward_angle = np.deg2rad(17)
    def rot(vec, angle):
        mat = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return mat @ vec

    # Slouch all upper points
    def slouch(pt):
        return hips_center + rot(pt - hips_center, forward_angle)
    head = slouch(head)
    neck = slouch(neck)
    shoulder_center = slouch(shoulder_center)
    chest = slouch(chest)
    R_shoulder = slouch(R_shoulder)
    L_shoulder = slouch(L_shoulder)

    # Project for heavy weight: right hand carrying "heavy" load, so wrist lower
    # Right arm: waving, with heavy load, so damped smooth motion
    # Left arm: pretty limp/hanging down
    # -- Right
    # Right elbow angle animates back/forth for wave, but restricted for weight
    wave_period = 2.2 if heavy_weight else 1.5  # slower wave
    wave_amp = np.deg2rad(33)
    wave_angle = np.sin(2 * np.pi * t / wave_period) * wave_amp

    # Base angle is depressed (weight), wave superposed
    base_shoulder_angle = np.deg2rad(-105)  # down and a bit forward
    right_shoulder_angle = base_shoulder_angle + 0.23*wave_angle
    right_elbow_angle = np.deg2rad(54) + 0.77*wave_angle  # mostly fixed, some wave

    # 1. Shoulder->Elbow
    upperarm_vec = upperarm * np.array([np.cos(right_shoulder_angle), np.sin(right_shoulder_angle)])
    R_elbow = R_shoulder + upperarm_vec

    # 2. Elbow->Wrist (always points down farther if weight)
    forearm_down_angle = np.deg2rad(90) + (np.deg2rad(9) if heavy_weight else 0)  # emphasized down
    right_forearm_angle = right_shoulder_angle + right_elbow_angle
    forearm_vec = forearm * np.array([np.cos(right_forearm_angle), np.sin(right_forearm_angle)])
    R_wrist = R_elbow + forearm_vec

    # Left arm, limp
    left_shoulder_angle = np.deg2rad(-140)
    left_elbow_angle = np.deg2rad(-3)
    # 1. Shoulder->Elbow
    L_elbow = L_shoulder + upperarm * np.array([np.cos(left_shoulder_angle), np.sin(left_shoulder_angle)])
    # 2. Elbow->Wrist (bent very slightly forward)
    L_wrist = L_elbow + forearm * np.array([np.cos(left_shoulder_angle + left_elbow_angle),
                                            np.sin(left_shoulder_angle + left_elbow_angle)])

    # Legs ("sad", so not energetic)
    step_period = 5.4  # very slow
    step_amp = np.deg2rad(13)
    step_phase = np.sin(2 * np.pi * t / step_period) * step_amp  # but subtle shift

    # Right leg
    right_hip_angle = np.deg2rad(-94) + 0.6 * step_phase
    right_knee_angle = np.deg2rad(30) - 0.3 * np.abs(step_phase)
    R_knee = R_hip + upperleg * np.array([np.cos(right_hip_angle), np.sin(right_hip_angle)])
    R_ankle = R_knee + lowerleg * np.array([np.cos(right_hip_angle + right_knee_angle),
                                            np.sin(right_hip_angle + right_knee_angle)])

    # Left leg
    left_hip_angle = np.deg2rad(-86) - 0.6 * step_phase
    left_knee_angle = np.deg2rad(27) + 0.3 * np.abs(step_phase)
    L_knee = L_hip + upperleg * np.array([np.cos(left_hip_angle), np.sin(left_hip_angle)])
    L_ankle = L_knee + lowerleg * np.array([np.cos(left_hip_angle + left_knee_angle),
                                            np.sin(left_hip_angle + left_knee_angle)])

    # Packing 15 point-lights for the stick-figure joint locations:
    # 0: Head, 1: Neck, 2: RShoulder, 3: LShoulder, 4: RElbow, 5: LElbow, 6: RWrist, 7: LWrist,
    # 8: Chest, 9: R hip, 10: L hip, 11: R knee, 12: L knee, 13: R ankle, 14: L ankle
    pts = np.stack([
        head,
        neck,
        R_shoulder,
        L_shoulder,
        R_elbow,
        L_elbow,
        R_wrist,
        L_wrist,
        chest,
        R_hip,
        L_hip,
        R_knee,
        L_knee,
        R_ankle,
        L_ankle
    ])
    return pts


# Matplotlib animation

fig, ax = plt.subplots(figsize=(3, 6))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.axis('off')

scat = ax.scatter([], [], s=55, color='white', edgecolor='white')

nframes = 120
DT = 0.025  # time between frames

def animate(i):
    t = i * DT
    pts = skeleton_pose(t, heavy_weight=True)
    scat.set_offsets(pts)
    return scat,

anim = FuncAnimation(fig, animate, frames=nframes, interval=1000*DT, blit=True)
plt.show()
