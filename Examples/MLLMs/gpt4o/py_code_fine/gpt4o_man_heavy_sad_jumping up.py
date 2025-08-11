
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define skeleton connections
connections = [
    (0, 1), (1, 2), (2, 3),  # Torso and head
    (1, 4), (4, 5), (5, 6),  # Left arm
    (1, 7), (7, 8), (8, 9),  # Right arm
    (2, 10), (10, 11), (11, 12),  # Left leg
    (2, 13), (13, 14), (14, 15)  # Right leg
]

# Define initial joint positions (x, y) for the sadman
base_pose = np.array([
    [0, 5],   # Joint 0 (head)
    [0, 4],   # Joint 1 (neck)
    [0, 3],   # Joint 2 (torso)
    [-1, 2],  # Joint 3 (left hip)
    [-1.5, 1],  # Joint 4 (left knee)
    [-1.5, 0],  # Joint 5 (left foot)
    [1, 2],   # Joint 6 (right hip)
    [1.5, 1],  # Joint 7 (right knee)
    [1.5, 0],  # Joint 8 (right foot)
    [-1.5, 3.5],  # Joint 9 (left shoulder)
    [-2, 2.5],  # Joint 10 (left elbow)
    [-2.5, 1.5],  # Joint 11 (left hand)
    [1.5, 3.5],  # Joint 12 (right shoulder)
    [2, 2.5],  # Joint 13 (right elbow)
    [2.5, 1.5]  # Joint 14 (right hand)
])

# Parameters for animation
num_frames = 50
jump_height = 1.2
frame_time = 100

def generate_motion(base_pose, frame_index):
    # Oscillate y-coordinate for jumping motion
    oscillation = np.sin(2 * np.pi * frame_index / num_frames)
    y_offset = oscillation * jump_height
    
    pose = base_pose.copy()
    
    # Apply y-offset to the upward motion of the torso (index 2), and propagate to other joints
    pose[:, 1] += y_offset
    
    # Add some swing motion for arms and legs
    swing_amplitude = 0.2
    sway = np.cos(2 * np.pi * frame_index / num_frames) * swing_amplitude
    
    # Swing arms
    pose[9:12, 0] += sway
    pose[12:15, 0] -= sway

    # Swing legs
    pose[3:6, 0] -= sway
    pose[6:9, 0] += sway
    
    return pose

# Initializing the animation figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 6)
ax.set_facecolor('black')
ax.axis('off')

# Initialize points and lines to represent the skeleton
points, = ax.plot([], [], 'wo', markersize=8)  # White points
lines = [ax.plot([], [], 'w-')[0] for _ in connections]  # Skeleton connections

def init():
    points.set_data([], [])
    for line in lines:
        line.set_data([], [])
    return [points] + lines

def update(frame):
    # Generate motion for the current frame
    pose = generate_motion(base_pose, frame)
    
    # Update positions of points
    points.set_data(pose[:, 0], pose[:, 1])
    
    # Update positions of connections
    for line, (start, end) in zip(lines, connections):
        line.set_data([pose[start, 0], pose[end, 0]], [pose[start, 1], pose[end, 1]])
    
    return [points] + lines

ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, interval=frame_time, blit=True)

plt.show()
