
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights
NUM_POINTS = 15
# Define the background color
BACKGROUND_COLOR = 'black'
# Define the point light color
POINT_COLOR = 'white'

# Define the skeleton structure for a bowing woman (simplified)
# This is a simplified 2D representation of a human body with joints
skeleton = {
    'hips': np.array([0, 0]),
    'knees': np.array([0, -50]),
    'ankles': np.array([0, -100]),
    'spine': np.array([0, 0]),
    'shoulders': np.array([0, 0]),
    'elbows': np.array([0, 0]),
    'wrists': np.array([0, 0]),
    'head': np.array([0, 0]),
    'neck': np.array([0, 0]),
    'left_hip': np.array([-20, 0]),
    'left_knee': np.array([-20, -50]),
    'left_ankle': np.array([-20, -100]),
    'left_shoulder': np.array([-20, 0]),
    'left_elbow': np.array([-20, 0]),
    'left_wrist': np.array([-20, 0]),
    'left_hand': np.array([-20, 0]),
    'right_hip': np.array([20, 0]),
    'right_knee': np.array([20, -50]),
    'right_ankle': np.array([20, -100]),
    'right_shoulder': np.array([20, 0]),
    'right_elbow': np.array([20, 0]),
    'right_wrist': np.array([20, 0]),
    'right_hand': np.array([20, 0]),
    'head': np.array([0, 0]),
    'neck': np.array([0, 0]),
}

# Define the joints for the skeleton
joints = [
    'hips', 'knees', 'ankles', 'spine', 'shoulders', 'elbows', 'wrists', 'head', 'neck',
    'left_hip', 'left_knee', 'left_ankle', 'left_shoulder', 'left_elbow', 'left_wrist',
    'left_hand', 'right_hip', 'right_knee', 'right_ankle', 'right_shoulder', 'right_elbow',
    'right_wrist', 'right_hand'
]

# Define the point lights as a list of positions
point_lights = [np.array([0, 0]) for _ in range(NUM_POINTS)]

# Define a function to generate realistic motion for a bowing action
def bowing_motion(t, total_time=10):
    # Normalize time to [0, 1]
    t_norm = t / total_time
    # Define the motion of the body parts
    # Hips: move down and then up
    hips = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Knees: move down and then up
    knees = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Ankles: move down and then up
    ankles = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Spine: move down and then up
    spine = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Shoulders: move down and then up
    shoulders = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Elbows: move down and then up
    elbows = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Wrists: move down and then up
    wrists = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Head: move down and then up
    head = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Neck: move down and then up
    neck = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Left hip: move down and then up
    left_hip = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left knee: move down and then up
    left_knee = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left ankle: move down and then up
    left_ankle = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left shoulder: move down and then up
    left_shoulder = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left elbow: move down and then up
    left_elbow = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left wrist: move down and then up
    left_wrist = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Left hand: move down and then up
    left_hand = np.array([-20, -100 * np.sin(np.pi * t_norm)])
    # Right hip: move down and then up
    right_hip = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right knee: move down and then up
    right_knee = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right ankle: move down and then up
    right_ankle = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right shoulder: move down and then up
    right_shoulder = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right elbow: move down and then up
    right_elbow = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right wrist: move down and then up
    right_wrist = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Right hand: move down and then up
    right_hand = np.array([20, -100 * np.sin(np.pi * t_norm)])
    # Head: move down and then up
    head = np.array([0, -100 * np.sin(np.pi * t_norm)])
    # Neck: move down and then up
    neck = np.array([0, -100 * np.sin(np.pi * t_norm)])

    # Assign the motion to the skeleton
    skeleton['hips'] = hips
    skeleton['knees'] = knees
    skeleton['ankles'] = ankles
    skeleton['spine'] = spine
    skeleton['shoulders'] = shoulders
    skeleton['elbows'] = elbows
    skeleton['wrists'] = wrists
    skeleton['head'] = head
    skeleton['neck'] = neck
    skeleton['left_hip'] = left_hip
    skeleton['left_knee'] = left_knee
    skeleton['left_ankle'] = left_ankle
    skeleton['left_shoulder'] = left_shoulder
    skeleton['left_elbow'] = left_elbow
    skeleton['left_wrist'] = left_wrist
    skeleton['left_hand'] = left_hand
    skeleton['right_hip'] = right_hip
    skeleton['right_knee'] = right_knee
    skeleton['right_ankle'] = right_ankle
    skeleton['right_shoulder'] = right_shoulder
    skeleton['right_elbow'] = right_elbow
    skeleton['right_wrist'] = right_wrist
    skeleton['right_hand'] = right_hand

    # Assign the point lights to the joints
    for i, joint in enumerate(joints):
        point_lights[i] = skeleton[joint]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-250, 250)
ax.set_ylim(-250, 250)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
points = [ax.scatter([], [], color=POINT_COLOR, s=20) for _ in range(NUM_POINTS)]

# Animation function
def animate(t):
    bowing_motion(t)
    for i, point in enumerate(points):
        point.set_offsets(point_lights[i])

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
