import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define 15 key joints in a standing posture (x, y).
# Approximate human figure in 2D (units in arbitrary scale).
# Joints are in this order: [head, neck, r_shoulder, l_shoulder, r_elbow, l_elbow,
#                           r_wrist, l_wrist, torso, r_hip, l_hip, r_knee, l_knee,
#                           r_ankle, l_ankle]
STANDING = np.array([
    [0.0, 1.70],  # head
    [0.0, 1.50],  # neck
    [0.2, 1.50],  # right shoulder
    [-0.2, 1.50], # left shoulder
    [0.3, 1.20],  # right elbow
    [-0.3, 1.20], # left elbow
    [0.3, 0.90],  # right wrist
    [-0.3, 0.90], # left wrist
    [0.0, 1.10],  # torso (mid-spine)
    [0.15, 0.95], # right hip
    [-0.15, 0.95],# left hip
    [0.15, 0.60], # right knee
    [-0.15, 0.60],# left knee
    [0.15, 0.30], # right ankle
    [-0.15, 0.30] # left ankle
])

def rotate_around(point, pivot, angle_radians):
    # Rotate "point" around "pivot" by "angle_radians" in 2D
    # Rotation in counter-clockwise direction.
    px, py = pivot
    x, y = point
    # Translate so pivot is origin
    x -= px
    y -= py
    # Apply rotation
    cos_a, sin_a = np.cos(angle_radians), np.sin(angle_radians)
    rx = x*cos_a - y*sin_a
    ry = x*sin_a + y*cos_a
    # Translate back
    rx += px
    ry += py
    return np.array([rx, ry])

def generate_bowed_posture(standing_points, bow_angle_degs=60.0):
    """
    Returns a bowed posture array for the upper body by rotating points around the hips.
    We'll pivot around an average of both hips for the trunk and arms,
    leaving legs/ankles/hips themselves in standing position.
    """
    bowed = standing_points.copy()
    angle_radians = np.radians(bow_angle_degs)

    # We'll treat both hips as an approximate pivot for the upper body.
    # (r_hip index = 9, l_hip index = 10)
    pivot = (bowed[9] + bowed[10]) / 2.0  # midpoint of both hips

    # Indices for the upper body: head=0, neck=1, r_shoulder=2, l_shoulder=3,
    # r_elbow=4, l_elbow=5, r_wrist=6, l_wrist=7, torso=8.
    upper_body_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for idx in upper_body_indices:
        bowed[idx] = rotate_around(bowed[idx], pivot, angle_radians)

    # To simulate "heaviness", we lower the torso and shoulders slightly
    # by shifting them downward.
    shift_down = 0.05
    for idx in upper_body_indices:
        bowed[idx, 1] -= shift_down

    return bowed

BOWED = generate_bowed_posture(STANDING)

def interpolate_positions(standing_pts, bowed_pts, fraction):
    """
    Linear interpolation between standing_pts and bowed_pts.
    fraction=0 -> fully standing
    fraction=1 -> fully bowed
    """
    return standing_pts + (bowed_pts - standing_pts) * fraction

def get_frame_positions(frame, total_frames):
    """
    Returns the 2D positions of each of the 15 joints for a given frame.
    Use a smooth (cosine-based) function for a bowing cycle:
      fraction = 0.5 - 0.5*cos(2*pi*(frame/total_frames))
    which moves from 0 to 1 and back to 0 as frame goes 0..total_frames/2..total_frames.
    """
    # We'll do one full bow-and-return cycle in total_frames frames:
    # fraction moves 0 -> 1 -> 0 from frame=0 -> total_frames.
    fraction = 0.5 - 0.5 * np.cos(2.0 * np.pi * frame / total_frames)
    return interpolate_positions(STANDING, BOWED, fraction)

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
scat = ax.scatter([], [], c='white', s=30)
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
plt.axis('off')

def init():
    scat.set_offsets([])
    return (scat,)

def update(frame):
    # Compute new positions for all 15 points
    positions = get_frame_positions(frame, total_frames=100)
    scat.set_offsets(positions)
    return (scat,)

ani = FuncAnimation(
    fig, update, frames=100, init_func=init,
    interval=50, blit=True, repeat=True
)

if __name__ == "__main__":
    plt.show()