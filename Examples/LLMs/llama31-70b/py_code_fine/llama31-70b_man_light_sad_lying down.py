
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light stimulus parameters
n_points = 15
n_frames = 100

# Define the point-light positions for the sadman lying down
point_positions = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.8],  # left wrist
    [0.6, 0.8],  # right wrist
    [0.5, 0.4],  # hip
    [0.4, 0.5],  # left knee
    [0.6, 0.5],  # right knee
    [0.4, 0.6],  # left ankle
    [0.6, 0.6],  # right ankle
    [0.5, 0.3],  # left toe
    [0.5, 0.7],  # right toe
    [0.5, 0.5]   # torso
])

# Define the motion trajectory for the sadman lying down
def get_point_positions(frame):
    angle = np.radians(frame * 2)
    hip_angle = np.radians(frame * 1.5)
    knee_angle = np.radians(frame * 3)
    ankle_angle = np.radians(frame * 4.5)
    
    # Torso
    torso_x = 0.5
    torso_y = 0.5 + np.sin(angle) * 0.05
    
    # Head
    head_x = 0.5
    head_y = 0.5 + np.cos(angle) * 0.05
    
    # Shoulders
    shoulder_angle = np.arctan2(point_positions[2, 1] - point_positions[1, 1], point_positions[2, 0] - point_positions[1, 0])
    left_shoulder_x = 0.4 + np.cos(shoulder_angle + angle) * 0.05
    left_shoulder_y = 0.6 + np.sin(shoulder_angle + angle) * 0.05
    right_shoulder_x = 0.6 + np.cos(shoulder_angle - angle) * 0.05
    right_shoulder_y = 0.6 + np.sin(shoulder_angle - angle) * 0.05
    
    # Elbows
    elbow_angle = np.arctan2(point_positions[4, 1] - point_positions[3, 1], point_positions[4, 0] - point_positions[3, 0])
    left_elbow_x = 0.4 + np.cos(elbow_angle + angle) * 0.05
    left_elbow_y = 0.7 + np.sin(elbow_angle + angle) * 0.05
    right_elbow_x = 0.6 + np.cos(elbow_angle - angle) * 0.05
    right_elbow_y = 0.7 + np.sin(elbow_angle - angle) * 0.05
    
    # Wrists
    wrist_angle = np.arctan2(point_positions[6, 1] - point_positions[5, 1], point_positions[6, 0] - point_positions[5, 0])
    left_wrist_x = 0.4 + np.cos(wrist_angle + angle) * 0.05
    left_wrist_y = 0.8 + np.sin(wrist_angle + angle) * 0.05
    right_wrist_x = 0.6 + np.cos(wrist_angle - angle) * 0.05
    right_wrist_y = 0.8 + np.sin(wrist_angle - angle) * 0.05
    
    # Hip
    hip_x = 0.5
    hip_y = 0.4 + np.sin(hip_angle) * 0.05
    
    # Knees
    knee_angle = np.arctan2(point_positions[10, 1] - point_positions[9, 1], point_positions[10, 0] - point_positions[9, 0])
    left_knee_x = 0.4 + np.cos(knee_angle + hip_angle) * 0.05
    left_knee_y = 0.5 + np.sin(knee_angle + hip_angle) * 0.05
    right_knee_x = 0.6 + np.cos(knee_angle - hip_angle) * 0.05
    right_knee_y = 0.5 + np.sin(knee_angle - hip_angle) * 0.05
    
    # Ankles
    ankle_angle = np.arctan2(point_positions[12, 1] - point_positions[11, 1], point_positions[12, 0] - point_positions[11, 0])
    left_ankle_x = 0.4 + np.cos(ankle_angle + knee_angle) * 0.05
    left_ankle_y = 0.6 + np.sin(ankle_angle + knee_angle) * 0.05
    right_ankle_x = 0.6 + np.cos(ankle_angle - knee_angle) * 0.05
    right_ankle_y = 0.6 + np.sin(ankle_angle - knee_angle) * 0.05
    
    # Toes
    toe_angle = np.arctan2(point_positions[14, 1] - point_positions[13, 1], point_positions[14, 0] - point_positions[13, 0])
    left_toe_x = 0.5 + np.cos(toe_angle + ankle_angle) * 0.05
    left_toe_y = 0.3 + np.sin(toe_angle + ankle_angle) * 0.05
    right_toe_x = 0.5 + np.cos(toe_angle - ankle_angle) * 0.05
    right_toe_y = 0.7 + np.sin(toe_angle - ankle_angle) * 0.05
    
    return np.array([
        [torso_x, torso_y],
        [head_x, head_y],
        [left_shoulder_x, left_shoulder_y],
        [right_shoulder_x, right_shoulder_y],
        [left_elbow_x, left_elbow_y],
        [right_elbow_x, right_elbow_y],
        [left_wrist_x, left_wrist_y],
        [right_wrist_x, right_wrist_y],
        [hip_x, hip_y],
        [left_knee_x, left_knee_y],
        [right_knee_x, right_knee_y],
        [left_ankle_x, left_ankle_y],
        [right_ankle_x, right_ankle_y],
        [left_toe_x, left_toe_y],
        [right_toe_x, right_toe_y]
    ])

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot of the initial point positions
scatter = ax.scatter(point_positions[:, 0], point_positions[:, 1], c='white')

# Define the animation function
def animate(frame):
    point_positions = get_point_positions(frame)
    scatter.set_offsets(point_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

# Display the animation
plt.show()
