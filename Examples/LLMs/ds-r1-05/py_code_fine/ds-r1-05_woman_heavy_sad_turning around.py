
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial 3D points: (x, y, z) with posture reflecting a sad, heavy woman
points_3d = np.array([
    (0, 0.8, 0.2),    # Head - lowered and leaning forward
    (0, 0.7, 0.15),   # Neck
    (-0.3, 0.6, 0.1), # Left shoulder
    (0.3, 0.6, 0.1),  # Right shoulder
    (-0.4, 0.35, 0.0),# Left elbow
    (0.4, 0.35, 0.0), # Right elbow
    (-0.42, 0.1, -0.1),# Left wrist
    (0.42, 0.1, -0.1),# Right wrist
    (0, 0.55, 0.0),   # Sternum (mid-torso)
    (0, 0.25, 0.0),   # Spine (base of rib cage)
    (-0.15, 0.0, 0.0),# Left hip
    (0.15, 0.0, 0.0), # Right hip
    (-0.15, -0.5, 0.0),# Left knee
    (0.15, -0.5, 0.0), # Right knee
    (-0.15, -0.9, 0.0) # Left ankle
])

# Total points: 15

# Set up the figure and axis
fig = plt.figure(figsize=(6, 6), facecolor='black')
ax = fig.add_subplot(111, aspect='equal')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Initialize scatter plot for the points
scatter = ax.scatter([], [], s=40, c='white', edgecolor='none')

# Camera distance for perspective
camera_distance = 3

def rotate_point(point, angle):
    """Rotate a point around the y-axis by given angle in radians."""
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    x, y, z = point
    # Rotation around y-axis
    x_new = x * cos_a + z * sin_a
    z_new = -x * sin_a + z * cos_a
    return (x_new, y, z_new)

def project_3d_to_2d(point_3d):
    """Project a 3D point to 2D using perspective projection."""
    x, y, z = point_3d
    # Perspective projection
    factor = camera_distance / (camera_distance + z)
    x_proj = x * factor
    y_proj = y * factor
    return (x_proj, y_proj)

def update_animation(frame, total_frames=150):
    """Update function for animation frames."""
    # Calculate rotation progress: 0 to 360 degrees over total_frames
    progress = frame / total_frames
    angle = 2 * np.pi * progress
    
    # Apply sinusoidal variations to the torso and head for realistic movement
    head_nod = 0.1 * np.sin(2 * angle)  # Simulate head nodding slightly
    spine_curve = 0.08 * np.sin(4 * angle)  # Gentle spine movement
    
    rotated_points = []
    for idx, point in enumerate(points_3d):
        # Adjust posture dynamically
        if idx == 0:  # Head
            x, y, z = point
            rotated = rotate_point((x, y + head_nod, z), angle)
        elif idx == 10 or idx == 9:  # Spine and sternum
            x, y, z = point
            rotated = rotate_point((x, y + spine_curve, z), angle)
        else:
            rotated = rotate_point(point, angle)
        rotated_points.append(rotated)
    
    # Project all rotated 3D points to 2D
    projected_2d = [project_3d_to_2d(p) for p in rotated_points]
    x_vals = [p[0] for p in projected_2d]
    y_vals = [p[1] for p in projected_2d]
    
    # Update scatter plot data
    scatter.set_offsets(np.column_stack([x_vals, y_vals]))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, 
    update_animation, 
    frames=150, 
    interval=50,  # 20 fps: 50 ms per frame
    blit=True
)

plt.show()
