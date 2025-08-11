
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_biological_motion_animation():
    """
    Generates and displays a point-light stimulus animation of a heavy woman lying down.
    The animation consists of 15 white points on a black background, depicting a
    biomechanically plausible motion.
    """

    # --- Animation Setup ---
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-2, 11)
    ax.set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)

    points, = ax.plot([], [], 'o', color='white', markersize=6)

    # --- Keyframe Poses ---
    # Define the coordinates for the 15 joints at critical points in the motion.
    # The figure is depicted as if viewed from the side, facing right.

    # Pose 1: Standing upright
    pose_stand = {
        'head': np.array([0, 9]), 'sternum': np.array([0, 7.5]), 'pelvis': np.array([0, 5]),
        'l_shoulder': np.array([-0.2, 7.5]), 'r_shoulder': np.array([0.2, 7.5]),
        'l_elbow': np.array([-0.2, 6]), 'r_elbow': np.array([0.2, 6]),
        'l_wrist': np.array([-0.2, 4.5]), 'r_wrist': np.array([0.2, 4.5]),
        'l_hip': np.array([-0.5, 5]), 'r_hip': np.array([0.5, 5]),
        'l_knee': np.array([-0.5, 2.5]), 'r_knee': np.array([0.5, 2.5]),
        'l_ankle': np.array([-0.5, 0]), 'r_ankle': np.array([0.5, 0])
    }
    joint_order = list(pose_stand.keys())

    # Pose 2: Deep squat, preparing to sit
    pose_squat = {
        'head': np.array([0.5, 5.5]), 'sternum': np.array([0.5, 4]), 'pelvis': np.array([-1, 2]),
        'l_shoulder': np.array([0.3, 4]), 'r_shoulder': np.array([0.7, 4]),
        'l_elbow': np.array([-1.5, 2.5]), 'r_elbow': np.array([-1.0, 2.5]),
        'l_wrist': np.array([-3.0, 1.0]), 'r_wrist': np.array([-2.5, 1.0]),
        'l_hip': np.array([-1.5, 2]), 'r_hip': np.array([-0.5, 2]),
        'l_knee': np.array([-0.5, 1]), 'r_knee': np.array([0.5, 1]),
        'l_ankle': np.array([-0.5, 0]), 'r_ankle': np.array([0.5, 0])
    }

    # Pose 3: Seated, supported by arms, leaning back
    pose_sit = {
        'head': np.array([-0.5, 4]), 'sternum': np.array([-1, 2.5]), 'pelvis': np.array([-2.5, 0.5]),
        'l_shoulder': np.array([-1.2, 2.5]), 'r_shoulder': np.array([-0.8, 2.5]),
        'l_elbow': np.array([-2.7, 1.25]), 'r_elbow': np.array([-2.3, 1.25]),
        'l_wrist': np.array([-4.0, 0]), 'r_wrist': np.array([-3.5, 0]),
        'l_hip': np.array([-3.0, 0.5]), 'r_hip': np.array([-2.0, 0.5]),
        'l_knee': np.array([-1.0, 1.5]), 'r_knee': np.array([0.0, 1.5]),
        'l_ankle': np.array([1.0, 0]), 'r_ankle': np.array([2.0, 0])
    }

    # Pose 4: Lying down flat
    pose_lie_down = {
        'head': np.array([2.0, 0.5]), 'sternum': np.array([0, 0.5]), 'pelvis': np.array([-2.5, 0.5]),
        'l_shoulder': np.array([-0.2, 0.5]), 'r_shoulder': np.array([0.2, 0.5]),
        'l_elbow': np.array([-1.2, 0.2]), 'r_elbow': np.array([1.2, 0.2]),
        'l_wrist': np.array([-1.7, 0.5]), 'r_wrist': np.array([1.7, 0.5]),
        'l_hip': np.array([-3.0, 0.5]), 'r_hip': np.array([-2.0, 0.5]),
        'l_knee': np.array([-2.5, 1.0]), 'r_knee': np.array([-1.5, 1.0]),
        'l_ankle': np.array([-1.5, 0]), 'r_ankle': np.array([-0.5, 0])
    }


    # --- Animation Logic ---
    def ease_in_out(t):
        """A simple easing function for smooth acceleration and deceleration."""
        return t * t * (3.0 - 2.0 * t)

    def interpolate_poses(pose1, pose2, t):
        """Linearly interpolates between two poses based on a factor t."""
        interpolated_pose = {}
        for joint in joint_order:
            interpolated_pose[joint] = pose1[joint] * (1 - t) + pose2[joint] * t
        return interpolated_pose

    def animate(frame):
        """Calculates the positions of the points for each frame."""
        num_frames = 150
        phase1_end = 50
        phase2_end = 100

        if frame < phase1_end:
            # Phase 1: Standing to Squatting
            t = frame / phase1_end
            t_eased = ease_in_out(t)
            current_pose = interpolate_poses(pose_stand, pose_squat, t_eased)
        elif frame < phase2_end:
            # Phase 2: Squatting to Sitting
            t = (frame - phase1_end) / (phase2_end - phase1_end)
            t_eased = ease_in_out(t)
            current_pose = interpolate_poses(pose_squat, pose_sit, t_eased)
        else:
            # Phase 3: Sitting to Lying Down
            t = (frame - phase2_end) / (num_frames - phase2_end)
            t_eased = ease_in_out(t)
            current_pose = interpolate_poses(pose_sit, pose_lie_down, t_eased)

        # Update the plot data
        coords = np.array([current_pose[joint] for joint in joint_order])
        points.set_data(coords[:, 0], coords[:, 1])
        return points,

    # --- Run Animation ---
    # Total frames = 151 to include the final pose
    ani = animation.FuncAnimation(fig, animate, frames=151, interval=33, blit=True)
    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
