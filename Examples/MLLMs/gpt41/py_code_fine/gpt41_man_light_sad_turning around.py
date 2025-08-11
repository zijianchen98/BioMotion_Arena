
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint names (for possible future reference)
JOINTS = [
    'head',         # 0
    'neck',         # 1
    'r_shoulder',   # 2
    'l_shoulder',   # 3
    'r_elbow',      # 4
    'l_elbow',      # 5
    'r_wrist',      # 6
    'l_wrist',      # 7
    'chest',        # 8
    'mid_hip',      # 9
    'r_hip',        # 10
    'l_hip',        # 11
    'r_knee',       # 12
    'l_knee',       # 13
    'r_ankle',      # 14
    'l_ankle',      # 15   (for this 15-point model, we'll not use l_ankle as point #15, so only up to 14)
]

# 15-point-light model: indices correspond to these joint positions
# [head, neck, r_shoulder, l_shoulder, r_elbow, l_elbow,
#  r_wrist, l_wrist, chest, mid_hip, r_hip, l_hip, r_knee, l_knee, r_ankle, l_ankle]
# We'll use only up to l_ankle for a total of 15 points

# 3D skeleton template in "T-pose" (unit lengths, origin at mid-hip)
# Columns: [x, y, z]; y: vertical (up)
TEMPLATE = np.array([
    [ 0.0,  1.10,  0.0],   # head
    [ 0.0,  1.00,  0.0],   # neck
    [ 0.15, 0.97,  0.0],   # r_shoulder
    [-0.15, 0.97,  0.0],   # l_shoulder
    [ 0.33, 0.67,  0.0],   # r_elbow
    [-0.33, 0.67,  0.0],   # l_elbow
    [ 0.47, 0.37,  0.0],   # r_wrist
    [-0.47, 0.37,  0.0],   # l_wrist
    [ 0.0,  0.92,  0.0],   # chest
    [ 0.0,  0.70,  0.0],   # mid_hip
    [ 0.08, 0.70,  0.0],   # r_hip
    [-0.08, 0.70,  0.0],   # l_hip
    [ 0.09, 0.32,  0.0],   # r_knee
    [-0.09, 0.32,  0.0],   # l_knee
    [ 0.10, 0.00,  0.0],   # r_ankle
    [-0.10, 0.00,  0.0],   # l_ankle
])[:15]

def sadman_adjust(skel, frame, nframes):
    """Adjusts head and shoulders to create a sad posture: head down, shoulders droop."""
    # Head droop
    head, neck = 0, 1
    theta = np.deg2rad(20) * np.sin(2 * np.pi * frame / nframes)  # Slight animation
    # Move head slightly forwards and down wrt neck
    rel = skel[head] - skel[neck]
    rotmat = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    skel[head] = skel[neck] + rel @ rotmat.T - np.array([0, 0.025, 0])
    # Shoulder droop
    r_sh, l_sh = 2, 3
    sh_theta = np.deg2rad(18)
    skel[r_sh][1] -= 0.045 + 0.01*np.sin(2 * np.pi * frame/nframes + 1)
    skel[l_sh][1] -= 0.045 + 0.01*np.sin(2 * np.pi * frame/nframes + 1.8)
    # Arms droop further
    for idx, sh_idx, el_idx, wr_idx, side in [
        (4, 2, 4, 6,  1),  # Right
        (5, 3, 5, 7, -1),  # Left
    ]:
        skel[el_idx][1] -= 0.035
        skel[wr_idx][1] -= 0.07
        skel[el_idx][0] += side*0.02
        skel[wr_idx][0] += side*0.01
    return skel

def rotate_y(points, theta):
    """Rotate points about the y-axis by theta radians."""
    mat = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)],
    ])
    return points @ mat.T

def animate_turning_around(nframes=120):
    # Animation parameters
    skel_default = TEMPLATE.copy()
    height = 1.20  # total body height (rough)
    width = 0.7    # visual width
    # Prepare figure
    fig, ax = plt.subplots(figsize=(3, 6))
    ax.set_facecolor('black')
    ax.set_xlim(-0.55, 0.55)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect('equal')
    plt.axis('off')

    # Initial points
    dots, = plt.plot([], [],
                     'o', color='white', markersize=8)

    def get_pose3d(frame):
        # Full turn: go from angle -90 to +90 deg, then back (yaw)
        t = frame / nframes
        turn_phase = np.pi * (2*t)  # -pi/2 to +pi/2 in 1 turn, then back
        if t < 0.5:
            yaw = -np.pi/2 + np.pi * (2*t)   # -90 to +90 deg
        else:
            yaw = +np.pi/2 - np.pi * (2*(t-0.5))  # +90 back to -90
        # Animate stride: subtle stepping so motion is biomechanical
        # We'll make legs/arms swing gently as the person "turns"
        stride_phase = 2*np.pi*(t)
        stride_mag = 0.08 * np.sin(stride_phase)
        skel = skel_default.copy()
        # Swing arms and legs
        for r in [(12,6,2,+1), (13,7,3,-1)]: # (knee,wrist,shoulder,side)
            knee, wrist, shoulder, lr = r
            # Knee swing back/forth
            skel[knee][2] += lr * 0.015 * stride_mag
            # Wrist swing to counterbalance
            skel[wrist][2] -= lr * 0.030 * stride_mag
            skel[wrist][1] += 0.015 * abs(stride_mag)
        # Move ankles with stride
        for a, sign in [(14,+1),(13,-1)]:
            skel[a][2] += sign * 0.012*stride_mag
        # Add sadman pose
        skel = sadman_adjust(skel, frame, nframes)
        # Apply global rotation (yaw/turn)
        skel = rotate_y(skel, yaw)
        return skel

    def get_projected2d(skel3d):
        # Perspective projection for slight depth effect
        cam_dist = 2.0
        X, Y, Z = skel3d[:,0], skel3d[:,1], skel3d[:,2]
        x_proj = X*cam_dist/(cam_dist - Z)
        y_proj = Y*cam_dist/(cam_dist - Z)
        return np.stack([x_proj, y_proj], axis=1)

    def init():
        dots.set_data([], [])
        return dots,

    def animate(frame):
        skel3d = get_pose3d(frame)
        pts2d = get_projected2d(skel3d)
        dots.set_data(pts2d[:,0], pts2d[:,1])
        return dots,

    ani = animation.FuncAnimation(
        fig, animate, frames=nframes, interval=1000/40, blit=True, init_func=init
    )
    plt.show()

if __name__ == "__main__":
    animate_turning_around(nframes=160)
