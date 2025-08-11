
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint indices: 15 markers
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Hand
# 6: Left Hand
# 7: Torso (chest/neck)
# 8: Hip (pelvis/crotch)
# 9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Ankle
# 14: Left Ankle

def sitting_down_pose(t):
    """
    Given t in [0,1], returns 15 x,y coordinates for a smiling, light posture human
    sitting down. t=0 is standing, t=1 is fully seated.
    """
    # Body model parameters
    # All lengths in body units; will be scaled for plotting
    head_y = 0.0  # base y for hip (everything is relative)
    head_to_shoulder = 1.0
    shoulder_to_torso = 1.0
    torso_to_hip = 1.2
    
    shoulder_width = 1.2
    hip_width = 0.8
    upper_arm = 0.8
    lower_arm = 0.8
    hand_size = 0.15
    upper_leg = 1.2
    lower_leg = 1.1
    foot_size = 0.2

    # During sit, knees bend, hips drop
    # t in [0,1]: 0 fully standing, 1 sitting on a chair
    # Animate vertical hip descent, hip/knee/ankle angles, arm movement

    # Standing reference height (used for foot anchoring)
    body_base_y = 6.5

    # Head and Torso
    # Torso angle: starts upright, then leans (slightly) forward while sitting
    torso_angle = np.deg2rad(0 + 25*t)  # degrees; positive = lean forward

    # Hip y descends from full stand to chair height
    hip_y = body_base_y - (2.2*t)   # drop to chair height
    # x center stays constant

    # Shoulders (neck/base of head) follow hip but at torso length and angle
    torso_length = head_to_shoulder + shoulder_to_torso + torso_to_hip
    shoulder_y = hip_y + torso_length * np.cos(torso_angle)
    shoulder_x = 0 + torso_length * np.sin(torso_angle)

    # Head
    head_x = shoulder_x
    head_y_ = shoulder_y + 0.42
    # Smile! (will plot mouth with three points below head for extra "happiness")

    # Shoulders (right and left)
    r_shoulder_x = shoulder_x + shoulder_width/2 * np.cos(np.pi/2 - torso_angle)
    r_shoulder_y = shoulder_y - shoulder_width/2 * np.sin(np.pi/2 - torso_angle)
    l_shoulder_x = shoulder_x - shoulder_width/2 * np.cos(np.pi/2 - torso_angle)
    l_shoulder_y = shoulder_y + shoulder_width/2 * np.sin(np.pi/2 - torso_angle)

    # Hips (right and left)
    r_hip_x = 0 + hip_width/2
    l_hip_x = 0 - hip_width/2
    r_hip_y = hip_y
    l_hip_y = hip_y

    # Torso (chest/neck and pelvis)
    torso_x = 0 + torso_length/2 * np.sin(torso_angle)
    torso_y = hip_y + torso_length/2 * np.cos(torso_angle)
    # Pelvis (midpoint between hips)
    pelvis_x = 0
    pelvis_y = hip_y

    # Arms
    # While sitting, arms bend at elbow and move forward slightly
    arm_forward = np.deg2rad(10 + 40 * t)  # angle arms move forward from vertical
    elbow_angle = np.pi - np.deg2rad(60 + 40*t)  # how much the elbow bends

    # Right upper arm
    r_elbow_x = r_shoulder_x + upper_arm * np.sin(arm_forward)
    r_elbow_y = r_shoulder_y - upper_arm * np.cos(arm_forward)
    # Right lower arm (bent)
    r_hand_x = r_elbow_x + lower_arm * np.sin(arm_forward - elbow_angle)
    r_hand_y = r_elbow_y - lower_arm * np.cos(arm_forward - elbow_angle)
    # Left upper arm
    l_elbow_x = l_shoulder_x + upper_arm * np.sin(arm_forward)
    l_elbow_y = l_shoulder_y - upper_arm * np.cos(arm_forward)
    # Left lower arm (bent)
    l_hand_x = l_elbow_x + lower_arm * np.sin(arm_forward - elbow_angle)
    l_hand_y = l_elbow_y - lower_arm * np.cos(arm_forward - elbow_angle)

    # Legs
    # Sitting: hips, knees, and ankles form approximately 90 deg angles at full sit
    # Animate that (from standing straight) using t
    hip_bend = np.deg2rad(5 + 80*t)  # angle hip flexes
    knee_bend = np.deg2rad(0 + 85*t)  # knee flexes toward 90

    # Right leg
    r_knee_x = r_hip_x + upper_leg * np.sin(hip_bend)
    r_knee_y = r_hip_y - upper_leg * np.cos(hip_bend)
    r_ankle_x = r_knee_x + lower_leg * np.sin(hip_bend + knee_bend)
    r_ankle_y = r_knee_y - lower_leg * np.cos(hip_bend + knee_bend)
    # Left leg
    l_knee_x = l_hip_x + upper_leg * np.sin(hip_bend)
    l_knee_y = l_hip_y - upper_leg * np.cos(hip_bend)
    l_ankle_x = l_knee_x + lower_leg * np.sin(hip_bend + knee_bend)
    l_ankle_y = l_knee_y - lower_leg * np.cos(hip_bend + knee_bend)

    # Offset whole figure upward to fit in plot
    offset = 0.3
    all_x = np.array([
        head_x,
        r_shoulder_x, l_shoulder_x,
        r_elbow_x, l_elbow_x,
        r_hand_x, l_hand_x,
        torso_x,
        pelvis_x,
        r_hip_x, l_hip_x,
        r_knee_x, l_knee_x,
        r_ankle_x, l_ankle_x,
    ])    
    all_y = np.array([
        head_y_+offset,
        r_shoulder_y+offset, l_shoulder_y+offset,
        r_elbow_y+offset, l_elbow_y+offset,
        r_hand_y+offset, l_hand_y+offset,
        torso_y+offset,
        pelvis_y+offset,
        r_hip_y+offset, l_hip_y+offset,
        r_knee_y+offset, l_knee_y+offset,
        r_ankle_y+offset, l_ankle_y+offset,
    ])
    return all_x, all_y

# Create the animation
fig, ax = plt.subplots(figsize=(3, 6))
ax.set_facecolor('black')
plt.axis('off')

# Set axis to fit standing and sitting cases
ax.set_xlim(-2, 2)
ax.set_ylim(0, 8)
ax.set_aspect('equal')

dots, = ax.plot([], [], 'o', color='white', markersize=8)

# Frame: show smile below head (for "happyman") as 3 points (not counting towards 15 spec; just visual add-on)
def smile_points(head_x, head_y):
    r = 0.18
    smile_angle = np.linspace(np.pi/6, 5*np.pi/6, 3)
    xs = head_x + r * np.cos(smile_angle)
    ys = head_y - 0.13 + r * np.sin(smile_angle)
    return xs, ys

smiles, = ax.plot([], [], 'o', color='white', markersize=4)

def init():
    dots.set_data([], [])
    smiles.set_data([], [])
    return dots, smiles

n_frames = 60  # smooth
def animate(i):
    t = i/(n_frames-1)
    # For smoothness, slow in/out: t in [0,1]
    t_ease = 0.5 - 0.5*np.cos(np.pi*t)
    x, y = sitting_down_pose(t_ease)
    dots.set_data(x, y)
    # Put smile under head only
    xs, ys = smile_points(x[0], y[0])
    smiles.set_data(xs, ys)
    return dots, smiles

ani = animation.FuncAnimation(fig, animate, frames=n_frames,
                              blit=True, interval=1000/30, init_func=init)

plt.show()
