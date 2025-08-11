
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Body joint order (15 markers, inspired by Johansson 1973):
JOINTS = [
    'Head',         # 0
    'Neck',         # 1
    'RShoulder',    # 2
    'LShoulder',    # 3
    'Chest',        # 4
    'RElbow',       # 5
    'LElbow',       # 6
    'RWrist',       # 7
    'LWrist',       # 8
    'Pelvis',       # 9
    'RHip',         # 10
    'LHip',         # 11
    'RKnee',        # 12
    'LKnee',        # 13
    'RAnkle',       # 14
    # 'LAnkle' omitted for 15 markers, only one foot down for jump.
]

# Helper function to create walking/jumping pose (2D)
def pose_jump(t, T, amplitude=1.3, step_amp=0.25, smile_amp=0.03):
    """
    Return an (n_markers, 2) array describing joint positions at time t
    t: frame/time
    T: total period
    amplitude: vertical jump maximum
    step_amp: arm/leg wiggle amplitude
    smile_amp: head bob/cheek wiggle for 'happy'
    """
    # Center body (pelvis) fixed
    pelvis_x, pelvis_y = 0.0, 0.0

    # Global vertical displacement (the "jump" arc, using parabolic trajectory)
    jump_phase = (t % T) / T
    jump_y = amplitude * 4 * jump_phase * (1 - jump_phase)   # symmetric parabola, peaks at t=T/2

    # Subtle up-and-down head bob (happy affect)
    head_bob = np.sin(2 * np.pi * jump_phase) * smile_amp

    # Spine lengthening during jump
    spine_stretch = 0.03 + 0.07 * jump_y/amplitude

    # Arm/leg swing
    leg_phase = np.sin(2*np.pi*(jump_phase))
    arm_phase = np.sin(2*np.pi*(jump_phase + 0.5))

    # Natural slightly forward arms pose and arms extended when jumping up phase
    arm_lift = 0.13 + 0.13 * (jump_y / amplitude)
    arm_swing = arm_phase * step_amp * 1.2
    leg_swing = leg_phase * step_amp

    # Joint locations (x, y), Y = up
    s = []

    # Head
    s.append([pelvis_x, pelvis_y + 0.87 + jump_y + head_bob])
    # Neck
    neck_y = pelvis_y + 0.78 + jump_y + 0.3*head_bob
    s.append([pelvis_x, neck_y])
    # RShoulder
    s.append([pelvis_x + 0.14, neck_y])
    # LShoulder
    s.append([pelvis_x - 0.14, neck_y])
    # Chest
    s.append([pelvis_x, pelvis_y + 0.66 + jump_y])
    # RElbow
    s.append([pelvis_x + 0.19, neck_y - 0.09 + arm_swing])
    # LElbow
    s.append([pelvis_x - 0.19, neck_y - 0.09 - arm_swing])
    # RWrist
    s.append([pelvis_x + 0.28, neck_y - 0.12 + arm_swing + arm_lift])
    # LWrist
    s.append([pelvis_x - 0.28, neck_y - 0.12 - arm_swing + arm_lift])
    # Pelvis (torso base)
    s.append([pelvis_x, pelvis_y + jump_y])
    # RHip
    s.append([pelvis_x + 0.08, pelvis_y + jump_y])
    # LHip
    s.append([pelvis_x - 0.08, pelvis_y + jump_y])
    # RKnee
    knee_swing = 0.11 * (1 - jump_phase)  # contract on take-off
    s.append([pelvis_x + 0.083, pelvis_y - 0.22 + jump_y + knee_swing])
    # LKnee
    s.append([pelvis_x - 0.083, pelvis_y - 0.22 + jump_y + knee_swing])
    # RAnkle
    ankle_down = 0 if jump_y > 0.03 else -0.015
    s.append([pelvis_x + 0.08, pelvis_y - 0.45 + jump_y + ankle_down])

    s = np.array(s)

    # Add cheerful shoulder/cheek wiggle ("happy" affect) to head, shoulders, wrists
    # Cheek smile: shoulders/wrists/hands
    smile_wiggle = 0.015 * np.sin(2*np.pi*jump_phase*2)
    s[2,0] += smile_wiggle
    s[3,0] -= smile_wiggle
    s[7,0] += 2*smile_wiggle
    s[8,0] -= 2*smile_wiggle

    # Sway slight left/right (lighter happy bounce)
    side_bounce = 0.01 * np.sin(2*np.pi*(jump_phase*3))
    s[:,0] += side_bounce

    return s

# Animate it!
fig, ax = plt.subplots(figsize=(4, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-0.45, 0.45)
ax.set_ylim(-0.25, 1.2)
scat = ax.scatter([], [], color='white', s=58)

def update(frame):
    n_frames = 60
    jump_period = 45   # frames per "jump" cycle (~0.75s at 60fps)
    s = pose_jump(frame % jump_period, jump_period)
    scat.set_offsets(s)
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=600, interval=1000/60, blit=True
)

plt.show()
