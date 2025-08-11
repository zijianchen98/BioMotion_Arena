
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define body points (joints): [head, neck, r_shoulder, l_shoulder, r_elbow, l_elbow,
#   r_wrist, l_wrist, mid_hip, r_hip, l_hip, r_knee, l_knee, r_ankle, l_ankle]
#
# Indices for readability
HEAD, NECK, R_SHOULDER, L_SHOULDER, R_ELBOW, L_ELBOW, \
R_WRIST, L_WRIST, MID_HIP, R_HIP, L_HIP, R_KNEE, L_KNEE, R_ANKLE, L_ANKLE = range(15)

def get_pose(t, jump_period=2.0, jump_height=2.5, fps=30):
    """
    Returns array of positions for body point-lights at time t (in seconds).
    """

    # Body segment lengths (units: arbitrary, for visual proportion)
    head2neck = 0.35
    neck2shoulder = 0.18
    shoulder_span = 0.55
    shoulder2elbow = 0.37
    elbow2wrist = 0.37
    neck2hip = 0.57
    hip_span = 0.35
    hip2knee = 0.43
    knee2ankle = 0.43

    # Body midline
    mid_x = 0.
    base_y = 0.

    # Jump: vertical trajectory (smooth take-off and landing, single jump per cycle)
    phase = (t % jump_period) / jump_period
    # Vertical displacement: smooth parabola, peak at phase=0.5
    jump_y = (np.sin(np.pi * phase)) * jump_height

    # Also modulate arms, legs based on phase (simulate true jump kinematics)
    # For a jump, knees/hips/ankles flex during crouch, then extend rapidly at take-off
    # We'll model simple, plausible angle curves:
    # - Crouch: flex at phase ~0.1-0.3, full extend at phase ~0.5 (airborne), flex at landing (0.7-1.0)
    def angle_curve(phase, flex=60, extend=180, crouch_start=0.1, crouch_end=0.3,
                   flight_start=0.3, flight_end=0.7, land_start=0.7, land_end=1.0):
        if crouch_start < phase < crouch_end:
            # Flex linearly
            return np.interp(phase, [crouch_start, crouch_end], [extend, flex])
        elif flight_start < phase < flight_end:
            # Extend in flight
            return extend
        elif land_start < phase < land_end:
            return np.interp(phase, [land_start, land_end], [extend, flex])
        else:
            return extend

    # Assign joint angles per phase:
    # - Hip: 0 = upright, positive = flex (bend)
    # - Knee: 0 = fully straight, positive = flexed
    # - Ankle: 0 = neutral, positive = dorsiflex

    # For simplicity, only move in sagittal plane (y is up, x is left-right), symmetric for both sides

    # Hip, knee, ankle angle evolution over jump
    hip_angle = angle_curve(phase, flex=50, extend=0)
    knee_angle = angle_curve(phase, flex=80, extend=0)
    ankle_angle = angle_curve(phase, flex=30, extend=0)

    # Arms swing up during jump for lift, then come down
    if phase < 0.5:
        arm_angle = np.interp(phase, [0.0, 0.5], [90, 200])  # degrees, 90=down, 180=straight up
    else:
        arm_angle = np.interp(phase, [0.5, 1.0], [200, 90])
    # Elbow flexes slightly at top
    elbow_flex = np.interp(abs(phase-0.5), [0, 0.5], [10, 70])

    # Build skeleton
    points = np.zeros((15,2))
    # Mid hip is origin
    points[MID_HIP] = [mid_x, base_y + jump_y]

    # Hips (left/right)
    points[R_HIP] = [mid_x - hip_span/2, base_y + jump_y]
    points[L_HIP] = [mid_x + hip_span/2, base_y + jump_y]

    # Spine up to neck
    neck_y = base_y + jump_y + neck2hip
    points[NECK] = [mid_x, neck_y]

    # Head
    points[HEAD] = [mid_x, neck_y + head2neck]

    # Shoulders
    points[R_SHOULDER] = [mid_x - shoulder_span/2, neck_y]
    points[L_SHOULDER] = [mid_x + shoulder_span/2, neck_y]

    # Arms: from shoulders with swing angle
    # Right arm (negative x)
    theta = np.deg2rad(arm_angle)
    points[R_ELBOW] = [
        points[R_SHOULDER,0] + shoulder2elbow * np.cos(theta),
        points[R_SHOULDER,1] + shoulder2elbow * np.sin(theta)
    ]
    points[R_WRIST] = [
        points[R_ELBOW,0] + elbow2wrist * np.cos(theta + np.deg2rad(elbow_flex)),
        points[R_ELBOW,1] + elbow2wrist * np.sin(theta + np.deg2rad(elbow_flex))
    ]
    # Left arm (positive x)
    points[L_ELBOW] = [
        points[L_SHOULDER,0] + shoulder2elbow * np.cos(theta),
        points[L_SHOULDER,1] + shoulder2elbow * np.sin(theta)
    ]
    points[L_WRIST] = [
        points[L_ELBOW,0] + elbow2wrist * np.cos(theta + np.deg2rad(elbow_flex)),
        points[L_ELBOW,1] + elbow2wrist * np.sin(theta + np.deg2rad(elbow_flex))
    ]

    # Legs: hips → knees → ankles
    # Both sides, in the direction of -pi/2 + hip_angle for thigh (down + hip flex), then knee for shin, ankle for foot (not rendered)
    for side, HIP, KNEE, ANKLE in [(R_HIP, R_HIP, R_KNEE, R_ANKLE), (L_HIP, L_HIP, L_KNEE, L_ANKLE)]:
        # Thigh: origin at hip; directed downward, flexed by hip_angle
        thigh_theta = -np.pi/2 + np.deg2rad(hip_angle)
        points[KNEE] = [
            points[HIP,0] + hip2knee * np.cos(thigh_theta),
            points[HIP,1] + hip2knee * np.sin(thigh_theta)
        ]
        # Shin: from knee, flexed by knee_angle (relative to thigh)
        shin_theta = thigh_theta + np.deg2rad(knee_angle)
        points[ANKLE] = [
            points[KNEE,0] + knee2ankle * np.cos(shin_theta),
            points[KNEE,1] + knee2ankle * np.sin(shin_theta)
        ]

    return points

# Matplotlib animation

fig, ax = plt.subplots(figsize=(3.2,6.4))
ax.set_facecolor('black')
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Plot range: big enough for man jumping
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 4.5)
ax.set_xticks([])
ax.set_yticks([])

# Prepare for 15 points
lights, = ax.plot([], [], 'o', color='white', markersize=9)

def init():
    lights.set_data([], [])
    return lights,

def animate(i):
    t = i / 30  # seconds, at 30 fps
    pts = get_pose(t)
    lights.set_data(pts[:,0], pts[:,1])
    return lights,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=60, interval=1000/30, blit=True
)

plt.show()
