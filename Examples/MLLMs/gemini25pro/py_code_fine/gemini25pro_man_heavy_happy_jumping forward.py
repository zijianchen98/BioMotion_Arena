
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import CubicSpline

def create_jumping_animation():
    """
    Generates and displays a point-light animation of a happy man 
    with heavy weight jumping forward.
    The animation consists of 15 white points on a black background,
    representing a biomechanically plausible motion.
    """
    
    # Define the 15 points representing the human figure's joints.
    # The order is:
    # 0: Head, 1: Neck, 2: Pelvis
    # 3: Left Shoulder, 4: Right Shoulder
    # 5: Left Elbow, 6: Right Elbow
    # 7: Left Wrist, 8: Right Wrist
    # 9: Left Hip, 10: Right Hip
    # 11: Left Knee, 12: Right Knee
    # 13: Left Ankle, 14: Right Ankle

    # Define keyframe times and the total number of frames for the animation.
    key_times = [0, 25, 40, 55, 70, 100]
    total_frames = 100

    # Define the (x, y) coordinates for each of the 15 points at each keyframe.
    # The poses are designed to simulate a powerful forward jump while holding a heavy weight.
    keyframes = np.array([
        # Pose 1 (t=0): Initial Stand. The figure is on the left, ready to jump.
        [(-40, 12), (-40, 5), (-40, -15), (-45, 4), (-35, 4), (-48, -5), (-32, -5), 
         (-46, -12), (-34, -12), (-42, -15), (-38, -15), (-43, -25), (-37, -25), 
         (-43, -35), (-37, -35)],
        
        # Pose 2 (t=25): Deep Crouch. The figure crouches to build potential energy.
        [(-33, -1), (-33, -8), (-38, -25), (-38, -9), (-28, -9), (-35, -17), (-29, -17), 
         (-34, -22), (-30, -22), (-40, -25), (-36, -25), (-43, -31), (-33, -31), 
         (-42, -35), (-34, -35)],
        
        # Pose 3 (t=40): Liftoff. Explosive extension propels the figure up and forward.
        [(-16, 17), (-16, 10), (-20, -8), (-22, 9), (-12, 9), (-20, 1), (-14, 1), 
         (-19, -4), (-15, -4), (-22, -8), (-18, -8), (-23, -18), (-17, -18), 
         (-24, -28), (-16, -28)],
        
        # Pose 4 (t=55): Apex. The peak of the jump, with legs tucked.
        [(0, 27), (0, 20), (0, 2), (-5, 19), (5, 19), (-4, 11), (4, 11), 
         (-2, 6), (2, 6), (-2, 2), (2, 2), (-3, -6), (3, -6), 
         (-4, -13), (4, -13)],
        
        # Pose 5 (t=70): Touchdown. The figure lands, absorbing the impact by bending.
        [(26, 4), (26, -3), (20, -20), (20, -4), (30, -4), (23, -12), (29, -12), 
         (24, -17), (28, -17), (18, -20), (22, -20), (20, -28), (28, -28), 
         (22, -35), (30, -35)],
        
        # Pose 6 (t=100): Final Stand. The figure stabilizes after landing on the right side.
        [(25, 12), (25, 5), (25, -15), (20, 4), (30, 4), (17, -5), (33, -5), 
         (19, -12), (31, -12), (23, -15), (27, -15), (22, -25), (28, -25), 
         (22, -35), (28, -35)]
    ])

    # Use cubic spline interpolation to generate smooth trajectories between keyframes.
    animation_times = np.arange(total_frames)
    animated_points = np.zeros((total_frames, 15, 2))

    for point_idx in range(keyframes.shape[1]):
        x_coords = keyframes[:, point_idx, 0]
        y_coords = keyframes[:, point_idx, 1]
        
        cs_x = CubicSpline(key_times, x_coords)
        cs_y = CubicSpline(key_times, y_coords)
        
        animated_points[:, point_idx, 0] = cs_x(animation_times)
        animated_points[:, point_idx, 1] = cs_y(animation_times)

    # Set up the Matplotlib figure and axes for the animation.
    fig, ax = plt.subplots(figsize=(10, 7.5))
    fig.canvas.manager.set_window_title('Jumping Forward Animation')
    fig.set_facecolor('black')
    ax.set_facecolor('black')

    # Configure the axes to be clean and to fit the animation.
    ax.set_xlim(-60, 40)
    ax.set_ylim(-45, 35)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Initialize the scatter plot object for the points.
    points, = ax.plot([], [], 'o', color='white', markersize=8)

    def update(frame):
        """Updates the points' positions for each animation frame."""
        frame_data = animated_points[frame]
        points.set_data(frame_data[:, 0], frame_data[:, 1])
        return points,

    # Create and run the animation.
    ani = FuncAnimation(
        fig=fig, 
        func=update, 
        frames=total_frames, 
        interval=25,  # 40 frames per second
        blit=True
    )

    plt.show()

if __name__ == '__main__':
    create_jumping_animation()
