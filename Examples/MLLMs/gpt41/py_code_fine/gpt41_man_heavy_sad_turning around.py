
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Marker order: (same as example image)
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Chest (Sternum)
# 6: Right Wrist
# 7: Left Wrist
# 8: Right Hip
# 9: Left Hip
#10: Right Knee
#11: Left Knee
#12: Right Ankle
#13: Left Ankle
#14: "Heavy weight" held by both hands (between both wrists)

# Define a canonical 3D skeleton (in standing position, facing +Z)
# All units are in arbitrary lengths (normalized to about 2 "meters" tall)
skeleton = np.array([
    [0.0, 1.2, 0.0],   # Head
    [0.18, 1.0, 0.0],  # R Shoulder
    [-0.18, 1.0, 0.0], # L Shoulder
    [0.33, 0.77, 0.0], # R Elbow
    [-0.33, 0.77, 0.0],# L Elbow
    [0.0, 0.9, 0.0],   # Chest/sternum
    [0.45, 0.55, 0.0], # R Wrist
    [-0.45, 0.55, 0.0],# L Wrist
    [0.15, 0.5, 0.0],  # R Hip
    [-0.15, 0.5, 0.0], # L Hip
    [0.15, 0.15, 0.0], # R Knee
    [-0.15, 0.15, 0.0],# L Knee
    [0.15, -0.38, 0.0],# R Ankle
    [-0.15, -0.38, 0.0],# L Ankle
    [0.0, 0.44, 0.0]   # Heavy weight, between wrists (held in front)
])

def get_weight_position(rwrist, lwrist):
    """Calculate the position of the weight as a point between two wrists, held low and slightly forward."""
    midpoint = 0.5 * (rwrist + lwrist)
    # Move slightly further forward in Z for plausible "heavy weight"
    forward = 0.11
    down = 0.11
    weight = midpoint + np.array([0.0, -down, forward])
    return weight

def rotateY(points, theta):
    """Rotate Nx3 points around Y axis by theta radians."""
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])
    return points @ R.T

def sad_posture(points, sadness=1.0, weight_factor=1.0):
    """Modify skeleton for 'sad' pose: hunched shoulders, bent head, arms down, knees flexed."""
    sad_points = points.copy()
    # Head droop
    sad_points[0,1] -= 0.09 * sadness
    sad_points[0,2] += 0.09 * sadness
    # Shoulders slouch forward
    sad_points[1,2] += 0.12 * sadness
    sad_points[2,2] += 0.12 * sadness
    sad_points[1,1] -= 0.07 * sadness
    sad_points[2,1] -= 0.07 * sadness
    # Elbows and wrists closer to body (arms hanging due to fatigue)
    v_right = sad_points[6] - sad_points[1]
    v_left  = sad_points[7] - sad_points[2]
    sad_points[3] = sad_points[1] + 0.5*(v_right)
    sad_points[4] = sad_points[2] + 0.5*(v_left)
    sad_points[6,1] -= 0.18 * weight_factor
    sad_points[7,1] -= 0.18 * weight_factor
    sad_points[6,2] += 0.08 * weight_factor
    sad_points[7,2] += 0.08 * weight_factor
    # Chest slumps forward
    sad_points[5,2] += 0.09 * sadness
    sad_points[5,1] -= 0.04 * sadness
    # Hips droop a little
    sad_points[8,1] -= 0.04 * sadness
    sad_points[9,1] -= 0.04 * sadness
    # Knees bent slightly (tired)
    sad_points[10,1] -= 0.13 * sadness
    sad_points[11,1] -= 0.13 * sadness
    sad_points[10,2] += 0.07 * sadness
    sad_points[11,2] += 0.07 * sadness
    # Ankles accordingly
    sad_points[12,1] -= 0.19 * sadness
    sad_points[13,1] -= 0.19 * sadness
    sad_points[12,2] += 0.09 * sadness
    sad_points[13,2] += 0.09 * sadness
    return sad_points

def turning_motion(t, T=2.5):
    """Return the pose for time t, total cycle T (in seconds).
    - Turning around smoothly in-place.
    - Adds natural weight shift, slight bobbing, biomechanical plausibility.
    """
    frac = (t % T) / T
    
    # Body rotates smoothly from 0 to pi (180 deg), then continues back.
    if frac < 0.5:
        theta = np.pi * 2 * frac    # turn left
    else:
        theta = np.pi * 2 * (1 - frac) # and back

    # Simulate a wobble during turning, and a weight shift
    wobble = 0.09 * np.sin(2 * np.pi * frac)
    bobbing = 0.06 * np.sin(4 * np.pi * frac)
    weight_swing = 0.21 * np.sin(np.pi * frac)
    arm_sag = 1.0 + 0.4 * np.abs(np.sin(np.pi * frac))

    # Base pose: sad and heavy
    base_pose = sad_posture(skeleton, sadness=1.0, weight_factor=arm_sag)

    # Simulate body turning (all rotation about Y, centered at midsagittal y=0.65)
    com_shift = np.array([0.0, 0.65, 0.0])
    pose = base_pose - com_shift
    pose = rotateY(pose, theta)
    pose = pose + com_shift

    # Add subtle wobble and bob
    pose[:,1] += bobbing
    pose[:,0] += wobble

    # Arm/weight: swing forward/back during turn, arms are tired (lowered more at turn mid-point)
    right_wrist_base = base_pose[6]
    left_wrist_base  = base_pose[7]
    pose[6,1] -= weight_swing * 0.21
    pose[7,1] -= weight_swing * 0.21
    pose[6,2] += weight_swing * 0.19
    pose[7,2] += weight_swing * 0.19

    # Update weight marker between wrists (in front of body)
    pose[14] = get_weight_position(pose[6], pose[7])

    return pose

# Visualization setup
fig, ax = plt.subplots(figsize=(3.5, 5.6), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Fixed display parameters
N = 15
pt_size = 52
xlims = (-0.7, 0.7)
ylims = (-0.65, 1.30)

# Create empty scatter plot
scat = ax.scatter([], [], s=pt_size, c='w', edgecolors='none', zorder=2)

ax.set_xlim(*xlims)
ax.set_ylim(*ylims)
ax.axis('off')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

def init():
    scat.set_offsets(np.zeros((N, 2)))
    scat.set_sizes([pt_size]*N)
    scat.set_color('w')
    return scat,

def update(frame):
    fps = 30
    t = frame / fps
    pose3d = turning_motion(t, T=2.7)
    # Project 3D to 2D (simple orthographic, X vs Y - as example image uses)
    xy = pose3d[:,[0,1]]
    scat.set_offsets(xy)
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=180, interval=1000/30, blit=True, init_func=init, repeat=True
)

plt.show()
