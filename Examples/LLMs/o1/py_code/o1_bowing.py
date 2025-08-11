import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base (rest) coordinates for 15 points in a standing pose (x, y).
# The pivot (hips) is at (0,4). Everything above hips will rotate.
base_points = np.array([
    [ 0,10],  # Head
    [ 0, 8],  # Neck
    [ 2, 8],  # Right Shoulder
    [ 2, 6],  # Right Elbow
    [ 2, 4],  # Right Wrist
    [-2, 8],  # Left Shoulder
    [-2, 6],  # Left Elbow
    [-2, 4],  # Left Wrist
    [ 0, 4],  # Hips (pivot)
    [ 1, 4],  # Right Hip
    [ 1, 2],  # Right Knee
    [ 1, 0],  # Right Ankle
    [-1, 4],  # Left Hip
    [-1, 2],  # Left Knee
    [-1, 0]   # Left Ankle
], dtype=float)

pivot_index = 8  # index of hips in base_points
pivot = base_points[pivot_index].copy()

# Number of frames in the animation
frames = 60

def rotate_point(point, center, theta):
    # Rotate a 2D point around a center by angle theta (radians)
    # Using standard 2D rotation around (0,0), then translate back
    shift = point - center
    c, s = np.cos(theta), np.sin(theta)
    x_new = c * shift[0] - s * shift[1]
    y_new = s * shift[0] + c * shift[1]
    return np.array([x_new, y_new]) + center

def get_angle(frame):
    # First half: 0 to 30 => angle 0 to 45 deg
    # Second half: 30 to 60 => angle 45 to 0 deg
    if frame <= 30:
        return np.radians(45.0 * frame / 30.0)
    else:
        return np.radians(45.0 - 45.0 * (frame - 30) / 30.0)

def get_frame_data(frame):
    angle = get_angle(frame)
    new_points = base_points.copy()
    # Rotate all joints above the hips around the pivot
    for i in range(len(new_points)):
        # Exclude legs and hips themselves from rotation
        # Indices 9,10,11,12,13,14 may remain unrotated
        if i < 9:  # head, neck, shoulders, elbows, wrists
            new_points[i] = rotate_point(new_points[i], pivot, angle)
    return new_points

# Setup the plot
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, facecolor='black')
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 11)
plt.axis('off')

# Create scatter object for the points (white on black)
scatter = ax.scatter(base_points[:, 0], base_points[:, 1], c='white', s=50)

def init():
    scatter.set_offsets(base_points)
    return (scatter,)

def update(frame):
    pts = get_frame_data(frame)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(
    fig, update, frames=frames, init_func=init, blit=True, interval=50, repeat=True
)

plt.show()