
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. Setup the plot ---
fig, ax = plt.subplots(figsize=(8, 8))
fig.set_facecolor('black')
ax.set_facecolor('black')

# Set axis limits and appearance
ax.set_xlim(-25, 10)
ax.set_ylim(-5, 25)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect('equal', adjustable='box')

# --- 2. Define Animation Data (Keyframes) ---
# The motion is defined by four key poses. The animation will interpolate between them.
# There are 15 points representing the major joints of the human body.
# Point Order: Head, Neck, Pelvis, L-Shoulder, R-Shoulder, L-Elbow, R-Elbow,
# L-Wrist, R-Wrist, L-Hip, R-Hip, L-Knee, R-Knee, L-Ankle, R-Ankle.
keyframes = np.array([
    # Keyframe 1: Standing upright, side view
    [
        [0, 22],      # Head
        [0, 20],      # Neck
        [0, 12],      # Pelvis
        [-0.5, 19.5], [0.5, 19.5],  # Shoulders (L, R)
        [-0.5, 15.5], [0.5, 15.5],  # Elbows (L, R)
        [-0.5, 12.5], [0.5, 12.5],  # Wrists (L, R)
        [-0.5, 12],   [0.5, 12],    # Hips (L, R)
        [-0.5, 6],    [0.5, 6],     # Knees (L, R)
        [-0.5, 0],    [0.5, 0]      # Ankles (L, R)
    ],
    # Keyframe 2: Crouching, preparing to sit
    [
        [3.5, 15],     # Head
        [3, 13],       # Neck
        [-2, 8],       # Pelvis
        [2.5, 12.5], [3.5, 12.5],   # Shoulders
        [1, 8],      [2, 8],        # Elbows
        [2, 5],      [3, 5],        # Wrists
        [-2.5, 8],   [-1.5, 8],     # Hips
        [3.5, 4],    [4.5, 4],      # Knees
        [-0.5, 0],   [0.5, 0]       # Ankles
    ],
    # Keyframe 3: Sitting on the ground, supported by hands
    [
        [-11, 8],      # Head
        [-11, 6],      # Neck
        [-8, 1],       # Pelvis
        [-11.5, 5.5], [-10.5, 5.5], # Shoulders
        [-13, 3],     [-12, 3],      # Elbows
        [-15, 0],     [-14, 0],      # Wrists
        [-8.5, 1],    [-7.5, 1],     # Hips
        [-4, 7],      [-3, 7],       # Knees
        [-0.5, 0],    [0.5, 0]       # Ankles
    ],
    # Keyframe 4: Lying down fully on the right side
    [
        [-20, 0.5],    # Head
        [-18, 0.5],    # Neck
        [-10, 0.5],    # Pelvis
        [-17, 1],     [-17, 0],      # Shoulders
        [-14, 1.5],   [-14, -0.5],   # Elbows
        [-12, 1.5],   [-12, -0.5],   # Wrists
        [-10, 1],     [-10, 0],      # Hips
        [-4.5, 1],    [-5, 0],       # Knees
        [0.5, 1],     [0, 0]         # Ankles
    ]
])

# Create the scatter plot object that will be updated in each frame
points, = ax.plot([], [], 'o', color='white', markersize=10)

# --- 3. Define Animation Logic ---
FRAMES_PER_TRANSITION = 60
TOTAL_FRAMES = FRAMES_PER_TRANSITION * (len(keyframes) - 1)

def init():
    """Initializes the plot for the animation."""
    points.set_data([], [])
    return points,

def animate(frame_num):
    """
    Calculates and sets the positions of the points for each frame.
    """
    # Determine the current transition segment (e.g., standing to crouching)
    transition_index = frame_num // FRAMES_PER_TRANSITION
    frame_in_transition = frame_num % FRAMES_PER_TRANSITION

    # Get the start and end poses for the current segment
    start_pose = keyframes[transition_index]
    end_pose = keyframes[transition_index + 1]

    # Calculate interpolation factor using a cosine easing function for smooth motion
    if FRAMES_PER_TRANSITION > 1:
        t = frame_in_transition / (FRAMES_PER_TRANSITION - 1)
    else:
        t = 1.0
    interp_factor = 0.5 * (1 - np.cos(np.pi * t))

    # Calculate the current pose by interpolating between keyframes
    current_pose = start_pose + (end_pose - start_pose) * interp_factor
    
    # Update the plot data
    points.set_data(current_pose[:, 0], current_pose[:, 1])
    return points,

# --- 4. Create and Run the Animation ---
ani = animation.FuncAnimation(fig, animate, frames=TOTAL_FRAMES,
                              init_func=init, blit=True, interval=30, repeat=False)

plt.show()
