
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_facecolor('black')
plt.xlim(-2, 2)
plt.ylim(0, 7)
ax.axis('off')

# Joint coordinates structure (15 points: head, shoulders, elbows, wrists, hips, knees, feet)
joint_connections = [
    (0,), (1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14)
]

# Initialize points for joints
points, = plt.plot([], [], 'wo', markersize=8)

# Walking animation function
def walking_motion(frame):
    t = frame / 10.0
    
    # Base vertical sinusoidal bobbing
    y_base = 3.5 + 0.05 * np.sin(t * 2 * np.pi)

    # Head
    head = (0, y_base + 3)

    # Shoulders
    shoulder_y = y_base + 2.4
    shoulder_move = 0.1 * np.sin(t * 2 * np.pi)
    shoulders = [(-0.5 + shoulder_move, shoulder_y),
                 (0.5 - shoulder_move, shoulder_y)]

    # Elbows
    elbow_y = y_base + 2.0
    elbow_move = 0.2 * np.sin(t * 2 * np.pi - np.pi / 4)
    elbows = [(-0.7 + elbow_move, elbow_y), 
              (0.7 - elbow_move, elbow_y)]

    # Wrists
    wrist_y = y_base + 1.6
    wrist_move = 0.2 * np.sin(t * 2 * np.pi - np.pi / 2)
    wrists = [(-0.9 + wrist_move, wrist_y),
              (0.9 - wrist_move, wrist_y)]

    # Hips
    hip_y = y_base + 1.6
    hip_move = 0.1 * np.sin(t * 2 * np.pi + np.pi)
    hips = [(-0.3 + hip_move, hip_y),
            (0.3 - hip_move, hip_y)]

    # Knees
    knee_y = y_base + 0.8
    knee_move = 0.2 * np.sin(t * 2 * np.pi - np.pi / 2)
    knees = [(-0.3 - knee_move, knee_y),
             (0.3 + knee_move, knee_y)]

    # Feet
    foot_y = 0.2 * np.abs(np.sin(t * 2 * np.pi)) + 0.2
    foot_move = 0.3 * np.sin(t * 2 * np.pi)
    feet = [(-0.3 - foot_move, foot_y),
            (0.3 + foot_move, foot_y)]

    # Combine all joints into one array
    joints = np.array([head, shoulders[0], shoulders[1], elbows[0], elbows[1],
                      wrists[0], wrists[1], hips[0], hips[1], knees[0],
                      knees[1], feet[0], feet[1], (0, y_base + 2.5), (0, y_base + 1.2)])

    points.set_data(joints[:,0], joints[:,1])
    return points,

ani = FuncAnimation(fig, walking_motion, frames=np.arange(0, 100, 1), interval=40, blit=True)

plt.show()
