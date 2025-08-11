
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This program creates a point-light animation of a sad man with heavy weight
# performing a forward roll.

# The 15 points represent the major joints of a human figure.
# The order is:
# 0: Head
# 1: Sternum (between shoulders)
# 2: Pelvis (center of hips)
# 3, 4: Left/Right Shoulder
# 5, 6: Left/Right Elbow
# 7, 8: Left/Right Wrist
# 9, 10: Left/Right Hip
# 11, 12: Left/Right Knee
# 13, 14: Left/Right Ankle

# Keyframes define the pose of the figure at critical moments in the animation.
# Each keyframe is a list of 15 points, and each point is an [x, y] coordinate.
keyframes = [
    # KF 0: Start in a deep, slumped crouch on the left.
    [[-0.7, 0.1], [-0.8, 0.0], [-1.0, -0.2], [-0.9, 0.2], [-0.7, 0.2], [-0.7, -0.3], [-0.5, -0.3], [-0.6, -0.7], [-0.4, -0.7], [-1.1, -0.2], [-0.9, -0.2], [-1.2, -0.5], [-1.0, -0.5], [-1.3, -0.9], [-1.1, -0.9]],
    
    # KF 1: Tuck and push off the ground. Hips rise as the body prepares to roll.
    [[-0.9, -0.3], [-0.9, -0.1], [-1.0, 0.3], [-1.0, 0.0], [-0.8, 0.0], [-0.9, -0.5], [-0.7, -0.5], [-0.8, -0.9], [-0.6, -0.9], [-1.1, 0.3], [-0.9, 0.3], [-1.2, 0.1], [-1.0, 0.1], [-1.4, -0.2], [-1.2, -0.2]],
    
    # KF 2: Mid-roll, body is a ball, upside down on the shoulders/back.
    [[0.0, -1.0], [0.0, -0.7], [0.0, 0.6], [-0.1, -0.8], [0.1, -0.8], [-0.2, -0.5], [0.2, -0.5], [-0.3, -0.3], [0.3, -0.3], [-0.1, 0.6], [0.1, 0.6], [-0.1, 0.2], [0.1, 0.2], [-0.2, -0.1], [0.2, -0.1]],
    
    # KF 3: Roll completes, feet land, body uncurls into a crouch.
    [[0.6, 0.3], [0.6, 0.0], [0.6, -0.4], [0.5, 0.1], [0.7, 0.1], [0.8, -0.1], [1.0, -0.1], [1.0, -0.3], [1.2, -0.3], [0.5, -0.4], [0.7, -0.4], [0.6, -0.5], [0.8, -0.5], [0.7, -0.9], [0.9, -0.9]],
    
    # KF 4: A brief, struggling attempt to rise, showing the effort/weight.
    [[0.7, 0.6], [0.7, 0.3], [0.7, -0.1], [0.6, 0.4], [0.8, 0.4], [0.7, 0.1], [0.9, 0.1], [0.8, -0.2], [1.0, -0.2], [0.6, -0.1], [0.8, -0.1], [0.7, -0.4], [0.9, -0.4], [0.7, -0.9], [0.9, -0.9]],
    
    # KF 5: Slumps back down into a final, tired crouch on the right.
    [[1.0, 0.3], [1.0, 0.1], [1.0, -0.3], [0.9, 0.2], [1.1, 0.2], [0.8, -0.2], [1.2, -0.2], [0.7, -0.6], [1.3, -0.6], [0.9, -0.3], [1.1, -0.3], [0.8, -0.5], [1.0, -0.5], [0.9, -0.9], [1.1, -0.9]],
    
    # KF 6: A copy of the final keyframe to create a pause at the end.
    [[1.0, 0.3], [1.0, 0.1], [1.0, -0.3], [0.9, 0.2], [1.1, 0.2], [0.8, -0.2], [1.2, -0.2], [0.7, -0.6], [1.3, -0.6], [0.9, -0.3], [1.1, -0.3], [0.8, -0.5], [1.0, -0.5], [0.9, -0.9], [1.1, -0.9]]
]

keyframes = np.array(keyframes)
N_POINTS = keyframes.shape[1]

# Define the transitions between keyframes and the number of animation frames for each.
# This controls the pacing of the movement to appear slow and labored.
transitions = [
    (0, 1, 25),  # Crouch to Tuck
    (1, 2, 30),  # The main roll
    (2, 3, 30),  # Landing
    (3, 4, 20),  # Struggling up
    (4, 5, 25),  # Slumping back down
    (5, 6, 20),  # Pause at the end
]

# Generate all intermediate frames using linear interpolation for smooth motion.
all_frames_list = []
for start_kf_idx, end_kf_idx, num_frames in transitions:
    start_frame = keyframes[start_kf_idx]
    end_frame = keyframes[end_kf_idx]
    
    # Create the frames for this specific transition
    transition_frames = np.zeros((num_frames, N_POINTS, 2))
    for p in range(N_POINTS):
        transition_frames[:, p, 0] = np.linspace(start_frame[p, 0], end_frame[p, 0], num_frames)
        transition_frames[:, p, 1] = np.linspace(start_frame[p, 1], end_frame[p, 1], num_frames)
    all_frames_list.append(transition_frames)

# Combine all transitions into a single sequence of frames.
all_frames = np.concatenate(all_frames_list, axis=0)
TOTAL_FRAMES = all_frames.shape[0]

# Set up the plot for the animation.
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
fig.set_facecolor('black')

# Set plot limits to ensure the entire animation is visible without rescaling.
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect('equal', adjustable='box')

# Hide the axes' ticks, labels, and spines for a clean look.
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Create the initial scatter plot object with the first frame's data.
scatter = ax.scatter(all_frames[0, :, 0], all_frames[0, :, 1], c='white', s=80)

# The update function is called for each frame of the animation.
def update(frame):
    # Update the positions of the 15 points.
    scatter.set_offsets(all_frames[frame])
    return scatter,

# Create the animation using FuncAnimation.
# interval: delay between frames in milliseconds.
# blit=True optimizes rendering by only redrawing the parts that have changed.
# repeat=True makes the animation loop.
ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=40, blit=True, repeat=True)

# Display the animation.
plt.show()
