
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# This program generates a point-light display animation of a sad man jumping.
# The animation consists of 15 white points on a black background, representing
# the major joints of a human figure.

# Define the 15 joints for the point-light figure.
# This structure represents the head, torso, and limbs.
HEAD, STERNUM, PELVIS, L_SHOULDER, R_SHOULDER, L_ELBOW, R_ELBOW, \
L_WRIST, R_WRIST, L_HIP, R_HIP, L_KNEE, R_KNEE, L_ANKLE, R_ANKLE = range(15)

# Keyframes define the pose of the figure at critical moments in the animation.
# Each keyframe is a (15, 2) numpy array for the (x, y) coordinates of the 15 joints.
# The animation is created by interpolating between these keyframes.
keyframes = np.zeros((7, 15, 2))

# Define the ground level for positioning the character.
y_floor = -90

# Keyframe 0: Initial slumped standing pose. This posture helps convey sadness.
keyframes[0] = [
    [8, 60],        # Head (tilted forward and down)
    [5, 30],        # Sternum (spine curved forward)
    [0, -10],       # Pelvis
    [-15, 45],      # L_Shoulder (hunched)
    [15, 45],       # R_Shoulder (hunched)
    [-18, 20],      # L_Elbow
    [18, 20],       # R_Elbow
    [-20, 0],       # L_Wrist
    [20, 0],        # R_Wrist
    [-12, -10],     # L_Hip
    [12, -10],      # R_Hip
    [-9, -50],      # L_Knee (slight natural bend)
    [9, -50],       # R_Knee (slight natural bend)
    [-10, y_floor], # L_Ankle
    [10, y_floor]   # R_Ankle
]

# Keyframe 1: Deepest part of the crouch (preparation for the jump).
keyframes[1] = [
    [18, 15],       # Head
    [15, -10],      # Sternum (leaned far forward)
    [0, -40],       # Pelvis (lowered center of mass)
    [-10, 5],       # L_Shoulder
    [20, 5],        # R_Shoulder
    [-15, -20],     # L_Elbow (arms swung back)
    [15, -20],      # R_Elbow (arms swung back)
    [-18, -40],     # L_Wrist (arms swung back)
    [18, -40],      # R_Wrist (arms swung back)
    [-15, -40],     # L_Hip
    [15, -40],      # R_Hip
    [-15, -65],     # L_Knee (deeply bent)
    [15, -65],      # R_Knee (deeply bent)
    [-12, y_floor], # L_Ankle
    [12, y_floor]   # R_Ankle
]

# Keyframe 2: Takeoff, the moment the feet leave the ground.
keyframes[2] = [
    [5, 85],        # Head
    [2, 55],        # Sternum (body extended upwards)
    [0, 10],        # Pelvis
    [-16, 70],      # L_Shoulder
    [16, 70],       # R_Shoulder
    [-25, 40],      # L_Elbow (arms swinging up for momentum)
    [25, 40],       # R_Elbow
    [-30, 15],      # L_Wrist
    [30, 15],       # R_Wrist
    [-6, 10],       # L_Hip
    [6, 10],        # R_Hip
    [-4, -40],      # L_Knee (extended for propulsion)
    [4, -40],       # R_Knee
    [-5, -85],      # L_Ankle (on toes)
    [5, -85]        # R_Ankle
]

# Keyframe 3: Apex of the jump. A low height and tucked pose reflect a low-energy, sad jump.
y_apex_pelvis = 40
keyframes[3] = [
    [8, 95],        # Head
    [5, 70],        # Sternum
    [0, y_apex_pelvis], # Pelvis
    [-15, 85],      # L_Shoulder
    [15, 85],       # R_Shoulder
    [-20, 60],      # L_Elbow (limp, low-energy arms)
    [20, 60],       # R_Elbow
    [-22, 40],      # L_Wrist
    [22, 40],       # R_Wrist
    [-12, y_apex_pelvis], # L_Hip
    [12, y_apex_pelvis],  # R_Hip
    [-10, 20],      # L_Knee (tucked)
    [10, 20],       # R_Knee
    [-8, 5],        # L_Ankle
    [8, 5]          # R_Ankle
]

# Keyframe 4: Landing preparation, with legs extending downwards to meet the ground.
keyframes[4] = [
    [5, 85],        # Head
    [2, 55],        # Sternum
    [0, 10],        # Pelvis
    [-16, 70],      # L_Shoulder
    [16, 70],       # R_Shoulder
    [-25, 50],      # L_Elbow (arms moving forward for balance)
    [25, 50],       # R_Elbow
    [-30, 30],      # L_Wrist
    [30, 30],       # R_Wrist
    [-6, 10],       # L_Hip
    [10, -30],      # L_Knee (extending down)
    [10, -30],      # R_Knee
    [-12, -70],     # L_Ankle
    [12, -70]       # R_Ankle
]

# Keyframe 5: Impact absorption, with knees bending to absorb the force of landing.
keyframes[5] = np.copy(keyframes[1]) # Base pose is similar to the crouch
keyframes[5, [L_ELBOW, R_ELBOW, L_WRIST, R_WRIST]] = [ # Arms are forward after landing
    [-5, -15], [25, -15], [0, -25], [30, -25]
]

# Keyframe 6: Return to the initial slumped standing pose, completing the cycle.
keyframes[6] = np.copy(keyframes[0])

# --- Animation Setup ---

# Total number of frames in the animation loop.
total_frames = 180
# Relative time points for each keyframe (from 0.0 to 1.0).
keyframe_times = np.array([0, 0.20, 0.30, 0.55, 0.75, 0.8, 1.0])
# Convert relative times to absolute frame indices.
keyframe_indices = (keyframe_times * (total_frames - 1)).astype(int)

# Easing functions to create smooth, natural, non-linear motion.
def ease_in_out_sine(t):
    return -(np.cos(np.pi * t) - 1) / 2

def ease_out_sine(t):
    return np.sin(t * np.pi / 2)

def ease_in_sine(t):
    return 1 - np.cos(t * np.pi / 2)

# --- Plotting and Animation ---

# Set up the figure and axes for the animation.
fig, ax = plt.subplots(figsize=(5, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Configure plot appearance: limits, aspect ratio, and no visible axes.
ax.set_xlim(-100, 100)
ax.set_ylim(-110, 120)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Create the scatter plot object (the 15 points) that will be animated.
scatter = ax.scatter([], [], c='white', s=70)

# The update function is called for each frame to calculate and draw the new point positions.
def update(frame):
    # Find which segment of the animation the current frame is in.
    segment_idx = np.searchsorted(keyframe_indices, frame, side='right') - 1
    
    start_frame_index = keyframe_indices[segment_idx]
    end_frame_index = keyframe_indices[segment_idx + 1]
    
    start_pose = keyframes[segment_idx]
    end_pose = keyframes[segment_idx + 1]

    # Calculate progress 't' (0 to 1) within the current segment.
    segment_duration = end_frame_index - start_frame_index
    t = (frame - start_frame_index) / segment_duration if segment_duration > 0 else 0
    
    # Apply an easing function based on the action in the segment.
    if segment_idx in [0, 5]:  # Crouch and Recovery: Smooth start and end.
        s = ease_in_out_sine(t)
        current_coords = (1 - s) * start_pose + s * end_pose
    elif segment_idx == 1:  # Propulsion: Starts fast, slows down.
        s = ease_out_sine(t)
        current_coords = (1 - s) * start_pose + s * end_pose
    elif segment_idx in [2, 3]:  # Flight Phase: Special handling for parabolic arc.
        # Interpolate the base pose linearly for limb movement.
        base_pose = (1 - t) * start_pose + t * end_pose
        # Apply easing to vertical motion to simulate gravity's effect.
        y_start, y_end = start_pose[:, 1], end_pose[:, 1]
        s_y = ease_out_sine(t) if segment_idx == 2 else ease_in_sine(t)
        current_y = y_start + (y_end - y_start) * s_y
        base_pose[:, 1] = current_y
        current_coords = base_pose
    else:  # Landing Impact: Fast, linear motion is sufficient.
        current_coords = (1 - t) * start_pose + t * end_pose
    
    scatter.set_offsets(current_coords)
    return scatter,

# Create the animation object.
# interval: Delay between frames in ms. 30ms -> ~33 FPS.
# blit=True: Optimizes animation by only redrawing changed parts.
ani = animation.FuncAnimation(fig, update, frames=total_frames,
                              interval=30, blit=True, repeat=True)

# Show the animation.
plt.show()
