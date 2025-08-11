import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define base skeleton points (15 total) in a neutral pose (x, y)
# Indices:
# 0 - head
# 1 - left shoulder
# 2 - right shoulder
# 3 - left elbow
# 4 - right elbow
# 5 - left hand
# 6 - right hand
# 7 - chest
# 8 - center hips
# 9 - left hip
# 10 - right hip
# 11 - left knee
# 12 - right knee
# 13 - left foot
# 14 - right foot

base_points = np.array([
    [0.0,  0.60],  # head
    [-0.20, 0.45], # left shoulder
    [ 0.20, 0.45], # right shoulder
    [-0.25, 0.25], # left elbow
    [ 0.25, 0.25], # right elbow
    [-0.30, 0.10], # left hand
    [ 0.30, 0.10], # right hand
    [ 0.00, 0.40], # chest
    [ 0.00, 0.00], # center hips
    [-0.10, 0.00], # left hip
    [ 0.10, 0.00], # right hip
    [-0.10,-0.40], # left knee
    [ 0.10,-0.40], # right knee
    [-0.10,-0.80], # left foot
    [ 0.10,-0.80]  # right foot
])

def rotate_point(px, py, cx, cy, angle_rad):
    """Rotate point (px, py) around center (cx, cy) by angle_rad (radians)."""
    dx, dy = px - cx, py - cy
    cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)
    rx = cx + cos_a * dx - sin_a * dy
    ry = cy + sin_a * dx + cos_a * dy
    return rx, ry

def get_positions(frame):
    """
    Returns the 2D positions of all 15 points at a given animation frame,
    creating a hand-waving motion (right arm) plus slight body bobbing.
    """
    # Copy base points
    points = base_points.copy()

    # Time parameter
    t = frame / 30.0  # 30 FPS assumption

    # Small vertical bobbing for a "happy" effect
    bob_offset = 0.05 * np.sin(2 * np.pi * t / 6.0)  # 6-second period
    points[:,1] += bob_offset

    # Waving angles (in degrees, converted to radians)
    # Shoulder wave
    shoulder_angle_deg = 20.0 * np.sin(2.0 * np.pi * t / 3.0)
    shoulder_angle_rad = np.deg2rad(shoulder_angle_deg)
    # Elbow wave
    elbow_angle_deg = 20.0 * np.sin(2.0 * np.pi * t / 3.0 + np.pi)
    elbow_angle_rad = np.deg2rad(elbow_angle_deg)

    # Indices for right shoulder, right elbow, right hand
    RSHO = 2
    RELB = 4
    RHND = 6

    # 1) Rotate elbow and hand about the right shoulder
    rsx, rsy = points[RSHO]
    ex, ey = points[RELB]
    hx, hy = points[RHND]

    exr, eyr = rotate_point(ex, ey, rsx, rsy, shoulder_angle_rad)
    hxr, hyr = rotate_point(hx, hy, rsx, rsy, shoulder_angle_rad)

    points[RELB] = [exr, eyr]
    points[RHND] = [hxr, hyr]

    # 2) Rotate hand about the (now-moved) elbow
    exr, eyr = points[RELB]
    hx, hy = points[RHND]
    hxr2, hyr2 = rotate_point(hx, hy, exr, eyr, elbow_angle_rad)
    points[RHND] = [hxr2, hyr2]

    return points

# Set up the figure and axes
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim([-0.6, 0.6])
ax.set_ylim([-1.0, 0.7])
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot for 15 points
scatter = ax.scatter([], [], c='white', s=40)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    positions = get_positions(frame)
    scatter.set_offsets(positions)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, update, init_func=init, frames=600, interval=33, blit=True, repeat=True
)

plt.show()