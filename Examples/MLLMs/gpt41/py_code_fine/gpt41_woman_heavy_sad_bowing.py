
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint indices:
# 0: Head
# 1: Neck
# 2: Right Shoulder
# 3: Left Shoulder
# 4: Chest/Upper back
# 5: Right Elbow
# 6: Left Elbow
# 7: Right Wrist
# 8: Left Wrist
# 9: Pelvis
#10: Right Hip
#11: Left Hip
#12: Right Knee
#13: Left Knee
#14: Both Ankles (approx, close feet for "sad" pose)

# Initial upright positions (X,Y) for each of the 15 joints
# Units are arbitrary; relative positioning for a standing woman
points_start = np.array([
    [0, 11],    # 0: Head
    [0, 10],    # 1: Neck
    [ 0.7,  9.7], # 2: R Shoulder
    [ -0.7,  9.7], # 3: L Shoulder
    [0, 9.4],   # 4: Chest
    [ 1.3, 8.4], # 5: R Elbow
    [ -1.3, 8.4], # 6: L Elbow
    [1.5, 7.4], # 7: R Wrist
    [ -1.5, 7.4], # 8: L Wrist
    [0, 7.6],   # 9: Pelvis
    [0.6, 7.5], #10: R Hip
    [-0.6, 7.5],#11: L Hip
    [0.5, 5.5], #12: R Knee
    [-0.5, 5.5],#13: L Knee
    [0, 3.7],   #14: Ankles (feet together, sad pose)
])

# "Heavy weight" is expressed by arms and upper body stooping down,
# shoulders forward, wrists hanging loosely forward, knees bending slightly, and
# head sunk.
def pose_func(t):
    """
    Return the 15x2 array of point-light positions at time t (0<=t<1)
    Simulate a bowing motion (down and up over 1s/animation cycle).
    """
    # Bowing follows a sine wave motion
    # 0: upright, pi/2: deepest bow, pi: upright. (i.e., bow and recover)
    angle = np.pi * t
    bow_frac = np.sin(angle)
    
    # Parameters
    bow_angle = np.deg2rad(50) * bow_frac  # Max body bow at 50 deg forward
    head_drop = 0.9 * bow_frac
    neck_drop = 0.7 * bow_frac
    shldr_fwd = 0.27 * bow_frac
    chest_drop = 0.45 * bow_frac
    pelvis_drop = 0.2 * bow_frac
    knee_bend = 1.0 * bow_frac  # y drop of knees
    hip_shift = 0.1 * bow_frac

    # Start from upright pose
    pts = np.copy(points_start)
    
    # Pelvis (body pivot point for bow cycle)
    pelvis = np.copy(pts[9])
    pelvis[1] -= pelvis_drop

    # Rotate points above pelvis (spine, head, shoulders, arms) around (pelvis)
    def rotate_around(pt, origin, theta):
        R = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta),  np.cos(theta)]])
        return (R @ (pt - origin).T).T + origin

    joint_indices_above_pelvis = [0,1,2,3,4,5,6,7,8]
    for idx in joint_indices_above_pelvis:
        pts[idx] = rotate_around(pts[idx], pts[9], -bow_angle)
    
    # Head extra "sad" drop and neck curve
    pts[0,1] -= head_drop
    pts[1,1] -= neck_drop
    
    # Shoulders slouch forward + down a bit, arms/forearms hang heavily
    pts[2,0] += shldr_fwd*1.35
    pts[3,0] -= shldr_fwd*1.35
    pts[4,1] -= chest_drop
    pts[2,1] -= chest_drop*0.6
    pts[3,1] -= chest_drop*0.6

    # Arms "hang" downward (bend at shoulder & elbow, wrists sag down and fwd) + symmetric
    arm_bow_angle = np.deg2rad(60) * bow_frac
    elbow_bend = np.deg2rad(50) * bow_frac
    wrist_drop = 0.3 * bow_frac
    wrist_fwd = 0.4 * bow_frac

    # Right side
    pts[5] = rotate_around(pts[5], pts[2], arm_bow_angle)
    pts[7] = rotate_around(pts[7], pts[5], elbow_bend)
    pts[7,1] -= wrist_drop
    pts[7,0] += wrist_fwd

    # Left side
    pts[6] = rotate_around(pts[6], pts[3], arm_bow_angle)
    pts[8] = rotate_around(pts[8], pts[6], elbow_bend)
    pts[8,1] -= wrist_drop
    pts[8,0] -= wrist_fwd
    
    # Legs: knees bend, lower legs and ankles come forward
    pts[12,1] -= knee_bend   # Right knee
    pts[13,1] -= knee_bend   # Left knee
    pts[12,0] += hip_shift
    pts[13,0] -= hip_shift

    # Move ankles forward and down a tiny bit (simulates struggling to support weight)
    pts[14,1] -= 0.05 * bow_frac
    # Ankles also close to together, feet a bit forward (sad pose)
    pts[14,0] = 0

    # Small random vertical "tremble" for emotional effect
    pts[:,1] -= 0.04 * bow_frac * np.sin(6*np.pi*t)

    return pts

# Plot and animate
fig, ax = plt.subplots(figsize=(4,7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Animation settings
n_frames = 48
duration = 2.0     # seconds per cycle (down then up)
repeat = True

# Get initial points
pts = pose_func(0)
dots, = ax.plot(pts[:,0], pts[:,1], 'o', color='white', markersize=11)

ax.set_xlim(-3,3)
ax.set_ylim(2.9,12.5)

# For smoothness, interpolate between two full bow cycles with time
def animate(frame):
    t = (frame % n_frames) / n_frames
    pts = pose_func(t)
    dots.set_data(pts[:,0], pts[:,1])
    return (dots,)

ani = animation.FuncAnimation(
    fig, animate, frames=n_frames, interval=duration*1000/n_frames, blit=True, repeat=repeat
)

plt.show()
