
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Biological motion points (Plestkin 15-point scheme):
# 0: Head
# 1: Left shoulder
# 2: Right shoulder
# 3: Left elbow
# 4: Right elbow
# 5: Left wrist
# 6: Right wrist
# 7: Chest
# 8: Pelvis
# 9: Left hip
# 10: Right hip
# 11: Left knee
# 12: Right knee
# 13: Left ankle
# 14: Right ankle

# Skeleton structure, links only (for visualization, but not drawing lines per instructions)
# For running:
# Running cycle via joint angles and positions.

def get_skeleton_coordinates(phase):
    # Model parameters (in arbitrary units)
    head_y = 4.8
    neck_len = 0.4
    trunk_len = 1.3
    hip_width = 0.5
    shld_width = 0.8
    upper_arm = 0.55
    lower_arm = 0.5
    upper_leg = 0.7
    lower_leg = 0.7

    # Phase is [0, 1) for a full gait cycle
    w = 2 * np.pi * phase

    # Running: emphasize aerial phase, 
    # alternating arm and leg swings, and slight head/body vertical oscillation

    # Torso and pelvis oscillation (vertical + forward progression)
    trunk_dx = 3.0 * phase  # forward movement
    trunk_dy = 0.12 * np.sin(w)  # vertical bounce
    trunk_angle = 5*np.pi/180 * np.sin(w)  # rad, trunk leans forward slightly

    # Head bounce (more due to "heavy weight" subject)
    head_dy = 0.2 * np.sin(w)
    
    base_x = trunk_dx
    base_y = 2.6 + trunk_dy

    # Pelvis center
    pelvis_x = base_x
    pelvis_y = base_y

    # Chest center
    chest_x = pelvis_x + trunk_len * np.sin(trunk_angle)
    chest_y = pelvis_y + trunk_len * np.cos(trunk_angle)

    # Head
    head_x = chest_x
    head_y = chest_y + neck_len + 0.3 + head_dy

    # Shoulders (left, right)
    shld_theta = np.pi/2 + trunk_angle
    shld_x_l = chest_x - shld_width/2 * np.cos(trunk_angle)
    shld_x_r = chest_x + shld_width/2 * np.cos(trunk_angle)
    shld_y_l = chest_y + shld_width/2 * np.sin(trunk_angle)
    shld_y_r = chest_y - shld_width/2 * np.sin(trunk_angle)

    # Hips (left, right)
    hip_theta = np.pi/2 + trunk_angle
    hip_x_l = pelvis_x - hip_width/2 * np.cos(trunk_angle)
    hip_x_r = pelvis_x + hip_width/2 * np.cos(trunk_angle)
    hip_y_l = pelvis_y + hip_width/2 * np.sin(trunk_angle)
    hip_y_r = pelvis_y - hip_width/2 * np.sin(trunk_angle)

    # Arms swing: swing arms strongly for "heavy" person
    arm_swing = 60 * np.pi/180  # max swing, radians

    # Left, right (anti-phase to legs)
    left_arm_angle = arm_swing * np.sin(w + np.pi)
    right_arm_angle = arm_swing * np.sin(w)

    # Elbows (offset downward from shoulder, rotated by swing)
    elb_len = upper_arm

    left_elb_x = shld_x_l + elb_len * np.sin(left_arm_angle + trunk_angle)
    left_elb_y = shld_y_l - elb_len * np.cos(left_arm_angle + trunk_angle)
    right_elb_x = shld_x_r + elb_len * np.sin(right_arm_angle + trunk_angle)
    right_elb_y = shld_y_r - elb_len * np.cos(right_arm_angle + trunk_angle)

    # Wrists (forearm, continuing the angle)
    wrst_len = lower_arm

    left_wrist_x = left_elb_x + wrst_len * np.sin(left_arm_angle + trunk_angle)
    left_wrist_y = left_elb_y - wrst_len * np.cos(left_arm_angle + trunk_angle)
    right_wrist_x = right_elb_x + wrst_len * np.sin(right_arm_angle + trunk_angle)
    right_wrist_y = right_elb_y - wrst_len * np.cos(right_arm_angle + trunk_angle)

    # Legs: running -- mainly one leg is in air, one is on/near ground, both have exaggerated swing.
    # Use cos(w) for left/right opposition.
    leg_lift = 85 * np.pi / 180  # maximum hip flex
    # Add a little bend at knee for realism

    # Hip angles
    left_hip_angle = leg_lift * np.cos(w)
    right_hip_angle = leg_lift * np.cos(w + np.pi)

    # Knee angles modulate for flight/stance
    # When hip flexed (forward), knee is bent more;
    # When hip extended (back), leg is straighter.
    left_knee_angle = 100*np.pi/180 - 30*np.pi/180 * np.cos(w)
    right_knee_angle = 100*np.pi/180 - 30*np.pi/180 * np.cos(w + np.pi)

    # Ankles: slightly point the toes at end of swing phase
    left_ankle_angle = 25*np.pi/180 * np.sin(w+0.3)
    right_ankle_angle = 25*np.pi/180 * np.sin(w+np.pi+0.3)

    # LEFT leg
    # Knee
    left_knee_x = hip_x_l + upper_leg * np.sin(left_hip_angle + trunk_angle)
    left_knee_y = hip_y_l - upper_leg * np.cos(left_hip_angle + trunk_angle)
    # Ankle
    left_ankle_x = left_knee_x + lower_leg * np.sin(left_hip_angle + trunk_angle + left_knee_angle)
    left_ankle_y = left_knee_y - lower_leg * np.cos(left_hip_angle + trunk_angle + left_knee_angle)

    # RIGHT leg
    right_knee_x = hip_x_r + upper_leg * np.sin(right_hip_angle + trunk_angle)
    right_knee_y = hip_y_r - upper_leg * np.cos(right_hip_angle + trunk_angle)
    right_ankle_x = right_knee_x + lower_leg * np.sin(right_hip_angle + trunk_angle + right_knee_angle)
    right_ankle_y = right_knee_y - lower_leg * np.cos(right_hip_angle + trunk_angle + right_knee_angle)

    return np.array([
        [head_x, head_y],                             # 0 head
        [shld_x_l, shld_y_l],                         # 1 left shoulder
        [shld_x_r, shld_y_r],                         # 2 right shoulder
        [left_elb_x, left_elb_y],                     # 3 left elbow
        [right_elb_x, right_elb_y],                   # 4 right elbow
        [left_wrist_x, left_wrist_y],                 # 5 left wrist
        [right_wrist_x, right_wrist_y],               # 6 right wrist
        [chest_x, chest_y],                           # 7 chest
        [pelvis_x, pelvis_y],                         # 8 pelvis
        [hip_x_l, hip_y_l],                           # 9 left hip
        [hip_x_r, hip_y_r],                           # 10 right hip
        [left_knee_x, left_knee_y],                   # 11 left knee
        [right_knee_x, right_knee_y],                 # 12 right knee
        [left_ankle_x, left_ankle_y],                 # 13 left ankle
        [right_ankle_x, right_ankle_y],               # 14 right ankle
    ])

# Set up animation
fig, ax = plt.subplots(figsize=(4, 7))
ax.set_facecolor('black')
plt.axis('off')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 7)

points, = ax.plot([], [], 'wo', ms=8)

def animate(frame):
    t = frame / 60  # seconds
    gait_period = 0.6  # seconds per stride (running: 0.5-0.7s)
    phase = (t / gait_period) % 1.0
    coords = get_skeleton_coordinates(phase)
    points.set_data(coords[:,0], coords[:,1])
    return points,

ani = FuncAnimation(
    fig, animate, frames=240, interval=1000/60, blit=True)

plt.show()
