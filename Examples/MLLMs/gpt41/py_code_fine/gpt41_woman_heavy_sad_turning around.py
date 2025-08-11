
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 point lights: [Head, Shoulders (L,R), Elbows (L,R), Wrists (L,R), Hips (L,R), Knees (L,R), Ankles (L,R)]
# Additional: Chest, Spine, Neck (for realism). We'll assign as:
# [Head, Neck, Chest, Spine, LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist, LHip, RHip, LKnee, RKnee, LAnkle, RAnkle]
# But will only display 15 main points as per the requirement.
# Let's map: [Head, LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist, Chest, Spine, LHip, RHip, LKnee, RKnee, LAnkle, RAnkle]

# Main stick figure in 3D coordinates
def get_biological_structure(is_heavy=True, is_sad=True):
    """
    Defines the canonical pose of the woman in 3D (XZ is the horizontal plane)
    Units: arbitrary, centered at pelvis/spine
    """
    # Y is up vertical. X is left-right, Z is forward-back
    size = 1.0
    width = 0.27 * size
    shoulder_width = (0.42 if is_heavy else 0.33) * size
    hip_width = (0.30 if is_heavy else 0.23) * size
    head_height = 0.22 * size
    neck_length = 0.11 * size
    spine_length = (0.47 if is_heavy else 0.53) * size
    upper_arm = 0.24 * size
    forearm = 0.24 * size
    thigh = (0.28 if is_heavy else 0.32) * size
    shank = (0.26 if is_heavy else 0.29) * size
    # sagittal slouch for sad
    neck_dz = -0.09 * size if is_sad else 0
    spine_dz = -0.11 * size if is_sad else 0
    chest_dz = -0.08 * size if is_sad else 0
    head_dz = -0.07 * size if is_sad else 0

    # y-up, z-forward, x-left
    pelvis_center = np.array([0, 0, 0])
    spine = pelvis_center + np.array([0, spine_length * 0.4, spine_dz])
    chest = spine + np.array([0, spine_length * 0.35, chest_dz])
    neck = chest + np.array([0, neck_length, neck_dz])
    head = neck + np.array([0, head_height, head_dz])
    
    # Shoulders
    LShoulder = chest + np.array([shoulder_width / 2, 0, 0])
    RShoulder = chest + np.array([-shoulder_width / 2, 0, 0])

    # Hips
    LHip = pelvis_center + np.array([hip_width/2, 0, 0])
    RHip = pelvis_center + np.array([-hip_width/2, 0, 0])

    # Arms (hanging down, a bit forward and in as if clutching or holding weight for sad)
    arm_pitch = np.pi/7  # forward angle of upper arms
    arm_roll = (np.pi/12 if is_heavy else np.pi/9)  # inward "hugging"
    # Elbows
    LElbow = LShoulder + np.array([np.sin(arm_roll)*upper_arm, 
                                   -np.cos(arm_pitch)*upper_arm, 
                                   np.sin(arm_pitch)*upper_arm])
    RElbow = RShoulder + np.array([-np.sin(arm_roll)*upper_arm, 
                                   -np.cos(arm_pitch)*upper_arm, 
                                   np.sin(arm_pitch)*upper_arm])
    # Wrists
    LWrist = LElbow + np.array([np.sin(arm_roll)*forearm*0.7, 
                                -forearm*0.95, 
                                -0.08*forearm])
    RWrist = RElbow + np.array([-np.sin(arm_roll)*forearm*0.7, 
                                -forearm*0.95, 
                                -0.08*forearm])

    # Legs (close together, as sad stance)
    thigh_spread = np.pi/25 # small
    knee_y = -thigh
    LKnee = LHip + np.array([-np.sin(thigh_spread)*thigh, knee_y, 0])
    RKnee = RHip + np.array([np.sin(thigh_spread)*thigh, knee_y, 0])
    # Ankles
    ankle_y = -shank
    LAnkle = LKnee + np.array([0, ankle_y, 0.02 if is_heavy else 0])
    RAnkle = RKnee + np.array([0, ankle_y, 0.02 if is_heavy else 0])

    # 15 points:
    return np.stack([
        head,                 # 0: Head
        LShoulder,            # 1: Left Shoulder
        RShoulder,            # 2: Right Shoulder
        LElbow,               # 3: Left Elbow
        RElbow,               # 4: Right Elbow
        LWrist,               # 5: Left Wrist
        RWrist,               # 6: Right Wrist
        chest,                # 7: Chest
        spine,                # 8: Spine
        LHip,                 # 9: Left Hip
        RHip,                 #10: Right Hip
        LKnee,                #11: Left Knee
        RKnee,                #12: Right Knee
        LAnkle,               #13: Left Ankle
        RAnkle,               #14: Right Ankle
    ])

def apply_turn(points, theta):
    """
    Rotates whole body around Y (vertical) axis by angle theta (in radians)
    Assumes points shape (n,3)
    """
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    # Returning rotated points
    return points @ R.T

def animate_point_lights():
    # Generate canonical pose
    canonical_pts = get_biological_structure(is_heavy=True, is_sad=True)

    # Animation frames for smooth turn -- turn left 180deg with a sad motion
    nframes = 120
    # Turning "around", but sad: motion slow at start/end, fast in middle
    t = np.linspace(0, 1, nframes)
    turn_progress = (1 - np.cos(np.pi * t)) / 2  # ease-in-out
    angle_total = np.pi  # 180 deg turn CCW
    # Optional: subtle head droop, weight shift for added realism
    head_droop = -0.06  # head drops further by this much at turn
    hip_shift = 0.09    # hips move laterally (as if carrying weight in one hand)
    chest_round = 0.05  # chest slouches/flexes more at mid-turn

    pts_seq = []
    for fi in range(nframes):
        prog = turn_progress[fi]
        theta = angle_total * prog
        pts = canonical_pts.copy()
        # Add biomechanics: head slouch increases at the midpoint of turn
        pts[0,1] += head_droop * np.sin(np.pi * prog)
        # Slouch more at chest at halfway
        pts[7,2] += chest_round * (np.sin(np.pi * prog) ** 2)
        # Hips sway as a weight moves to L side
        pts[9,0] += hip_shift * (np.sin(np.pi * prog) ** 1.5) # LHip left
        pts[10,0] += hip_shift * (np.sin(np.pi * prog) ** 1.5) # RHip left
        # Tuck one wrist in, as if clutching a heavy load
        clutch = 0.12 * np.sin(np.pi * prog)
        pts[5,0] -= clutch  # Left wrist moves in
        pts[6,0] -= clutch/2 # Right wrist, just a tad
        # All points rotate around Y axis (spine at (0,0,0))
        pts = apply_turn(pts, theta)
        pts_seq.append(pts)

    # Prepare animation
    fig, ax = plt.subplots(figsize=(4,7))
    ax.set_facecolor('black')
    
    # Set up axes -- make similar to sample image
    ax.set_xlim(-0.75,0.75)
    ax.set_ylim(-0.35,1.85)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Points for scatter plot
    scatter = ax.scatter([], [], s=56, c='white', edgecolors='none')
    
    # Frame update function
    def update(frame):
        pts = pts_seq[frame]
        # Project 3D to 2D: X (horizontal), Y (vertical) (ignore Z, or do weak perspective) 
        # For natural weak perspective, closer (larger Z) is slightly higher
        # We'll add small scaling by Z for slight 3D effect
        z_offset = pts[:,2] * 0.07
        x2d = pts[:,0] + z_offset
        y2d = pts[:,1] + z_offset * 0.12
        scatter.set_offsets(np.stack([x2d, y2d], axis=1))
        return scatter,

    # Animation
    ani = animation.FuncAnimation(fig, update, frames=nframes, interval=1000/35, blit=True)
    plt.show()

if __name__ == '__main__':
    animate_point_lights()
