
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define skeleton points in 3D space (base frame, facing +z)
points_3d = np.array([
    [0.00, 1.75, 0.00],  # Head (top)
    [0.00, 1.65, 0.00],  # Neck
    [0.00, 1.40, 0.00],  # Center shoulder (torso)
    [-0.25, 1.65, 0.00], # Left shoulder
    [0.25, 1.65, 0.00],  # Right shoulder
    [-0.45, 1.40, 0.00], # Left elbow
    [0.45, 1.40, 0.00],  # Right elbow
    [-0.60, 1.10, 0.00], # Left hand
    [0.60, 1.10, 0.00],  # Right hand
    [0.00, 0.90, 0.00],  # Spine base (hip center)
    [-0.15, 0.90, 0.00], # Left hip
    [0.15, 0.90, 0.00],  # Right hip
    [-0.15, 0.40, 0.00], # Left knee
    [0.15, 0.40, 0.00],  # Right knee
    [-0.15, 0.05, 0.00]  # Left foot (ankle)
])

# Define the angles for a typical turning sequence (in degrees)
rotation_sequence = [0, 45, 90, 135, 180, 225, 270, 315, 360]

# Set up figure and axis
fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.grid(False)
ax.set_axis_off()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-0.5, 2.0])

# Initialize scatter plot for point lights
scatter = ax.scatter([], [], [], s=70, c='white', edgecolors='none')

# Calculate intermediate frames using cubic spline interpolation
def create_smooth_rotation_sequence(n_frames=100):
    from scipy.interpolate import CubicSpline
    keyframes = np.linspace(0, 1, len(rotation_sequence))
    angles = CubicSpline(keyframes, rotation_sequence, bc_type='periodic')(np.linspace(0, 1, n_frames))
    return angles

# Rotate function using rotation matrix around Y axis
def rotate_y(points, angle_deg):
    theta = np.radians(angle_deg)
    rotation = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return np.dot(points, rotation.T)

# Animation update function
def update(frame):
    angles = create_smooth_rotation_sequence()
    rotated_points = rotate_y(points_3d, angles[frame])
    
    # Weight shift simulation (forward/backward to simulate turning effort)
    weight_shift = -0.15 * np.cos(np.radians(2 * angles[frame]))
    shifted_points = rotated_points.copy()
    shifted_points[:] += [0, 0, weight_shift]
    
    # Arm swing simulation (natural arm movement during turn)
    arm_swing = 0.05 * np.sin(np.radians(4 * angles[frame]))
    shifted_points[3:9] += [0, 0, arm_swing]
    
    # Head movement (slight bobbing)
    head_bob = 0.01 * np.sin(np.radians(6 * angles[frame]))
    shifted_points[0:2] += [0, head_bob, 0]
    
    # Update scatter plot data
    scatter._offsets3d = (shifted_points[:,0], shifted_points[:,1], shifted_points[:,2])
    return scatter,

# Create animation
n_frames = 200
ani = FuncAnimation(fig, update, frames=n_frames, blit=True, interval=40)
plt.tight_layout(pad=0)
plt.show()
