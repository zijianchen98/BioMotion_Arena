
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# POINT-LIGHT WALKER: 15 points, 'sad, heavy' walk

# Define point indices for body parts:
# 0: Head
# 1-2: Shoulders (Left, Right)
# 3-4: Elbows (Left, Right)
# 5-6: Wrists (Left, Right)
# 7-8: Hips (Left, Right)
# 9-10: Knees (Left, Right)
# 11-12: Ankles (Left, Right)
# 13-14: Feet (Left, Right)

# Skeleton structure: (x0,y0) = center top (head), positive y points down!

def generate_walker_frame(t, step_period=1.4):
    """Generates 2D positions for the 15 joints at phase t (0-1) of walking.
       Sad, heavy look: head down, hunched, less arm swing, down shoulders."""

    # Basic dimensions (in arbitrary units)
    head_height = 2.2
    neck_height = 2.0
    shoulder_height = 1.9
    shoulder_width = 0.42
    spine_len = 0.42
    hip_height = 1.1
    hip_width = 0.29
    upperleg_len = 0.54
    lowerleg_len = 0.52
    foot_len = 0.13

    upperarm_len = 0.37
    forearm_len = 0.36

    # 'Sad/Heavy' parameters
    head_drop = 0.09
    trunk_hunch = np.deg2rad(18)   # trunk lean forward
    shoulder_drop = 0.09
    arm_swing_scale = 0.60  # reduced arm swing
    step_vscale = 0.78  # shorter step
    head_pitch = np.deg2rad(18) # head down

    phase = 2*np.pi*t  # (0-2pi)

    # Hip move (horizontal swing: pelvis shifts L/R)
    hip_lr = 0.035* np.sin(phase)    

    # COM forward motion (heavy/slower/no bounce)
    stride = 0.35 * step_vscale
    com_y = 0 + 0.14 * np.sin(phase + np.pi) # weight sink
    com_x = stride * np.sin(phase)

    # Trunk base position (mid-hips)
    trunk_bx = com_x
    trunk_by = hip_height + (shoulder_height-hip_height) * 0.52 + com_y

    # Trunk/hunch vector for body
    trunk_angle = trunk_hunch
    trunk_dx = np.sin(trunk_angle)*(shoulder_height-hip_height)
    trunk_dy = np.cos(trunk_angle)*(shoulder_height-hip_height)

    # Head
    head_x = trunk_bx + trunk_dx*0.7 + np.sin(head_pitch)*head_height*0.09
    head_y = shoulder_height + head_height + com_y - head_drop

    # Shoulders
    sh_mid_x = trunk_bx + trunk_dx
    sh_mid_y = shoulder_height + com_y - shoulder_drop
    
    sh_l = [sh_mid_x - shoulder_width/2, sh_mid_y]
    sh_r = [sh_mid_x + shoulder_width/2, sh_mid_y]

    # Hips
    hip_mid_x = com_x + hip_lr
    hip_mid_y = hip_height + com_y
    hi_l = [hip_mid_x - hip_width/2, hip_mid_y]
    hi_r = [hip_mid_x + hip_width/2, hip_mid_y]

    # Leg phases (opposite swings)
    leg_theta = np.arccos(np.clip((upperleg_len**2 + lowerleg_len**2 - (0.75*foot_len)**2)/(2*upperleg_len*lowerleg_len), -1.0, 1.0))
    left_leg_phase = phase
    right_leg_phase = phase + np.pi

    # Step trajectory (heavier walk: foot lifts less and spends more time on ground)
    foot_lift = 0.10
    foot_apex = 0.20
    
    def leg_angles(phase0):
        theta = 0.66*np.sin(phase0)*step_vscale    # swing angle from hip
        knee = 0.33*np.sin(2*phase0)
        a = trunk_angle
        hip_angle = a + theta
        knee_angle = 0.8*np.abs(np.sin(phase0))
        ankle_angle = -0.35*np.sin(phase0)
        return hip_angle, knee_angle, ankle_angle

    def leg_points(hip_pos, phase0, side=1):
        hip_angle, knee_angle, ankle_angle = leg_angles(phase0)
        hx, hy = hip_pos

        # knee
        kx = hx + upperleg_len * np.sin(hip_angle)
        ky = hy - upperleg_len * np.cos(hip_angle)

        # ankle
        ax = kx + lowerleg_len * np.sin(hip_angle + knee_angle)
        ay = ky - lowerleg_len * np.cos(hip_angle + knee_angle)

        # foot (subtle foot roll: point slightly forward for 'heavier' look)
        fx = ax + foot_len * np.sin(hip_angle + knee_angle + ankle_angle + 0.2*side)
        fy = ay - foot_len * np.cos(hip_angle + knee_angle + ankle_angle + 0.18*side)

        # vertical foot trajectory (heavier: less lift)
        t步 = (phase0%(2*np.pi))/ (2*np.pi)
        alpha = np.fmax(0.0, (np.sin(phase0)))+0.05
        lift = foot_lift*alpha
        ay -= lift
        fy -= lift

        return [kx, ky], [ax, ay], [fx, fy]

    # Left leg
    knee_l, ankle_l, foot_l = leg_points(hi_l, left_leg_phase, side=-1)
    # Right leg
    knee_r, ankle_r, foot_r = leg_points(hi_r, right_leg_phase, side=1)

    # Arm phases (smaller swing, hunched, wrists/forearms drop lower)
    arm_swing = 0.41 * arm_swing_scale
    elbow_drop = 0.05

    def arm_points(shoulder_pos, phase0, side=1):
        hx, hy = shoulder_pos
        arm_phase = np.sin(phase0) * arm_swing * side

        # Shoulders further forward due to hunch
        upper_angle_base = trunk_angle + np.deg2rad(11)*side + np.deg2rad(22)*(-1)
        upper_angle = upper_angle_base + arm_phase
        elbow_x = hx + upperarm_len * np.sin(upper_angle)
        elbow_y = hy - upperarm_len * np.cos(upper_angle) + elbow_drop

        lower_angle = upper_angle + 0.72*side + 0.11*np.sin(phase0+1.1*side)
        wrist_x = elbow_x + forearm_len * np.sin(lower_angle)
        wrist_y = elbow_y - forearm_len * np.cos(lower_angle) + 0.04*side

        return [elbow_x, elbow_y], [wrist_x, wrist_y]

    # Left arm (counter phase to right leg)
    elbow_l, wrist_l = arm_points(sh_l, right_leg_phase, side=-1)
    # Right arm (counter phase to left leg)
    elbow_r, wrist_r = arm_points(sh_r, left_leg_phase, side=1)

    # Each point: [x, y]
    positions = np.array([
        [head_x, head_y],       # 0: Head
        sh_l,                   # 1: Left Shoulder
        sh_r,                   # 2: Right Shoulder
        elbow_l,                # 3: Left Elbow
        elbow_r,                # 4: Right Elbow
        wrist_l,                # 5: Left Wrist
        wrist_r,                # 6: Right Wrist
        hi_l,                   # 7: Left Hip
        hi_r,                   # 8: Right Hip
        knee_l,                 # 9: Left Knee
        knee_r,                 #10: Right Knee
        ankle_l,                #11: Left Ankle
        ankle_r,                #12: Right Ankle
        foot_l,                 #13: Left Foot
        foot_r,                 #14: Right Foot
    ])
    return positions

# === Animation ===

fig, ax = plt.subplots(figsize=(3.0, 7.0), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Axes limits (centered body, y down)
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.7, 2.65)

points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    t = (i % 56)/56.0
    pos = generate_walker_frame(t)
    points.set_data(pos[:,0], pos[:,1])
    return points,

anim = FuncAnimation(
    fig, animate, init_func=init, frames=56, interval=33, blit=True
)

plt.show()
