
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint order for 15 points: [Head, ShoulderL, ShoulderR, ElbowL, ElbowR, WristL, WristR,
# HipL, HipR, KneeL, KneeR, AnkleL, AnkleR, Hand_L_weight, Hand_R_weight]
# We'll denote anatomical symmetry by having L(Left) as the viewer's right, and vice versa.

# Parameters
FPS = 30
DURATION = 5  # seconds
N_FRAMES = DURATION * FPS
N_JOINTS = 15

# Link lengths (scaled)
HEAD_TO_NECK = 0.14
NECK_TO_SHOULDER = 0.055
SHOULDER_TO_ELBOW = 0.18
ELBOW_TO_WRIST = 0.16
SHOULDER_WIDTH = 0.23
HIP_WIDTH = 0.18
NECK_TO_HIP = 0.21
HIP_TO_KNEE = 0.22
KNEE_TO_ANKLE = 0.21
WRIST_TO_WEIGHT = 0.06

# "Heavy weights": makes arms hang down and swing smaller, with hands offset by weights

def walk_cycle(t):
    # t: phase, 0~2pi
    # Biomechanical walk parameters
    stride = 0.17  # Half stride amplitude
    height = 0.0  # vertical offset

    # Hip bob (vertical)
    hip_bob = 0.015 * np.sin(2*t)

    # Horizontal swing
    xhip = stride * np.sin(t)
    yhip = -NECK_TO_HIP + hip_bob

    # Shoulder rotation (arms swing opposite to legs)
    shoulder_swing = 0.45 * np.sin(t + np.pi)

    # Arms swing less and hang lower due to "heavy weight"
    arm_swing = 0.25 * np.sin(t + np.pi)
    arm_hang = 0.13

    # Leg swing
    leg_swing = 0.50 * np.sin(t)

    # Head
    head = np.array([0.0, HEAD_TO_NECK + 0.02*np.sin(2*t)])

    # Shoulders (midpoint at (0,0)), then offset outward
    shoulder_center = np.array([0.0, 0.0 + 0.01*np.sin(2*t)])
    shoulder_L = shoulder_center + np.array([-SHOULDER_WIDTH/2, 0])
    shoulder_R = shoulder_center + np.array([+SHOULDER_WIDTH/2, 0])

    # Hips
    hip_center = np.array([xhip, yhip])
    hip_L = hip_center + np.array([-HIP_WIDTH/2, 0])
    hip_R = hip_center + np.array([+HIP_WIDTH/2, 0])

    # Knees
    knee_L = hip_L + np.array([
        leg_swing * 0.6,               # Leg swing (horiz)
        -HIP_TO_KNEE + 0.04*np.cos(t + np.pi) # Vertical, little flexion
    ])
    knee_R = hip_R + np.array([
        -leg_swing * 0.6,              # Opposite swing
        -HIP_TO_KNEE + 0.04*np.cos(t)
    ])

    # Ankles
    ankle_L = knee_L + np.array([
        leg_swing * 0.4,                # Lower leg swing
        -KNEE_TO_ANKLE + 0.015*np.cos(2*t)
    ])
    ankle_R = knee_R + np.array([
        -leg_swing * 0.4,               # Lower leg
        -KNEE_TO_ANKLE + 0.015*np.cos(2*t + np.pi)
    ])

    # Elbows
    elbow_L = shoulder_L + np.array([
        arm_swing * 0.8,                # Arm swing
        -SHOULDER_TO_ELBOW * np.sqrt(1-arm_hang**2) + arm_hang
    ])
    elbow_R = shoulder_R + np.array([
        -arm_swing * 0.8,
        -SHOULDER_TO_ELBOW * np.sqrt(1-arm_hang**2) + arm_hang
    ])

    # Wrists
    wrist_L = elbow_L + np.array([
        arm_swing * 0.65,
        -ELBOW_TO_WRIST * np.sqrt(1-arm_hang**2) + arm_hang
    ])
    wrist_R = elbow_R + np.array([
        -arm_swing * 0.65,
        -ELBOW_TO_WRIST * np.sqrt(1-arm_hang**2) + arm_hang
    ])

    # Hand positions with weight (downward offset)
    hand_weight_L = wrist_L + np.array([
        0, -WRIST_TO_WEIGHT - 0.02*np.abs(arm_swing)
    ])
    hand_weight_R = wrist_R + np.array([
        0, -WRIST_TO_WEIGHT - 0.02*np.abs(arm_swing)
    ])

    # Collect all points: [Head, ShoulderL, ShoulderR, ElbowL, ElbowR, WristL, WristR,
    # HipL, HipR, KneeL, KneeR, AnkleL, AnkleR, Hand_L_weight, Hand_R_weight]
    points = np.vstack([
        head,
        shoulder_L,
        shoulder_R,
        elbow_L,
        elbow_R,
        wrist_L,
        wrist_R,
        hip_L,
        hip_R,
        knee_L,
        knee_R,
        ankle_L,
        ankle_R,
        hand_weight_L,
        hand_weight_R,
    ])
    # Apply an overall vertical shift for display
    points[:,1] += 0.6
    return points

# Create animation frames
walk_times = np.linspace(0, 2*np.pi, N_FRAMES, endpoint=False)
frames = [walk_cycle(t) for t in walk_times]

# Prepare the plot
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')
lim = 0.51
ax.set_xlim(-lim, lim)
ax.set_ylim(0.15, 1.15)  # Y range

dots, = ax.plot([], [], 'o', color='white', markersize=8)

def init():
    dots.set_data([], [])
    return (dots,)

def animate(i):
    pts = frames[i]
    dots.set_data(pts[:,0], pts[:,1])
    return (dots,)

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=N_FRAMES, interval=1000/FPS, blit=True)

plt.show()
