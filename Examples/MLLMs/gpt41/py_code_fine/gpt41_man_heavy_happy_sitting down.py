
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- Point-light Model Configuration ---- #
# Joint order (from top to bottom, left to right, standard for 15 points):
# 1. Head
# 2-3. Right shoulder, Left shoulder
# 4-5. Right elbow, Left elbow
# 6-7. Right wrist, Left wrist
# 8-9. Right hip, Left hip
# 10-11. Right knee, Left knee
# 12-13. Right ankle, Left ankle
# 14-15. Right foot, Left foot

# Define the neutral (standing/starting) pose in 2D (X, Y), in arbitrary units

def get_heavy_weight_offsets():
    """Offsets for heavyman: broader and bulkier body."""
    # Slight offsets for shoulders, hips, knees, ankles for heavier appearance
    # These offsets will be added to X coordinates of shoulder, hips, knees, ankles, feet
    offset = {
        'shoulder': 0.15,
        'hip': 0.18,
        'knee': 0.16,
        'ankle': 0.16,
        'foot': 0.12
    }
    return offset

def get_body_points(t, duration=2.0):
    """
    Returns 15 (X, Y) points for the current time t in the sit-down animation.

    Arguments:
      t: elapsed time in seconds.
      duration: total duration of the animation (sit down).

    Returns: np.ndarray shape (15,2)
    """
    # Parameters
    offsets = get_heavy_weight_offsets()
    # Key body proportions (base positions)
    y_head = 3.6
    y_shoulder = 3.2
    y_hip = 2.2
    y_knee = 1.1
    y_ankle = 0.3
    # X coords (midline = 0). We'll space arms/legs from here using offsets
    x_shoulder = 0.45 + offsets['shoulder']
    x_hip = 0.35 + offsets['hip']
    x_knee = 0.28 + offsets['knee']
    x_ankle = 0.30 + offsets['ankle']
    x_foot = 0.40 + offsets['foot']
    # Angles (degrees)
    max_knee_angle = 90  # degrees: final sitting
    max_hip_angle = 70   # degrees: how far hip comes forward

    # Interpolate
    phase = min(max(t / duration, 0), 1)
    # Use ease-in-out for smooth movement
    s = 0.5 - 0.5 * np.cos(np.pi * phase)

    # Hip & knee bending: standing (angle=0) -> sitting
    hip_shift = max_hip_angle * s
    knee_bend = max_knee_angle * s

    # Hip moves slightly forward and down when sitting down.
    hip_y = y_hip - 0.45 * s      # goes down
    hip_x = 0.0 + 0.20 * s        # slides slightly forward ("heavy" weight exaggerates this)
    # Knee calculation
    upper_leg_length = y_hip - y_knee
    theta_hip = np.deg2rad(hip_shift)  # from vertical
    knee_x = hip_x + np.sin(theta_hip) * upper_leg_length
    knee_y = hip_y - np.cos(theta_hip) * upper_leg_length
    # Ankle calculation
    lower_leg_length = y_knee - y_ankle
    theta_knee = np.deg2rad(knee_bend)
    # The shank bends relative to the thigh.
    # Final shank points almost horizontally in a sitting position (heavy person: might go out a bit)
    ankle_x = knee_x + np.sin(theta_hip + theta_knee) * lower_leg_length
    ankle_y = knee_y - np.cos(theta_hip + theta_knee) * lower_leg_length
    # Foot
    foot_x = ankle_x + 0.12 * (1.0 + 0.4 * s)  # extends outward in sitting
    foot_y = ankle_y

    # Mirror for left/right
    def side(val, side):  # side=1 for right, -1 for left
        return val * side

    # Arms: move forward and down ("heavy" people use arms when sitting)
    arm_swing = 45 * s     # degrees, forward swing
    elbow_spread = 0.15 * (1-s) + 0.25 * s  # arms open a bit while sitting
    
    # Shoulders
    r_shoulder = np.array([ side(x_shoulder, 1), y_shoulder ])
    l_shoulder = np.array([ side(x_shoulder, -1), y_shoulder ])
    # Elbows (relative: down and to the side, swinging forward)
    upper_arm_length = y_shoulder - (y_shoulder - y_hip)*0.55
    elbow_xr = r_shoulder[0] + np.sin(np.deg2rad(arm_swing)) * upper_arm_length + elbow_spread
    elbow_xl = l_shoulder[0] + np.sin(np.deg2rad(arm_swing)) * upper_arm_length - elbow_spread
    elbow_yr = r_shoulder[1] - np.cos(np.deg2rad(arm_swing)) * upper_arm_length
    elbow_yl = l_shoulder[1] - np.cos(np.deg2rad(arm_swing)) * upper_arm_length
    # Wrists (arms bend more as subject sits)
    forearm_length = 0.33
    wrist_angle = 80 * s   # bends upward
    wrist_xr = elbow_xr + np.sin(np.deg2rad(wrist_angle)) * forearm_length
    wrist_xl = elbow_xl + np.sin(np.deg2rad(wrist_angle)) * forearm_length
    wrist_yr = elbow_yr - np.cos(np.deg2rad(wrist_angle)) * forearm_length
    wrist_yl = elbow_yl - np.cos(np.deg2rad(wrist_angle)) * forearm_length

    # Shoulders also move slightly forward
    shoulder_shift = 0.07 * s
    r_shoulder[0] += shoulder_shift
    l_shoulder[0] += shoulder_shift

    # Hips (left/right)
    r_hip = np.array([ hip_x + side(x_hip,1), hip_y ])
    l_hip = np.array([ hip_x + side(x_hip,-1), hip_y ])
    # Knees
    r_knee = np.array([ knee_x + side(x_knee,1), knee_y ])
    l_knee = np.array([ knee_x + side(x_knee,-1), knee_y ])
    # Ankles
    r_ankle = np.array([ ankle_x + side(x_ankle,1), ankle_y ])
    l_ankle = np.array([ ankle_x + side(x_ankle,-1), ankle_y ])
    # Feet
    r_foot = np.array([ foot_x + side(x_foot,1), foot_y ])
    l_foot = np.array([ foot_x + side(x_foot,-1), foot_y ])

    # Assemble 15 markers: [head, R shldr, L shldr, R elbow, L elbow, R wrist, L wrist,
    #                      R hip, L hip, R knee, L knee, R ankle, L ankle, R foot, L foot]
    head = np.array([0.0, y_head])
    points = np.vstack([
        head,
        r_shoulder, l_shoulder,
        [elbow_xr, elbow_yr], [elbow_xl, elbow_yl],
        [wrist_xr, wrist_yr], [wrist_xl, wrist_yl],
        r_hip, l_hip,
        r_knee, l_knee,
        r_ankle, l_ankle,
        r_foot, l_foot,
    ])
    return points

# ---- Animation ---- #
fig, ax = plt.subplots(figsize=(4,7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Black BG, white dots
marker_style = dict(color='white', marker='o', linestyle='None', markersize=10)
lines, = ax.plot([], [], **marker_style)

def init():
    lines.set_data([], [])
    return lines,

def animate(frame):
    duration = 2.0  # seconds
    fps = 30
    t = frame / fps
    points = get_body_points(t, duration=duration)
    # Adjust for 'happyman' - add a slight up-down bob for a cheerful effect (frequency low)
    if t < duration:
        bob = 0.05 * np.sin(2*np.pi*(0.7)*t)
        points[:,1] += bob
    # Display
    lines.set_data(points[:,0], points[:,1])
    return lines,

ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 4.1)
ax.set_xticks([])
ax.set_yticks([])

anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=65, interval=1000/30, blit=True, repeat=True
)
plt.tight_layout()
plt.show()
