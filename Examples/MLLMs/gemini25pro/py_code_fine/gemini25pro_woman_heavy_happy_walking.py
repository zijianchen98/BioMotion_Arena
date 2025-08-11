
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_heavy_happy_walk_data():
    """
    Generates coordinate data for 15 point-lights to animate a walking motion.
    The style of walking is designed to represent a "happy woman with heavy weight".
    This is achieved by combining parameters for a wider stance, increased lateral
    sway, and reduced vertical bob (heavy) with a subtle, higher-frequency
    vertical bounce and head nod (happy).

    Returns:
        A NumPy array of shape (num_frames, 15, 2) with the xy coordinates
        for each point in each frame.
    """
    NUM_FRAMES = 120

    # Body proportions are set to represent a heavier build with wider shoulders and hips.
    PROPS = {
        "torso_len": 60,
        "head_rad": 25,
        "shoulder_w": 60,
        "hip_w": 40,
        "u_arm_len": 45,
        "l_arm_len": 40,
        "u_leg_len": 55,
        "l_leg_len": 50,
    }

    # Motion parameters are tuned to create the specific walking style.
    PARAMS = {
        "sway_amp": 18,           # Increased lateral sway for a heavy feel
        "bob_amp": 3,             # Reduced main vertical bob
        "happy_bounce_amp": 2,    # Added high-frequency bounce for "happy"
        "head_nod_amp": 3,        # Subtle head nod for "happy"
        "shoulder_sway_amp": 8,   # Upper body counter-sway
        "leg_lift_amp": -7,       # Hip drop during swing phase
        "thigh_angle_amp": 0.45,  # Gait angle
        "knee_flex_amp": 1.3,     # Knee bend during leg swing
        "arm_angle_amp": 0.35,    # Arm swing magnitude
        "elbow_flex": 0.6,        # Constant elbow bend
    }

    # Point-light indices for joint identification
    p_map = {
        'head': 0, 'sternum': 1, 'pelvis': 2, 'l_shoulder': 3, 'l_elbow': 4,
        'l_wrist': 5, 'r_shoulder': 6, 'r_elbow': 7, 'r_wrist': 8, 'l_hip': 9,
        'l_knee': 10, 'l_ankle': 11, 'r_hip': 12, 'r_knee': 13, 'r_ankle': 14
    }

    data = np.zeros((NUM_FRAMES, 15, 2))
    t = np.linspace(0, 2 * np.pi, NUM_FRAMES, endpoint=False)

    # --- Core Body Motion ---
    pelvis_x = PARAMS["sway_amp"] * np.sin(t)
    pelvis_y = PARAMS["bob_amp"] * np.cos(2 * t) + PARAMS["happy_bounce_amp"] * np.cos(4 * t)
    data[:, p_map['pelvis']] = np.stack([pelvis_x, pelvis_y], axis=1)

    sternum_x = pelvis_x - PARAMS["shoulder_sway_amp"] * np.sin(t)
    sternum_y = pelvis_y + PROPS["torso_len"]
    data[:, p_map['sternum']] = np.stack([sternum_x, sternum_y], axis=1)

    head_y = sternum_y + PROPS["head_rad"] + PARAMS["head_nod_amp"] * np.cos(2 * t)
    data[:, p_map['head']] = np.stack([sternum_x, head_y], axis=1)

    # --- Shoulders and Hips ---
    data[:, p_map['r_shoulder'], 0] = sternum_x + PROPS["shoulder_w"] / 2
    data[:, p_map['l_shoulder'], 0] = sternum_x - PROPS["shoulder_w"] / 2
    data[:, [p_map['r_shoulder'], p_map['l_shoulder']], 1] = sternum_y - 2

    data[:, p_map['r_hip'], 0] = pelvis_x + PROPS["hip_w"] / 2
    data[:, p_map['l_hip'], 0] = pelvis_x - PROPS["hip_w"] / 2
    data[:, p_map['r_hip'], 1] = pelvis_y + PARAMS["leg_lift_amp"] * np.cos(t + np.pi / 2)
    data[:, p_map['l_hip'], 1] = pelvis_y + PARAMS["leg_lift_amp"] * np.cos(t - np.pi / 2)

    # --- Right Leg Motion ---
    thigh_angle_r = PARAMS["thigh_angle_amp"] * np.sin(t)
    knee_flex_r = PARAMS["knee_flex_amp"] * np.maximum(0, np.sin(t))
    data[:, p_map['r_knee'], 0] = data[:, p_map['r_hip'], 0] + PROPS["u_leg_len"] * np.sin(thigh_angle_r)
    data[:, p_map['r_knee'], 1] = data[:, p_map['r_hip'], 1] - PROPS["u_leg_len"] * np.cos(thigh_angle_r)
    data[:, p_map['r_ankle'], 0] = data[:, p_map['r_knee'], 0] + PROPS["l_leg_len"] * np.sin(thigh_angle_r - knee_flex_r)
    data[:, p_map['r_ankle'], 1] = data[:, p_map['r_knee'], 1] - PROPS["l_leg_len"] * np.cos(thigh_angle_r - knee_flex_r)

    # --- Left Leg Motion (phase-shifted) ---
    thigh_angle_l = PARAMS["thigh_angle_amp"] * np.sin(t + np.pi)
    knee_flex_l = PARAMS["knee_flex_amp"] * np.maximum(0, np.sin(t + np.pi))
    data[:, p_map['l_knee'], 0] = data[:, p_map['l_hip'], 0] + PROPS["u_leg_len"] * np.sin(thigh_angle_l)
    data[:, p_map['l_knee'], 1] = data[:, p_map['l_hip'], 1] - PROPS["u_leg_len"] * np.cos(thigh_angle_l)
    data[:, p_map['l_ankle'], 0] = data[:, p_map['l_knee'], 0] + PROPS["l_leg_len"] * np.sin(thigh_angle_l - knee_flex_l)
    data[:, p_map['l_ankle'], 1] = data[:, p_map['l_knee'], 1] - PROPS["l_leg_len"] * np.cos(thigh_angle_l - knee_flex_l)

    # --- Right Arm Motion (opposition to right leg) ---
    arm_angle_r = PARAMS["arm_angle_amp"] * np.sin(t + np.pi)
    data[:, p_map['r_elbow'], 0] = data[:, p_map['r_shoulder'], 0] + PROPS["u_arm_len"] * np.sin(arm_angle_r)
    data[:, p_map['r_elbow'], 1] = data[:, p_map['r_shoulder'], 1] - PROPS["u_arm_len"] * np.cos(arm_angle_r)
    data[:, p_map['r_wrist'], 0] = data[:, p_map['r_elbow'], 0] + PROPS["l_arm_len"] * np.sin(arm_angle_r - PARAMS["elbow_flex"])
    data[:, p_map['r_wrist'], 1] = data[:, p_map['r_elbow'], 1] - PROPS["l_arm_len"] * np.cos(arm_angle_r - PARAMS["elbow_flex"])

    # --- Left Arm Motion (opposition to left leg) ---
    arm_angle_l = PARAMS["arm_angle_amp"] * np.sin(t)
    data[:, p_map['l_elbow'], 0] = data[:, p_map['l_shoulder'], 0] + PROPS["u_arm_len"] * np.sin(arm_angle_l)
    data[:, p_map['l_elbow'], 1] = data[:, p_map['l_shoulder'], 1] - PROPS["u_arm_len"] * np.cos(arm_angle_l)
    data[:, p_map['l_wrist'], 0] = data[:, p_map['l_elbow'], 0] + PROPS["l_arm_len"] * np.sin(arm_angle_l - PARAMS["elbow_flex"])
    data[:, p_map['l_wrist'], 1] = data[:, p_map['l_elbow'], 1] - PROPS["l_arm_len"] * np.cos(arm_angle_l - PARAMS["elbow_flex"])

    # Center the entire figure vertically in the frame
    y_center = (data[:, :, 1].max() + data[:, :, 1].min()) / 2
    data[:, :, 1] -= y_center

    return data

def main():
    """
    Sets up the matplotlib figure and runs the animation.
    """
    motion_data = generate_heavy_happy_walk_data()
    num_frames = motion_data.shape[0]

    fig, ax = plt.subplots(figsize=(5, 8))
    fig.set_facecolor('black')
    ax.set_facecolor('black')

    ax.set_xlim(-110, 110)
    ax.set_ylim(-110, 110)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    scatter = ax.scatter(
        motion_data[0, :, 0],
        motion_data[0, :, 1],
        c='white',
        s=80  # Marker size
    )

    def update(frame):
        """Animation update function."""
        scatter.set_offsets(motion_data[frame])
        return scatter,

    ani = animation.FuncAnimation(
        fig=fig,
        func=update,
        frames=num_frames,
        interval=30,  # Milliseconds between frames
        blit=True
    )

    plt.show()

if __name__ == '__main__':
    main()
