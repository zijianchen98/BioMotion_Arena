
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_biological_motion_animation():
    """
    Generates and displays a point-light stimulus animation of a person lying down.
    The animation consists of 15 white points on a black background, depicting
    a biomechanically plausible motion.
    """
    # Define the 15 joint positions for each keyframe of the "lying down" action.
    # Each keyframe is a (15, 2) numpy array representing the (x, y) coordinates
    # of the 15 points.
    # The points represent:
    # 0: Head, 1: Neck, 2: L Shoulder, 3: R Shoulder, 4: L Elbow, 5: R Elbow,
    # 6: L Wrist, 7: R Wrist, 8: Pelvis, 9: L Hip, 10: R Hip, 11: L Knee,
    # 12: R Knee, 13: L Ankle, 14: R Ankle
    
    keyframes = [
        # Keyframe 0: Standing upright
        np.array([
            [50, 95], [50, 85], [42, 83], [58, 83], [38, 70], [62, 70],
            [34, 57], [66, 57], [50, 55], [44, 54], [56, 54], [42, 35],
            [58, 35], [40, 15], [60, 15]
        ]),
        # Keyframe 1: Crouching down
        np.array([
            [50, 75], [50, 67], [42, 65], [58, 65], [38, 52], [62, 52],
            [34, 39], [66, 39], [50, 37], [44, 36], [56, 36], [42, 25],
            [58, 25], [40, 15], [60, 15]
        ]),
        # Keyframe 2: Leaning to the side, placing one hand on the ground
        np.array([
            [40, 65], [40, 57], [35, 55], [45, 55], [30, 40], [50, 48],
            [25, 20], [55, 40], [40, 30], [35, 29], [45, 29], [38, 22],
            [50, 25], [40, 15], [55, 15]
        ]),
        # Keyframe 3: Hip makes contact with the ground
        np.array([
            [35, 50], [38, 42], [35, 40], [45, 42], [28, 28], [53, 35],
            [25, 20], [58, 30], [40, 20], [35, 18], [45, 22], [50, 18],
            [55, 25], [65, 18], [65, 25]
        ]),
        # Keyframe 4: Final pose, lying on the side
        np.array([
            [20, 25], [30, 25], [35, 22], [35, 28], [45, 20], [45, 30],
            [55, 22], [55, 28], [50, 25], [55, 22], [55, 28], [70, 20],
            [70, 30], [85, 18], [85, 32]
        ])
    ]

    # Animation parameters
    frames_per_transition = 25
    total_frames = (len(keyframes) - 1) * frames_per_transition

    # Interpolate between keyframes to generate all frames for the animation
    motion_data = np.zeros((total_frames, 15, 2))
    for i in range(len(keyframes) - 1):
        start_pose = keyframes[i]
        end_pose = keyframes[i + 1]
        for frame_num in range(frames_per_transition):
            # Calculate interpolation factor (t)
            t = frame_num / float(frames_per_transition)
            
            # Linear interpolation for each point
            current_pose = start_pose * (1 - t) + end_pose * t
            
            # Store the calculated pose
            motion_data[i * frames_per_transition + frame_num] = current_pose

    # Set up the figure and axis for the animation
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Set plot limits to encompass the entire motion with some padding
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 105)
    
    # Hide the axes and ticks for a clean look
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ensure aspect ratio is equal to prevent distortion
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()

    # Initialize the scatter plot with the first frame's data
    scatter = ax.scatter(motion_data[0, :, 0], motion_data[0, :, 1], c='white', s=70)

    def update(frame):
        """
        Update function for the animation. Sets the positions of the points for each frame.
        """
        scatter.set_offsets(motion_data[frame])
        return scatter,

    # Create the animation object
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=total_frames,
        interval=40,  # Interval between frames in milliseconds (for ~25 fps)
        blit=True,
        repeat=True
    )

    # Display the animation
    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
