
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Skeleton structure: [name, parent_index, x, y, z, length]
JOINTS = [
    # Torso and head
    {"name": "head",   "parent": 1,  "offset": [0, 0.51, 0]},   # 0
    {"name": "neck",   "parent": 2,  "offset": [0, 0.09, 0]},   # 1
    {"name": "spine",  "parent": 3,  "offset": [0, 0.14, 0]},   # 2
    {"name": "hip",    "parent":-1,  "offset": [0, 0.16, 0]},   # 3

    # Right arm
    {"name": "r_shoulder", "parent": 1, "offset": [0.13, 0.07, 0]},  # 4
    {"name": "r_elbow",    "parent": 4, "offset": [0.17, 0, 0]},     # 5
    {"name": "r_wrist",    "parent": 5, "offset": [0.17, 0, 0]},     # 6

    # Left arm
    {"name": "l_shoulder", "parent": 1, "offset": [-0.13, 0.07, 0]}, # 7
    {"name": "l_elbow",    "parent": 7, "offset": [-0.17, 0, 0]},    # 8
    {"name": "l_wrist",    "parent": 8, "offset": [-0.17, 0, 0]},    # 9

    # Right leg
    {"name": "r_hip",   "parent": 3, "offset": [0.07, -0.02, 0]}, # 10
    {"name": "r_knee",  "parent":10, "offset": [0.04, -0.21, 0]}, # 11
    {"name": "r_ankle", "parent":11, "offset": [0.02, -0.21, 0]}, # 12

    # Left leg
    {"name": "l_hip",   "parent": 3, "offset": [-0.07, -0.02, 0]}, # 13
    {"name": "l_knee",  "parent":13, "offset": [-0.04, -0.21, 0]}, # 14
    {"name": "l_ankle", "parent":14, "offset": [-0.02, -0.21, 0]}, # 15
]
# We want 15 points: head, neck, spine, hip, r_sh, r_elb, r_wrist, l_sh, l_elb, l_wrist, r_hip, r_knee, r_ankle, l_knee, l_ankle
JOINT_IX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]

def build_skeleton():
    skeleton = []
    for joint in JOINTS:
        skeleton.append(np.array(joint["offset"]))
    return np.array(skeleton)

def get_pos(skeleton, joint_ix, rotations):
    # Forward kinematics
    pos = [np.zeros(3)]
    parents = [JOINTS[i]["parent"] for i in range(len(JOINTS))]
    # Root is in the center
    for i in range(1, len(JOINTS)):
        p = parents[i]
        parent_pos = pos[p] if p >= 0 else np.zeros(3)
        offset = skeleton[i]
        if rotations[i] is not None:
            offset = rotations[i] @ offset
        pos.append(parent_pos + offset)
    return [pos[i] for i in JOINT_IX]

def rotation_matrix(axis, theta):
    # Rodrigues' rotation formula
    axis = np.asarray(axis)
    axis = axis/np.linalg.norm(axis)
    a = np.cos(theta/2)
    b, c, d = -axis*np.sin(theta/2)
    return np.array([
        [a*a + b*b - c*c - d*d, 2*(b*c-a*d),     2*(b*d+a*c)],
        [2*(b*c+a*d),       a*a + c*c - b*b - d*d, 2*(c*d-a*b)],
        [2*(b*d-a*c),       2*(c*d+a*b),      a*a + d*d - b*b - c*c]
    ])

def animate_biomotion():
    np.random.seed(1234)
    skeleton = build_skeleton()
    nframes = 120
    fps = 30
    T = 2*np.pi  # One full turn
    RADIUS = 0.2

    # Make approximate cyclic arm and leg swings for bounce
    time = np.linspace(0, 2*np.pi, nframes)
    arm_swing = 0.8*np.sin(time*1.5)
    leg_swing = 0.6*np.sin(time*1.5)
    bob = 0.03*np.sin(time*3)

    fig, ax = plt.subplots(figsize=(4,8))
    ax.set_facecolor("black")
    scat = ax.scatter([0]*15, [0]*15, s=55, color='white')
    ax.axis('off')
    ax.set_xlim(-0.7, 0.7)
    ax.set_ylim(-0.35, 1.25)

    def get_frame(frame):
        theta = (frame / nframes) * T  # Turning angle
        # All rotations are identity first
        rotations = [None for _ in range(len(JOINTS))]
        # Body turns: yaw (y-axis) all parts
        yaw = rotation_matrix([0,1,0], theta)
        # Apply overall body yaw rotation
        for i, _ in enumerate(JOINTS):
            rotations[i] = yaw.copy()
        # Add some up-down bob to root
        root_delta = np.array([0., bob[frame], 0])
        # Animate arms and legs (with cyclical swing)
        # Arms
        r_sh_ix, r_elb_ix, r_wrist_ix = 4, 5, 6
        l_sh_ix, l_elb_ix, l_wrist_ix = 7, 8, 9
        # Animate arms with forward/backward swings (about z-axis local to the spine)
        r_arm_angle =  0.5*arm_swing[frame]
        l_arm_angle = -0.5*arm_swing[frame]
        rotations[r_sh_ix] = yaw @ rotation_matrix([0,0,1], r_arm_angle)
        rotations[r_elb_ix] = yaw @ rotation_matrix([0,0,1], r_arm_angle)
        rotations[r_wrist_ix] = yaw @ rotation_matrix([0,0,1], r_arm_angle)
        rotations[l_sh_ix] = yaw @ rotation_matrix([0,0,1], l_arm_angle)
        rotations[l_elb_ix] = yaw @ rotation_matrix([0,0,1], l_arm_angle)
        rotations[l_wrist_ix] = yaw @ rotation_matrix([0,0,1], l_arm_angle)
        # Legs: knee swing
        r_hip_ix, r_knee_ix, r_ankle_ix = 10, 11, 12
        l_hip_ix, l_knee_ix, l_ankle_ix = 13, 14, 15
        r_leg_angle = -0.5*leg_swing[frame]
        l_leg_angle =  0.5*leg_swing[frame]
        rotations[r_hip_ix] = yaw @ rotation_matrix([0,0,1], r_leg_angle)
        rotations[r_knee_ix] = yaw @ rotation_matrix([0,0,1], r_leg_angle)
        rotations[r_ankle_ix] = yaw @ rotation_matrix([0,0,1], r_leg_angle)
        rotations[l_hip_ix] = yaw @ rotation_matrix([0,0,1], l_leg_angle)
        rotations[l_knee_ix] = yaw @ rotation_matrix([0,0,1], l_leg_angle)
        rotations[l_ankle_ix] = yaw @ rotation_matrix([0,0,1], l_leg_angle)
        # Spine and head slight nod
        rotations[1] = yaw @ rotation_matrix([1,0,0], 0.03*np.sin(time[frame]*2+1))
        rotations[0] = yaw @ rotation_matrix([1,0,0], 0.1*np.sin(time[frame]*1.1))
        # Forward kinematics
        pos = [np.zeros(3)]
        parents = [JOINTS[i]["parent"] for i in range(len(JOINTS))]
        for i in range(1, len(JOINTS)):
            p = parents[i]
            parent_pos = pos[p] if p >= 0 else np.zeros(3)
            offset = skeleton[i]
            if rotations[i] is not None:
                offset = rotations[i] @ offset
            pos.append(parent_pos + offset)
        # Just the named points, and add root bob
        pts = [pos[i] for i in JOINT_IX]
        pts = np.array(pts) + root_delta
        # 3D to 2D: orthographic, but simulate a small depth cue with x->x*(1+z*0.2)
        z_proj = pts[:,2]
        x_proj = pts[:,0]*(1+z_proj * 0.2)
        y_proj = pts[:,1]
        return x_proj, y_proj

    def update(frame):
        x, y = get_frame(frame)
        scat.set_offsets(np.c_[x, y])
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=len(np.arange(nframes)), interval=1000/fps, blit=True)
    plt.show()

if __name__ == "__main__":
    animate_biomotion()
