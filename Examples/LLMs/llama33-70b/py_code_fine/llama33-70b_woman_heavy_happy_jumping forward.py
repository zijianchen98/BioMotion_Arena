
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the woman's joints
point_lights = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_wrist',
    'left_shoulder', 'left_elbow', 'left_wrist', 'right_hip', 'right_knee',
    'right_ankle', 'left_hip', 'left_knee', 'left_ankle', 'torso'
]

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 10],  # head
    [0, 8],   # neck
    [2, 6],   # right_shoulder
    [4, 4],   # right_elbow
    [6, 2],   # right_wrist
    [-2, 6],  # left_shoulder
    [-4, 4],  # left_elbow
    [-6, 2],  # left_wrist
    [2, -2],  # right_hip
    [4, -6],  # right_knee
    [6, -10], # right_ankle
    [-2, -2], # left_hip
    [-4, -6], # left_knee
    [-6, -10],# left_ankle
    [0, 0]    # torso
])

# Define the movement of the point-lights over time
def update(frame):
    positions = initial_positions.copy()
    
    # Jumping motion
    positions[:, 1] += np.sin(frame / 10.0) * 2
    
    # Arm movement
    positions[2, 0] += np.sin(frame / 5.0) * 1  # right_shoulder
    positions[3, 0] += np.sin(frame / 5.0) * 2  # right_elbow
    positions[4, 0] += np.sin(frame / 5.0) * 3  # right_wrist
    positions[5, 0] -= np.sin(frame / 5.0) * 1  # left_shoulder
    positions[6, 0] -= np.sin(frame / 5.0) * 2  # left_elbow
    positions[7, 0] -= np.sin(frame / 5.0) * 3  # left_wrist
    
    # Leg movement
    positions[8, 1] -= np.sin(frame / 10.0) * 2  # right_hip
    positions[9, 1] -= np.sin(frame / 10.0) * 4  # right_knee
    positions[10, 1] -= np.sin(frame / 10.0) * 6  # right_ankle
    positions[11, 1] -= np.sin(frame / 10.0) * 2  # left_hip
    positions[12, 1] -= np.sin(frame / 10.0) * 4  # left_knee
    positions[13, 1] -= np.sin(frame / 10.0) * 6  # left_ankle
    
    # Forward movement
    positions[:, 0] += frame / 50.0
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
point_light_scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    positions = update(frame)
    point_light_scatter.set_offsets(positions)
    return point_light_scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(200), interval=20)

plt.show()
