
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 point-light marker labels:
JOINTS = [
    "head",          # 0
    "r_shoulder",    # 1
    "l_shoulder",    # 2
    "neck",          # 3
    "r_elbow",       # 4
    "l_elbow",       # 5
    "r_hand",        # 6
    "l_hand",        # 7
    "torso",         # 8
    "hip",           # 9
    "r_knee",        #10
    "l_knee",        #11
    "r_ankle",       #12
    "l_ankle",       #13
    "weight"         #14 <- The lifted heavy weight
]

# Canonical positions of each joint in T-pose (in meters, in 3D XYZ)
# (origin is at hip joint)
JOINT_POSITIONS = np.array([
    [0.0,   0.6, 0.0],     # head
    [0.15,  0.45, 0.0],    # r_shoulder
    [-0.15, 0.45, 0.0],    # l_shoulder
    [0.0,   0.43, 0.0],    # neck
    [0.27,  0.25, 0.0],    # r_elbow
    [-0.27, 0.25, 0.0],    # l_elbow
    [0.32,  0.1, 0.0],     # r_hand
    [-0.32, 0.1, 0.0],     # l_hand
    [0.0,   0.2, 0.0],     # torso
    [0.0,   0.0, 0.0],     # hip/pelvis
    [0.08, -0.25, 0.0],    # r_knee
    [-0.08,-0.25, 0.0],    # l_knee
    [0.10,-0.5, 0.0],      # r_ankle
    [-0.10,-0.5, 0.0],     # l_ankle
    [0.0,   0.1, 0.3],     # weight (will be moved with both hands)
])

# Segment connections for biomechanical plausibility (not drawn, just for kinematics)
BONES = [
    (9,8), (8,3), (3,0),          # spine/neck/head
    (3,1), (1,4), (4,6),          # right arm
    (3,2), (2,5), (5,7),          # left arm
    (9,10), (10,12),              # right leg
    (9,11), (11,13),              # left leg
    (6,14), (7,14)                # both hands to held weight
]

def animate_point_light_turning(num_frames=120):
    # Animation Settings
    fig, ax = plt.subplots(figsize=(3.5, 5.6), facecolor='black')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_xlim(-0.6,0.6)
    ax.set_ylim(-0.7,0.75)
    ax.axis('off')
    plt.tight_layout(pad=0)
    
    # Points (initialized)
    scat = ax.scatter([], [], s=45, c='w', edgecolor='none')
    
    # Pre-compute smooth "walking in place and turning" kinematics (yaw, arm motion)
    # --- Create smooth turning from -90deg to +90deg (pi/2)
    turn_angles = np.linspace(-np.pi/2, np.pi/2, num_frames)      # Yaw angles
    
    # Simulate simple limb/weight movement while turning
    hand_lift = 0.05*np.sin(np.linspace(0, 2*np.pi, num_frames))  # "happy motion" up-down
    hand_side = 0.03*np.sin(np.linspace(0, 4*np.pi, num_frames))  # a little wiggle
    
    # Weight "bob" to reflect heavy lifting with both hands
    weight_bob = 0.11 + 0.025*np.abs(np.sin(np.linspace(0, 2*np.pi, num_frames)))
    
    def get_pose3D(frame):
        # Start with the canonical pose
        P = JOINT_POSITIONS.copy()
        # --- Animate arms and hands: both hands lift the weight with some bounce
        # (joined forward, bobbing up and down)
        # The hands (6,7) approach middle + move up/down synchronously.
        hand_forward = 0.15 + 0.05*np.sin(2*np.pi * frame/num_frames)
        P[6][0] = 0.09+hand_side[frame]  # r_hand X
        P[6][1] = 0.18+hand_lift[frame]
        P[6][2] = hand_forward
        
        P[7][0] = -0.09-hand_side[frame] # l_hand X
        P[7][1] = 0.18+hand_lift[frame]
        P[7][2] = hand_forward
        
        # Elbows bend toward midline as well (simulate "happyman")
        P[4][0] = 0.24+0.03*hand_side[frame]
        P[4][1] = 0.32 + 0.5*(P[6][1]-0.1)
        P[4][2] = 0.07 + 0.5*(P[6][2]-0)
        P[5][0] = -0.24-0.03*hand_side[frame]
        P[5][1] = 0.32 + 0.5*(P[7][1]-0.1)
        P[5][2] = 0.07 + 0.5*(P[7][2]-0)
        
        # Weight goes in front of hands and bobs
        P[14][0] = 0.0
        P[14][1] = 0.10 + hand_lift[frame]*0.7
        P[14][2] = weight_bob[frame]
        
        # Add a little happy head bounce and lean
        P[0][1] += 0.025*np.sin(np.pi*frame/num_frames)
        P[0][0] += 0.01*np.sin(2*np.pi*frame/num_frames)
        
        # Slight shift of legs and knees, so he is lively
        P[10][0] += 0.03*np.sin(np.pi*frame/num_frames)
        P[11][0] -= 0.03*np.sin(np.pi*frame/num_frames)
        P[12][0] += 0.03*np.sin(np.pi*frame/num_frames)
        P[13][0] -= 0.03*np.sin(np.pi*frame/num_frames)
        P[10][1] -= 0.015*np.abs(np.sin(2*np.pi*frame/num_frames))
        P[11][1] -= 0.015*np.abs(np.sin(2*np.pi*frame/num_frames))
        P[12][1] -= 0.004*np.abs(np.sin(2*np.pi*frame/num_frames))
        P[13][1] -= 0.004*np.abs(np.sin(2*np.pi*frame/num_frames))
        
        # The whole body will rotate (turn) in place by yaw angle
        theta = turn_angles[frame]
        R = np.array([
            [np.cos(theta), 0, np.sin(theta)],
            [0,             1,            0],
            [-np.sin(theta),0, np.cos(theta)]
        ])
        # Center at "hip" (JOINT 9)
        center = P[9:10]
        # subtract center, rotate, add back at origin (so body rotates in place)
        P = (P-center) @ R.T + center
        # Optionally, shift slightly for a pleasing path
        # P[:,0] += 0.07*np.sin(theta) 
        return P
    
    # Animation update function
    def update(frame):
        pose3D = get_pose3D(frame)
        # Orthographic "camera": Project to 2D (x, y)
        XY = pose3D[:,:2]
        # Optional: center vertically
        XY[:,0] = XY[:,0]
        XY[:,1] = XY[:,1]
        # For weight: make it bolder visually (draw twice)
        scat.set_offsets(XY)
        return scat,
    
    scat.set_offsets(np.zeros((15,2)))  # initialize
    
    ani = animation.FuncAnimation(
        fig, update, frames=num_frames, interval=1000/30, blit=True, repeat=True
    )
    
    plt.show()

if __name__ == "__main__":
    animate_point_light_turning(num_frames=120)
