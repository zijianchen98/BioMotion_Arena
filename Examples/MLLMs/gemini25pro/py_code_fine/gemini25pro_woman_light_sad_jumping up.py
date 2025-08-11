
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_biological_motion_animation():
    """
    Generates and displays a point-light animation of a sad, lightweight woman jumping up.
    The animation consists of 15 white points on a black background, representing
    the major joints of the human body.
    """

    # Joint indices for the 15-point model:
    # 0: Head, 1: L_Shoulder, 2: R_Shoulder, 3: Sternum, 4: L_Elbow, 5: R_Elbow,
    # 6: Pelvis, 7: L_Hip, 8: R_Hip, 9: L_Wrist, 10: R_Wrist, 11: L_Knee, 12: R_Knee,
    # 13: L_Ankle, 14: R_Ankle

    def define_keyframes():
        """Defines the key poses for the sad jumping motion."""
        keyframes = {}
        
        # A sad posture is characterized by slumped shoulders, a forward head tilt,
        # and less energetic movements. The jump height is kept modest.

        # Frame 0: Start (sad, slumped stand)
        pose_start = np.array([
            [0.0, 6.0],  # Head
            [-0.7, 5.2], # L_Shoulder
            [0.7, 5.2],  # R_Shoulder
            [0.0, 5.0],  # Sternum
            [-0.9, 4.0], # L_Elbow
            [0.9, 4.0],  # R_Elbow
            [0.0, 3.5],  # Pelvis
            [-0.5, 3.5], # L_Hip
            [0.5, 3.5],  # R_Hip
            [-1.0, 2.8], # L_Wrist
            [1.0, 2.8],  # R_Wrist
            [-0.6, 1.8], # L_Knee
            [0.6, 1.8],  # R_Knee
            [-0.7, 0.1], # L_Ankle
            [0.7, 0.1],  # R_Ankle
        ])
        keyframes[0] = pose_start

        # Frame 20: Crouch (anticipation)
        pose_crouch = np.array([
            [0.3, 4.5],  # Head (leans forward)
            [-0.5, 3.7], # L_Shoulder
            [0.9, 3.7],  # R_Shoulder
            [0.2, 3.5],  # Sternum
            [-0.8, 2.8], # L_Elbow (swings slightly back)
            [1.2, 2.8],  # R_Elbow (swings slightly back)
            [0.0, 2.0],  # Pelvis (lower)
            [-0.5, 2.0], # L_Hip
            [0.5, 2.0],  # R_Hip
            [-1.0, 1.8], # L_Wrist (swings slightly back)
            [1.4, 1.8],  # R_Wrist (swings slightly back)
            [-1.0, 1.0], # L_Knee (bent)
            [1.0, 1.0],  # R_Knee (bent)
            [-0.7, 0.1], # L_Ankle (fixed on ground)
            [0.7, 0.1],  # R_Ankle (fixed on ground)
        ])
        keyframes[20] = pose_crouch

        # Frame 30: Takeoff (legs extended, pushing off)
        pose_takeoff = np.array([
            [0.0, 6.3],  # Head
            [-0.8, 5.5], # L_Shoulder
            [0.8, 5.5],  # R_Shoulder
            [0.0, 5.3],  # Sternum
            [-1.0, 4.5], # L_Elbow
            [1.0, 4.5],  # R_Elbow
            [0.0, 3.8],  # Pelvis
            [-0.5, 3.8], # L_Hip
            [0.5, 3.8],  # R_Hip
            [-1.1, 3.5], # L_Wrist
            [1.1, 3.5],  # R_Wrist
            [-0.6, 2.0], # L_Knee
            [0.6, 2.0],  # R_Knee
            [-0.7, 0.3], # L_Ankle (on toes)
            [0.7, 0.3],  # R_Ankle (on toes)
        ])
        keyframes[30] = pose_takeoff

        # Frame 50: Apex of jump (tucked, sad posture)
        pose_apex = np.array([
            [0.0, 5.0],  # Head (tucked)
            [-0.7, 4.4], # L_Shoulder
            [0.7, 4.4],  # R_Shoulder
            [0.0, 4.2],  # Sternum
            [-1.0, 3.2], # L_Elbow
            [1.0, 3.2],  # R_Elbow
            [0.0, 3.0],  # Pelvis
            [-0.5, 3.0], # L_Hip
            [0.5, 3.0],  # R_Hip
            [-0.8, 2.2], # L_Wrist
            [0.8, 2.2],  # R_Wrist
            [-0.6, 2.0], # L_Knee (tucked)
            [0.6, 2.0],  # R_Knee (tucked)
            [-0.7, 1.0], # L_Ankle (tucked)
            [0.7, 1.0],  # R_Ankle (tucked)
        ])
        keyframes[50] = pose_apex

        # Frame 70: Landing preparation (legs extended to meet ground)
        pose_land_prep = np.array([
            [0.0, 6.3],  # Head
            [-0.8, 5.5], # L_Shoulder
            [0.8, 5.5],  # R_Shoulder
            [0.0, 5.3],  # Sternum
            [-1.5, 4.8], # L_Elbow (out for balance)
            [1.5, 4.8],  # R_Elbow (out for balance)
            [0.0, 3.8],  # Pelvis
            [-0.5, 3.8], # L_Hip
            [0.5, 3.8],  # R_Hip
            [-1.8, 4.0], # L_Wrist (out for balance)
            [1.8, 4.0],  # R_Wrist (out for balance)
            [-0.6, 2.0], # L_Knee (extended down)
            [0.6, 2.0],  # R_Knee (extended down)
            [-0.7, 0.3], # L_Ankle (ready for contact)
            [0.7, 0.3],  # R_Ankle (ready for contact)
        ])
        keyframes[70] = pose_land_prep

        # Frame 80: Landing crouch (absorbing impact)
        pose_land_crouch = np.array([
            [0.3, 4.5],  # Head (leans forward)
            [-0.5, 3.7], # L_Shoulder
            [0.9, 3.7],  # R_Shoulder
            [0.2, 3.5],  # Sternum
            [-0.4, 2.8], # L_Elbow (forward for balance)
            [1.2, 2.8],  # R_Elbow (forward for balance)
            [0.0, 2.0],  # Pelvis (lower)
            [-0.5, 2.0], # L_Hip
            [0.5, 2.0],  # R_Hip
            [-0.2, 2.0], # L_Wrist (forward for balance)
            [1.4, 2.0],  # R_Wrist (forward for balance)
            [-1.0, 1.0], # L_Knee (bent)
            [1.0, 1.0],  # R_Knee (bent)
            [-0.7, 0.1], # L_Ankle (fixed)
            [0.7, 0.1],  # R_Ankle (fixed)
        ])
        keyframes[80] = pose_land_crouch
        
        # Frame 100: End (return to sad, slumped stand)
        keyframes[100] = pose_start.copy()

        return keyframes

    def generate_frames(keyframes, total_frames):
        """Interpolates between keyframes and adds ballistic trajectory."""
        all_coords = np.zeros((total_frames, 15, 2))
        keyframe_indices = sorted(keyframes.keys())

        for i in range(len(keyframe_indices) - 1):
            start_frame_idx = keyframe_indices[i]
            end_frame_idx = keyframe_indices[i+1]
            
            start_pose = keyframes[start_frame_idx]
            end_pose = keyframes[end_frame_idx]
            
            num_inter_frames = end_frame_idx - start_frame_idx
            
            if num_inter_frames == 0: continue

            for frame_offset in range(num_inter_frames):
                current_frame_idx = start_frame_idx + frame_offset
                
                # Use cosine easing for smoother, more natural transitions
                progress = (1 - np.cos(np.pi * frame_offset / num_inter_frames)) / 2
                
                interp_pose = start_pose * (1 - progress) + end_pose * progress
                all_coords[current_frame_idx] = interp_pose
                
        # Ensure the last frame is set correctly
        all_coords[total_frames-1] = keyframes[keyframe_indices[-1]]

        # Add ballistic trajectory (parabolic arc) for the flight phase
        takeoff_frame = 30
        land_frame = 70
        jump_height = 2.0  # A modest jump height
        flight_duration = land_frame - takeoff_frame

        if flight_duration > 0:
            for i in range(flight_duration):
                frame_idx = takeoff_frame + i
                flight_progress = i / flight_duration
                y_offset = jump_height * np.sin(np.pi * flight_progress)
                all_coords[frame_idx, :, 1] += y_offset

        return all_coords

    # --- Animation Setup ---
    TOTAL_FRAMES = 100
    keyframes = define_keyframes()
    motion_data = generate_frames(keyframes, TOTAL_FRAMES)

    # --- Matplotlib Figure Setup ---
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 8)
    fig.set_facecolor('black')
    ax.set_facecolor('black')

    # Set plot limits and aspect ratio for a consistent view
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal', adjustable='box')

    # Hide axes ticks, labels, and spines
    ax.axis('off')

    # Create the scatter plot object for the 15 points
    scatter = ax.scatter(motion_data[0, :, 0], motion_data[0, :, 1], c='white', s=50)

    def init():
        """Initializes the animation plot."""
        scatter.set_offsets(np.empty((15, 2)))
        return scatter,

    def update(frame):
        """Updates the plot for each frame of the animation."""
        scatter.set_offsets(motion_data[frame])
        return scatter,

    # Create and run the animation
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=range(TOTAL_FRAMES), 
        init_func=init, 
        blit=True, 
        interval=50  # 50ms interval for ~20 FPS
    )

    plt.show()


if __name__ == '__main__':
    create_biological_motion_animation()
