
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-0.2, 2.5))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)

# Constants
H = 2.0  # Body height
R = H / 2.0  # Circle radius
total_frames = 100  # Total animation frames

# Define 15 body points in standing pose [x, y, z]
standing = np.array([
    [0.0, 2.0, 0.0],    # head_top
    [0.5, 1.8, 0.0],    # right_shoulder
    [0.8, 1.6, 0.0],    # right_elbow
    [0.9, 1.4, 0.0],    # right_hand
    [-0.5, 1.8, 0.0],   # left_shoulder
    [-0.8, 1.6, 0.0],   # left_elbow
    [-0.9, 1.4, 0.0],   # left_hand
    [0.0, 1.7, 0.0],    # chest
    [0.0, 1.5, 0.0],    # waist
    [0.4, 1.2, 0.0],    # right_hip
    [0.5, 0.6, 0.0],    # right_knee
    [0.5, 0.0, 0.0],    # right_ankle
    [-0.4, 1.2, 0.0],   # left_hip
    [-0.5, 0.6, 0.0],   # left_knee
    [-0.5, 0.0, 0.0]    # left_ankle
])

# Calculate initial angles for each point
angle_i = np.pi * standing[:, 1] / H
theta_rot = np.radians(30)  # Rotation angle for 3/4 view

# Animation update function
def update(frame):
    new_coords = []
    t = frame / total_frames
    if frame <= 20:  # Morph to circle (frames 0-20)
        t_phase = frame / 20.0
        for i in range(15):
            y_circle = R * (1 - np.cos(angle_i[i]))
            z_circle = R * np.sin(angle_i[i])
            x = standing[i, 0] * (1 - t_phase)  # Reduce width while morphing
            y = (1 - t_phase) * standing[i, 1] + t_phase * y_circle
            z = t_phase * z_circle
            # Rotate for 3/4 view
            x_rot = x * np.cos(theta_rot) - z * np.sin(theta_rot)
            y_rot = y
            new_coords.append([x_rot, y_rot])
            
    elif frame <= 80:  # Rolling phase (frames 21-80)
        roll_progress = (frame - 20) / 60.0
        global_angle = 2 * np.pi * roll_progress
        for i in range(15):
            angle = angle_i[i] + global_angle
            x_orig = standing[i, 0] * 0.4  # Tuck width reduced
            y = R * (1 - np.cos(angle))
            z = R * np.sin(angle)
            # Rotate for 3/4 view
            x_rot = x_orig * np.cos(theta_rot) - z * np.sin(theta_rot)
            y_rot = y
            new_coords.append([x_rot, y_rot])
            
    else:  # Morph to stand (frames 81-100)
        t_phase = (frame - 80) / 20.0
        for i in range(15):
            y_circle = R * (1 - np.cos(angle_i[i]))
            z_circle = R * np.sin(angle_i[i])
            x = standing[i, 0] * t_phase  # Restore width
            y = (t_phase) * standing[i, 1] + (1 - t_phase) * y_circle
            z = (1 - t_phase) * z_circle
            # Rotate for 3/4 view
            x_rot = x * np.cos(theta_rot) - z * np.sin(theta_rot)
            y_rot = y
            new_coords.append([x_rot, y_rot])
            
    new_coords = np.array(new_coords).T
    points.set_data(new_coords[0], new_coords[1])
    return points,

# Create animation
ani = FuncAnimation(
    fig, 
    update, 
    frames=total_frames, 
    interval=50, 
    blit=True
)
plt.show()
