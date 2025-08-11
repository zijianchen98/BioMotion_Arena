import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This function computes the 2D coordinates of the 15 point-lights at a given time t.
def get_points(t):
    # Basic body dimensions (arbitrary units)
    head_height = 0.1
    neck_to_shoulder = 0.05
    shoulder_to_elbow = 0.15
    elbow_to_wrist = 0.15
    torso_length = 0.25
    hip_to_knee = 0.20
    knee_to_ankle = 0.20
    shoulder_width = 0.25
    hip_width = 0.20
    
    # Base offsets for center of torso
    torso_center_x = 0.0
    torso_center_y = 0.5
    
    # Slight oscillation of the torso (to add realism)
    torso_sway = 0.01 * np.sin(2.0 * np.pi * 0.5 * t)
    
    # Right arm wave angles (smooth wave motion)
    # Angular speed for shoulder and elbow
    angle_shoulder = np.deg2rad(30) + 0.4 * np.sin(2.0 * np.pi * 1.0 * t)
    angle_elbow = np.deg2rad(70) + 0.2 * np.sin(2.0 * np.pi * 2.0 * t)
    
    # Left arm is relaxed and static (slight bend)
    angle_shoulder_left = np.deg2rad(-10)
    angle_elbow_left = np.deg2rad(30)
    
    # Define torso center
    torso_center = np.array([torso_center_x + torso_sway, torso_center_y])
    
    # Head (directly above torso center)
    head = torso_center + np.array([0.0, torso_length + head_height])
    # Neck (just below head)
    neck = torso_center + np.array([0.0, torso_length])
    
    # Right shoulder
    right_shoulder = torso_center + np.array([shoulder_width/2, torso_length])
    # Right elbow
    r_elbow_x = right_shoulder[0] + shoulder_to_elbow * np.sin(angle_shoulder)
    r_elbow_y = right_shoulder[1] - shoulder_to_elbow * np.cos(angle_shoulder)
    right_elbow = np.array([r_elbow_x, r_elbow_y])
    # Right wrist
    r_wrist_x = r_elbow_x + elbow_to_wrist * np.sin(angle_shoulder + angle_elbow)
    r_wrist_y = r_elbow_y - elbow_to_wrist * np.cos(angle_shoulder + angle_elbow)
    right_wrist = np.array([r_wrist_x, r_wrist_y])
    
    # Left shoulder
    left_shoulder = torso_center + np.array([-shoulder_width/2, torso_length])
    # Left elbow
    l_elbow_x = left_shoulder[0] + shoulder_to_elbow * np.sin(angle_shoulder_left)
    l_elbow_y = left_shoulder[1] - shoulder_to_elbow * np.cos(angle_shoulder_left)
    left_elbow = np.array([l_elbow_x, l_elbow_y])
    # Left wrist
    l_wrist_x = l_elbow_x + elbow_to_wrist * np.sin(angle_shoulder_left + angle_elbow_left)
    l_wrist_y = l_elbow_y - elbow_to_wrist * np.cos(angle_shoulder_left + angle_elbow_left)
    left_wrist = np.array([l_wrist_x, l_wrist_y])
    
    # Hips
    right_hip = torso_center + np.array([hip_width/2, 0.0])
    left_hip = torso_center + np.array([-hip_width/2, 0.0])
    
    # Right leg
    r_knee_x = right_hip[0]
    r_knee_y = right_hip[1] - hip_to_knee
    right_knee = np.array([r_knee_x, r_knee_y])
    r_ankle_x = right_hip[0]
    r_ankle_y = right_hip[1] - (hip_to_knee + knee_to_ankle)
    right_ankle = np.array([r_ankle_x, r_ankle_y])
    
    # Left leg
    l_knee_x = left_hip[0]
    l_knee_y = left_hip[1] - hip_to_knee
    left_knee = np.array([l_knee_x, l_knee_y])
    l_ankle_x = left_hip[0]
    l_ankle_y = left_hip[1] - (hip_to_knee + knee_to_ankle)
    left_ankle = np.array([l_ankle_x, l_ankle_y])
    
    # Compile all 15 points
    points = np.array([
        head,             # 1
        neck,             # 2
        right_shoulder,   # 3
        right_elbow,      # 4
        right_wrist,      # 5
        left_shoulder,    # 6
        left_elbow,       # 7
        left_wrist,       # 8
        right_hip,        # 9
        right_knee,       # 10
        right_ankle,      # 11
        left_hip,         # 12
        left_knee,        # 13
        left_ankle,       # 14
        torso_center      # 15
    ])
    return points

fig, ax = plt.subplots(figsize=(5, 5))
fig.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0.0, 1.2)
ax.axis("off")

# Create the scatter plot (15 points)
scat = ax.scatter([], [], s=40, c="white")

def init():
    scat.set_offsets([])
    return (scat,)

def update(frame):
    t = frame / 30.0  # 30 FPS assumption
    pts = get_points(t)
    scat.set_offsets(pts)
    return (scat,)

ani = FuncAnimation(
    fig, update, frames=300, init_func=init, interval=33, blit=True, repeat=True
)

plt.show()