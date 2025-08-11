
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint labels for reference:
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Wrist
# 6: Left Wrist
# 7: Spine (Upper)
# 8: Spine (Middle)
# 9: Spine (Lower)
# 10: Right Hip
# 11: Left Hip
# 12: Right Knee
# 13: Left Knee
# 14: Right Foot
# 15: Left Foot

# For 15 points, use the major joints of the happy man.
# We'll use 0-Head, 1-Right Shoulder, 2-Left Shoulder, 3-Right Elbow, 4-Left Elbow, 5-Right Wrist, 6-Left Wrist,
# 7-Chest(Upper Spine), 8-Hip(Center), 9-Right Hip, 10-Left Hip, 11-Right Knee, 12-Left Knee, 13-Right Foot, 14-Left Foot.

# Define the skeleton: stick figure proportions (arbitrary units)
def get_base_pose():
    # X,Y initial positions for each joint
    # The model is facing forward (wave with right hand), centered horizontally, standing up
    pose = np.array([
        [0.0, 8.0],    # 0: Head
        [1.2, 7.0],    # 1: Right Shoulder
        [-1.2, 7.0],   # 2: Left Shoulder
        [2.0, 6.0],    # 3: Right Elbow
        [-2.0, 6.0],   # 4: Left Elbow
        [2.8, 5.0],    # 5: Right Wrist
        [-2.8, 5.0],   # 6: Left Wrist
        [0.0, 7.2],    # 7: Chest (Upper Spine)
        [0.0, 5.2],    # 8: Hip Center
        [0.8, 5.2],    # 9: Right Hip
        [-0.8, 5.2],   #10: Left Hip
        [0.8, 3.2],    #11: Right Knee
        [-0.8, 3.2],   #12: Left Knee
        [0.8, 1.0],    #13: Right Foot
        [-0.8, 1.0],   #14: Left Foot
    ])
    return pose

# Animate arm-waving: right arm (shoulder-elbow-wrist)
# We'll rotate the right elbow and right wrist to create the wave!
def joint_angle_transform(t):
    # t should be [0, 2*pi] over the animation loop

    # Right arm waving: sinusoidal elbow flexion and wrist swinging up
    shoulder = np.array([1.2, 7.0])
    elbow_length = 1.2  # Shoulder to Elbow
    wrist_length = 1.1  # Elbow to Wrist

    # Elbow angle: base ~ -50 degrees, oscillate +/- 35 deg (rads)
    elbow_angle = np.deg2rad(-50 + 35*np.sin(t*2))
    # Wrist angle (relative to forearm): oscillates "waving" motion
    wrist_angle = np.deg2rad(50*np.sin(t*3) + 10*np.sin(t*7))

    # Calculate right elbow position
    r_elbow = shoulder + elbow_length * np.array([np.sin(elbow_angle), -np.cos(elbow_angle)])

    # Calculate right wrist position
    r_wrist = r_elbow + wrist_length * np.array([np.sin(elbow_angle + wrist_angle),
                                                 -np.cos(elbow_angle + wrist_angle)])
    return r_elbow, r_wrist

def left_arm_motion(t):
    # Minimal movement (natural deflection)
    shoulder = np.array([-1.2, 7.0])
    elbow_length = 1.2
    wrist_length = 1.1
    # Elbow gentle "relaxed" swing
    elbow_angle = np.deg2rad(-130 + 10*np.sin(t+2))
    wrist_angle = np.deg2rad(-8 + 10*np.sin(t+2))
    l_elbow = shoulder + elbow_length * np.array([np.sin(elbow_angle), -np.cos(elbow_angle)])
    l_wrist = l_elbow + wrist_length * np.array([np.sin(elbow_angle + wrist_angle),
                                                 -np.cos(elbow_angle + wrist_angle)])
    return l_elbow, l_wrist

def body_bounce(t):
    # Simple subtle vertical "bouncy" shift to make it happy and alive
    amplitude = 0.12
    return amplitude*np.sin(t*2.0)

def animate_func(i, dots,):
    # Animation callback
    # Time for smoothness (loop period)
    t = 2.0 * np.pi * i / Nframes

    basedots = get_base_pose()
    # Get arm motion
    r_elbow, r_wrist = joint_angle_transform(t)
    l_elbow, l_wrist = left_arm_motion(t)

    bounce = body_bounce(t)

    # Update positions for animated joints
    basedots[3] = r_elbow
    basedots[5] = r_wrist
    basedots[4] = l_elbow
    basedots[6] = l_wrist

    # Add the bounce to body parts (all except feet)
    for j in range(len(basedots)):
        if j not in [13,14]:  # Don't bounce feet
            basedots[j,1] += bounce

    # Update dot objects
    for d, xy in zip(dots, basedots):
        d.set_data(xy[0], xy[1])
    return dots

# Matplotlib setup
fig, ax = plt.subplots(figsize=(4,8))
ax.set_facecolor('black')
ax.set_xlim(-4,4)
ax.set_ylim(0,9)
ax.axis('off')

# Create 15 point-lights
dots = [ax.plot([],[], 'o', markersize=8, color='white')[0] for _ in range(15)]

Nframes = 120
ani = animation.FuncAnimation(fig, animate_func, fargs=(dots,), frames=Nframes, interval=1000/30, blit=True)

plt.show()
