
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 joints of a human (biological motion)
joint_names = [
    'hips', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
    'left_ankle', 'right_ankle', 'torso', 'left_shoulder', 'right_shoulder',
    'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'head'
]

# Initial joint positions (approximate skeleton)
joint_positions = np.array([
    [0, 0],  # hips
    [-2, -2],  # left_hip
    [2, -2],  # right_hip
    [-3, -4],  # left_knee
    [3, -4],  # right_knee
    [-4, -7],  # left_ankle
    [4, -7],  # right_ankle
    [0, 2],  # torso
    [-1.5, 3],  # left_shoulder
    [1.5, 3],  # right_shoulder
    [-2, 5],  # left_elbow
    [2, 5],  # right_elbow
    [-2.5, 7],  # left_wrist
    [2.5, 7],  # right_wrist
    [0, 4]  # head
])

# Create scatter points for each joint
scat = ax.scatter(joint_positions[:, 0], joint_positions[:, 1], c='white', s=100, zorder=2)

# Define a function to generate a forward rolling motion with a heavy feeling
# and a happy emotion (bouncy, but grounded)
def animate(t):
    t = t / 10  # slow it down

    # Forward rolling motion with a heavy feeling
    global joint_positions

    # Base forward motion (hips and torso)
    joint_positions[0] = [t, 0]  # hips
    joint_positions[6] = [t, 2]  # torso

    # Rolling motion: legs
    leg_amp = 2.5
    leg_freq = 1.2
    joint_positions[1] = [t - 2 * np.sin(t * leg_freq), -2 + 0.5 * np.cos(t * leg_freq)]  # left_hip
    joint_positions[2] = [t + 2 * np.sin(t * leg_freq), -2 + 0.5 * np.cos(t * leg_freq)]  # right_hip
    joint_positions[3] = [t - 3 * np.sin(t * leg_freq), -4 + 0.5 * np.cos(t * leg_freq)]  # left_knee
    joint_positions[4] = [t + 3 * np.sin(t * leg_freq), -4 + 0.5 * np.cos(t * leg_freq)]  # right_knee
    joint_positions[5] = [t - 4 * np.sin(t * leg_freq), -7 + 0.5 * np.cos(t * leg_freq)]  # left_ankle
    joint_positions[6] = [t + 4 * np.sin(t * leg_freq), -7 + 0.5 * np.cos(t * leg_freq)]  # right_ankle

    # Happy emotion: bouncy arms
    arm_amp = 1.5
    arm_freq = 1.5
    joint_positions[7] = [t - 1.5, 3 + arm_amp * np.sin(t * arm_freq)]  # left_shoulder
    joint_positions[8] = [t + 1.5, 3 + arm_amp * np.sin(t * arm_freq)]  # right_shoulder
    joint_positions[9] = [t - 2, 5 + 0.8 * np.sin(t * arm_freq)]  # left_elbow
    joint_positions[10] = [t + 2, 5 + 0.8 * np.sin(t * arm_freq)]  # right_elbow
    joint_positions[11] = [t - 2.5, 7 + 0.5 * np.sin(t * arm_freq)]  # left_wrist
    joint_positions[12] = [t + 2.5, 7 + 0.5 * np.sin(t * arm_freq)]  # right_wrist

    # Head bounces slightly for happy emotion
    joint_positions[13] = [t, 4 + 0.3 * np.sin(t * arm_freq)]  # head

    # Update the scatter plot
    scat.set_offsets(joint_positions)

    return scat,

# Create animation
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()
