
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_animation():
    """
    Generates and displays a point-light animation of a sad man lying down.
    """
    # Point indices for clarity, though not used directly in the code logic:
    # 0:Head, 1:LShoulder, 2:RShoulder, 3:Sternum, 4:LElbow, 5:RElbow,
    # 6:Pelvis, 7:LWrist, 8:RWrist, 9:LHip, 10:RHip, 11:LKnee, 12:RKnee,
    # 13:LAnkle, 14:RAnkle.
    
    # Define the key poses for the animation.
    keyframes = np.array([
        # Keyframe 0: Sad Stand (slumped posture)
        [
            [0.0, 0.5], [-0.2, 0.25], [0.2, 0.25], [0.0, 0.3], [-0.25, -0.05],
            [0.25, -0.05], [0.0, -0.05], [-0.25, -0.35], [0.25, -0.35],
            [-0.15, -0.1], [0.15, -0.1], [-0.1, -0.5], [0.1, -0.5],
            [-0.1, -0.9], [0.1, -0.9]
        ],
        # Keyframe 1: Kneeling down, hands on the floor
        [
            [0.05, 0.0], [-0.2, -0.25], [0.2, -0.25], [0.0, -0.2], [-0.1, -0.6],
            [0.3, -0.6], [0.0, -0.45], [0.0, -0.9], [0.4, -0.9],
            [-0.2, -0.5], [0.2, -0.5], [-0.2, -0.9], [0.2, -0.9],
            [-0.2, -0.7], [0.2, -0.7]
        ],
        # Keyframe 2: Collapsing and lying on the side
        [
            [-0.45, -0.8], [-0.25, -0.9], [-0.25, -0.8], [-0.2, -0.85], [-0.35, -0.9],
            [-0.05, -0.8], [0.2, -0.85], [-0.25, -0.9], [0.05, -0.8],
            [0.15, -0.9], [0.15, -0.8], [-0.05, -0.9], [-0.05, -0.8],
            [-0.25, -0.9], [-0.25, -0.8]
        ]
    ])

    # Animation parameters
    hold_start_duration = 20
    transition_durations = [60, 60]
    hold_end_duration = 40
    
    def ease_in_out_quad(t):
        """A simple easing function for smooth acceleration and deceleration."""
        return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2

    # Generate all frames by interpolating between keyframes
    all_frames = []
    
    # Initial hold
    all_frames.extend([keyframes[0]] * hold_start_duration)

    # Transitions
    for i in range(len(keyframes) - 1):
        start_pose = keyframes[i]
        end_pose = keyframes[i+1]
        duration = transition_durations[i]
        for j in range(duration):
            t = j / (duration - 1)
            eased_t = ease_in_out_quad(t)
            frame = start_pose * (1 - eased_t) + end_pose * eased_t
            all_frames.append(frame)

    # Final hold
    all_frames.extend([keyframes[-1]] * hold_end_duration)
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')

    # Create the scatter plot object
    scatter = ax.scatter(all_frames[0][:, 0], all_frames[0][:, 1], c='white', s=70)

    # Animation update function
    def update(frame_number):
        scatter.set_offsets(all_frames[frame_number])
        return scatter,

    # Create and display the animation
    # interval=33ms -> ~30fps
    ani = animation.FuncAnimation(fig, update, frames=len(all_frames), interval=33, blit=True)
    plt.show()

if __name__ == '__main__':
    create_animation()
