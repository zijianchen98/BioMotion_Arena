import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of frames and frame rate
FRAMES = 60
FPS = 30

# Time array for one complete roll (2 seconds)
t_vals = np.linspace(0, 2, FRAMES)  # 2 seconds total

# Fifteen points (head, neck, shoulders, elbows, wrists, hips, knees, ankles, plus torso midpoint)
# We'll generate positions in 2D for each point across time, storing in a (FRAMES, 15, 2) array.
points_data = np.zeros((FRAMES, 15, 2))

# Parameters to control "sad posture" and "heavy weight" look
# We'll keep the arms slightly drooped and the trunk hunched forward.
# For a forward roll, the entire figure will rotate around a rolling contact.
roll_radius = 0.6        # Approximate radius for the rolling body
body_center_x_start = 0  # Starting horizontal position
body_center_y = 0.0      # Vertical offset

# Angles and lengths for a simplified skeleton
# Trunk length, arm segment lengths, leg segment lengths, etc.
trunk_len = 0.4
upper_arm_len = 0.25
lower_arm_len = 0.25
upper_leg_len = 0.3
lower_leg_len = 0.3
head_offset = 0.15

# Relative angles in a "hunched" posture (in radians)
# We'll define them as if the trunk is circularly rolling, arms droop, legs tuck.
trunk_angle_rel = 0.6       # angle of trunk relative to body "center"
upper_arm_angle_rel = 1.6   # arms drooped (relative to trunk)
lower_arm_angle_rel = 1.4
upper_leg_angle_rel = 2.0
lower_leg_angle_rel = 1.3

for i, t in enumerate(t_vals):
    # Fraction of the roll cycle
    frac = t / 2.0  # 2 seconds total for one roll

    # Rolling angle (one full rotation in 2 seconds):
    theta = 2.0 * np.pi * frac

    # Center of the body (pelvis) rolling along the x-axis
    # We'll treat the roll as if pelvis traces out a circle of radius = roll_radius
    # around a pivot at y=0, traveling to the right.
    # The midpoint (pelvis) of the body is rotating around contact point at ground.
    # Center_x = start + roll_radius * theta (approx linear movement)
    # We'll also ensure the center y moves up/down to simulate rolling.
    center_x = body_center_x_start + roll_radius * theta
    center_y = body_center_y + roll_radius * (1 - np.cos(theta))

    # The skeleton is rotated around its center by theta as well
    # to simulate a full body roll. We'll define a rotation matrix:
    R = np.array([
        [ np.cos(theta), -np.sin(theta)],
        [ np.sin(theta),  np.cos(theta)]
    ])

    # Define local rest positions of the 15 markers in a crouched/hunched posture
    # Pelvis (body center) is at (0,0) in local coordinates
    # We'll define offsets for trunk, head, shoulders, elbows, wrists, hips, knees, ankles.
    # The figure is oriented with trunk pointing up in local space, then we rotate by trunk_angle_rel, etc.

    # Pelvis
    pelvis_local = np.array([0, 0])

    # Torso midpoint (roughly halfway trunk)
    torso_mid_local = np.array([0, trunk_len/2])

    # Shoulders (left, right) at top of trunk. We'll shift them horizontally a bit.
    shoulder_width = 0.2
    right_shoulder_local = np.array([ shoulder_width/2,  trunk_len])
    left_shoulder_local  = np.array([-shoulder_width/2,  trunk_len])

    # Neck (near top of trunk, slightly above shoulders)
    neck_local = np.array([0, trunk_len + 0.05])

    # Head top
    head_local = np.array([0, trunk_len + 0.05 + head_offset])

    # Hips (just a bit below pelvis in local coords)
    # We'll consider pelvis as midpoint between hips for simplicity
    hip_offset = 0.1
    right_hip_local = np.array([ hip_offset, 0])
    left_hip_local  = np.array([-hip_offset, 0])

    # Elbows (arm angles relative to trunk)
    # We'll place them in local space by pivoting from each shoulder
    def arm_joint(shoulder, upper_angle, length):
        # The arm angle is trunk_angle_rel + offset
        angle = trunk_angle_rel + upper_angle
        offset = np.array([
            length * np.sin(angle),
            length * np.cos(angle)
        ])
        return shoulder + offset

    right_elbow_local = arm_joint(right_shoulder_local,  upper_arm_angle_rel,  upper_arm_len)
    left_elbow_local  = arm_joint(left_shoulder_local,   upper_arm_angle_rel,  upper_arm_len)

    # Wrists (from elbows, additional angle)
    def forearm_joint(elbow, shoulder, lower_angle, length):
        # We'll measure angle relative from shoulder->elbow line plus an offset
        elbow_vec = elbow - shoulder
        base_angle = np.arctan2(elbow_vec[1], elbow_vec[0])
        # Add relative angle for forearm
        angle = base_angle + lower_angle
        offset = np.array([
            length * np.cos(angle),
            length * np.sin(angle)
        ])
        return elbow + offset

    right_wrist_local = forearm_joint(right_elbow_local, right_shoulder_local,
                                      lower_arm_angle_rel, lower_arm_len)
    left_wrist_local  = forearm_joint(left_elbow_local,  left_shoulder_local,
                                      lower_arm_angle_rel, lower_arm_len)

    # Knees (leg angles relative to trunk)
    def leg_joint(hip, upper_angle, length):
        angle = -trunk_angle_rel - upper_angle  # negative because legs go downward
        offset = np.array([
            length * np.sin(angle),
            length * np.cos(angle)
        ])
        return hip + offset

    right_knee_local = leg_joint(right_hip_local, upper_leg_angle_rel, upper_leg_len)
    left_knee_local  = leg_joint(left_hip_local,  upper_leg_angle_rel, upper_leg_len)

    # Ankles (from knees)
    def lower_leg_joint(knee, hip, lower_angle, length):
        knee_vec = knee - hip
        base_angle = np.arctan2(knee_vec[1], knee_vec[0])
        angle = base_angle - lower_angle  # subtract to curl back
        offset = np.array([
            length * np.cos(angle),
            length * np.sin(angle)
        ])
        return knee + offset

    right_ankle_local = lower_leg_joint(right_knee_local, right_hip_local,
                                        lower_leg_angle_rel, lower_leg_len)
    left_ankle_local  = lower_leg_joint(left_knee_local,  left_hip_local,
                                        lower_leg_angle_rel, lower_leg_len)

    # Gather these local coordinates into an array
    local_coords = np.array([
        head_local,
        neck_local,
        right_shoulder_local,
        right_elbow_local,
        right_wrist_local,
        left_shoulder_local,
        left_elbow_local,
        left_wrist_local,
        right_hip_local,
        right_knee_local,
        right_ankle_local,
        left_hip_local,
        left_knee_local,
        left_ankle_local,
        torso_mid_local
    ])

    # Rotate entire local skeleton by theta to simulate the roll
    # then shift by the global (center_x, center_y).
    rotated = (R @ local_coords.T).T
    global_coords = rotated + np.array([center_x, center_y])

    # Store for this frame
    points_data[i] = global_coords

# Set up the plotting environment
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_facecolor('black')
scat = ax.scatter([], [], c='white', s=30)
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 2)
plt.axis('off')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    scat.set_offsets(points_data[frame])
    return scat,

ani = FuncAnimation(fig, update, frames=FRAMES, init_func=init, interval=1000/FPS, blit=True)
plt.show()