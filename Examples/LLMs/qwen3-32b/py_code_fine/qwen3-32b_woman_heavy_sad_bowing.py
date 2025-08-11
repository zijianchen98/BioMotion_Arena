
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define joint positions over time for a sad woman bowing with heavy weight
# This is a simplified representation of biological motion for demonstration purposes

# Time frames
num_frames = 60
num_joints = 15

# Initialize joint positions (x, y)
positions = np.zeros((num_frames, num_joints, 2))

# Define a simple motion for a sad bowing action
# These are approximate joint positions in a 2D space
# Joint indices: 0=neck, 1=left shoulder, 2=right shoulder, 3=left elbow, 4=right elbow,
#                 5=left wrist, 6=right wrist, 7=left hip, 8=right hip, 9=left knee,
#                 10=right knee, 11=left ankle, 12=right ankle, 13=head, 14=spine

# Head and neck motion
for i in range(num_frames):
    positions[i, 13, 0] = 0  # head x
    positions[i, 13, 1] = 1.0 - 0.8 * (i / num_frames)  # head y, bowing down
    positions[i, 0, 0] = 0  # neck x
    positions[i, 0, 1] = 0.8 - 0.6 * (i / num_frames)  # neck y, bowing down
    positions[i, 14, 0] = 0  # spine x
    positions[i, 14, 1] = 0.4 - 0.3 * (i / num_frames)  # spine y, bowing down

# Shoulder motion
for i in range(num_frames):
    positions[i, 1, 0] = -0.2 + 0.1 * (i / num_frames)  # left shoulder x
    positions[i, 1, 1] = 0.6 - 0.4 * (i / num_frames)  # left shoulder y
    positions[i, 2, 0] = 0.2 - 0.1 * (i / num_frames)  # right shoulder x
    positions[i, 2, 1] = 0.6 - 0.4 * (i / num_frames)  # right shoulder y

# Elbow motion
for i in range(num_frames):
    positions[i, 3, 0] = -0.4 + 0.2 * (i / num_frames)  # left elbow x
    positions[i, 3, 1] = 0.4 - 0.3 * (i / num_frames)  # left elbow y
    positions[i, 4, 0] = 0.4 - 0.2 * (i / num_frames)  # right elbow x
    positions[i, 4, 1] = 0.4 - 0.3 * (i / num_frames)  # right elbow y

# Wrist motion
for i in range(num_frames):
    positions[i, 5, 0] = -0.6 + 0.3 * (i / num_frames)  # left wrist x
    positions[i, 5, 1] = 0.2 - 0.2 * (i / num_frames)  # left wrist y
    positions[i, 6, 0] = 0.6 - 0.3 * (i / num_frames)  # right wrist x
    positions[i, 6, 1] = 0.2 - 0.2 * (i / num_frames)  # right wrist y

# Hip motion
for i in range(num_frames):
    positions[i, 7, 0] = -0.3 + 0.15 * (i / num_frames)  # left hip x
    positions[i, 7, 1] = 0.0 - 0.1 * (i / num_frames)  # left hip y
    positions[i, 8, 0] = 0.3 - 0.15 * (i / num_frames)  # right hip x
    positions[i, 8, 1] = 0.0 - 0.1 * (i / num_frames)  # right hip y

# Knee motion
for i in range(num_frames):
    positions[i, 9, 0] = -0.5 + 0.25 * (i / num_frames)  # left knee x
    positions[i, 9, 1] = -0.4 + 0.2 * (i / num_frames)  # left knee y
    positions[i, 10, 0] = 0.5 - 0.25 * (i / num_frames)  # right knee x
    positions[i, 10, 1] = -0.4 + 0.2 * (i / num_frames)  # right knee y

# Ankle motion
for i in range(num_frames):
    positions[i, 11, 0] = -0.7 + 0.35 * (i / num_frames)  # left ankle x
    positions[i, 11, 1] = -0.8 + 0.4 * (i / num_frames)  # left ankle y
    positions[i, 12, 0] = 0.7 - 0.35 * (i / num_frames)  # right ankle x
    positions[i, 12, 1] = -0.8 + 0.4 * (i / num_frames)  # right ankle y

# Normalize positions to fit in the plot
positions = positions * 10  # scale up for visibility

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create point light markers
points = [plt.Circle((0, 0), radius=0.1, color='white') for _ in range(num_joints)]
for point in points:
    ax.add_patch(point)

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        point.center = positions[frame, i, 0], positions[frame, i, 1]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display animation
plt.show()
