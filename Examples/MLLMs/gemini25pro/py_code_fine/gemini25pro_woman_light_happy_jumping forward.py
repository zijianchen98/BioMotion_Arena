
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_data(num_frames=100):
    """
    Generates the keypoint data for a forward jump animation.
    The motion is designed to be energetic and light, representing a happy person 
    with light weight jumping forward.
    Returns a numpy array of shape (num_frames, 15, 2).
    """
    data = np.zeros((num_frames, 15, 2))

    # Define indices for the 15 joints for clarity
    HEAD, L_SHOULDER, R_SHOULDER, L_ELBOW, R_ELBOW, L_WRIST, R_WRIST, \
    L_HIP, R_HIP, L_KNEE, R_KNEE, L_ANKLE, R_ANKLE, STERNUM, PELVIS = range(15)

    # --- Biomechanical Parameters ---
    # Proportions of the body model
    PELVIS_STERNUM_DY = 0.28
    STERNUM_HEAD_DY = 0.32
    SHOULDER_WIDTH = 0.35
    HIP_WIDTH = 0.22
    UPPER_ARM_LEN = 0.26
    LOWER_ARM_LEN = 0.24
    THIGH_LEN = 0.42
    CALF_LEN = 0.40

    # Dynamics of the jump
    total_jump_dist = 2.5
    jump_height = 0.7
    crouch_depth = 0.25

    # Timing of the jump phases (as fractions of total frames)
    crouch_end_f = 20 / num_frames
    takeoff_f = 30 / num_frames
    flight_end_f = 65 / num_frames
    land_absorb_end_f = 75 / num_frames

    # --- Frame-by-Frame Generation Loop ---
    for i in range(num_frames):
        t = i / (num_frames - 1)  # Normalized time [0, 1]

        # 1. Pelvis Trajectory (Root of the hierarchy)
        # The pelvis defines the overall position and trajectory of the body.
        pelvis_x = total_jump_dist * t
        pelvis_y = 0.0
        if t <= crouch_end_f:  # Crouching down in anticipation
            progress = t / crouch_end_f
            pelvis_y = -crouch_depth * 0.5 * (1 - np.cos(np.pi * progress))
        elif t <= takeoff_f:  # Pushing off the ground
            progress = (t - crouch_end_f) / (takeoff_f - crouch_end_f)
            pelvis_y = -crouch_depth * (1 - progress)
        elif t <= flight_end_f:  # Airborne phase
            progress = (t - takeoff_f) / (flight_end_f - takeoff_f)
            pelvis_y = jump_height * np.sin(np.pi * progress)
        elif t <= land_absorb_end_f:  # Landing and absorbing impact
            progress = (t - flight_end_f) / (land_absorb_end_f - flight_end_f)
            pelvis_y = -crouch_depth * 0.5 * (1 - np.cos(np.pi * progress))
        else:  # Recovering to a standing position
            progress = (t - land_absorb_end_f) / (1.0 - land_absorb_end_f)
            pelvis_y = -crouch_depth * (0.5 * (1 + np.cos(np.pi * progress)))
        data[i, PELVIS] = [pelvis_x, pelvis_y]

        # 2. Torso and Head Motion
        # The torso leans forward for balance during the crouch and landing.
        torso_lean = 0.0
        if t <= takeoff_f:
            progress = t / takeoff_f
            torso_lean = np.deg2rad(25) * np.sin(np.pi * progress)
        elif t > flight_end_f:
            progress = (t - flight_end_f) / (1.0 - flight_end_f)
            torso_lean = np.deg2rad(20) * np.sin(np.pi * progress)
        
        data[i, STERNUM] = data[i, PELVIS] + np.array([-PELVIS_STERNUM_DY * np.sin(torso_lean), PELVIS_STERNUM_DY * np.cos(torso_lean)])
        data[i, HEAD] = data[i, STERNUM] + np.array([-STERNUM_HEAD_DY * np.sin(torso_lean), STERNUM_HEAD_DY * np.cos(torso_lean)])
        
        # 3. Arm Motion (energetic swing)
        shoulder_angle = 0.0
        elbow_bend = np.deg2rad(30)  # Natural elbow bend
        if t <= crouch_end_f:  # Swing arms back
            progress = t / crouch_end_f
            shoulder_angle = np.deg2rad(-90) * 0.5 * (1 - np.cos(np.pi * progress))
        elif t <= takeoff_f:  # Swing arms forward forcefully for momentum
            progress = (t - crouch_end_f) / (takeoff_f - crouch_end_f)
            shoulder_angle = np.deg2rad(-90) + np.deg2rad(210) * 0.5 * (1 - np.cos(np.pi * progress))
        elif t <= flight_end_f:  # Arms float upwards during flight
            progress = (t - takeoff_f) / (flight_end_f - takeoff_f)
            shoulder_angle = np.deg2rad(120) - np.deg2rad(60) * progress
            elbow_bend = np.deg2rad(30) + np.deg2rad(20) * np.sin(np.pi * progress)
        else:  # Arms come down for balance during recovery
            progress = (t - flight_end_f) / (1.0 - flight_end_f)
            shoulder_angle = np.deg2rad(60) * (1 - progress) - np.deg2rad(20) * progress
        
        # Position shoulders relative to the sternum, accounting for torso lean
        shoulder_offset_x = (SHOULDER_WIDTH / 2) * np.cos(torso_lean)
        shoulder_offset_y = (SHOULDER_WIDTH / 2) * np.sin(torso_lean)
        data[i, L_SHOULDER] = data[i, STERNUM] + np.array([-shoulder_offset_x, shoulder_offset_y])
        data[i, R_SHOULDER] = data[i, STERNUM] + np.array([shoulder_offset_x, shoulder_offset_y])
        
        # Calculate positions of elbows and wrists
        for shoulder, elbow, wrist in [(L_SHOULDER, L_ELBOW, L_WRIST), (R_SHOULDER, R_ELBOW, R_WRIST)]:
            shoulder_pos = data[i, shoulder]
            elbow_pos = shoulder_pos + np.array([UPPER_ARM_LEN * np.sin(shoulder_angle), -UPPER_ARM_LEN * np.cos(shoulder_angle)])
            wrist_pos = elbow_pos + np.array([LOWER_ARM_LEN * np.sin(shoulder_angle - elbow_bend), -LOWER_ARM_LEN * np.cos(shoulder_angle - elbow_bend)])
            data[i, elbow], data[i, wrist] = elbow_pos, wrist_pos
        
        # 4. Leg Motion
        hip_angle = torso_lean
        knee_bend = 0.0
        if t <= crouch_end_f:  # Bend legs to crouch
            progress = 0.5 * (1 - np.cos(np.pi * t / crouch_end_f))
            hip_angle += np.deg2rad(85) * progress
            knee_bend = np.deg2rad(120) * progress
        elif t <= takeoff_f:  # Extend legs powerfully
            progress = np.sin(0.5 * np.pi * (t - crouch_end_f) / (takeoff_f - crouch_end_f))
            hip_angle += np.deg2rad(85) - np.deg2rad(105) * progress
            knee_bend = np.deg2rad(120) * (1 - progress)
        elif t <= flight_end_f:  # Tuck legs during flight, then extend for landing
            progress = (t - takeoff_f) / (flight_end_f - takeoff_f)
            hip_angle = np.deg2rad(-20) + np.deg2rad(100) * np.sin(np.pi * progress)
            knee_bend = np.deg2rad(130) * np.sin(np.pi * progress * 1.1)
        else:  # Bend legs to absorb landing and recover
            progress = (t - flight_end_f) / (1.0 - flight_end_f)
            ease_in_out = 0.5 * (1 - np.cos(np.pi * progress))
            hip_angle = torso_lean + np.deg2rad(80) * ease_in_out
            knee_bend = np.deg2rad(110) * ease_in_out

        # Position hips relative to the pelvis
        data[i, L_HIP] = data[i, PELVIS] + np.array([-HIP_WIDTH/2, 0])
        data[i, R_HIP] = data[i, PELVIS] + np.array([HIP_WIDTH/2, 0])

        # Calculate positions of knees and ankles
        for hip, knee, ankle in [(L_HIP, L_KNEE, L_ANKLE), (R_HIP, R_KNEE, R_ANKLE)]:
            hip_pos = data[i, hip]
            knee_pos = hip_pos + np.array([-THIGH_LEN * np.sin(hip_angle), -THIGH_LEN * np.cos(hip_angle)])
            ankle_pos = knee_pos + np.array([-CALF_LEN * np.sin(hip_angle - knee_bend), -CALF_LEN * np.cos(hip_angle - knee_bend)])
            data[i, knee], data[i, ankle] = knee_pos, ankle_pos

    # --- Post-processing: Center and Align Animation ---
    # Center the animation horizontally in the view
    final_x = data[-1, PELVIS, 0]
    data[:, :, 0] -= final_x / 2
    # Align the figure so the lowest point is at y=0
    min_y = data.min(axis=(0, 1))[1]
    data[:, :, 1] -= min_y
    
    return data

if __name__ == '__main__':
    # --- Matplotlib Setup ---
    # Create a figure and axis for the animation
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Configure the axis for a clean, borderless look
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Generate the motion data
    motion_data = generate_motion_data(num_frames=100)
    num_frames = motion_data.shape[0]

    # Set axis limits based on the full range of motion, with padding
    x_min, x_max = np.min(motion_data[:, :, 0]), np.max(motion_data[:, :, 0])
    y_min, y_max = np.min(motion_data[:, :, 1]), np.max(motion_data[:, :, 1])
    ax.set_xlim(x_min - 0.2, x_max + 0.2)
    ax.set_ylim(y_min - 0.2, y_max + 0.2)

    # Initialize the 15 point-lights using a scatter plot
    scatter = ax.scatter(motion_data[0, :, 0], motion_data[0, :, 1], color='white', s=40)

    # --- Animation Function ---
    def update(frame):
        """Updates the position of the point-lights for each frame."""
        scatter.set_offsets(motion_data[frame])
        return scatter,

    # Create and display the animation
    # interval is in milliseconds (1000ms / 50fps = 20ms) for a smooth playback
    ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

    plt.show()
