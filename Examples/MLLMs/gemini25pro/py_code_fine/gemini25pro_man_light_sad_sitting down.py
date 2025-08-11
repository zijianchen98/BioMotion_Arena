
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_sad_sitting_animation():
    """
    Generates and displays a point-light animation of a sad person sitting down.
    """
    # --- Animation Configuration ---
    NUM_FRAMES = 120
    PAUSE_FRAMES = 15
    MOTION_FRAMES = NUM_FRAMES - 2 * PAUSE_FRAMES
    INTERVAL = 50  # milliseconds per frame
    DOT_SIZE = 70

    # --- Point Indices for a 15-point model ---
    HEAD = 0
    TOP_TORSO, BOTTOM_TORSO = 1, 2
    L_SHOULDER, R_SHOULDER = 3, 4
    L_ELBOW, R_ELBOW = 5, 6
    L_WRIST, R_WRIST = 7, 8
    L_HIP, R_HIP = 9, 10
    L_KNEE, R_KNEE = 11, 12
    L_ANKLE, R_ANKLE = 13, 14

    # --- Keyframe Poses ---
    # Keyframe 1: Standing with a sad, slumped posture
    coords_start = np.array([
        [-4, 95],   # HEAD (bowed forward)
        [-2, 80],   # TOP_TORSO (slumped)
        [0, 50],    # BOTTOM_TORSO (Pelvis)
        [-14, 78],  # L_SHOULDER (rounded forward)
        [10, 78],   # R_SHOULDER
        [-16, 60],  # L_ELBOW (hanging limp)
        [12, 60],   # R_ELBOW
        [-17, 45],  # L_WRIST
        [13, 45],   # R_WRIST
        [-12, 50],  # L_HIP
        [12, 50],   # R_HIP
        [-11, 25],  # L_KNEE (slight bend)
        [11, 25],   # R_KNEE
        [-10, 0],   # L_ANKLE
        [10, 0]     # R_ANKLE
    ])

    # Keyframe 2: Seated, maintaining the sad posture
    coords_end = np.array([
        [-28, 70],  # HEAD (remains bowed)
        [-25, 55],  # TOP_TORSO (leans forward)
        [-20, 25],  # BOTTOM_TORSO (moves down and back)
        [-37, 53],  # L_SHOULDER
        [-13, 53],  # R_SHOULDER
        [-30, 38],  # L_ELBOW (arms rest on legs)
        [-10, 38],  # R_ELBOW
        [-22, 22],  # L_WRIST
        [0, 22],    # R_WRIST
        [-32, 25],  # L_HIP
        [-8, 25],   # R_HIP
        [-15, 20],  # L_KNEE (bent for sitting)
        [8, 20],    # R_KNEE
        [-10, 0],   # L_ANKLE (fixed)
        [10, 0]     # R_ANKLE (fixed)
    ])

    # --- Generate Animation Data ---
    all_frames = np.zeros((NUM_FRAMES, 15, 2))

    # Hold starting pose
    all_frames[:PAUSE_FRAMES] = coords_start

    # Interpolate for motion using an ease-in-out curve
    t = np.linspace(0, 1, MOTION_FRAMES)
    ease_factor = 0.5 - 0.5 * np.cos(t * np.pi)
    
    for i in range(MOTION_FRAMES):
        frame_index = PAUSE_FRAMES + i
        all_frames[frame_index] = coords_start + (coords_end - coords_start) * ease_factor[i]

    # Hold ending pose
    all_frames[PAUSE_FRAMES + MOTION_FRAMES:] = coords_end

    # --- Set up the Plot ---
    fig, ax = plt.subplots(figsize=(5, 8))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Define plot limits and appearance
    ax.set_xlim(-60, 40)
    ax.set_ylim(-10, 110)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Initialize the scatter plot
    scatter = ax.scatter([], [], c='white', s=DOT_SIZE)

    # --- Animation Function ---
    def update(frame):
        """Updates the scatter plot for each frame."""
        scatter.set_offsets(all_frames[frame])
        return scatter,

    # --- Create and Display Animation ---
    ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES,
                                  interval=INTERVAL, blit=True)
    plt.show()

create_sad_sitting_animation()
