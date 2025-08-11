
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fixed points
neck = (0, 9)
torso_center = (0, 7)
left_shoulder = (-2, 8)
right_shoulder = (2, 8)
left_hip = (-1, 5)
right_hip = (1, 5)

# Lengths of the limbs
length_upper_arm = np.sqrt(2)
length_forearm = np.sqrt(2)
length_thigh = 2
length_shin = 2

# Animation parameters
T = 2  # period in seconds
fps = 30
num_frames = int(T * fps)

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the points
points = ax.scatter([], [], color='white', s=50)

# Update function for animation
def update(frame):
    t = frame / fps
    # Compute angles in radians
    theta_head = (90 + 10 * np.sin(2 * np.pi * t / T)) * np.pi / 180
    theta_elbow_left = -10 * (1 - np.cos(2 * np.pi * t / T)) * np.pi / 180
    theta_elbow_right = 10 * (1 - np.cos(2 * np.pi * t / T)) * np.pi / 180
    theta_knee_left = 10 * (1 - np.cos(2 * np.pi * t / T)) * np.pi / 180
    theta_knee_right = 10 * (1 - np.cos(2 * np.pi * t / T)) * np.pi / 180
    # Fixed angles
    theta_shoulder_left = -135 * np.pi / 180
    theta_shoulder_right = -45 * np.pi / 180
    theta_hip_left = -90 * np.pi / 180
    theta_hip_right = -90 * np.pi / 180
    # Compute positions
    head_x = 0 + 1 * np.cos(theta_head)
    head_y = 9 + 1 * np.sin(theta_head)
    left_elbow_x = left_shoulder[0] + length_upper_arm * np.cos(theta_shoulder_left)
    left_elbow_y = left_shoulder[1] + length_upper_arm * np.sin(theta_shoulder_left)
    left_wrist_x = left_elbow_x + length_forearm * np.cos(theta_shoulder_left + theta_elbow_left)
    left_wrist_y = left_elbow_y + length_forearm * np.sin(theta_shoulder_left + theta_elbow_left)
    right_elbow_x = right_shoulder[0] + length_upper_arm * np.cos(theta_shoulder_right)
    right_elbow_y = right_shoulder[1] + length_upper_arm * np.sin(theta_shoulder_right)
    right_wrist_x = right_elbow_x + length_forearm * np.cos(theta_shoulder_right + theta_elbow_right)
    right_wrist_y = right_elbow_y + length_forearm * np.sin(theta_shoulder_right + theta_elbow_right)
    left_knee_x = left_hip[0] + length_thigh * np.cos(theta_hip_left)
    left_knee_y = left_hip[1] + length_thigh * np.sin(theta_hip_left)
    left_ankle_x = left_knee_x + length_shin * np.cos(theta_hip_left + theta_knee_left)
    left_ankle_y = left_knee_y + length_shin * np.sin(theta_hip_left + theta_knee_left)
    right_knee_x = right_hip[0] + length_thigh * np.cos(theta_hip_right)
    right_knee_y = right_hip[1] + length_thigh * np.sin(theta_hip_right)
    right_ankle_x = right_knee_x + length_shin * np.cos(theta_hip_right + theta_knee_right)
    right_ankle_y = right_knee_y + length_shin * np.sin(theta_hip_right + theta_knee_right)
    # Collect all points
    x = [head_x, neck[0], torso_center[0], left_shoulder[0], right_shoulder[0],
         left_elbow_x, right_elbow_x, left_wrist_x, right_wrist_x,
         left_hip[0], right_hip[0], left_knee_x, right_knee_x, left_ankle_x, right_ankle_x]
    y = [head_y, neck[1], torso_center[1], left_shoulder[1], right_shoulder[1],
         left_elbow_y, right_elbow_y, left_wrist_y, right_wrist_y,
         left_hip[1], right_hip[1], left_knee_y, right_knee_y, left_ankle_y, right_ankle_y]
    # Update scatter plot
    points.set_offsets(np.c_[x, y])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.show()
