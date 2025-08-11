
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_biological_motion_animation():
    """
    Generates and displays a point-light animation of a person with heavy weight bowing.
    """
    # --- Animation Parameters ---
    NUM_FRAMES = 120  # Total frames for one full cycle (bow down and up)

    # --- 15-Point Body Model ---
    # The 15 points represent: Head, Torso Center, Pelvis Center, L/R Shoulders,
    # L/R Elbows, L/R Wrists, L/R Hips, L/R Knees, L/R Ankles.

    # Keyframe 1: Initial Stance (standing upright, holding weight)
    # The stance is stable and slightly crouched, appropriate for holding a heavy weight.
    pose_start = np.array([
        [0, 70],    # 0: Head
        [0, 50],    # 1: Torso Center (between shoulders)
        [0, 15],    # 2: Pelvis Center
        [-15, 50],  # 3: L_Shoulder
        [15, 50],   # 4: R_Shoulder
        [-22, 30],  # 5: L_Elbow
        [22, 30],   # 6: R_Elbow
        [-8, 20],   # 7: L_Wrist
        [8, 20],    # 8: R_Wrist
        [-12, 15],  # 9: L_Hip
        [12, 15],   # 10: R_Hip
        [-15, -20], # 11: L_Knee
        [15, -20],  # 12: R_Knee
        [-17, -55], # 13: L_Ankle
        [17, -55]   # 14: R_Ankle
    ])

    # Keyframe 2: Full Bow Position
    # Biomechanics: Hinge at the hips, move hips backward to counterbalance,
    # keep the back relatively straight, bend knees more, let arms hang.
    pose_end = np.copy(pose_start)
    
    pivot_start = pose_start[[9, 10]].mean(axis=0)

    # Lower body movement
    hip_translation = np.array([-20, -15])
    pose_end[[2, 9, 10]] = pose_start[[2, 9, 10]] + hip_translation
    pivot_end = pose_end[[9, 10]].mean(axis=0)
    
    knee_translation = np.array([5, -20])
    pose_end[11:13] = pose_start[11:13] + knee_translation
    
    pose_end[13:15] = pose_start[13:15] # Ankles are fixed

    # Upper body rotation
    bow_angle = np.deg2rad(85)
    c, s = np.cos(bow_angle), np.sin(bow_angle)
    rotation_matrix = np.array([[c, s], [-s, c]])

    upper_body_indices = [0, 1, 3, 4]
    for i in upper_body_indices:
        v = pose_start[i] - pivot_start
        v_rot = v @ rotation_matrix
        pose_end[i] = v_rot + pivot_end

    # Arm movement (hanging down)
    l_shoulder_end, r_shoulder_end = pose_end[3], pose_end[4]
    pose_end[5] = l_shoulder_end + np.array([-5, -25])  # L Elbow
    pose_end[7] = l_shoulder_end + np.array([-4, -45])  # L Wrist
    pose_end[6] = r_shoulder_end + np.array([5, -25])   # R Elbow
    pose_end[8] = r_shoulder_end + np.array([4, -45])   # R Wrist

    # --- Generate Frames via Interpolation ---
    phase = np.linspace(0, 2 * np.pi, NUM_FRAMES, endpoint=False)
    interp_factor = (1 - np.cos(phase)) / 2
    interp_reshaped = interp_factor.reshape(NUM_FRAMES, 1, 1)

    all_frames_data = pose_start[np.newaxis, :, :] * (1 - interp_reshaped) + \
                      pose_end[np.newaxis, :, :] * interp_reshaped

    # --- Set up Matplotlib Animation ---
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Set plot limits dynamically
    x_min, x_max = all_frames_data[:, :, 0].min(), all_frames_data[:, :, 0].max()
    y_min, y_max = all_frames_data[:, :, 1].min(), all_frames_data[:, :, 1].max()
    x_range, y_range = x_max - x_min, y_max - y_min
    ax.set_xlim(x_min - 0.1 * x_range, x_max + 0.1 * x_range)
    ax.set_ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)
    
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    scatter = ax.scatter(all_frames_data[0, :, 0], all_frames_data[0, :, 1], c='white', s=50)

    def update(frame):
        scatter.set_offsets(all_frames_data[frame])
        return scatter,

    ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES, interval=33, blit=True)
    plt.show()

if __name__ == '__main__':
    create_biological_motion_animation()
