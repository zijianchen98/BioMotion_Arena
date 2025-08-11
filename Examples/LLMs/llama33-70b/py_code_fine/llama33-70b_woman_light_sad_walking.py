
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the sad woman
points = {
    'head': np.array([0, 10]),
   'shoulder_left': np.array([-3, 8]),
   'shoulder_right': np.array([3, 8]),
    'elbow_left': np.array([-5, 5]),
    'elbow_right': np.array([5, 5]),
    'wrist_left': np.array([-7, 2]),
    'wrist_right': np.array([7, 2]),
    'hip_left': np.array([-2, 0]),
    'hip_right': np.array([2, 0]),
    'knee_left': np.array([-2, -5]),
    'knee_right': np.array([2, -5]),
    'ankle_left': np.array([-2, -10]),
    'ankle_right': np.array([2, -10]),
    'foot_left': np.array([-2, -12]),
    'foot_right': np.array([2, -12]),
}

# Define the walking motion
def walking_motion(frame):
    points_motion = {
        'head': np.array([0, 10 + np.sin(frame / 10.0) * 2]),
       'shoulder_left': np.array([-3, 8 + np.sin(frame / 10.0) * 1]),
       'shoulder_right': np.array([3, 8 + np.sin(frame / 10.0) * 1]),
        'elbow_left': np.array([-5, 5 + np.sin(frame / 5.0) * 2]),
        'elbow_right': np.array([5, 5 + np.sin(frame / 5.0 + np.pi) * 2]),
        'wrist_left': np.array([-7, 2 + np.sin(frame / 5.0) * 2]),
        'wrist_right': np.array([7, 2 + np.sin(frame / 5.0 + np.pi) * 2]),
        'hip_left': np.array([-2, 0 + np.sin(frame / 10.0) * 1]),
        'hip_right': np.array([2, 0 + np.sin(frame / 10.0) * 1]),
        'knee_left': np.array([-2, -5 + np.sin(frame / 5.0) * 2]),
        'knee_right': np.array([2, -5 + np.sin(frame / 5.0 + np.pi) * 2]),
        'ankle_left': np.array([-2, -10 + np.sin(frame / 5.0) * 2]),
        'ankle_right': np.array([2, -10 + np.sin(frame / 5.0 + np.pi) * 2]),
        'foot_left': np.array([-2 + np.sin(frame / 10.0) * 1, -12]),
        'foot_right': np.array([2 + np.sin(frame / 10.0 + np.pi) * 1, -12]),
    }
    return points_motion

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

# Update the plot
def update(frame):
    ax.clear()
    init()
    points_motion = walking_motion(frame)
    for point in points_motion.values():
        ax.plot(point[0], point[1], 'o', markersize=5, color='white')
    for pair in [('head','shoulder_left'), ('head','shoulder_right'), 
                 ('shoulder_left', 'elbow_left'), ('shoulder_right', 'elbow_right'), 
                 ('elbow_left', 'wrist_left'), ('elbow_right', 'wrist_right'), 
                 ('shoulder_left', 'hip_left'), ('shoulder_right', 'hip_right'), 
                 ('hip_left', 'knee_left'), ('hip_right', 'knee_right'), 
                 ('knee_left', 'ankle_left'), ('knee_right', 'ankle_right'), 
                 ('ankle_left', 'foot_left'), ('ankle_right', 'foot_right')]:
        ax.plot([points_motion[pair[0]][0], points_motion[pair[1]][0]], 
                [points_motion[pair[0]][1], points_motion[pair[1]][1]], 
                color='white', linewidth=1)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
