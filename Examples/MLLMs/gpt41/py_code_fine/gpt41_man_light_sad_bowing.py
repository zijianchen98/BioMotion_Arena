
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Skeleton Model with 15 points ---
# Point order: [Head, RShoulder, LShoulder, Chest, Back, RElbow, LElbow, RHand, LHand, RHip, LHip, RKnee, LKnee, RFoot, LFoot]
# Center on (0, 0), upright
SKELETON_DEF = {
    'Head':      [0, 1.0],
    'RShoulder': [-0.18, 0.82],
    'LShoulder': [ 0.18, 0.82],
    'Chest':     [ 0.0, 0.75],
    'Back':      [ 0.0, 0.68],
    'RElbow':    [-0.33, 0.65],
    'LElbow':    [ 0.33, 0.65],
    'RHand':     [-0.43, 0.5 ],
    'LHand':     [ 0.43, 0.5 ],
    'RHip':      [-0.13, 0.38],
    'LHip':      [ 0.13, 0.38],
    'RKnee':     [-0.13, 0.18],
    'LKnee':     [ 0.13, 0.18],
    'RFoot':     [-0.17, 0.0 ],
    'LFoot':     [ 0.17, 0.0],
}
JOINT_ORDER = list(SKELETON_DEF.keys())
SKELETON_BASE = np.array([SKELETON_DEF[joint] for joint in JOINT_ORDER])

def bowing_pose(t):
    """
    Returns the 15x2 coordinates at phase t in [0,1], where t=0 is upright and t=0.5 is max bow.
    Smooths bowing-in, bow-hold, bow-out as a function of t (period 1.0).
    """
    # Bow cycle: bow-in (0-0.2), hold (0.2-0.35), bow-out (0.35-0.6), upright (0.6-1.0)
    t = t % 1.0

    # Bow amount (angle in radians). Bow is around the hips, forward flex at spine.
    if t < 0.2:
        bow = np.sin(t/0.2 * (np.pi/2)) * 55  # 0 -> 55 deg
    elif t < 0.35:
        bow = 55
    elif t < 0.6:
        bow = np.sin((0.6-t)/0.25 * (np.pi/2)) * 55
    else:
        bow = 0

    bow = np.deg2rad(bow)  # Forward flexion (positive: down)

    # Head/torso bow -- pivot at hip y = 0.38
    coords = SKELETON_BASE.copy()
    offset = np.array([0, SKELETON_DEF['RHip'][1]])
    bow_matrix = np.array([[np.cos(bow), 0, np.sin(bow)],
                           [0, 1, 0],
                           [-np.sin(bow), 0, np.cos(bow)]])
    # We work in 2D: only rotate in xz plane.
    # We fake 3D by compressing with some "sadness" (shoulders droop in bow)
    z = np.zeros(coords.shape[0])
    upperbody_mask = np.array([
        joint in ['Head','RShoulder','LShoulder','Chest','Back','RElbow','LElbow','RHand','LHand']
        for joint in JOINT_ORDER
    ])
    coords3d = np.zeros((coords.shape[0],3))
    coords3d[:,0] = coords[:,0]
    coords3d[:,1] = coords[:,1]-offset[1]
    coords3d[:,2] = z

    coords3d[upperbody_mask] = (
        (coords3d[upperbody_mask]) @ bow_matrix.T
    )
    coords3d[:,1] += offset[1]

    # -- Sadness cues: slumped shoulders, drooping head, arms hang more forward --
    # Shoulders forward (z-axis) in bow
    sadness_drop = min(t/0.2, 1) if t < 0.2 else (1 if t < 0.35 else max((0.6-t)/0.25,0))
    sadness_drop *= 0.08
    for idx in [JOINT_ORDER.index('RShoulder'),JOINT_ORDER.index('LShoulder')]:
        coords3d[idx,1] -= sadness_drop
        coords3d[idx,2] += 0.07 * sadness_drop * (1 if idx==2 else -1)
    # Head drops more (nods) in bow
    head_idx = JOINT_ORDER.index('Head')
    coords3d[head_idx,1] -= sadness_drop*1.25

    # Move arms forward as in bow (simulate holding a light object with slacked arms)
    arm_ang = np.deg2rad(-25 * (min(bow/np.deg2rad(55),1)))  # swing forward
    def arm_forward(joint, elbow, hand, ang_sign=1):
        orig_shoulder = coords3d[JOINT_ORDER.index(joint)]
        orig_elbow = coords3d[JOINT_ORDER.index(elbow)] - orig_shoulder
        orig_hand = coords3d[JOINT_ORDER.index(hand)] - coords3d[JOINT_ORDER.index(elbow)]
        R_z = np.array([
            [np.cos(arm_ang*ang_sign),-np.sin(arm_ang*ang_sign),0],
            [np.sin(arm_ang*ang_sign),np.cos(arm_ang*ang_sign),0],
            [0,0,1]
        ])
        delta_elbow = orig_elbow @ R_z.T
        delta_hand = orig_hand @ R_z.T
        coords3d[JOINT_ORDER.index(elbow)] = orig_shoulder + delta_elbow
        coords3d[JOINT_ORDER.index(hand)] = orig_shoulder + delta_elbow + delta_hand
    arm_forward('RShoulder','RElbow','RHand',ang_sign=1)
    arm_forward('LShoulder','LElbow','LHand',ang_sign=-1)

    # Legs and feet: knees bend a bit in max bow
    knee_shift = min(bow/np.deg2rad(55),1) * 0.07
    for hipjoint, kneejoint, footjoint, sign in [
        ('RHip', 'RKnee', 'RFoot', -1),
        ('LHip', 'LKnee', 'LFoot', 1)
    ]:
        hidx = JOINT_ORDER.index(hipjoint)
        kidx = JOINT_ORDER.index(kneejoint)
        fidx = JOINT_ORDER.index(footjoint)
        coords3d[kidx,0] += sign*knee_shift*0.5
        coords3d[kidx,1] -= knee_shift
        coords3d[fidx,0] += sign*knee_shift*0.7

    # Perspective projection: "camera up front"
    persp = 2.3
    x = coords3d[:,0] / (1 + coords3d[:,2]/persp)
    y = coords3d[:,1]
    out = np.stack([x,y],axis=1)
    # Scale and center for display
    out *= 250  # scaling
    out[:,0] += 250  # center x
    out[:,1] = 500 - out[:,1]  # y axis: downward
    return out

# --- Animation setup ---
fig = plt.figure(figsize=(4,8), facecolor='black')
ax = plt.axes(xlim=(0,500), ylim=(0,600))
ax.set_facecolor('black')
plt.axis('off')

ln, = ax.plot([], [], 'wo', markersize=10)

def init():
    ln.set_data([], [])
    return ln,

def animate(i):
    t = (i % 80) / 80.0  # 80 frames per cycle
    pose = bowing_pose(t)
    ln.set_data(pose[:,0], pose[:,1])
    return ln,

ani = animation.FuncAnimation(fig, animate, frames=160, interval=33, blit=True, init_func=init)
plt.show()
