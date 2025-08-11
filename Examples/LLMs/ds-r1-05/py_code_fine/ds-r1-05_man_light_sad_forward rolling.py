
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

# Define key poses for a forward roll
def get_key_poses():
    pose0 = np.array([  # Standing
        [0.0, 1.7], [0.0, 1.5], [-0.2, 1.5], [-0.2, 1.2], [-0.2, 0.9],
        [0.2, 1.5], [0.2, 1.2], [0.2, 0.9], [0.0, 1.0],
        [-0.2, 1.0], [-0.2, 0.5], [-0.2, 0.0],
        [0.2, 1.0], [0.2, 0.5], [0.2, 0.0]
    ])
    pose1 = np.array([  # Hands on ground
        [0.0, 1.2], [0.2, 1.0], [-0.2, 1.0], [-0.3, 0.5], [-0.4, 0.0],
        [0.2, 1.0], [0.3, 0.5], [0.4, 0.0], [0.0, 0.8],
        [-0.2, 0.8], [-0.2, 0.3], [-0.2, 0.0],
        [0.2, 0.8], [0.2, 0.3], [0.2, 0.0]
    ])
    pose2 = np.array([  # Tucked rolling
        [0.0, 0.5], [0.0, 0.7], [-0.2, 0.7], [-0.3, 0.8], [-0.4, 0.9],
        [0.2, 0.7], [0.3, 0.8], [0.4, 0.9], [0.0, 0.9],
        [-0.1, 0.9], [-0.1, 0.6], [-0.05, 0.4],
        [0.1, 0.9], [0.1, 0.6], [0.05, 0.4]
    ])
    pose3 = np.array([  # Halfway through
        [0.0, 0.2], [0.0, 0.4], [-0.2, 0.4], [-0.2, 0.6], [-0.2, 0.8],
        [0.2, 0.4], [0.2, 0.6], [0.2, 0.8], [0.0, 0.9],
        [-0.2, 0.9], [-0.2, 1.2], [-0.2, 1.5],
        [0.2, 0.9], [0.2, 1.2], [0.2, 1.5]
    ])
    pose4 = np.array([  # Landing
        [0.0, 1.2], [0.0, 1.0], [-0.2, 0.9], [-0.4, 0.8], [-0.5, 0.7],
        [0.2, 0.9], [0.4, 0.8], [0.5, 0.7], [0.0, 0.7],
        [-0.2, 0.7], [-0.2, 0.3], [-0.2, 0.0],
        [0.2, 0.7], [0.2, 0.3], [0.2, 0.0]
    ])
    pose5 = pose0.copy()  # Back to standing
    return [pose0, pose1, pose2, pose3, pose4, pose5]

# Precompute trajectory for smooth animation
def generate_trajectory(key_poses, total_frames=100):
    trajectory = np.zeros((total_frames + 1, 15, 2))
    key_frames = [0, 20, 40, 60, 80, 100]
    for frame in range(total_frames + 1):
        if frame in key_frames:
            k = key_frames.index(frame)
            trajectory[frame] = key_poses[k]
        else:
            for i, kf in enumerate(key_frames[:-1]):
                if kf <= frame < key_frames[i + 1]:
                    start_pose = key_poses[i]
                    end_pose = key_poses[i + 1]
                    fraction = (frame - kf) / (key_frames[i + 1] - kf)
                    trajectory[frame] = (1 - fraction) * start_pose + fraction * end_pose
                    break
    return trajectory

# Set up animation
key_poses = get_key_poses()
trajectory = generate_trajectory(key_poses, total_frames=100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.2, 2.2)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Point-Light Stimulus: Forward Roll', color='white')

scat = ax.scatter([], [], s=60, c='white', edgecolors='none')

def update(frame):
    points = trajectory[frame]
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=101, interval=50, blit=True
)

plt.tight_layout()
plt.show()
