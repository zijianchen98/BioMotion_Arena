
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
fps = 50                       # frames per second
dt = 1.0 / fps                 # time step
f = 2.0                        # running cycle frequency (Hz)
omega = 2 * np.pi * f

# Body segment lengths
torso_len = 0.5
head_len = 0.15
shoulder_offset_x = 0.2
hip_offset_x = 0.15
upper_arm_len = 0.3
forearm_len = 0.3
thigh_len = 0.4
shin_len = 0.4

# Bounce (vertical) parameters for the root
root_base_y = 0.5
root_bounce_amp = 0.05

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(5, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot for 15 point-lights
pts = ax.scatter([], [], s=50, c='white')

def init():
    """Initialize the scatter offsets to empty."""
    pts.set_offsets(np.zeros((15, 2)))
    return pts,

def animate(frame):
    """Update function for animation."""
    t = frame * dt
    # Vertical bounce of the "root" (center of mass)
    y_root = root_base_y + root_bounce_amp * np.abs(np.sin(omega * t))
    x_root = 0.0

    # Joint positions array (15 joints)
    P = np.zeros((15, 2))

    #  0: Head
    #  1: Neck
    #  2: Left shoulder
    #  3: Left elbow
    #  4: Left hand
    #  5: Right shoulder
    #  6: Right elbow
    #  7: Right hand
    #  8: Root (pelvis)
    #  9: Left hip
    # 10: Left knee
    # 11: Left ankle
    # 12: Right hip
    # 13: Right knee
    # 14: Right ankle

    # Root (pelvis)
    P[8] = [x_root, y_root]

    # Neck and head
    neck = np.array([x_root, y_root + torso_len])
    head = neck + np.array([0.0, head_len])
    P[1] = neck
    P[0] = head

    # Shoulders
    ls = neck + np.array([-shoulder_offset_x, -0.1 * torso_len])
    rs = neck + np.array([shoulder_offset_x, -0.1 * torso_len])
    P[2] = ls
    P[5] = rs

    # Hips
    lh = np.array([x_root - hip_offset_x, y_root])
    rh = np.array([x_root + hip_offset_x, y_root])
    P[9] = lh
    P[12] = rh

    # Calculate limb angles
    # Legs: sinusoidal hip flexion/extension plus knee flexion
    hip_ang_l =  0.5 * np.sin(omega * t)
    hip_ang_r =  0.5 * np.sin(omega * t + np.pi)
    knee_ang_l = 1.0 * np.sin(omega * t + 0.5 * np.pi)
    knee_ang_r = 1.0 * np.sin(omega * t + np.pi + 0.5 * np.pi)

    # Left leg
    knee_l = lh + thigh_len * np.array([np.sin(hip_ang_l), np.cos(hip_ang_l)])
    shin_ang_l = hip_ang_l - knee_ang_l
    ankle_l = knee_l + shin_len * np.array([np.sin(shin_ang_l), np.cos(shin_ang_l)])
    P[10] = knee_l
    P[11] = ankle_l

    # Right leg
    knee_r = rh + thigh_len * np.array([np.sin(hip_ang_r), np.cos(hip_ang_r)])
    shin_ang_r = hip_ang_r - knee_ang_r
    ankle_r = knee_r + shin_len * np.array([np.sin(shin_ang_r), np.cos(shin_ang_r)])
    P[13] = knee_r
    P[14] = ankle_r

    # Arms: contralateral to legs
    shoulder_ang_r = 0.5 * np.sin(omega * t)            # right arm swings with right hip
    shoulder_ang_l = 0.5 * np.sin(omega * t + np.pi)    # left arm opposite
    elbow_ang_r =    0.6 * np.sin(omega * t + 0.5*np.pi)
    elbow_ang_l =    0.6 * np.sin(omega * t + np.pi + 0.5*np.pi)

    # Right arm
    elbow_r = rs + upper_arm_len * np.array([np.sin(shoulder_ang_r),
                                              np.cos(shoulder_ang_r)])
    hand_r = elbow_r + forearm_len * np.array([np.sin(shoulder_ang_r + elbow_ang_r),
                                                np.cos(shoulder_ang_r + elbow_ang_r)])
    P[6] = elbow_r
    P[7] = hand_r

    # Left arm
    elbow_l = ls + upper_arm_len * np.array([np.sin(shoulder_ang_l),
                                              np.cos(shoulder_ang_l)])
    hand_l = elbow_l + forearm_len * np.array([np.sin(shoulder_ang_l + elbow_ang_l),
                                                np.cos(shoulder_ang_l + elbow_ang_l)])
    P[3] = elbow_l
    P[4] = hand_l

    # Update scatter plot
    pts.set_offsets(P)
    return pts,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=500, interval=1000/fps, blit=True)

plt.show()
