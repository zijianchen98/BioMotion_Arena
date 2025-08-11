
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
HEIGHT_RANGE = 10
WIDTH_RANGE = 10

# Man's joints positions
joints = [
    ['head', 50, 20],
    ['shoulder_left', 30, 40],
    'elbow_left', 25, 35,
    'wrist_left', 20, 30,
    'hands_left', 15, 25,
   'shoulder_right', 70, 40,
    'elbow_right', 65, 35,
    'wrist_right', 60, 30,
    'hands_right', 55, 25,
    'hip_left', 40, 60,
    'knee_left', 35, 55,
    'ankle_left', 30, 50],
    'hands_left', 15, 25,
   'shoulder_right', 70, 40,
    'elbow_right', 65, 35,
    'wrist_right', 60, 30,
    'hands_right', 55, 25,
    'hip_left', 40, 60,
    'knee_left', 35, 55,
    'ankle_left', 30, 50],
    'hands_right', 55, 25,
   'shoulder_right', 70, 40,
    'elbow_right', 65, 35,
    'wrist_right', 60, 30,
    'hands_right', 55, 25,
    'hip_left', 40, 60,
    'knee_left', 35, 55,
    'ankle_left', 30, 50]
]

def update_positions(frame, pts):
    x_positions = [j[1] for j in joints]
    y_positions = [j[2] for j in joints]

    # Smooth transition using sine function
    x_positions = [np.sin(0.1 * frame * j[0] + np.pi / 2) * j[1]
                   for j in joints]
    y_positions = [np.sin(0.1 * frame * j[0] + np.pi) * j[2]
                   for j in joints]

    for pt in pts:
        i = joints.index(pt)
        pt.set_data(x_positions[i], y_positions[i])

    return pts,

fig, ax = plt.subplots()
ax.set_xlim([-5, 105])
ax.set_ylim([-5, 105])
ax.axis('off')

# Create points
pts = [ax.plot([], [], 'o', markersize=5, color='white')[0]
       for _ in range(NUM_POINTS)]
line, = ax.plot([], [], 'k', linewidth=0.1)

# Animation
ani = animation.FuncAnimation(fig, update_positions, frames=range(360),
                              fargs=(pts,),
                              interval=100, blit=False)

plt.show()
