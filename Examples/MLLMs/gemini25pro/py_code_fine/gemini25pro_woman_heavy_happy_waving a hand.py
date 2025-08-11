
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def create_biological_motion_animation():
    """
    Creates and displays a point-light animation of a happy, heavy-weight woman waving her hand.
    """
    # 1. --- SETUP THE FIGURE AND AXES ---
    fig = plt.figure(figsize=(5, 8))
    ax = fig.add_subplot(111, xlim=(-2.5, 2.5), ylim=(-1.5, 4.0))
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.axis('off')

    # 2. --- INITIALIZE THE 15 POINTS ---
    # The points represent major joints:
    # 0: Head, 1: Neck, 2: R Shoulder, 3: R Elbow, 4: R Wrist,
    # 5: L Shoulder, 6: L Elbow, 7: L Wrist, 8: Torso Center,
    # 9: R Hip, 10: R Knee, 11: R Ankle, 12: L Hip, 13: L Knee, 14: L Ankle
    initial_positions = np.zeros((15, 2))
    scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=70, c='white')

    # 3. --- DEFINE THE ANIMATION UPDATE FUNCTION ---
    def update(frame):
        # Time variable for smooth oscillations
        t = frame / 60.0

        # --- Motion Parameters ---
        # Heavy-weight proportions
        hip_width = 0.6
        shoulder_width = 0.5  # Shoulders narrower than hips
        upper_arm_len = 0.75
        lower_arm_len = 0.65
        thigh_len = 0.9
        shin_len = 0.9

        # Happy motion characteristics
        bob_amplitude = 0.04
        bob_freq = 2.0
        sway_amplitude = 0.12
        sway_freq = 0.5
        wave_freq = 2.5 # Energetic wave

        # --- Calculate Joint Positions for the current frame ---

        # A. Global Body Motion (Sway and Bob)
        bob_y = bob_amplitude * np.sin(t * 2 * np.pi * bob_freq)
        sway_x = sway_amplitude * np.sin(t * 2 * np.pi * sway_freq)

        # B. Lower Body (Hips, Legs, Ankles)
        # Hips are the base of the sway
        hip_center_y = 1.0
        l_hip_pos = np.array([-hip_width + sway_x, hip_center_y + bob_y])
        r_hip_pos = np.array([hip_width + sway_x, hip_center_y + bob_y])

        # Legs bend in response to the sway to shift weight
        r_knee_bend = 0.1 * (1 - np.sin(t * 2 * np.pi * sway_freq))
        l_knee_bend = 0.1 * (1 + np.sin(t * 2 * np.pi * sway_freq))

        r_knee_pos = r_hip_pos + np.array([0.1, -thigh_len + r_knee_bend])
        l_knee_pos = l_hip_pos + np.array([-0.1, -thigh_len + l_knee_bend])

        r_ankle_pos = r_knee_pos + np.array([0.0, -shin_len])
        l_ankle_pos = l_knee_pos + np.array([0.0, -shin_len])

        # C. Upper Body (Torso, Neck, Head, Shoulders)
        # Torso and shoulders follow the hip sway
        torso_sway_factor = 1.1
        shoulder_center_y = 2.5
        torso_center_pos = (l_hip_pos + r_hip_pos) / 2 + np.array([0, 0.75])
        neck_pos = np.array([sway_x * torso_sway_factor, shoulder_center_y + bob_y])
        head_pos = neck_pos + np.array([0, 0.5])
        l_shoulder_pos = neck_pos + np.array([-shoulder_width, 0])
        r_shoulder_pos = neck_pos + np.array([shoulder_width, 0])

        # D. Arms Motion
        # Left arm (non-waving): hangs and swings slightly for balance
        l_arm_swing = 0.15 * np.sin(t * 2 * np.pi * sway_freq + np.pi) # Counter-sway
        l_elbow_pos = l_shoulder_pos + upper_arm_len * np.array([np.sin(l_arm_swing), -np.cos(l_arm_swing)])
        l_wrist_pos = l_elbow_pos + lower_arm_len * np.array([np.sin(l_arm_swing * 0.5), -np.cos(l_arm_swing * 0.5)])

        # Right arm (waving): raised and waving
        r_shoulder_wave_pos = r_shoulder_pos + np.array([0.1, 0.1])
        
        # Upper arm is held up at an angle
        upper_arm_angle = np.deg2rad(45)
        r_elbow_pos = r_shoulder_wave_pos + upper_arm_len * np.array([np.cos(upper_arm_angle), np.sin(upper_arm_angle)])
        
        # Forearm/hand pivots at the elbow for the wave
        wave_angle_offset = -np.deg2rad(90)
        wave_amplitude = np.deg2rad(45)
        wave_angle = wave_amplitude * np.sin(t * 2 * np.pi * wave_freq)
        final_wrist_angle = upper_arm_angle + wave_angle_offset + wave_angle
        r_wrist_pos = r_elbow_pos + lower_arm_len * np.array([np.cos(final_wrist_angle), np.sin(final_wrist_angle)])

        # --- Assemble and Update All Point Positions ---
        points_data = np.array([
            head_pos,
            neck_pos,
            r_shoulder_wave_pos,
            r_elbow_pos,
            r_wrist_pos,
            l_shoulder_pos,
            l_elbow_pos,
            l_wrist_pos,
            torso_center_pos,
            r_hip_pos,
            r_knee_pos,
            r_ankle_pos,
            l_hip_pos,
            l_knee_pos,
            l_ankle_pos
        ])
        scatter.set_offsets(points_data)
        return scatter,

    # 4. --- CREATE AND RUN THE ANIMATION ---
    # Animate for 4 seconds to show a few cycles of the motion.
    # At 60 fps, this is 240 frames.
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=240,
        interval=16.67,  # Corresponds to 60 FPS
        blit=True
    )

    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
