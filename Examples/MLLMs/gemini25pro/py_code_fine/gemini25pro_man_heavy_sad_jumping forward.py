
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_biological_motion_animation():
    """
    Generates and displays a point-light animation of a sad man with heavy weight
    jumping forward.
    """

    # Define joint indices for clarity
    HEAD, NECK = 0, 1
    L_SHOULDER, R_SHOULDER = 2, 3
    L_ELBOW, R_ELBOW = 4, 5
    L_WRIST, R_WRIST = 6, 7
    PELVIS = 8
    L_HIP, R_HIP = 9, 10
    L_KNEE, R_KNEE = 11, 12
    L_ANKLE, R_ANKLE = 13, 14

    def create_pose_from_dict(points_dict):
        """Creates a (15, 2) numpy array from a dictionary of joint positions."""
        pose = np.zeros((15, 2))
        for joint_index, pos in points_dict.items():
            pose[joint_index] = pos
        return pose

    # Define keyframes for the "sad, heavy forward jump"
    # The poses are designed to show a slumped posture, low energy, and effort.
    # An x_offset is used to move the figure forward across the screen.

    # Keyframe 0: Initial sad standing pose
    x_offset = -30
    p0_dict = {
        PELVIS: (0 + x_offset, 0), L_HIP: (-5 + x_offset, -1), R_HIP: (5 + x_offset, -1),
        L_KNEE: (-6 + x_offset, -15), R_KNEE: (6 + x_offset, -15),
        L_ANKLE: (-7 + x_offset, -30), R_ANKLE: (7 + x_offset, -30),
        NECK: (2 + x_offset, 20),
        HEAD: (4 + x_offset, 30),  # Head forward/down
        L_SHOULDER: (-4 + x_offset, 18), R_SHOULDER: (8 + x_offset, 18),  # Shoulders slumped
        L_ELBOW: (-5 + x_offset, 6), R_ELBOW: (9 + x_offset, 6),
        L_WRIST: (-6 + x_offset, -6), R_WRIST: (10 + x_offset, -6)  # Arms hanging low
    }

    # Keyframe 1: Deep crouch, preparing to jump
    x_offset = -25
    p1_dict = {
        PELVIS: (0 + x_offset, -15), L_HIP: (-6 + x_offset, -16), R_HIP: (6 + x_offset, -16),
        L_KNEE: (-10 + x_offset, -25), R_KNEE: (10 + x_offset, -25),
        L_ANKLE: (-7 + x_offset, -30), R_ANKLE: (7 + x_offset, -30),
        NECK: (5 + x_offset, 5),  # Torso leans forward
        HEAD: (8 + x_offset, 15),
        L_SHOULDER: (-2 + x_offset, 3), R_SHOULDER: (12 + x_offset, 3),
        L_ELBOW: (-3 + x_offset, -8), R_ELBOW: (13 + x_offset, -8),
        L_WRIST: (-4 + x_offset, -19), R_WRIST: (14 + x_offset, -19)
    }

    # Keyframe 2: Take-off, pushing off the ground
    x_offset = -20
    p2_dict = {
        PELVIS: (0 + x_offset, -5), L_HIP: (-6 + x_offset, -6), R_HIP: (6 + x_offset, -6),
        L_KNEE: (-2 + x_offset, -18), R_KNEE: (8 + x_offset, -18),
        L_ANKLE: (0 + x_offset, -29), R_ANKLE: (10 + x_offset, -29),  # On toes
        NECK: (4 + x_offset, 15),
        HEAD: (6 + x_offset, 25),
        L_SHOULDER: (-2 + x_offset, 13), R_SHOULDER: (10 + x_offset, 13),
        L_ELBOW: (-4 + x_offset, 1), R_ELBOW: (12 + x_offset, 1),
        L_WRIST: (-6 + x_offset, -10), R_WRIST: (14 + x_offset, -10)
    }

    # Keyframe 3: Peak of the jump, low arc due to "weight"
    x_offset = 10
    p3_dict = {
        PELVIS: (0 + x_offset, 10), L_HIP: (-6 + x_offset, 9), R_HIP: (6 + x_offset, 9),
        L_KNEE: (-5 + x_offset, -3), R_KNEE: (7 + x_offset, -3),  # Legs tucked
        L_ANKLE: (-4 + x_offset, -13), R_ANKLE: (8 + x_offset, -13),
        NECK: (3 + x_offset, 27),
        HEAD: (5 + x_offset, 37),
        L_SHOULDER: (-3 + x_offset, 25), R_SHOULDER: (9 + x_offset, 25),
        L_ELBOW: (-5 + x_offset, 13), R_ELBOW: (11 + x_offset, 13),
        L_WRIST: (-7 + x_offset, 2), R_WRIST: (13 + x_offset, 2)
    }

    # Keyframe 4: Landing impact, absorbing the force
    x_offset = 40
    p4_dict = {
        PELVIS: (0 + x_offset, -14), L_HIP: (-6 + x_offset, -15), R_HIP: (6 + x_offset, -15),
        L_KNEE: (-10 + x_offset, -24), R_KNEE: (10 + x_offset, -24),  # Deep crouch
        L_ANKLE: (-7 + x_offset, -30), R_ANKLE: (7 + x_offset, -30),  # On ground
        NECK: (5 + x_offset, 6),  # Leaning forward
        HEAD: (8 + x_offset, 16),
        L_SHOULDER: (-2 + x_offset, 4), R_SHOULDER: (12 + x_offset, 4),
        L_ELBOW: (-3 + x_offset, -7), R_ELBOW: (13 + x_offset, -7),
        L_WRIST: (-4 + x_offset, -18), R_WRIST: (14 + x_offset, -18)
    }

    # Keyframe 5: Recovered to sad standing pose at the new location
    x_offset = 40
    p5_dict = {
        PELVIS: (0 + x_offset, 0), L_HIP: (-5 + x_offset, -1), R_HIP: (5 + x_offset, -1),
        L_KNEE: (-6 + x_offset, -15), R_KNEE: (6 + x_offset, -15),
        L_ANKLE: (-7 + x_offset, -30), R_ANKLE: (7 + x_offset, -30),
        NECK: (2 + x_offset, 20),
        HEAD: (4 + x_offset, 30),
        L_SHOULDER: (-4 + x_offset, 18), R_SHOULDER: (8 + x_offset, 18),
        L_ELBOW: (-5 + x_offset, 6), R_ELBOW: (9 + x_offset, 6),
        L_WRIST: (-6 + x_offset, -6), R_WRIST: (10 + x_offset, -6)
    }

    keyframes = [
        create_pose_from_dict(p0_dict), create_pose_from_dict(p1_dict),
        create_pose_from_dict(p2_dict), create_pose_from_dict(p3_dict),
        create_pose_from_dict(p4_dict), create_pose_from_dict(p5_dict)
    ]

    # Animation timing parameters
    total_duration_s = 4.0
    fps = 30
    total_frames = int(total_duration_s * fps)
    keyframe_times_norm = np.array([0, 0.25, 0.4, 0.6, 0.8, 1.0])
    keyframe_indices = (keyframe_times_norm * (total_frames - 1)).astype(int)

    def ease_in_out_quad(t):
        """A quadratic easing function for smooth acceleration and deceleration."""
        return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2

    # Interpolate between keyframes to generate all animation frames
    all_frames_data = []
    for i in range(len(keyframe_indices) - 1):
        start_frame_idx = keyframe_indices[i]
        end_frame_idx = keyframe_indices[i+1]
        start_pose = keyframes[i]
        end_pose = keyframes[i+1]
        
        num_frames_in_segment = end_frame_idx - start_frame_idx
        if num_frames_in_segment <= 0:
            continue
            
        for j in range(num_frames_in_segment):
            progress = j / num_frames_in_segment
            eased_progress = ease_in_out_quad(progress)
            current_pose = start_pose * (1 - eased_progress) + end_pose * eased_progress
            all_frames_data.append(current_pose)

    all_frames_data.append(keyframes[-1]) # Ensure the last frame is the final keyframe

    # Add a pause at the end before looping
    pause_frames = int(fps * 1.0) # 1-second pause
    for _ in range(pause_frames):
        all_frames_data.append(keyframes[-1])

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(-50, 60)
    ax.set_ylim(-40, 50)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')

    # The scatter plot object that will be updated each frame
    scatter = ax.scatter([], [], c='white', s=70)

    def init():
        """Initializes the animation plot."""
        scatter.set_offsets(np.empty((0, 2)))
        return scatter,

    def update(frame):
        """Updates the scatter plot for each frame of the animation."""
        scatter.set_offsets(all_frames_data[frame])
        return scatter,

    # Create and run the animation
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=len(all_frames_data),
        init_func=init, 
        blit=True, 
        interval=1000/fps
    )

    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
