
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure:
# 0-Head, 1-Neck, 2-Spine, 3-Hips, 4-Left Shoulder, 5-Right Shoulder,
# 6-Left Elbow, 7-Right Elbow, 8-Left Wrist, 9-Right Wrist,
# 10-Left Hip, 11-Right Hip, 12-Left Knee, 13-Right Knee, 14-Left Ankle

initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.8], # Neck
    [0, 0.6], # Spine
    [0, 0.2], # Hips
    [-0.3, 0.8], # Left Shoulder
    [0.3, 0.8],  # Right Shoulder
    [-0.5, 0.5], # Left Elbow
    [0.5, 0.5],  # Right Elbow
    [-0.7, 0.3], # Left Wrist
    [0.7, 0.3],  # Right Wrist
    [-0.2, 0.2], # Left Hip
    [0.2, 0.2],  # Right Hip
    [-0.2, -0.2], # Left Knee
    [0.2, -0.2], # Right Knee
    [0, -0.5]    # Left Ankle (assuming right ankle is symmetric)
])

# Define the keyframes for the bowing motion
# Keyframe 1: Upright position
keyframe1 = initial_positions.copy()

# Keyframe 2: Bowing position (head down, spine curved, arms slightly forward)
keyframe2 = initial_positions.copy()
keyframe2[0] = [0, 0.5]  # Head moves down
keyframe2[1] = [0, 0.4]  # Neck curves
keyframe2[2] = [0, 0.3]  # Spine curves
keyframe2[3] = [0, 0.1]  # Hips move slightly down
keyframe2[4] = [-0.3, 0.6]  # Left shoulder moves slightly forward
keyframe2[5] = [0.3, 0.6]   # Right shoulder moves slightly forward
keyframe2[6] = [-0.5, 0.4]  # Left elbow moves slightly forward
keyframe2[7] = [0.5, 0.4]   # Right elbow moves slightly forward
keyframe2[8] = [-0.7, 0.2]  # Left wrist moves slightly forward
keyframe2[9] = [0.7, 0.2]   # Right wrist moves slightly forward
keyframe2[10] = [-0.2, 0.1] # Left hip moves slightly down
keyframe2[11] = [0.2, 0.1]  # Right hip moves slightly down
keyframe2[12] = [-0.2, -0.3] # Left knee moves slightly down
keyframe2[13] = [0.2, -0.3] # Right knee moves slightly down
keyframe2[14] = [0, -0.7]   # Left ankle moves slightly down

# Interpolate between keyframes to create smooth motion
num_frames = 50
interpolated_positions = []
for t in np.linspace(0, 1, num_frames):
    interpolated_positions.append((1 - t) * keyframe1 + t * keyframe2)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Plot the initial positions
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

def update(frame):
    scatter.set_offsets(interpolated_positions[frame])
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
