
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joints and their initial positions
joints = {
    'head': np.array([0, 10]),
   'shoulder_left': np.array([-2, 8]),
   'shoulder_right': np.array([2, 8]),
    'elbow_left': np.array([-4, 6]),
    'elbow_right': np.array([4, 6]),
    'wrist_left': np.array([-6, 4]),
    'wrist_right': np.array([6, 4]),
    'hip_left': np.array([-2, 2]),
    'hip_right': np.array([2, 2]),
    'knee_left': np.array([-2, 0]),
    'knee_right': np.array([2, 0]),
    'ankle_left': np.array([-2, -2]),
    'ankle_right': np.array([2, -2]),
    'hand_left': np.array([-6, 2]),
    'hand_right': np.array([6, 2])
}

# Define the movement functions
def turn_around(t):
    angle = np.radians(t)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    joints['head'] = np.array([0, 10])
    joints['shoulder_left'] = np.dot(rotation_matrix, np.array([-2, 8]))
    joints['shoulder_right'] = np.dot(rotation_matrix, np.array([2, 8]))
    joints['elbow_left'] = np.dot(rotation_matrix, np.array([-4, 6])) + np.array([-1, 0])
    joints['elbow_right'] = np.dot(rotation_matrix, np.array([4, 6])) + np.array([1, 0])
    joints['wrist_left'] = np.dot(rotation_matrix, np.array([-6, 4])) + np.array([-1.5, 0])
    joints['wrist_right'] = np.dot(rotation_matrix, np.array([6, 4])) + np.array([1.5, 0])
    joints['hip_left'] = np.dot(rotation_matrix, np.array([-2, 2]))
    joints['hip_right'] = np.dot(rotation_matrix, np.array([2, 2]))
    joints['knee_left'] = np.dot(rotation_matrix, np.array([-2, 0])) + np.array([0, -1])
    joints['knee_right'] = np.dot(rotation_matrix, np.array([2, 0])) + np.array([0, -1])
    joints['ankle_left'] = np.dot(rotation_matrix, np.array([-2, -2])) + np.array([0, -2])
    joints['ankle_right'] = np.dot(rotation_matrix, np.array([2, -2])) + np.array([0, -2])
    joints['hand_left'] = np.dot(rotation_matrix, np.array([-6, 2])) + np.array([-1.5, 0])
    joints['hand_right'] = np.dot(rotation_matrix, np.array([6, 2])) + np.array([1.5, 0])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot
scatter = ax.scatter(*zip(*joints.values()), color='white')

# Define the animation function
def animate(t):
    turn_around(t)
    scatter.set_offsets(list(joints.values()))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(0, 360, 2), interval=50)

plt.show()
