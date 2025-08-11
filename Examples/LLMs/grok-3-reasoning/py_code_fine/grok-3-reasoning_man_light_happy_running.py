
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Placeholder for loading motion data
# In actual use, implement a function to load joint positions from a BVH file
# For example:
# joint_positions, frame_rate = load_bvh('running.bvh', selected_joints)
# selected_joints = ['Head', 'Neck', 'LeftShoulder', 'RightShoulder', 'LeftElbow', 'RightElbow', 'LeftWrist', 'RightWrist', 'Spine', 'LeftHip', 'RightHip', 'LeftKnee', 'RightKnee', 'LeftAnkle', 'RightAnkle']
# For this example, we use dummy data
num_frames = 100
joint_positions = [ [ (50 + 10*i + 5*np.sin(0.1*frame), 100 + 10*j + 5*np.cos(0.1*frame), 0) for i in range(5) for j in range(3) ] for frame in range(num_frames) ]
# Ensure exactly 15 joints
joint_positions = [frame[:15] for frame in joint_positions]
frame_rate = 30

# Parameters for bounce effect to convey happiness
amplitude = 5  # Adjust based on motion scale
frequency = 2  # Hz

# Compute centered positions and find plot limits
all_centered_positions = []
for frame in joint_positions:
    positions_2d = [(x, y) for x, y, z in frame]
    centroid_x = sum(x for x, y in positions_2d) / 15
    centroid_y = sum(y for x, y in positions_2d) / 15
    centered = [(x - centroid_x, y - centroid_y) for x, y in positions_2d]
    all_centered_positions.extend(centered)

min_x = min(x for x, y in all_centered_positions)
max_x = max(x for x, y in all_centered_positions)
min_y = min(y for x, y in all_centered_positions)
max_y = max(y for x, y in all_centered_positions)
limit_x = max(abs(min_x), abs(max_x)) * 1.2
limit_y = max(abs(min_y), abs(max_y)) * 1.2 + amplitude

# Set up figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
scatter = ax.scatter([0]*15, [0]*15, color='white', s=10)  # s=10 for dot size
ax.set_xlim(-limit_x, limit_x)
ax.set_ylim(-limit_y, limit_y)
ax.set_aspect('equal')

# Update function for animation
def update(frame_index):
    positions = joint_positions[frame_index]
    positions_2d = [(x, y) for x, y, z in positions]
    centroid_x = sum(x for x, y in positions_2d) / 15
    centroid_y = sum(y for x, y in positions_2d) / 15
    centered = [(x - centroid_x, y - centroid_y) for x, y in positions_2d]
    time = frame_index / frame_rate
    offset = amplitude * np.sin(2 * np.pi * frequency * time)
    bounced = [(x, y + offset) for x, y in centered]
    scatter.set_offsets(bounced)
    return scatter,

# Create and show animation
ani = animation.FuncAnimation(fig, update, frames=len(joint_positions), interval=1000/frame_rate, blit=True)
plt.show()
