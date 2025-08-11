
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import CubicSpline

def generate_motion_data():
    """
    Generates the point-light motion data for a forward roll.

    The function defines a series of keyframes for a 15-point human model
    and uses cubic spline interpolation to generate smooth motion between them.
    The motion depicts a heavy person performing a forward roll.

    Returns:
        numpy.ndarray: An array of shape (num_frames, 15, 2) containing
                       the (x, y) coordinates for each point in each frame.
    """
    num_frames = 100
    
    # Keyframe definitions
    # Each pose is a (15, 2) numpy array for the 15 joint coordinates.
    # Joint indices: 0:head, 1:neck, 2:sternum, 3:l_shoulder, 4:r_shoulder,
    # 5:l_elbow, 6:r_elbow, 7:l_wrist, 8:r_wrist, 9:l_hip, 10:r_hip,
    # 11:l_knee, 12:r_knee, 13:l_ankle, 14:r_ankle
    
    keyframe_poses = []
    keyframe_times = [0, 18, 38, 58, 75, 88, 99]

    # --- Keyframe 1 (t=0): Deep squat, preparing to roll ---
    pose1 = np.zeros((15, 2))
    c_x, c_y = -1.8, -0.6
    pose1[9]  = [c_x - 0.2, c_y]         # L Hip
    pose1[10] = [c_x + 0.2, c_y]         # R Hip
    pose1[2]  = [c_x + 0.1,  c_y + 0.5]   # Sternum (bent forward)
    pose1[3]  = [c_x - 0.05, c_y + 0.75]  # L Shoulder
    pose1[4]  = [c_x + 0.25, c_y + 0.75]  # R Shoulder
    pose1[1]  = [c_x + 0.1,  c_y + 0.85]  # Neck
    pose1[0]  = [c_x + 0.1,  c_y + 1.1]   # Head
    pose1[11] = [c_x - 0.2,  c_y - 0.45]  # L Knee
    pose1[12] = [c_x + 0.2,  c_y - 0.45]  # R Knee
    pose1[13] = [c_x - 0.15, c_y - 0.9]   # L Ankle
    pose1[14] = [c_x + 0.25, c_y - 0.9]   # R Ankle
    pose1[5]  = [c_x + 0.4,  c_y + 0.4]   # L Elbow
    pose1[6]  = [c_x + 0.6,  c_y + 0.4]   # R Elbow
    pose1[7]  = [c_x + 0.6,  c_y]         # L Wrist
    pose1[8]  = [c_x + 0.8,  c_y]         # R Wrist
    keyframe_poses.append(pose1)

    # --- Keyframe 2 (t=18): Hands down, pushing off ---
    pose2 = np.zeros((15, 2))
    c_x, c_y = -1.2, -0.4
    pose2[9]  = [c_x - 0.2, c_y + 0.25]  # L Hip
    pose2[10] = [c_x + 0.2, c_y + 0.25]  # R Hip
    pose2[2]  = [c_x + 0.3, c_y]         # Sternum
    pose2[3]  = [c_x + 0.15,c_y + 0.3]   # L Shoulder
    pose2[4]  = [c_x + 0.45,c_y + 0.3]   # R Shoulder
    pose2[1]  = [c_x + 0.3, c_y + 0.4]   # Neck
    pose2[0]  = [c_x + 0.2, c_y + 0.15]  # Head (tucked)
    pose2[11] = [c_x - 0.4, c_y - 0.2]   # L Knee
    pose2[12] = [c_x,       c_y - 0.2]   # R Knee
    pose2[13] = [c_x - 0.7, c_y - 0.7]   # L Ankle
    pose2[14] = [c_x - 0.3, c_y - 0.7]   # R Ankle
    pose2[5]  = [c_x + 0.6, c_y - 0.1]   # L Elbow
    pose2[6]  = [c_x + 0.9, c_y - 0.1]   # R Elbow
    pose2[7]  = [c_x + 0.7, c_y - 0.6]   # L Wrist (on ground)
    pose2[8]  = [c_x + 1.0, c_y - 0.6]   # R Wrist (on ground)
    keyframe_poses.append(pose2)

    # --- Keyframe 3 (t=38): Tucked roll, inverted ---
    pose3 = np.zeros((15, 2))
    c_x, c_y = -0.1, 0.0
    pose3[9]  = [c_x - 0.2,  c_y + 0.55]  # L Hip
    pose3[10] = [c_x + 0.2,  c_y + 0.55]  # R Hip
    pose3[2]  = [c_x,        c_y - 0.2]   # Sternum
    pose3[3]  = [c_x - 0.2,  c_y - 0.4]   # L Shoulder
    pose3[4]  = [c_x + 0.2,  c_y - 0.4]   # R Shoulder
    pose3[1]  = [c_x,        c_y - 0.5]   # Neck
    pose3[0]  = [c_x,        c_y - 0.3]   # Head (tucked)
    pose3[11] = [c_x + 0.05, c_y + 0.8]   # L Knee
    pose3[12] = [c_x + 0.45, c_y + 0.8]   # R Knee
    pose3[13] = [c_x + 0.15, c_y + 0.4]   # L Ankle
    pose3[14] = [c_x + 0.55, c_y + 0.4]   # R Ankle
    pose3[5]  = [c_x - 0.35, c_y - 0.1]   # L Elbow
    pose3[6]  = [c_x + 0.35, c_y - 0.1]   # R Elbow
    pose3[7]  = [c_x - 0.25, c_y + 0.2]   # L Wrist
    pose3[8]  = [c_x + 0.25, c_y + 0.2]   # R Wrist
    keyframe_poses.append(pose3)
    
    # --- Keyframe 4 (t=58): Preparing to land ---
    pose4 = np.zeros((15, 2))
    c_x, c_y = 0.9, -0.3
    pose4[9]  = [c_x - 0.2, c_y - 0.4]   # L Hip
    pose4[10] = [c_x + 0.2, c_y - 0.4]   # R Hip
    pose4[2]  = [c_x,       c_y]         # Sternum
    pose4[3]  = [c_x - 0.2, c_y + 0.3]   # L Shoulder
    pose4[4]  = [c_x + 0.2, c_y + 0.3]   # R Shoulder
    pose4[1]  = [c_x,       c_y + 0.4]   # Neck
    pose4[0]  = [c_x,       c_y + 0.65]  # Head
    pose4[11] = [c_x + 0.1, c_y - 0.75]  # L Knee
    pose4[12] = [c_x + 0.5, c_y - 0.75]  # R Knee
    pose4[13] = [c_x + 0.3, c_y - 1.1]   # L Ankle
    pose4[14] = [c_x + 0.7, c_y - 1.1]   # R Ankle
    pose4[5]  = [c_x - 0.3, c_y + 0.6]   # L Elbow
    pose4[6]  = [c_x + 0.3, c_y + 0.6]   # R Elbow
    pose4[7]  = [c_x - 0.2, c_y + 0.9]   # L Wrist
    pose4[8]  = [c_x + 0.2, c_y + 0.9]   # R Wrist
    keyframe_poses.append(pose4)

    # --- Keyframe 5 (t=75): Landed in a low squat ---
    pose5 = np.zeros((15, 2))
    c_x, c_y = 1.6, -0.7
    pose5[9]  = [c_x - 0.2, c_y]        # L Hip
    pose5[10] = [c_x + 0.2, c_y]        # R Hip
    pose5[2]  = [c_x,       c_y + 0.5]  # Sternum
    pose5[3]  = [c_x - 0.25,c_y + 0.75] # L Shoulder
    pose5[4]  = [c_x + 0.25,c_y + 0.75] # R Shoulder
    pose5[1]  = [c_x,       c_y + 0.85] # Neck
    pose5[0]  = [c_x,       c_y + 1.1]  # Head
    pose5[11] = [c_x - 0.15,c_y - 0.45] # L Knee
    pose5[12] = [c_x + 0.25,c_y - 0.45] # R Knee
    pose5[13] = [c_x - 0.15,c_y - 0.9]  # L Ankle
    pose5[14] = [c_x + 0.25,c_y - 0.9]  # R Ankle
    pose5[5]  = [c_x - 0.1, c_y + 1.1]  # L Elbow
    pose5[6]  = [c_x + 0.1, c_y + 1.1]  # R Elbow
    pose5[7]  = [c_x,       c_y + 1.4]  # L Wrist
    pose5[8]  = [c_x + 0.2, c_y + 1.4]  # R Wrist
    keyframe_poses.append(pose5)
    
    # --- Keyframe 6 (t=88): Rising up energetically ---
    pose6 = np.zeros((15, 2))
    c_x, c_y = 1.8, -0.4
    pose6[9]  = [c_x - 0.2, c_y]        # L Hip
    pose6[10] = [c_x + 0.2, c_y]        # R Hip
    pose6[2]  = [c_x,       c_y + 0.6]  # Sternum
    pose6[3]  = [c_x - 0.25,c_y + 0.85] # L Shoulder
    pose6[4]  = [c_x + 0.25,c_y + 0.85] # R Shoulder
    pose6[1]  = [c_x,       c_y + 0.95] # Neck
    pose6[0]  = [c_x,       c_y + 1.2]  # Head
    pose6[11] = [c_x - 0.2, c_y - 0.35] # L Knee
    pose6[12] = [c_x + 0.2, c_y - 0.35] # R Knee
    pose6[13] = [c_x - 0.2, c_y - 0.8]  # L Ankle
    pose6[14] = [c_x + 0.2, c_y - 0.8]  # R Ankle
    pose6[5]  = [c_x - 0.3, c_y + 0.5]  # L Elbow
    pose6[6]  = [c_x + 0.3, c_y + 0.5]  # R Elbow
    pose6[7]  = [c_x - 0.35,c_y + 0.1]  # L Wrist
    pose6[8]  = [c_x + 0.35,c_y + 0.1]  # R Wrist
    keyframe_poses.append(pose6)
    
    # --- Keyframe 7 (t=99): Settling down (small bounce) ---
    pose7 = pose6.copy()
    pose7[:, 1] -= 0.08 # Settle down slightly
    pose7[:, 0] += 0.05 # Tiny drift
    keyframe_poses.append(pose7)

    # Convert list of poses to a numpy array
    keyframe_poses = np.array(keyframe_poses)
    
    # Create time arrays for interpolation
    full_time_vector = np.arange(num_frames)
    interpolated_data = np.zeros((num_frames, 15, 2))

    # Interpolate each point's trajectory
    for point_idx in range(15):
        x_coords = keyframe_poses[:, point_idx, 0]
        y_coords = keyframe_poses[:, point_idx, 1]
        
        # Use cubic splines for smooth interpolation
        cs_x = CubicSpline(keyframe_times, x_coords)
        cs_y = CubicSpline(keyframe_times, y_coords)
        
        interpolated_data[:, point_idx, 0] = cs_x(full_time_vector)
        interpolated_data[:, point_idx, 1] = cs_y(full_time_vector)
        
    return interpolated_data

# --- Main Animation Setup ---
# Generate the motion data
motion_data = generate_motion_data()

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set axis limits to encompass the entire motion, with some padding
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 2.0)

# Ensure aspect ratio is equal and turn off the axis labels/ticks
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Initialize the scatter plot with the first frame of data
scatter = ax.scatter(motion_data[0, :, 0], motion_data[0, :, 1], 
                     s=80, c='white')

# Update function for the animation
def update(frame):
    """Updates the positions of the points for each frame."""
    scatter.set_offsets(motion_data[frame])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(motion_data),
                              interval=33, blit=True)

# To display the animation
plt.show()
