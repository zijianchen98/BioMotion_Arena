
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Constants
T = 1.0  # period of gait cycle in seconds
fps = 30
dt = 1.0 / fps
num_frames = int(T * fps * 2)  # for two cycles
A_hip = math.radians(30)
B_knee = math.radians(45)
A_arm = math.radians(20)
C_elbow = math.radians(10)
v = 1.0  # walking speed
C_bounce = 0.05  # vertical bounce amplitude

# Define parents and lengths
parents = {
    'neck': 'sternum',
    'head': 'neck',
    'left_shoulder': 'sternum',
    'left_elbow': 'left_shoulder',
    'left_wrist': 'left_elbow',
    'right_shoulder': 'sternum',
    'right_elbow': 'right_shoulder',
    'right_wrist': 'right_elbow',
    'left_hip': 'sternum',
    'left_knee': 'left_hip',
    'left_ankle': 'left_knee',
    'right_hip': 'sternum',
    'right_knee': 'right_hip',
    'right_ankle': 'right_knee',
}

lengths = {
    'neck': 0.2,
    'head': 0.1,
    'left_shoulder': 0.2,
    'left_elbow': 0.4,
    'left_wrist': 0.4,
    'right_shoulder': 0.2,
    'right_elbow': 0.4,
    'right_wrist': 0.4,
    'left_hip': 0.4,
    'left_knee': 0.5,
    'left_ankle': 0.5,
    'right_hip': 0.4,
    'right_knee': 0.5,
    'right_ankle': 0.5,
}

# Define local angle functions
def get_local_angle(joint, t):
    if joint == 'sternum':
        return 0
    elif joint == 'neck':
        return math.pi / 2
    elif joint == 'head':
        return 0
    elif joint == 'left_shoulder':
        return -math.pi / 2 + A_arm * math.sin(2*math.pi*t / T)
    elif joint == 'left_elbow':
        return C_elbow
    elif joint == 'left_wrist':
        return 0
    elif joint == 'right_shoulder':
        return -math.pi / 2 + A_arm * math.sin(2*math.pi*t / T + math.pi)
    elif joint == 'right_elbow':
        return C_elbow
    elif joint == 'right_wrist':
        return 0
    elif joint == 'left_hip':
        return -math.pi / 2 + A_hip * math.sin(2*math.pi*t / T)
    elif joint == 'left_knee':
        return B_knee * (1 - math.sin(2*math.pi*t / T + math.pi / 2))
    elif joint == 'left_ankle':
        return 0
    elif joint == 'right_hip':
        return -math.pi / 2 + A_hip * math.sin(2*math.pi*t / T + math.pi)
    elif joint == 'right_knee':
        return B_knee * (1 - math.sin(2*math.pi*t / T + math.pi / 2 + math.pi))
    elif joint == 'right_ankle':
        return 0
    else:
        return 0

# Compute positions
order = ['sternum', 'neck', 'head', 'left_shoulder', 'left_elbow', 'left_wrist', 'right_shoulder', 'right_elbow', 'right_wrist', 'left_hip', 'left_knee', 'left_ankle', 'right_hip', 'right_knee', 'right_ankle']

def compute_positions(t):
    positions = {}
    angles = {}
    # Set sternum position
    x_root = v * t
    y_root = C_bounce * math.sin(4*math.pi*t / T)
    positions['sternum'] = (x_root, y_root)
    angles['sternum'] = get_local_angle('sternum', t)
    # Compute positions for other joints
    for joint in order[1:]:
        parent = parents[joint]
        parent_pos = positions[parent]
        parent_angle = angles[parent]
        local_angle = get_local_angle(joint, t)
        absolute_angle = parent_angle + local_angle
        angles[joint] = absolute_angle
        length = lengths[joint]
        dx = length * math.cos(absolute_angle)
        dy = length * math.sin(absolute_angle)
        positions[joint] = (parent_pos[0] + dx, parent_pos[1] + dy)
    return positions

# Set up plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
points, = ax.plot([], [], 'o', color='white', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
  # This line was incomplete in the original code
    t = i * dt
    positions = compute_positions(t)
    x = [positions[joint][0] for joint in order]
    y = [positions[joint][1] for joint in order]
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, interval=1000/fps)
plt.show()
