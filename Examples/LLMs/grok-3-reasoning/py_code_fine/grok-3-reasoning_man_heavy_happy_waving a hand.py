
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
f = 1  # frequency of waving in Hz
A = 20  # amplitude of hand movement
T = 5  # total time in seconds
frames = 100  # number of frames

# Time array
t = np.linspace(0, T, frames)

# Fixed positions
head = (0, 160)
left_shoulder = (-10, 140)
right_shoulder = (10, 140)
right_elbow = (10, 110)
right_wrist = (10, 80)
right_hand = (10, 70)
left_hip = (-5, 80)
left_knee = (-5, 40)
left_ankle = (-5, 0)
right_hip = (5, 80)
right_knee = (5, 40)
right_ankle = (5, 0)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-40, 40)
ax.set_ylim(-10, 170)

# Initial positions for the left arm
left_hand_x_init = -10
left_hand_y_init = 140
left_elbow_x_init = -10
left_elbow_y_init = 140 - 10 * (1 + 0)  # since sin(0)=0
left_wrist_x_init = left_elbow_x_init + 0.7 * (left_hand_x_init - left_elbow_x_init)
left_wrist_y_init = left_elbow_y_init + 0.7 * (left_hand_y_init - left_elbow_y_init)

# Initial points
points_x_init = [
    head[0], left_shoulder[0], left_elbow_x_init, left_wrist_x_init, left_hand_x_init,
    right_shoulder[0], right_elbow[0], right_wrist[0], right_hand[0],
    left_hip[0], left_knee[0], left_ankle[0],
    right_hip[0], right_knee[0], right_ankle[0]
]
points_y_init = [
    head[1], left_shoulder[1], left_elbow_y_init, left_wrist_y_init, left_hand_y_init,
    right_shoulder[1], right_elbow[1], right_wrist[1], right_hand[1],
    left_hip[1], left_knee[1], left_ankle[1],
    right_hip[1], right_knee[1], right_ankle[1]
]

# Create scatter plot
scatter = ax.scatter(points_x_init, points_y_init, color='white')

# Update function for animation
def update(frame):
    t_frame = t[frame]
    left_hand_x = -10 + A * np.sin(2 * np.pi * f * t_frame)
    left_hand_y = 140
    left_elbow_x = -10 + (A / 2) * np.sin(2 * np.pi * f * t_frame)
    left_elbow_y = 140 - 10 * (1 + np.sin(2 * np.pi * f * t_frame))
    left_wrist_x = left_elbow_x + 0.7 * (left_hand_x - left_elbow_x)
    left_wrist_y = left_elbow_y + 0.7 * (left_hand_y - left_elbow_y)
    
    points_x = [
        head[0], left_shoulder[0], left_elbow_x, left_wrist_x, left_hand_x,
        right_shoulder[0], right_elbow[0], right_wrist[0], right_hand[0],
        left_hip[0], left_knee[0], left_ankle[0],
        right_hip[0], right_knee[0], right_ankle[0]
    ]
    points_y = [
        head[1], left_shoulder[1], left_elbow_y, left_wrist_y, left_hand_y,
        right_shoulder[1], right_elbow[1], right_wrist[1], right_hand[1],
        left_hip[1], left_knee[1], left_ankle[1],
        right_hip[1], right_knee[1], right_ankle[1]
    ]
    
    scatter.set_offsets(np.c_[points_x, points_y])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
