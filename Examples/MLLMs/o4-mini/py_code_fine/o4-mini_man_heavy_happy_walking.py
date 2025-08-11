
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Marker layout:
# 0: head top
# 1: neck
# 2: left shoulder
# 3: right shoulder
# 4: left elbow
# 5: right elbow
# 6: left wrist
# 7: right wrist
# 8: pelvis (hip center)
# 9: left hip
# 10: right hip
# 11: left knee
# 12: right knee
# 13: left ankle
# 14: right ankle

# Body dimension parameters (in arbitrary units)
head_neck = 0.2
neck_pelvis = 0.5
shoulder_width = 0.2
hip_width = 0.2
upper_arm = 0.3
lower_arm = 0.3
upper_leg = 0.5
lower_leg = 0.5

# Motion parameters
fps = 60
stride_freq = 1.0            # strides per second
stride_phase = 2 * np.pi * stride_freq
arm_amp = np.deg2rad(30)     # arm swing amplitude
leg_amp = np.deg2rad(30)     # leg swing amplitude
knee_amp = np.deg2rad(40)    # knee flexion amplitude
com_vert_amp = 0.05          # vertical COM oscillation amplitude

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 2.0)
ax.set_aspect('equal')

# Initialize scatter plot for 15 points
scatter = ax.scatter(np.zeros(15), np.zeros(15), c='white', s=100)

def compute_markers(t):
    """
    Compute the 15 marker positions at time t (seconds).
    Returns an array of shape (15, 2).
    """
    # Center of mass trajectory (we keep horizontal position zero)
    com_x = 0.0
    com_y = 1.0 + com_vert_amp * np.cos(stride_phase * t)

    # Pelvis (hip center)
    pelvis = np.array([com_x, com_y])

    # Neck
    neck = pelvis + np.array([0.0, neck_pelvis])

    # Head top
    head = neck + np.array([0.0, head_neck])

    # Shoulders
    left_shoulder  = neck + np.array([-shoulder_width/2, 0.0])
    right_shoulder = neck + np.array([ shoulder_width/2, 0.0])

    # Hips
    left_hip  = pelvis + np.array([-hip_width/2, 0.0])
    right_hip = pelvis + np.array([ hip_width/2, 0.0])

    # Leg angles (sinusoidal)
    leg_phase = stride_phase * t
    left_leg_angle  =  leg_amp * np.sin(leg_phase)
    right_leg_angle = -leg_amp * np.sin(leg_phase)

    # Knee flexion pattern (peak at mid-swing)
    left_knee_flex  = knee_amp * np.maximum(0, np.sin(leg_phase))
    right_knee_flex = knee_amp * np.maximum(0, np.sin(leg_phase + np.pi))

    # Compute knee positions
    left_knee  = left_hip + upper_leg * np.array([ np.sin(left_leg_angle),
                                                   -np.cos(left_leg_angle)])
    right_knee = right_hip + upper_leg * np.array([ np.sin(right_leg_angle),
                                                     -np.cos(right_leg_angle)])

    # Compute ankle positions
    # Lower leg rotates further by knee flexion
    left_lower_dir  = np.array([ np.sin(left_leg_angle) * np.cos(left_knee_flex) - np.cos(left_leg_angle)*np.sin(left_knee_flex),
                                  -np.cos(left_leg_angle)*np.cos(left_knee_flex) - np.sin(left_leg_angle)*np.sin(left_knee_flex)])
    right_lower_dir = np.array([ np.sin(right_leg_angle)*np.cos(right_knee_flex) - np.cos(right_leg_angle)*np.sin(right_knee_flex),
                                  -np.cos(right_leg_angle)*np.cos(right_knee_flex) - np.sin(right_leg_angle)*np.sin(right_knee_flex)])
    left_ankle  = left_knee  + lower_leg * left_lower_dir
    right_ankle = right_knee + lower_leg * right_lower_dir

    # Arm swing opposite to legs
    left_arm_angle  = -arm_amp * np.sin(leg_phase)
    right_arm_angle =  arm_amp * np.sin(leg_phase)

    # Elbow positions
    left_elbow  = left_shoulder + upper_arm * np.array([ np.sin(left_arm_angle),
                                                          -np.cos(left_arm_angle)])
    right_elbow = right_shoulder + upper_arm * np.array([ np.sin(right_arm_angle),
                                                           -np.cos(right_arm_angle)])

    # Wrist positions (straight extension)
    left_wrist  = left_elbow  + lower_arm * np.array([ np.sin(left_arm_angle),
                                                       -np.cos(left_arm_angle)])
    right_wrist = right_elbow + lower_arm * np.array([ np.sin(right_arm_angle),
                                                        -np.cos(right_arm_angle)])

    # Pack all markers
    markers = np.vstack([
        head,
        neck,
        left_shoulder, right_shoulder,
        left_elbow, right_elbow,
        left_wrist, right_wrist,
        pelvis,
        left_hip, right_hip,
        left_knee, right_knee,
        left_ankle, right_ankle
    ])
    return markers

def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return (scatter,)

def animate(frame):
    t = frame / fps
    pts = compute_markers(t)
    scatter.set_offsets(pts)
    return (scatter,)

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=range(0, fps * 5), interval=1000/fps, blit=True)

plt.show()
