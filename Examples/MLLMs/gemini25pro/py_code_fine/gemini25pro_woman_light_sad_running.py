
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_running_animation():
    """
    Generates and displays a point-light animation of a sad woman with light weight running.
    The animation consists of 15 white points on a black background, depicting
    a biomechanically plausible but emotionally dejected running gait.
    """

    # --- Animation and Model Parameters ---

    # General animation settings
    NUM_FRAMES = 120  # Total frames for a smooth loop (2 full cycles)
    CYCLE_FRAMES = 60 # Frames for one complete running cycle
    INTERVAL = 33     # milliseconds per frame (approx 30 FPS)

    # Body proportions (relative units)
    TORSO_LENGTH = 0.55
    SHOULDER_WIDTH = 0.32
    HIP_WIDTH = 0.28
    HEAD_SIZE = 0.15
    UPPER_ARM_LENGTH = 0.26
    LOWER_ARM_LENGTH = 0.24
    THIGH_LENGTH = 0.35
    SHIN_LENGTH = 0.33
    
    # "Sad" motion characteristics
    # A neutral lean is slightly forward. A sad lean is more pronounced.
    LEAN_ANGLE = -np.pi / 16
    # Head droops down relative to the torso's lean
    HEAD_DROOP_ANGLE = -np.pi / 8
    # Shoulders are slumped lower than normal
    SHOULDER_SLUMP = -0.04
    # Vertical bounce is subdued
    VERTICAL_BOUNCE_AMP = 0.02
    # Arm swing is less energetic
    ARM_SWING_AMP = 0.45
    # Leg swing might be slightly less extended
    LEG_SWING_AMP = 0.75
    

    # --- Kinematic Model ---

    def calculate_coordinates(frame):
        """
        Calculates the (x, y) coordinates for all 15 points for a given frame.
        """
        # `t` represents the phase of the running cycle (0 to 2*pi)
        t = 2 * np.pi * frame / CYCLE_FRAMES

        # 1. Central Body Calculation
        # The entire figure moves up and down slightly.
        hip_center_y = 0.9 + VERTICAL_BOUNCE_AMP * np.cos(2 * t)
        hip_center_x = 0

        # Define the main axis of the torso based on the lean
        spine_vec = np.array([TORSO_LENGTH * np.sin(LEAN_ANGLE), 
                              TORSO_LENGTH * np.cos(LEAN_ANGLE)])
        
        # Calculate key points along the spine
        p_hip_center = np.array([hip_center_x, hip_center_y])
        p_neck = p_hip_center + spine_vec
        p_torso_center = p_hip_center + 0.5 * spine_vec
        
        # Calculate head position with added droop
        head_angle = LEAN_ANGLE + HEAD_DROOP_ANGLE
        p_head = p_neck + np.array([HEAD_SIZE * np.sin(head_angle), 
                                    HEAD_SIZE * np.cos(head_angle)])

        # Define a vector perpendicular to the spine for shoulders and hips
        perp_vec = np.array([np.cos(LEAN_ANGLE), -np.sin(LEAN_ANGLE)])

        # 2. Shoulders and Hips
        p_shoulder_r = p_neck + (SHOULDER_WIDTH / 2) * perp_vec + np.array([0, SHOULDER_SLUMP])
        p_shoulder_l = p_neck - (SHOULDER_WIDTH / 2) * perp_vec + np.array([0, SHOULDER_SLUMP])
        p_hip_r = p_hip_center + (HIP_WIDTH / 2) * perp_vec
        p_hip_l = p_hip_center - (HIP_WIDTH / 2) * perp_vec
        
        # 3. Arms (swing in opposition to legs)
        # Right Arm (swings with left leg, phase t + pi)
        arm_phase_r = t + np.pi
        arm_angle_r = LEAN_ANGLE - ARM_SWING_AMP * np.sin(arm_phase_r)
        elbow_bend_r = np.pi / 3 + 0.3 * (np.cos(arm_phase_r) + 1)
        p_elbow_r = p_shoulder_r + np.array([UPPER_ARM_LENGTH * np.sin(arm_angle_r), 
                                             -UPPER_ARM_LENGTH * np.cos(arm_angle_r)])
        p_wrist_r = p_elbow_r + np.array([LOWER_ARM_LENGTH * np.sin(arm_angle_r + elbow_bend_r), 
                                          -LOWER_ARM_LENGTH * np.cos(arm_angle_r + elbow_bend_r)])

        # Left Arm (swings with right leg, phase t)
        arm_phase_l = t
        arm_angle_l = LEAN_ANGLE - ARM_SWING_AMP * np.sin(arm_phase_l)
        elbow_bend_l = np.pi / 3 + 0.3 * (np.cos(arm_phase_l) + 1)
        p_elbow_l = p_shoulder_l + np.array([UPPER_ARM_LENGTH * np.sin(arm_angle_l), 
                                             -UPPER_ARM_LENGTH * np.cos(arm_angle_l)])
        p_wrist_l = p_elbow_l + np.array([LOWER_ARM_LENGTH * np.sin(arm_angle_l + elbow_bend_l), 
                                          -LOWER_ARM_LENGTH * np.cos(arm_angle_l + elbow_bend_l)])
        
        # 4. Legs
        # Right Leg
        leg_phase_r = t
        thigh_angle_r = LEAN_ANGLE + LEG_SWING_AMP * np.sin(leg_phase_r)
        knee_bend_r = 1.1 * (np.cos(leg_phase_r - 0.8) + 1) / 2
        p_knee_r = p_hip_r + np.array([THIGH_LENGTH * np.sin(thigh_angle_r), 
                                       -THIGH_LENGTH * np.cos(thigh_angle_r)])
        p_ankle_r = p_knee_r + np.array([SHIN_LENGTH * np.sin(thigh_angle_r + knee_bend_r), 
                                         -SHIN_LENGTH * np.cos(thigh_angle_r + knee_bend_r)])

        # Left Leg
        leg_phase_l = t + np.pi
        thigh_angle_l = LEAN_ANGLE + LEG_SWING_AMP * np.sin(leg_phase_l)
        knee_bend_l = 1.1 * (np.cos(leg_phase_l - 0.8) + 1) / 2
        p_knee_l = p_hip_l + np.array([THIGH_LENGTH * np.sin(thigh_angle_l), 
                                       -THIGH_LENGTH * np.cos(thigh_angle_l)])
        p_ankle_l = p_knee_l + np.array([SHIN_LENGTH * np.sin(thigh_angle_l + knee_bend_l), 
                                         -SHIN_LENGTH * np.cos(thigh_angle_l + knee_bend_l)])

        # 5. Assemble all 15 points
        # Order: Head, Torso (x3), Shoulders (x2), Hips (x2), Arms (x4), Legs (x4)
        all_points = np.array([
            p_head, p_neck, p_torso_center,
            p_shoulder_l, p_shoulder_r,
            p_hip_l, p_hip_r,
            p_elbow_l, p_elbow_r,
            p_wrist_l, p_wrist_r,
            p_knee_l, p_knee_r,
            p_ankle_l, p_ankle_r
        ])
        
        # The model defines hips and shoulders relative to the spine.
        # A slight rocking motion of shoulders vs hips adds realism.
        # Let's add a subtle counter-rotation based on the leg phase.
        rocking_angle = 0.05 * np.sin(t)
        # Rotate shoulders one way
        rot_matrix_shoulders = np.array([[np.cos(rocking_angle), -np.sin(rocking_angle)],
                                         [np.sin(rocking_angle), np.cos(rocking_angle)]])
        # Rotate hips the other way
        rot_matrix_hips = np.array([[np.cos(-rocking_angle), -np.sin(-rocking_angle)],
                                    [np.sin(-rocking_angle), np.cos(-rocking_angle)]])
        
        # This part is complex to add post-hoc. The existing model is sufficient.
        # The core kinematics already capture the necessary movements.

        return all_points

    # --- Matplotlib Setup ---
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 8)
    ax.set_facecolor('black')

    # Set axis limits to keep the figure centered and scaled
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.2, 2.0)
    ax.set_aspect('equal', adjustable='box')

    # Remove all axis decorations
    ax.axis('off')
    plt.tight_layout()
    
    # Initialize the plot element (the 15 points)
    # We start with empty data, which will be filled by the animation function.
    points_plot, = ax.plot([], [], 'o', color='white', markersize=8)

    # --- Animation Functions ---

    def init():
        """Initializes the animation plot."""
        points_plot.set_data([], [])
        return (points_plot,)

    def animate(frame):
        """
        This function is called for each frame of the animation.
        It calculates the new coordinates and updates the plot.
        """
        # Calculate coordinates for the current frame
        coords = calculate_coordinates(frame)
        
        # Update the data of the plot
        points_plot.set_data(coords[:, 0], coords[:, 1])
        
        return (points_plot,)

    # --- Create and run the animation ---
    
    # Create the FuncAnimation object
    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=NUM_FRAMES,
        init_func=init,
        interval=INTERVAL,
        blit=True
    )

    # Display the animation
    plt.show()

if __name__ == '__main__':
    generate_sad_running_animation()
