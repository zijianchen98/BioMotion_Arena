
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define joint positions for a running "happy man" (simplified 15-point model)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
base_positions = np.array([
    [0, 0.8],  # head
    [-0.2, 0.6], [0.2, 0.6],  # shoulders
    [-0.4, 0.4], [0.4, 0.4],  # elbows
    [-0.6, 0.2], [0.6, 0.2],  # wrists
    [-0.1, 0.3], [0.1, 0.3],  # hips
    [-0.2, 0.0], [0.2, 0.0],  # knees
    [-0.3, -0.3], [0.3, -0.3],  # ankles
    [0, 0.5], [0, 0.4]  # torso points
])

# Number of frames for one cycle of running
n_frames = 30
positions = np.zeros((n_frames, 15, 2))

# Simulate running motion (simplified biomechanical movement)
for i in range(n_frames):
    t = i / n_frames * 2 * np.pi
    # Head and torso move slightly up and down
    vertical_offset = 0.1 * np.sin(t)
    # Legs and arms swing
    leg_angle = 0.5 * np.sin(t)
    arm_angle = 0.5 * np.cos(t)
    
    # Update positions
    pos = base_positions.copy()
    pos[0] += [0, vertical_offset]  # head
    pos[8:10] += [0, vertical_offset]  # torso
    pos[10] = [0.1 + 0.1 * np.cos(leg_angle), -0.3 + 0.1 * np.sin(leg_angle)]  # left knee
    pos[11] = [-0.1 - 0.1 * np.cos(leg_angle), -0.3 - 0.1 * np.sin(leg_angle)]  # right knee
    pos[12] = [0.1 + 0.2 * np.cos(leg_angle + np.pi/2), -0.6 + 0.1 * np.sin(leg_angle + np.pi/2)]  # left ankle
    pos[13] = [-0.1 - 0.2 * np.cos(leg_angle + np.pi/2), -0.6 - 0.1 * np.sin(leg_angle + np.pi/2)]  # right ankle
    pos[2] = [0.2 + 0.1 * np.cos(arm_angle), 0.6 + 0.1 * np.sin(arm_angle)]  # right elbow
    pos[3] = [-0.2 - 0.1 * np.cos(arm_angle), 0.6 - 0.1 * np.sin(arm_angle)]  # left elbow
    pos[4] = [0.4 + 0.2 * np.cos(arm_angle + np.pi/2), 0.4 + 0.1 * np.sin(arm_angle + np.pi/2)]  # right wrist
    pos[5] = [-0.4 - 0.2 * np.cos(arm_angle + np.pi/2), 0.4 - 0.1 * np.sin(arm_angle + np.pi/2)]  # left wrist
    
    positions[i] = pos

# Initialize scatter plot
scat = ax.scatter([], [], c='white', s=50)

# Animation update function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True, repeat=True)

plt.show()
