
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 anatomical keypoints: [Head, Neck, RShoulder, LShoulder, Spine, RElbow, LElbow, RWrist, LWrist,
# RHip, LHip, RKnee, LKnee, RAnkle, LAnkle]
#
# All coordinates in 3D canonical pose (woman standing upright)
# Units: arbitrary but consistent for visualization

def get_pose():
    # Y is up, X left-right, Z front-back
    pose = np.array([
        [0, 13, 0],     # Head
        [0, 12, 0],     # Neck
        [1.8, 12, 0.1],  # RShoulder
        [-1.8, 12, -0.1],# LShoulder
        [0, 10.5, 0],   # Spine (torso center)
        [2.5, 10.5, 0.2],# RElbow
        [-2.5, 10.5, -0.2],# LElbow
        [3.2, 8.0, 0.4], # RWrist
        [-3.2, 8.0, -0.4],# LWrist
        [1.0, 9, 0],    # RHip
        [-1.0, 9, 0],   # LHip
        [1.0, 5.5, 0.1],# RKnee
        [-1.0, 5.5, 0.1],# LKnee
        [1.0, 2, 0.25], # RAnkle
        [-1.0, 2, 0.25] # LAnkle
    ])
    return pose

def apply_biological_variation(base, frame, nframes):
    # Adds happy/light-weight posture and some coherent joint movement variation for "turning"
    t = frame / nframes * 2 * np.pi
    # Vertical bob (light-weight, happy)
    bob_y = 0.25 * np.sin(2 * t)
    base = np.copy(base)
    base[:,1] += bob_y

    # Sway at head and shoulders for "happiness" gesture
    base[0,0] += 0.20 * np.sin(2 * t)
    base[1,0] += 0.18 * np.sin(2 * t)
    base[2,0] += 0.15 * np.sin(2 * t)
    base[3,0] += 0.15 * np.sin(2 * t)
    # Arm swing
    base[5,0] += 0.25 * np.sin(2*t + np.pi/2)
    base[6,0] += 0.25 * np.sin(2*t - np.pi/2)
    base[7,0] += 0.40 * np.sin(2*t + np.pi)
    base[8,0] += 0.40 * np.sin(2*t)

    # Step/dip for knees/ankles
    base[11,1] += 0.20 * np.abs(np.sin(t))      # RKnee
    base[12,1] += 0.20 * np.abs(np.sin(t + np.pi))
    base[13,1] += 0.25 * np.abs(np.sin(t))
    base[14,1] += 0.25 * np.abs(np.sin(t + np.pi))
    return base

def project_points(points3d, azim, elev):
    # azim, elev in degrees
    # Simple orthographic projection
    # First rotate around Y (azimuth, turning around vertical axis), then around X (elevation)
    a = np.deg2rad(azim)
    e = np.deg2rad(elev)
    # Rotation matrix around Y
    Ry = np.array([
        [np.cos(a), 0, np.sin(a)],
        [0,         1,       0],
        [-np.sin(a),0, np.cos(a)]
    ])
    # Rotation matrix around X
    Rx = np.array([
        [1,    0,    0],
        [0, np.cos(e), -np.sin(e)],
        [0, np.sin(e),  np.cos(e)]
    ])
    R = Rx @ Ry
    points3d_rot = points3d @ R.T
    # Orthographic projection: take x, y only (ignore z)
    projected = points3d_rot[:,[0,1]]
    return projected

# Animation parameters
nframes = 120
interval = 33  # ms/frame ~30fps
figsize = (7, 14)

# Main animation function
def animate():
    pose3d = get_pose()
    # We'll rotate subject slowly 360deg around the vertical "Y" axis
    azims = np.linspace(0, 360, nframes)
    elev = 14 # slight camera elevation for aesthetics

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor('black')
    dots, = ax.plot([], [], 'wo', ms=10)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(0.5, 14)
    plt.tight_layout()

    def init():
        dots.set_data([], [])
        return (dots,)

    def update(frame):
        # Natural body motion on top of the rigid-body turn
        pose_mod = apply_biological_variation(pose3d, frame, nframes)
        pts2d = project_points(pose_mod, azims[frame], elev)
        dots.set_data(pts2d[:,0], pts2d[:,1])
        return (dots,)

    ani = animation.FuncAnimation(
        fig, update, frames=nframes,
        blit=True, init_func=init, interval=interval
    )
    plt.show()

if __name__ == "__main__":
    animate()
