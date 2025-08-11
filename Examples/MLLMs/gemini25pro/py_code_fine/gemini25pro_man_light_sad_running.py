
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_running_animation():
    """
    Creates and displays a point-light animation of a sad, light-weight person running.
    The animation consists of 15 white points on a black background, representing
    major body joints and segments, moving in a biomechanically plausible manner.
    """

    # --- Configuration ---
    # General animation settings
    N_FRAMES = 120  # Number of frames for one smooth gait cycle
    FPS = 33
    INTERVAL = 1000 / FPS

    # Visual style settings
    FIG_SIZE = (6, 8)
    BG_COLOR = 'black'
    DOT_COLOR = 'white'
    DOT_SIZE = 35

    # Biomechanical model parameters (relative body part lengths)
    TORSO_LENGTH = 1.9
    NECK_LENGTH = 0.4
    SHOULDER_WIDTH = 1.6
    HIP_WIDTH = 1.2
    UPPER_ARM_LENGTH = 1.4
    FOREARM_LENGTH = 1.2
    UPPER_LEG_LENGTH = 2.0
    LOWER_LEG_LENGTH = 1.9

    def get_point_light_data(num_frames):
        """
        Generates 2D coordinates for 15 joints over a running cycle.
        The motion is styled to represent a "sad, light-weight run".

        The 15 points represent:
        - Midline: Hips_Center, Spine, Head
        - Arms (x2): Shoulder, Elbow, Wrist
        - Legs (x2): Hip, Knee, Ankle
        """
        # Time array for one full cycle (0 to 2*pi)
        t = np.linspace(0, 2 * np.pi, num_frames, endpoint=False)
        
        # Data array: (frames, joints, xy-coords)
        data = np.zeros((num_frames, 15, 2))

        # --- Motion Parameters to convey emotion and weight ---
        # "Sad" posture: slumped forward, head down
        torso_lean = -0.3
        head_tilt = torso_lean - 0.7

        # "Sad" motion: reduced, heavy-feeling arm swing
        arm_swing_amplitude = 0.5

        # "Light weight" motion: less vertical displacement (smoother run)
        vertical_bob_amplitude = 0.1

        # --- Base Torso and Head Motion ---
        # Joint 0: Hips_Center (the root of the model)
        data[:, 0, 1] = -vertical_bob_amplitude * np.cos(2 * t)
        
        # Joint 1: Spine (between shoulders)
        data[:, 1, 0] = data[:, 0, 0] + TORSO_LENGTH * np.sin(torso_lean)
        data[:, 1, 1] = data[:, 0, 1] + TORSO_LENGTH * np.cos(torso_lean)

        # Joint 2: Head
        data[:, 2, 0] = data[:, 1, 0] + NECK_LENGTH * np.sin(head_tilt)
        data[:, 2, 1] = data[:, 1, 1] + NECK_LENGTH * np.cos(head_tilt)

        # --- Limb Angle Calculations ---
        # Angles are relative to the vertical axis.
        # Right leg leads (phase=0), left leg is opposite (phase=pi).
        # Arms swing opposite to their corresponding legs.
        
        # Leg angles
        l_hip_angle = torso_lean + 1.1 * np.sin(t + np.pi)
        r_hip_angle = torso_lean + 1.1 * np.sin(t)
        l_knee_angle = 0.85 - 0.85 * np.cos(t + np.pi)
        r_knee_angle = 0.85 - 0.85 * np.cos(t)

        # Arm angles
        l_shoulder_angle = torso_lean + arm_swing_amplitude * np.sin(t)
        r_shoulder_angle = torso_lean + arm_swing_amplitude * np.sin(t + np.pi)
        l_elbow_angle = 0.7 + 0.6 * np.sin(t + np.pi/4)
        r_elbow_angle = 0.7 + 0.6 * np.sin(t + np.pi + np.pi/4)

        # --- Forward Kinematics to calculate all joint positions ---
        
        # Joints 3 & 4: L/R Shoulder anchors
        data[:, 3, 0] = data[:, 1, 0] - (SHOULDER_WIDTH / 2) * np.cos(torso_lean)
        data[:, 3, 1] = data[:, 1, 1] + (SHOULDER_WIDTH / 2) * np.sin(torso_lean)
        data[:, 4, 0] = data[:, 1, 0] + (SHOULDER_WIDTH / 2) * np.cos(torso_lean)
        data[:, 4, 1] = data[:, 1, 1] - (SHOULDER_WIDTH / 2) * np.sin(torso_lean)
        
        # Joints 5 & 6: L/R Hip anchors
        data[:, 5, 0] = data[:, 0, 0] - (HIP_WIDTH / 2) * np.cos(torso_lean)
        data[:, 5, 1] = data[:, 0, 1] + (HIP_WIDTH / 2) * np.sin(torso_lean)
        data[:, 6, 0] = data[:, 0, 0] + (HIP_WIDTH / 2) * np.cos(torso_lean)
        data[:, 6, 1] = data[:, 0, 1] - (HIP_WIDTH / 2) * np.sin(torso_lean)

        # Joints 7 & 8: L/R Elbow
        data[:, 7, 0] = data[:, 3, 0] + UPPER_ARM_LENGTH * np.sin(l_shoulder_angle)
        data[:, 7, 1] = data[:, 3, 1] - UPPER_ARM_LENGTH * np.cos(l_shoulder_angle)
        data[:, 8, 0] = data[:, 4, 0] + UPPER_ARM_LENGTH * np.sin(r_shoulder_angle)
        data[:, 8, 1] = data[:, 4, 1] - UPPER_ARM_LENGTH * np.cos(r_shoulder_angle)
        
        # Joints 9 & 10: L/R Wrist
        data[:, 9, 0] = data[:, 7, 0] + FOREARM_LENGTH * np.sin(l_shoulder_angle + l_elbow_angle)
        data[:, 9, 1] = data[:, 7, 1] - FOREARM_LENGTH * np.cos(l_shoulder_angle + l_elbow_angle)
        data[:, 10, 0] = data[:, 8, 0] + FOREARM_LENGTH * np.sin(r_shoulder_angle + r_elbow_angle)
        data[:, 10, 1] = data[:, 8, 1] - FOREARM_LENGTH * np.cos(r_shoulder_angle + r_elbow_angle)
        
        # Joints 11 & 12: L/R Knee
        data[:, 11, 0] = data[:, 5, 0] + UPPER_LEG_LENGTH * np.sin(l_hip_angle)
        data[:, 11, 1] = data[:, 5, 1] - UPPER_LEG_LENGTH * np.cos(l_hip_angle)
        data[:, 12, 0] = data[:, 6, 0] + UPPER_LEG_LENGTH * np.sin(r_hip_angle)
        data[:, 12, 1] = data[:, 6, 1] - UPPER_LEG_LENGTH * np.cos(r_hip_angle)

        # Joints 13 & 14: L/R Ankle
        data[:, 13, 0] = data[:, 11, 0] + LOWER_LEG_LENGTH * np.sin(l_hip_angle + l_knee_angle)
        data[:, 13, 1] = data[:, 11, 1] - LOWER_LEG_LENGTH * np.cos(l_hip_angle + l_knee_angle)
        data[:, 14, 0] = data[:, 12, 0] + LOWER_LEG_LENGTH * np.sin(r_hip_angle + r_knee_angle)
        data[:, 14, 1] = data[:, 12, 1] - LOWER_LEG_LENGTH * np.cos(r_hip_angle + r_knee_angle)

        return data

    # --- Animation Setup ---
    motion_data = get_point_light_data(N_FRAMES)
    
    fig = plt.figure(figsize=FIG_SIZE, facecolor=BG_COLOR)
    ax = fig.add_subplot(111)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 4)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    scatter = ax.scatter([], [], c=DOT_COLOR, s=DOT_SIZE)

    def init():
        scatter.set_offsets(np.empty((0, 2)))
        return scatter,

    def update(frame):
        offsets = motion_data[frame]
        scatter.set_offsets(offsets)
        return scatter,

    _ = animation.FuncAnimation(
        fig, update, frames=N_FRAMES, init_func=init, blit=True, interval=INTERVAL
    )
    
    plt.show()

if __name__ == '__main__':
    create_running_animation()
