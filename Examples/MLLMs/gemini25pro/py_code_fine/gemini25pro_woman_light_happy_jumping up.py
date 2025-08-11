
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_jumping_animation():
    """
    Generates and displays a point-light animation of a person jumping.
    """
    # Define 15 joint points for the body model
    # Order: Head, NeckC, R_Sh, R_Elb, R_Wr, L_Sh, L_Elb, L_Wr, 
    #        PelvisC, R_Hip, R_Knee, R_Ank, L_Hip, L_Knee, L_Ank

    # Keyframe 1: Standing pose
    pose_stand = np.array([
        [0.0, 1.5],   # Head
        [0.0, 1.35],  # NeckC
        [-0.15, 1.35],# R Shoulder
        [-0.15, 1.05],# R Elbow
        [-0.15, 0.75],# R Wrist
        [0.15, 1.35], # L Shoulder
        [0.15, 1.05], # L Elbow
        [0.15, 0.75], # L Wrist
        [0.0, 0.9],   # PelvisC
        [-0.1, 0.9],  # R Hip
        [-0.1, 0.45], # R Knee
        [-0.1, 0.0],  # R Ankle
        [0.1, 0.9],   # L Hip
        [0.1, 0.45],  # L Knee
        [0.1, 0.0],   # L Ankle
    ])

    # Keyframe 2: Crouching pose
    pose_crouch = np.array([
        [0.05, 1.1],   # Head
        [0.05, 0.95],  # NeckC
        [-0.1, 0.95],  # R Shoulder
        [-0.2, 0.65],  # R Elbow
        [-0.25, 0.35], # R Wrist
        [0.2, 0.95],   # L Shoulder
        [0.3, 0.65],   # L Elbow
        [0.35, 0.35],  # L Wrist
        [0.0, 0.5],    # PelvisC
        [-0.1, 0.5],   # R Hip
        [-0.15, 0.25], # R Knee
        [-0.1, 0.0],   # R Ankle
        [0.1, 0.5],    # L Hip
        [0.15, 0.25],  # L Knee
        [0.1, 0.0],    # L Ankle
    ])

    # Keyframe 3: Takeoff pose (fully extended)
    pose_takeoff = np.array([
        [0.0, 1.85],   # Head
        [0.0, 1.7],    # NeckC
        [-0.15, 1.7],  # R Shoulder
        [-0.1, 2.0],   # R Elbow
        [-0.05, 2.3],  # R Wrist
        [0.15, 1.7],   # L Shoulder
        [0.1, 2.0],    # L Elbow
        [0.05, 2.3],   # L Wrist
        [0.0, 1.2],    # PelvisC
        [-0.1, 1.2],   # R Hip
        [-0.1, 0.7],   # R Knee
        [-0.1, 0.1],   # R Ankle
        [0.1, 1.2],    # L Hip
        [0.1, 0.7],    # L Knee
        [0.1, 0.1],    # L Ankle
    ])

    # Keyframe 4: Peak of the jump
    jump_height = 0.9
    pose_peak = pose_takeoff.copy() + np.array([0, jump_height])
    # Adjust for tuck and "happy" arms
    pose_peak[10, :] = pose_peak[9] + np.array([0, -0.3])   # R Knee tucks
    pose_peak[11, :] = pose_peak[10] + np.array([0, -0.3])  # R Ankle tucks
    pose_peak[13, :] = pose_peak[12] + np.array([0, -0.3])  # L Knee tucks
    pose_peak[14, :] = pose_peak[13] + np.array([0, -0.3])  # L Ankle tucks
    pose_peak[3, :] += np.array([-0.1, 0.1])   # R Elbow out
    pose_peak[4, :] += np.array([-0.2, 0.2])   # R Wrist out
    pose_peak[6, :] += np.array([0.1, 0.1])    # L Elbow out
    pose_peak[7, :] += np.array([0.2, 0.2])    # L Wrist out

    # Keyframe 5: Landing impact (deep crouch)
    pose_land_impact = np.array([
        [0.05, 1.0],   # Head
        [0.05, 0.85],  # NeckC
        [-0.1, 0.85],  # R Shoulder
        [-0.3, 0.7],   # R Elbow
        [-0.4, 0.5],   # R Wrist
        [0.2, 0.85],   # L Shoulder
        [0.4, 0.7],    # L Elbow
        [0.5, 0.5],    # L Wrist
        [0.0, 0.4],    # PelvisC
        [-0.1, 0.4],   # R Hip
        [-0.15, 0.2],  # R Knee
        [-0.1, 0.0],   # R Ankle
        [0.1, 0.4],    # L Hip
        [0.15, 0.2],   # L Knee
        [0.1, 0.0],    # L Ankle
    ])

    # Define the sequence of poses and transition durations
    keyframe_data = [
        (pose_stand, 10),
        (pose_crouch, 15),
        (pose_takeoff, 8),
        (pose_peak, 20),
        (pose_takeoff, 20),
        (pose_land_impact, 8),
        (pose_stand, 25)
    ]

    all_frames = []
    # Hold the initial pose
    for _ in range(keyframe_data[0][1]):
        all_frames.append(keyframe_data[0][0])

    # Generate frames by interpolating between keyframes
    for i in range(len(keyframe_data) - 1):
        start_pose = keyframe_data[i][0]
        end_pose = keyframe_data[i+1][0]
        duration = keyframe_data[i+1][1]

        for frame_num in range(1, duration + 1):
            t = frame_num / duration
            # Use smoothstep easing for non-ballistic phases
            if i not in [2, 3]:  # Linear interpolation for flight
                t_eased = t * t * (3.0 - 2.0 * t)
            else:
                t_eased = t
            
            interp_pose = start_pose * (1 - t_eased) + end_pose * t_eased
            all_frames.append(interp_pose)

    point_data = np.array(all_frames)
    num_frames = point_data.shape[0]

    # Set up the plotting environment
    fig, ax = plt.subplots(figsize=(5, 7))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Set plot limits and aspect ratio
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal', adjustable='box')
    
    # Hide the axes
    ax.axis('off')
    plt.tight_layout()

    # Initialize the scatter plot for the points
    scatter = ax.scatter(point_data[0, :, 0], point_data[0, :, 1], c='white', s=70)

    # Animation update function
    def update(frame):
        scatter.set_offsets(point_data[frame])
        return scatter,

    # Create and run the animation
    ani = animation.FuncAnimation(fig, update, frames=num_frames, 
                                  interval=25, blit=True)
    plt.show()

if __name__ == '__main__':
    generate_jumping_animation()
