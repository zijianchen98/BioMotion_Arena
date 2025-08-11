
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def _create_pose(pelvis_pos, torso_angle, arm_angle, forearm_angle, thigh_angle, calf_angle):
    """
    Helper function to generate a 15x2 pose array from high-level parameters.
    This defines the skeleton's structure and calculates joint positions based on angles.
    """
    # Constants for body proportions ('light weight woman')
    NECK_LENGTH = 0.12
    SHOULDER_WIDTH = 0.35
    UPPER_ARM_LENGTH = 0.3
    LOWER_ARM_LENGTH = 0.28
    TORSO_LENGTH = 0.55
    PELVIS_WIDTH = 0.28
    UPPER_LEG_LENGTH = 0.45
    LOWER_LEG_LENGTH = 0.45
    
    pose = np.zeros((15, 2))
    
    pelvis_pos = np.array(pelvis_pos)
    
    # Torso and Head
    # The torso angle is defined relative to the horizontal positive x-axis
    neck_pos = pelvis_pos + np.array([TORSO_LENGTH * np.cos(torso_angle), TORSO_LENGTH * np.sin(torso_angle)])
    # Head is always tucked forward relative to the neck-pelvis line for a rolling motion
    head_tuck_angle = np.deg2rad(-45)
    head_angle = torso_angle + head_tuck_angle
    head_pos = neck_pos + np.array([NECK_LENGTH * np.cos(head_angle), NECK_LENGTH * np.sin(head_angle)])

    # Shoulders and Hips are perpendicular to the torso
    shoulder_perp_angle = torso_angle + np.pi / 2
    hip_perp_angle = torso_angle + np.pi / 2
    
    shoulder_vec = np.array([np.cos(shoulder_perp_angle), np.sin(shoulder_perp_angle)]) * SHOULDER_WIDTH / 2
    l_shoulder_pos = neck_pos + shoulder_vec
    r_shoulder_pos = neck_pos - shoulder_vec

    hip_vec = np.array([np.cos(hip_perp_angle), np.sin(hip_perp_angle)]) * PELVIS_WIDTH / 2
    l_hip_pos = pelvis_pos + hip_vec
    r_hip_pos = pelvis_pos - hip_vec
    
    # Limb angles are relative to the torso vector
    ua_ang = torso_angle + arm_angle
    la_ang = ua_ang + forearm_angle
    ul_ang = torso_angle + np.pi + thigh_angle
    ll_ang = ul_ang + calf_angle
    
    # Calculate all limb end positions (both sides are symmetrical in this 2D view)
    l_elbow_pos = l_shoulder_pos + np.array([UPPER_ARM_LENGTH * np.cos(ua_ang), UPPER_ARM_LENGTH * np.sin(ua_ang)])
    l_wrist_pos = l_elbow_pos + np.array([LOWER_ARM_LENGTH * np.cos(la_ang), LOWER_ARM_LENGTH * np.sin(la_ang)])
    r_elbow_pos = r_shoulder_pos + np.array([UPPER_ARM_LENGTH * np.cos(ua_ang), UPPER_ARM_LENGTH * np.sin(ua_ang)])
    r_wrist_pos = r_elbow_pos + np.array([LOWER_ARM_LENGTH * np.cos(la_ang), LOWER_ARM_LENGTH * np.sin(la_ang)])
    
    l_knee_pos = l_hip_pos + np.array([UPPER_LEG_LENGTH * np.cos(ul_ang), UPPER_LEG_LENGTH * np.sin(ul_ang)])
    l_ankle_pos = l_knee_pos + np.array([LOWER_LEG_LENGTH * np.cos(ll_ang), LOWER_LEG_LENGTH * np.sin(ll_ang)])
    r_knee_pos = r_hip_pos + np.array([UPPER_LEG_LENGTH * np.cos(ul_ang), UPPER_LEG_LENGTH * np.sin(ul_ang)])
    r_ankle_pos = r_knee_pos + np.array([LOWER_LEG_LENGTH * np.cos(ll_ang), LOWER_LEG_LENGTH * np.sin(ll_ang)])
    
    # Assign to pose array in the standard order
    # 0:Head, 1:Neck, 2:LSh, 3:RSh, 4:LElb, 5:RElb, 6:LWrist, 7:RWrist
    # 8:Pelvis, 9:LHip, 10:RHip, 11:LKnee, 12:RKnee, 13:LAnkle, 14:RAnkle
    pose[0], pose[1], pose[8] = head_pos, neck_pos, pelvis_pos
    pose[2], pose[3] = l_shoulder_pos, r_shoulder_pos
    pose[9], pose[10] = l_hip_pos, r_hip_pos
    pose[4], pose[5] = l_elbow_pos, r_elbow_pos
    pose[6], pose[7] = l_wrist_pos, r_wrist_pos
    pose[11], pose[12] = l_knee_pos, r_knee_pos
    pose[13], pose[14] = l_ankle_pos, r_ankle_pos
    
    return pose

def generate_motion_data(num_frames=120):
    """
    Generates motion data for a sad forward roll using keyframe interpolation.
    The "sad" quality is conveyed through a slumped posture and less dynamic movement.
    """
    
    # Define angles for different states. All angles are in radians.
    # Sad posture implies a slumped torso, reflected in the base torso angle.
    slump_angle = np.deg2rad(-20)
    
    # State 1: Standing/Slumped
    stand_torso = np.deg2rad(-90) + slump_angle
    stand_arm = np.deg2rad(15)
    stand_forearm = np.deg2rad(-15)
    stand_thigh = np.deg2rad(-100)
    stand_calf = np.deg2rad(-10)

    # State 2: Crouching to roll
    crouch_torso = np.deg2rad(-70) + slump_angle
    crouch_arm = np.deg2rad(-135)
    crouch_forearm = np.deg2rad(-30)
    crouch_thigh = np.deg2rad(-45)
    crouch_calf = np.deg2rad(-90)

    # State 3: Tucked for roll
    tuck_arm = np.deg2rad(-45)
    tuck_forearm = np.deg2rad(-140)
    tuck_thigh = np.deg2rad(-35)
    tuck_calf = np.deg2rad(-130)

    # Define keyframes by specifying the parameters for our pose helper function at different times.
    keyframes_params = {
        0.0:  {'pelvis_pos': [-1.2, 0.8], 'torso_angle': stand_torso, 
               'arm_angle': stand_arm, 'forearm_angle': stand_forearm, 'thigh_angle': stand_thigh, 'calf_angle': stand_calf},
        0.15: {'pelvis_pos': [-1.0, 0.3], 'torso_angle': crouch_torso,
               'arm_angle': crouch_arm, 'forearm_angle': crouch_forearm, 'thigh_angle': crouch_thigh, 'calf_angle': crouch_calf},
        0.4:  {'pelvis_pos': [-0.4, 0.25], 'torso_angle': stand_torso - np.pi, # Rotated 180 deg
               'arm_angle': tuck_arm, 'forearm_angle': tuck_forearm, 'thigh_angle': tuck_thigh, 'calf_angle': tuck_calf},
        0.6:  {'pelvis_pos': [0.4, 0.25], 'torso_angle': stand_torso - 1.8 * np.pi, # Almost full circle
               'arm_angle': tuck_arm, 'forearm_angle': tuck_forearm, 'thigh_angle': tuck_thigh, 'calf_angle': tuck_calf},
        0.85: {'pelvis_pos': [1.0, 0.3], 'torso_angle': stand_torso - 2 * np.pi, # Back upright
               'arm_angle': crouch_arm, 'forearm_angle': crouch_forearm, 'thigh_angle': crouch_thigh, 'calf_angle': crouch_calf},
        1.0:  {'pelvis_pos': [1.2, 0.8], 'torso_angle': stand_torso - 2 * np.pi,
               'arm_angle': stand_arm, 'forearm_angle': stand_forearm, 'thigh_angle': stand_thigh, 'calf_angle': stand_calf}
    }
    
    key_times = sorted(keyframes_params.keys())
    key_poses_list = [_create_pose(**keyframes_params[t]) for t in key_times]
    key_poses = np.array(key_poses_list)

    frame_times = np.linspace(0, 1, num_frames)
    motion_data = np.zeros((num_frames, 15, 2))

    for point_idx in range(15):
        for coord_idx in range(2): # 0 for x, 1 for y
            key_coords = key_poses[:, point_idx, coord_idx]
            motion_data[:, point_idx, coord_idx] = np.interp(frame_times, key_times, key_coords)

    # Center and scale the entire animation to fit the view
    min_coords = np.min(motion_data.reshape(-1, 2), axis=0)
    max_coords = np.max(motion_data.reshape(-1, 2), axis=0)
    center = (min_coords + max_coords) / 2
    motion_data -= center
    
    scale = np.max(max_coords - min_coords)
    if scale > 1e-6:
        motion_data /= (scale * 0.6)

    return motion_data

# --- Animation Setup ---
NUM_FRAMES = 120
INTERVAL = 50  # Interval in milliseconds (120 frames * 50ms = 6s animation)

# Generate the point-light motion data
motion_data = generate_motion_data(NUM_FRAMES)

# Set up the plot
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Configure axes for a clean, centered look
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Initialize the plot object for the 15 points
points_plot, = ax.plot([], [], 'o', color='white', markersize=8)

# Initialization function for the animation
def init():
    points_plot.set_data([], [])
    return (points_plot,)

# Update function called for each frame
def update(frame):
    frame_data = motion_data[frame]
    points_plot.set_data(frame_data[:, 0], frame_data[:, 1])
    return (points_plot,)

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES,
                              init_func=init, blit=True, interval=INTERVAL)

# Display the animation
plt.show()
