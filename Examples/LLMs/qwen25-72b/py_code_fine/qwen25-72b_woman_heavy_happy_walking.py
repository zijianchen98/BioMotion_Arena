
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a walking woman with heavy weight
key_points = [
    "head", "neck", "right_shoulder", "left_shoulder", "right_elbow", "left_elbow",
    "right_wrist", "left_wrist", "right_hip", "left_hip", "right_knee", "left_knee",
    "right_ankle", "left_ankle", "center_of_mass"
]

# Define initial positions for the key points
initial_positions = np.array([
    [0, 1.7],  # head
    [0, 1.6],  # neck
    [0.2, 1.5],  # right_shoulder
    [-0.2, 1.5],  # left_shoulder
    [0.4, 1.3],  # right_elbow
    [-0.4, 1.3],  # left_elbow
    [0.6, 1.1],  # right_wrist
    [-0.6, 1.1],  # left_wrist
    [0.2, 1.0],  # right_hip
    [-0.2, 1.0],  # left_hip
    [0.4, 0.6],  # right_knee
    [-0.4, 0.6],  # left_knee
    [0.6, 0.2],  # right_ankle
    [-0.6, 0.2],  # left_ankle
    [0, 0.8]  # center_of_mass
])

# Define the animation parameters
frame_rate = 30  # frames per second
total_frames = 180  # total number of frames (6 seconds)
step_size = 1 / frame_rate  # time step in seconds

# Define the walking gait function
def walk_gait(t):
    phase = t * 2 * np.pi
    x_offset = 0.3 * np.sin(phase)
    y_offset = 0.1 * np.sin(2 * phase)
    
    positions = initial_positions.copy()
    positions[:, 0] += x_offset
    positions[:, 1] += y_offset
    
    # Adjust for heavy weight
    positions[10:, 1] -= 0.1 * np.sin(phase)  # lower body sinks more
    positions[12:, 0] += 0.1 * np.cos(phase)  # feet move more side-to-side
    
    return positions

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, color='white')

# Update function for the animation
def update(frame):
    t = frame * step_size
    positions = walk_gait(t)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/frame_rate, blit=True)

# Display the animation
plt.show()
