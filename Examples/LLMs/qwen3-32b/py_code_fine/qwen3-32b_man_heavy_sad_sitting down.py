
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the joints and their motion for a sad man sitting down
# We'll simulate the joint positions over time (frames)
# We will assume a simplified 2D model of 15 joints

# Define a function to simulate the motion of the sad man sitting down
def get_joint_positions(t):
    # t is a normalized time between 0 and 1
    # Define joint positions at time t
    # Each joint is represented as [x, y]

    # Initial joint positions (standing)
    base_positions = np.array([
        [0, 0],     # 0: pelvis
        [0, 1],     # 1: spine
        [0, 2],     # 2: head
        [-0.5, 0],  # 3: left hip
        [0, -1],    # 4: left knee
        [-0.5, -2], # 5: left ankle
        [0.5, 0],   # 6: right hip
        [0, -1],    # 7: right knee
        [0.5, -2],  # 8: right ankle
        [-0.3, 1.5],# 9: left shoulder
        [-0.3, 2.5],# 10: left elbow
        [-0.3, 3.5],# 11: left hand
        [0.3, 1.5], # 12: right shoulder
        [0.3, 2.5], # 13: right elbow
        [0.3, 3.5], # 14: right hand
    ])

    # Apply motion over time to simulate sitting down with a sad posture
    t = np.clip(t, 0, 1)  # Ensure t is between 0 and 1

    # Pelvis and spine move down and slightly forward
    pelvis_offset = np.array([0.0, -2 * t])
    spine_offset = np.array([0.0, -1.5 * t])
    head_offset = np.array([0.0, -0.5 * t])

    # Hips move down and slightly inward (sad posture)
    left_hip_offset = np.array([0.0, -1.5 * t])
    right_hip_offset = np.array([0.0, -1.5 * t])

    # Knees and ankles bend
    left_knee_offset = np.array([0.0, -1.5 * t])
    left_ankle_offset = np.array([0.0, -1.5 * t])
    right_knee_offset = np.array([0.0, -1.5 * t])
    right_ankle_offset = np.array([0.0, -1.5 * t])

    # Shoulders drop slightly
    left_shoulder_offset = np.array([0.0, -0.5 * t])
    right_shoulder_offset = np.array([0.0, -0.5 * t])

    # Elbows and hands move down and inward (slumped posture)
    left_elbow_offset = np.array([0.0, -1.5 * t])
    left_hand_offset = np.array([0.0, -2.5 * t])
    right_elbow_offset = np.array([0.0, -1.5 * t])
    right_hand_offset = np.array([0.0, -2.5 * t])

    # Apply the offsets
    base_positions[0] += pelvis_offset
    base_positions[1] += spine_offset
    base_positions[2] += head_offset
    base_positions[3] += left_hip_offset
    base_positions[4] += left_knee_offset
    base_positions[5] += left_ankle_offset
    base_positions[6] += right_hip_offset
    base_positions[7] += right_knee_offset
    base_positions[8] += right_ankle_offset
    base_positions[9] += left_shoulder_offset
    base_positions[10] += left_elbow_offset
    base_positions[11] += left_hand_offset
    base_positions[12] += right_shoulder_offset
    base_positions[13] += right_elbow_offset
    base_positions[14] += right_hand_offset

    return base_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Black background
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axis('off')

# Create 15 white points (joints)
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(15)]

# Animation function
def animate(t):
    positions = get_joint_positions(t)
    for i, point in enumerate(points):
        point.set_data(positions[i][0], positions[i][1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
