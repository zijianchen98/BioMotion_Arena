
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_jumping_forward_animation():
    """
    Generates and displays a point-light animation of a happy woman
    with heavy weight jumping forward, consisting of 15 points.
    """

    # --- Animation Parameters ---
    TOTAL_FRAMES = 120
    INTERVAL = 50  # Milliseconds between frames
    FIGURE_SCALE = 100

    # --- Point-light Model (15 points) ---
    # This conceptual mapping is used to build the motion logically.
    # 0: Head, 1: Neck, 2: Pelvis, 3: L_Shoulder, 4: R_Shoulder,
    # 5: L_Elbow, 6: R_Elbow, 7: L_Wrist, 8: R_Wrist,
    # 9: L_Hip, 10: R_Hip, 11: L_Knee, 12: R_Knee,
    # 13: L_Ankle, 14: R_Ankle

    def generate_motion_data(num_frames):
        """
        Calculates the coordinates for all 15 points over all frames.
        The motion is procedurally generated using sine waves and physics
        principles to create a smooth and plausible animation.
        """
        all_coords = np.zeros((num_frames, 15, 2))
        t = np.linspace(0, 2 * np.pi, num_frames)

        # --- Skeleton Proportions ---
        head_to_neck = 0.25
        neck_to_pelvis = 0.55
        shoulder_width = 0.45
        neck_to_shoulder = shoulder_width / 2
        upper_arm_len = 0.35
        forearm_len = 0.3
        hip_width = 0.35
        pelvis_to_hip = hip_width / 2
        thigh_len = 0.5
        shin_len = 0.45

        # --- Simulating "Heavy Weight" and "Happy" ---
        # Heavy: Deep crouch, low jump arc, heavy landing absorption.
        # Happy: Energetic arm swing, bouncy landing.
        crouch_depth = 0.5 * FIGURE_SCALE
        jump_height = 0.6 * FIGURE_SCALE

        # --- Phase Timings ---
        takeoff_time = np.pi * 0.85
        landing_start_time = np.pi * 1.5
        bounce_start_time = np.pi * 1.85

        # --- Core Body Motion (Pelvis) ---
        pelvis_x = np.zeros(num_frames)
        start_x = -1.5 * FIGURE_SCALE
        end_x = 1.5 * FIGURE_SCALE
        
        crouch_phase = t <= takeoff_time
        jump_phase = t > takeoff_time
        
        pelvis_x[crouch_phase] = np.linspace(start_x, start_x - 0.2 * FIGURE_SCALE, crouch_phase.sum())
        pelvis_x[jump_phase] = np.linspace(start_x - 0.2 * FIGURE_SCALE, end_x, jump_phase.sum())

        pelvis_y = np.zeros(num_frames)
        crouch_y = -crouch_depth * (1 - np.cos(t * (np.pi / takeoff_time))) / 2
        pelvis_y[crouch_phase] = crouch_y[crouch_phase]

        jump_t = np.linspace(0, 1, jump_phase.sum())
        jump_arc = jump_height * (4 * jump_t - 4 * jump_t**2)
        pelvis_y[jump_phase] = crouch_y[crouch_phase][-1] + jump_arc
        
        bounce_phase = t > bounce_start_time
        if bounce_phase.any():
            bounce_t = np.linspace(0, np.pi, bounce_phase.sum())
            bounce = 0.1 * FIGURE_SCALE * np.sin(bounce_t)
            pelvis_y[bounce_phase] += bounce

        # --- Torso and Head Motion ---
        torso_lean_angle = -0.6 * np.sin(t * (np.pi / takeoff_time) - np.pi/2)
        straighten_phase = t > landing_start_time
        if straighten_phase.any():
            torso_lean_angle[straighten_phase] *= np.linspace(1, 0, straighten_phase.sum())

        neck_y = pelvis_y + (neck_to_pelvis * FIGURE_SCALE * np.cos(torso_lean_angle))
        neck_x = pelvis_x + (neck_to_pelvis * FIGURE_SCALE * np.sin(torso_lean_angle))
        head_y = neck_y + (head_to_neck * FIGURE_SCALE * np.cos(torso_lean_angle))
        head_x = neck_x + (head_to_neck * FIGURE_SCALE * np.sin(torso_lean_angle))

        # --- Limb Base Positions (Shoulders, Hips) ---
        l_shoulder_x = neck_x - (neck_to_shoulder * FIGURE_SCALE * np.cos(torso_lean_angle))
        l_shoulder_y = neck_y + (neck_to_shoulder * FIGURE_SCALE * np.sin(torso_lean_angle))
        r_shoulder_x = neck_x + (neck_to_shoulder * FIGURE_SCALE * np.cos(torso_lean_angle))
        r_shoulder_y = neck_y - (neck_to_shoulder * FIGURE_SCALE * np.sin(torso_lean_angle))
        l_hip_x = pelvis_x - (pelvis_to_hip * FIGURE_SCALE * np.cos(torso_lean_angle))
        l_hip_y = pelvis_y + (pelvis_to_hip * FIGURE_SCALE * np.sin(torso_lean_angle))
        r_hip_x = pelvis_x + (pelvis_to_hip * FIGURE_SCALE * np.cos(torso_lean_angle))
        r_hip_y = pelvis_y - (pelvis_to_hip * FIGURE_SCALE * np.sin(torso_lean_angle))

        # --- Arm Motion ---
        arm_swing = 1.8 * np.sin(t * 1.2 - np.pi * 0.7)
        elbow_bend = 0.8 + 0.8 * np.cos(t * 2)

        r_upper_arm = torso_lean_angle + arm_swing
        r_lower_arm = r_upper_arm - elbow_bend
        r_elbow_x = r_shoulder_x + (upper_arm_len * FIGURE_SCALE * np.sin(r_upper_arm))
        r_elbow_y = r_shoulder_y - (upper_arm_len * FIGURE_SCALE * np.cos(r_upper_arm))
        r_wrist_x = r_elbow_x + (forearm_len * FIGURE_SCALE * np.sin(r_lower_arm))
        r_wrist_y = r_elbow_y - (forearm_len * FIGURE_SCALE * np.cos(r_lower_arm))
        
        l_upper_arm = torso_lean_angle + arm_swing * 1.1
        l_lower_arm = l_upper_arm - (elbow_bend + 0.2)
        l_elbow_x = l_shoulder_x + (upper_arm_len * FIGURE_SCALE * np.sin(l_upper_arm))
        l_elbow_y = l_shoulder_y - (upper_arm_len * FIGURE_SCALE * np.cos(l_upper_arm))
        l_wrist_x = l_elbow_x + (forearm_len * FIGURE_SCALE * np.sin(l_lower_arm))
        l_wrist_y = l_elbow_y - (forearm_len * FIGURE_SCALE * np.cos(l_lower_arm))

        # --- Leg Motion ---
        sway = 0.05 * np.sin(t * 2)
        thigh_angle = np.zeros(num_frames)
        shin_angle = np.zeros(num_frames)

        thigh_angle[crouch_phase] = np.pi/2.5 * (1 - np.cos(t[crouch_phase] * (np.pi / takeoff_time))) / 2
        shin_angle[crouch_phase] = -np.pi/2.0 * (1 - np.cos(t[crouch_phase] * (np.pi / takeoff_time))) / 2

        flight_phase = (t > takeoff_time) & (t <= landing_start_time)
        if flight_phase.any():
            prog = np.linspace(0, 1, flight_phase.sum())
            thigh_angle[flight_phase] = thigh_angle[crouch_phase][-1] * (1-prog) - 0.2
            shin_angle[flight_phase] = shin_angle[crouch_phase][-1] * (1-prog) + (np.pi/3) * prog

        land_phase = t > landing_start_time
        if land_phase.any():
            prog = np.linspace(0, 1, land_phase.sum())
            thigh_start = thigh_angle[flight_phase][-1] if flight_phase.any() else thigh_angle[crouch_phase][-1]
            shin_start = shin_angle[flight_phase][-1] if flight_phase.any() else shin_angle[crouch_phase][-1]
            thigh_angle[land_phase] = thigh_start + (np.pi/3 - thigh_start) * prog
            shin_angle[land_phase] = shin_start + (-np.pi/2.5 - shin_start) * prog

        r_thigh = torso_lean_angle + np.pi + thigh_angle
        l_thigh = torso_lean_angle + np.pi + thigh_angle + sway
        r_shin = r_thigh + shin_angle
        l_shin = l_thigh + shin_angle

        r_knee_x = r_hip_x + (thigh_len * FIGURE_SCALE * np.sin(r_thigh))
        r_knee_y = r_hip_y - (thigh_len * FIGURE_SCALE * np.cos(r_thigh))
        l_knee_x = l_hip_x + (thigh_len * FIGURE_SCALE * np.sin(l_thigh))
        l_knee_y = l_hip_y - (thigh_len * FIGURE_SCALE * np.cos(l_thigh))
        
        r_ankle_x = r_knee_x + (shin_len * FIGURE_SCALE * np.sin(r_shin))
        r_ankle_y = r_knee_y - (shin_len * FIGURE_SCALE * np.cos(r_shin))
        l_ankle_x = l_knee_x + (shin_len * FIGURE_SCALE * np.sin(l_shin))
        l_ankle_y = l_knee_y - (shin_len * FIGURE_SCALE * np.cos(l_shin))

        # --- Assemble Raw Data and Perform Ground Correction ---
        point_data = [
            (head_x, head_y), (neck_x, neck_y), (pelvis_x, pelvis_y),
            (l_shoulder_x, l_shoulder_y), (r_shoulder_x, r_shoulder_y),
            (l_elbow_x, l_elbow_y), (r_elbow_x, r_elbow_y),
            (l_wrist_x, l_wrist_y), (r_wrist_x, r_wrist_y),
            (l_hip_x, l_hip_y), (r_hip_x, r_hip_y),
            (l_knee_x, l_knee_y), (r_knee_x, r_knee_y),
            (l_ankle_x, l_ankle_y), (r_ankle_x, r_ankle_y)
        ]
        for i, (px, py) in enumerate(point_data):
            all_coords[:, i] = np.stack([px, py], axis=-1)

        ground_y = -1.5 * FIGURE_SCALE
        ankle_y_min = np.minimum(all_coords[:, 13, 1], all_coords[:, 14, 1])
        takeoff_frame = np.where(crouch_phase)[0][-1]
        
        pelvis_y_flight = all_coords[takeoff_frame+1:, 2, 1]
        apex_frame = (takeoff_frame + 1) + np.argmax(pelvis_y_flight) if len(pelvis_y_flight) > 0 else takeoff_frame
        
        ankle_y_post_apex = ankle_y_min[apex_frame:]
        landing_frame = apex_frame + np.argmin(ankle_y_post_apex) if len(ankle_y_post_apex) > 0 else num_frames - 1

        for i in range(takeoff_frame + 1):
            offset = ground_y - ankle_y_min[i]
            all_coords[i, :, 1] += offset
        for i in range(landing_frame, num_frames):
            offset = ground_y - ankle_y_min[i]
            all_coords[i, :, 1] += offset
            
        return all_coords

    # --- Setup the Animation Plot ---
    animation_data = generate_motion_data(TOTAL_FRAMES)
    
    fig, ax = plt.subplots(facecolor='black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')

    min_vals = animation_data.min(axis=(0, 1))
    max_vals = animation_data.max(axis=(0, 1))
    ax.set_xlim(min_vals[0] - 20, max_vals[0] + 20)
    ax.set_ylim(min_vals[1] - 20, max_vals[1] + 20)
    ax.axis('off')

    scatter = ax.scatter([], [], c='white', s=40)

    def update(frame):
        scatter.set_offsets(animation_data[frame])
        return scatter,

    ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                                  interval=INTERVAL, blit=True, repeat=True)
    plt.show()

create_jumping_forward_animation()
