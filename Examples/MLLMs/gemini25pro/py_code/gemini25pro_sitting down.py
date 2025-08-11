
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_sitting_down_animation():
    """
    Generates and displays a point-light animation of a person sitting down.
    """
    # --- Configuration ---
    # Animation settings
    TOTAL_FRAMES = 100
    MOTION_START_FRAME = 10
    MOTION_MID_FRAME = 50
    MOTION_END_FRAME = 80
    INTERVAL = 33  # milliseconds per frame, ~30 fps

    # Visuals
    BG_COLOR = 'black'
    DOT_COLOR = 'white'
    DOT_SIZE = 40
    FIG_SIZE = (5, 8)  # Figure size in inches

    # --- Keyframe Data ---
    # The 15 joints are indexed as follows:
    # 0: Head, 1: Sternum, 2: R Shoulder, 3: R Elbow, 4: R Wrist,
    # 5: L Shoulder, 6: L Elbow, 7: L Wrist, 8: Pelvis, 9: R Hip,
    # 10: R Knee, 11: R Ankle, 12: L Hip, 13: L Knee, 14: L Ankle

    # Start Pose (standing)
    start_pose = np.array([
        [0.0, 10.0],   # Head
        [0.0, 8.0],    # Sternum
        [1.5, 8.0],    # R Shoulder
        [1.5, 5.0],    # R Elbow
        [1.5, 2.0],    # R Wrist
        [-1.5, 8.0],   # L Shoulder
        [-1.5, 5.0],   # L Elbow
        [-1.5, 2.0],   # L Wrist
        [0.0, 2.0],    # Pelvis
        [1.0, 2.0],    # R Hip
        [1.0, -2.0],   # R Knee
        [1.0, -6.0],   # R Ankle
        [-1.0, 2.0],   # L Hip
        [-1.0, -2.0],  # L Knee
        [-1.0, -6.0],  # L Ankle
    ])

    # Intermediate Pose (bending down)
    mid_pose = np.array([
        [-1.0, 7.5],   # Head
        [-2.0, 4.5],   # Sternum (leaning forward)
        [0.0, 5.0],    # R Shoulder
        [2.5, 3.0],    # R Elbow (arms forward for balance)
        [4.0, 1.0],    # R Wrist
        [-4.0, 4.0],   # L Shoulder
        [-6.5, 3.0],   # L Elbow
        [-8.0, 1.0],   # L Wrist
        [-3.0, 0.0],   # Pelvis (moving down and back)
        [-2.0, 0.0],   # R Hip
        [0.5, -3.0],   # R Knee (bending)
        [1.0, -6.0],   # R Ankle (fixed)
        [-4.0, 0.0],   # L Hip
        [-1.5, -3.0],  # L Knee (bending)
        [-1.0, -6.0],  # L Ankle (fixed)
    ])

    # End Pose (seated)
    end_pose = np.array([
        [-4.0, 8.0],   # Head
        [-4.0, 6.0],   # Sternum (upright again)
        [-2.5, 6.0],   # R Shoulder
        [-0.5, 4.0],   # R Elbow (arms resting)
        [1.0, 2.5],    # R Wrist
        [-5.5, 6.0],   # L Shoulder
        [-7.5, 4.0],   # L Elbow
        [-6.0, 2.5],   # L Wrist
        [-4.5, 2.0],   # Pelvis (low and back)
        [-3.5, 2.0],   # R Hip
        [-0.5, 2.0],   # R Knee (thighs horizontal)
        [1.0, -6.0],   # R Ankle (fixed)
        [-5.5, 2.0],   # L Hip
        [-2.5, 2.0],   # L Knee (thighs horizontal)
        [-1.0, -6.0],  # L Ankle (fixed)
    ])

    # --- Data Generation ---

    def ease_in_out_sine(x):
        """Easing function for smooth, natural-looking motion."""
        return -(np.cos(np.pi * x) - 1) / 2

    def generate_frames_data():
        """Interpolates between keyframes to generate all animation frames."""
        all_frames = np.zeros((TOTAL_FRAMES, 15, 2))

        # Phase 1: Stand still for a moment
        all_frames[:MOTION_START_FRAME] = start_pose

        # Phase 2.1: Motion from standing to intermediate pose
        frames_part1 = MOTION_MID_FRAME - MOTION_START_FRAME
        for i in range(frames_part1):
            progress = i / (frames_part1 - 1)
            eased_progress = ease_in_out_sine(progress)
            current_pose = start_pose + (mid_pose - start_pose) * eased_progress
            all_frames[MOTION_START_FRAME + i] = current_pose

        # Phase 2.2: Motion from intermediate to seated pose
        frames_part2 = MOTION_END_FRAME - MOTION_MID_FRAME
        for i in range(frames_part2):
            progress = i / (frames_part2 - 1)
            eased_progress = ease_in_out_sine(progress)
            current_pose = mid_pose + (end_pose - mid_pose) * eased_progress
            all_frames[MOTION_MID_FRAME + i] = current_pose

        # Phase 3: Hold the seated position
        all_frames[MOTION_END_FRAME:] = end_pose
        
        return all_frames

    motion_data = generate_frames_data()

    # --- Animation Setup ---
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Set axes limits to encompass the entire animation
    ax.set_xlim(-12, 6)
    ax.set_ylim(-8, 12)
    ax.set_aspect('equal', adjustable='box')

    # Hide the axes and ticks for a clean look
    ax.axis('off')

    # Initialize the scatter plot with the first frame's data
    scatter = ax.scatter(motion_data[0, :, 0], motion_data[0, :, 1],
                         c=DOT_COLOR, s=DOT_SIZE)

    # --- Animation Function ---
    def update(frame):
        """Updates the positions of the points for each frame."""
        scatter.set_offsets(motion_data[frame])
        return scatter,

    # --- Create and run the animation ---
    ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                                  interval=INTERVAL, blit=True)

    plt.show()

if __name__ == '__main__':
    create_sitting_down_animation()
