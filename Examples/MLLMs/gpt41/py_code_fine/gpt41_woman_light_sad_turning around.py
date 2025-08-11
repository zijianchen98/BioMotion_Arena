
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# =========================
#     POINT-LIGHT MODEL
# =========================

# Skeleton definition (biomechanically plausible woman, 15 points)
#    0: Head top
#    1: Right shoulder
#    2: Left shoulder
#    3: Right elbow
#    4: Left elbow
#    5: Right wrist
#    6: Left wrist
#    7: Pelvis (hips center)
#    8: Right knee
#    9: Left knee
#   10: Right ankle
#   11: Left ankle
#   12: Spine base (close to pelvis)
#   13: Chest (upper torso)
#   14: Sternum (mid-chest)

# Bones: (for reference, not drawn)
bones = [
    (0,13),    # Head top to chest
    (13,1),    # Chest to right shoulder
    (13,2),    # Chest to left shoulder
    (1,3),     # R shoulder to R elbow
    (3,5),     # R elbow to R wrist
    (2,4),     # L shoulder to L elbow
    (4,6),     # L elbow to L wrist
    (13,14),   # Chest to sternum
    (14,7),    # Sternum to pelvis
    (7,12),    # Pelvis to spine base
    (7,8),     # Pelvis to R knee
    (8,10),    # R knee to R ankle
    (7,9),     # Pelvis to L knee
    (9,11)     # L knee to L ankle
]

# Proportions: in units, [X, Y, Z]
skeleton_rest = np.array([
    [0, 8.0, 0],   # 0 head top
    [1.0, 6.7, 0], # 1 right shoulder
    [-1.0, 6.7, 0],# 2 left shoulder
    [1.4, 5.6, 0], # 3 right elbow
    [-1.4, 5.6, 0],# 4 left elbow
    [1.7, 4.3, 0], # 5 right wrist
    [-1.7, 4.3, 0],# 6 left wrist
    [0, 4.2, 0],   # 7 pelvis (hips center)
    [0.7, 2.7, 0], # 8 right knee
    [-0.7, 2.7, 0],# 9 left knee
    [0.7, 1.0, 0], #10 right ankle
    [-0.7, 1.0, 0],#11 left ankle
    [0, 4.0, 0],   #12 spine base
    [0, 6.0, 0],   #13 chest
    [0, 5.1, 0],   #14 sternum
])

# ========== SAD POSE ==========

def sad_posture(skel):
    """Apply pose modifications for a sad woman (slumped, hunched, head down, arms downward/forward)."""
    s = skel.copy()
    # Head tip lowered, a bit forward (Z negative)
    s[0,1] -= 0.5
    s[0,2] -= 0.15
    # Chest/shoulder rounded forward/slouched
    s[1,2] -= 0.25 # R shoulder Z
    s[1,1] -= 0.15
    s[2,2] -= 0.25 # L shoulder Z
    s[2,1] -= 0.15

    s[13,1] -= 0.2 # chest Y
    s[13,2] -= 0.18 # chest Z
    s[14,1] -= 0.25
    s[14,2] -= 0.10
    s[12,1] -= 0.25
    s[12,2] -= 0.10
    # Hips slightly tilted forward
    s[7,2] -= 0.06
    # Arms hang more downward and in front of body
    for i, sign in [(3, 1), (4, -1)]:
        s[i,1] -= 0.10
        s[i,2] -= 0.12
    for i, sign in [(5, 1), (6, -1)]:
        s[i,0] *= 0.85  # wrists closer in
        s[i,1] -= 0.25  # lower
        s[i,2] -= 0.14  # more frontal
    # Knees/hips/ankles aligned, only minor changes
    return s

# ========== TURN ANIMATION ==========

def turn_around(total_frames):
    """Return an array of skeletons (T x 15 x 3) simulating a woman turning slowly."""
    # She turns 360 deg, with a sad, reserved body posture.
    skel = sad_posture(skeleton_rest)
    T = total_frames
    out = []
    # Sway & slight arm motion: hands move gently in sym
    sway_amp = 0.035
    hands_forward = 0.04

    for t in range(T):
        theta = 2*np.pi * t/T   # Full 360-degree turn over T frames
        # For slightly more realism: change direction at halfway point
        frac = t/T
        if frac < 0.5:
            y_rot = theta
        else:
            y_rot = 2*np.pi - theta
        # Turning around the Y axis (vertical)
        R = rotation_matrix_y(y_rot)
        pts = skel.dot(R.T)
        # Animate head dipping slightly, arms moving in gentle sync
        pts[0,1] -= 0.09*np.sin(frac * np.pi)
        hand_sway = sway_amp * np.sin(2* np.pi * frac)
        # Move wrists gently through the turn, also infront for "sad"
        for idx, s in [(5, 1), (6, -1)]:
            pts[idx,0] += s*hand_sway
            pts[idx,2] -= hands_forward*np.abs(np.sin(np.pi*frac))
        # Gentle spine/chest lean forward
        pts[13,2] -= 0.06
        pts[14,2] -= 0.04
        pts[12,2] -= 0.02
        out.append(pts.copy())
    return np.stack(out)

def rotation_matrix_y(theta):
    """Return 3x3 rotation matrix for a rotation theta around Y axis."""
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c,0,s],
                     [0,1,0],
                     [-s,0,c]])

# ========== ANIMATION ==========

# Parameters for animation
fps = 30
n_frames = 120
anim_data = turn_around(n_frames)

# Convert to image coords (for display)
def to_display_coords(skel3d, W=3, H=8, imgW=560, imgH=350):
    """Project from 3D to 2D, then map to image coords."""
    # Simple orthographic projection (x vs y), with 2D scaling
    scale = 0.9 * min(imgW/(W*2), imgH/(H*2))
    # Center at (0, 4) in world, map to center of image
    x = skel3d[:,0]
    y = skel3d[:,1]
    px = (x - 0) * scale + imgW/2
    py = imgH - ((y - 1) * scale + imgH/2) # y up is up
    return px, py

# ========== DRAWING ==========

fig = plt.figure(figsize=(imgW/100, imgH/100), facecolor='black')
ax = plt.axes([0,0,1,1])
plt.axis('off')
imgW, imgH = 560, 350

dots, = ax.plot([], [], 'wo', markersize=8)

def init():
    ax.set_xlim(0, imgW)
    ax.set_ylim(0, imgH)
    ax.set_facecolor('black')
    dots.set_data([], [])
    return (dots,)

def animate(i):
    pts3d = anim_data[i]
    xs, ys = to_display_coords(pts3d, imgW=imgW, imgH=imgH)
    dots.set_data(xs, ys)
    return (dots,)

ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=1000/fps,
                              blit=True, init_func=init, repeat=True)

plt.show()
