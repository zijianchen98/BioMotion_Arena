
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.interpolate import CubicSpline

def create_biological_motion_animation():
    """
    Generates and displays a point-light animation of a sad person with light weight
    performing a forward jump.

    The animation consists of 15 white points on a black background, representing
    the major joints of a human body. The motion is designed to be
    biomechanically plausible and smooth.
    """

    # 1. Define Keyframes and Timings for the "Sad Jump Forward"
    # The skeleton is represented by 15 points:
    # 0: Head, 1: Neck, 2: Torso (Sternum)
    # 3: Left Shoulder, 4: Right Shoulder
    # 5: Left Elbow, 6: Right Elbow
    # 7: Left Wrist, 8: Right Wrist
    # 9: Left Hip, 10: Right Hip
    # 11: Left Knee, 12: Right Knee
    # 13: Left Ankle, 14: Right Ankle
    # The motion is viewed from the side profile.

    # Keyframe 0: Initial sad stance (t=0). Character is slumped.
    k0 = np.array([
        [0.00, 0.90], [0.00, 0.75], [0.02, 0.40], [-0.10, 0.65], [0.10, 0.65],
        [-0.12, 0.30], [0.12, 0.30], [-0.14, -0.05], [0.14, -0.05], [-0.10, 0.10],
        [0.10, 0.10], [-0.08, -0.30], [0.12, -0.30], [-0.08, -0.70], [0.12, -0.70]
    ])
    k0[:, 1] -= 0.1  # Lower the overall posture
    k0 += np.array([-1.0, 0.0])  # Starting position on the left

    # Keyframe 1: Deep crouch in preparation for the jump (t=30).
    k1 = np.array([
        [0.10, 0.60], [0.10, 0.45], [0.15, 0.15], [0.00, 0.35], [0.20, 0.35],
        [-0.15, 0.00], [0.05, 0.00], [-0.25, -0.20], [-0.05, -0.20], [-0.10, -0.15],
        [0.10, -0.15], [-0.15, -0.50], [0.15, -0.50], [-0.15, -0.80], [0.15, -0.80]
    ])
    k1 += np.array([-0.9, 0.0])

    # Keyframe 2: Take-off, body extends upwards and forwards (t=40).
    k2 = np.array([
        [0.25, 1.00], [0.20, 0.80], [0.15, 0.40], [0.00, 0.70], [0.30, 0.70],
        [0.20, 0.80], [0.50, 0.80], [0.40, 0.70], [0.70, 0.70], [-0.05, 0.10],
        [0.15, 0.10], [0.00, -0.30], [0.20, -0.30], [0.00, -0.70], [0.20, -0.70]
    ])
    k2 += np.array([-0.7, 0.0])

    # Keyframe 3: Apex of the jump, highest point (t=70).
    k3 = np.array([
        [0.00, 1.00], [0.00, 0.85], [0.00, 0.50], [-0.15, 0.75], [0.15, 0.75],
        [-0.30, 0.45], [0.30, 0.45], [-0.20, 0.15], [0.20, 0.15], [-0.10, 0.20],
        [0.10, 0.20], [-0.15, -0.15], [0.15, -0.15], [-0.10, -0.50], [0.10, -0.50]
    ])
    k3[:, 1] += 0.35  # Vertical lift for a 'light weight' feel
    k3 += np.array([0.0, 0.0])  # Center of the jump arc

    # Keyframe 4: Descending, preparing for landing (t=90).
    k4 = np.array([
        [0.05, 0.70], [0.05, 0.55], [0.10, 0.20], [-0.05, 0.45], [0.25, 0.45],
        [-0.30, 0.40], [0.50, 0.40], [-0.40, 0.10], [0.60, 0.10], [-0.10, -0.10],
        [0.10, -0.10], [-0.20, -0.45], [0.20, -0.45], [-0.30, -0.80], [0.30, -0.80]
    ])
    k4 += np.array([0.7, 0.0])

    # Keyframe 5: Impact absorption, knees and hips flex (t=100).
    k5 = np.array([
        [0.00, 0.60], [0.00, 0.45], [0.05, 0.15], [-0.10, 0.35], [0.15, 0.35],
        [-0.25, 0.20], [0.30, 0.20], [-0.35, -0.05], [0.40, -0.05], [-0.10, -0.15],
        [0.10, -0.15], [-0.15, -0.50], [0.15, -0.50], [-0.15, -0.80], [0.15, -0.80]
    ])
    k5 += np.array([0.8, 0.0])

    # Keyframe 6: Recover to the final sad stance (t=120).
    k6 = np.array([
        [0.00, 0.90], [0.00, 0.75], [0.02, 0.40], [--0.10, 0.65], [0.10, 0.65],
        [-0.12, 0.30], [0.12, 0.30], [-0.14, -0.05], [0.14, -0.05], [-0.10, 0.10],
        [0.10, 0.10], [-0.08, -0.30], [0.12, -0.30], [-0.08, -0.70], [0.12, -0.70]
    ])
    k6[:, 1] -= 0.1
    k6 += np.array([0.9, 0.0]) # Final position on the right

    keyframes = np.array([k0, k1, k2, k3, k4, k5, k6])
    t_keyframes = np.array([0, 30, 40, 70, 90, 100, 120])
    num_frames = 121

    # 2. Interpolate Frames for Smooth Motion
    # Use Cubic Spline interpolation for natural, non-linear movement.
    t_animation = np.linspace(t_keyframes[0], t_keyframes[-1], num_frames)
    interpolated_frames = np.zeros((num_frames, 15, 2))

    for i in range(15):  # For each of the 15 points
        # Interpolate x and y coordinates independently over time
        x_coords = keyframes[:, i, 0]
        y_coords = keyframes[:, i, 1]
        cs_x = CubicSpline(t_keyframes, x_coords)
        cs_y = CubicSpline(t_keyframes, y_coords)
        interpolated_frames[:, i, 0] = cs_x(t_animation)
        interpolated_frames[:, i, 1] = cs_y(t_animation)

    # 3. Set up the Matplotlib Figure and Axes
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    ax.set_aspect('equal', adjustable='box')

    # Determine axis limits dynamically with some padding
    x_min = interpolated_frames[:, :, 0].min() - 0.5
    x_max = interpolated_frames[:, :, 0].max() + 0.5
    y_min = interpolated_frames[:, :, 1].min() - 0.5
    y_max = interpolated_frames[:, :, 1].max() + 0.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    
    # Hide the axes for a clean look
    ax.axis('off')

    # Create the scatter plot object that will be updated each frame
    points, = ax.plot([], [], 'o', color='white', markersize=7)

    # 4. Define Animation Functions
    def init():
        """Initializes the animation plot."""
        points.set_data([], [])
        return points,

    def update(frame):
        """Updates the plot for each frame of the animation."""
        frame_data = interpolated_frames[frame]
        points.set_data(frame_data[:, 0], frame_data[:, 1])
        return points,

    # 5. Create and Display the Animation
    # blit=True optimizes rendering by only redrawing changed parts.
    # interval=20 corresponds to a 50 FPS animation (1000ms / 20ms = 50 FPS).
    ani = animation.FuncAnimation(fig, update, frames=num_frames,
                                  init_func=init, blit=True, interval=20)
    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
