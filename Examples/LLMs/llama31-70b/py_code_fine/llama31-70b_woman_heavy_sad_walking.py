
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joints and their initial positions
joints = {
    'head': np.array([0, 10]),
    'left_shoulder': np.array([-2, 8]),
    'right_shoulder': np.array([2, 8]),
    'left_elbow': np.array([-4, 6]),
    'right_elbow': np.array([4, 6]),
    'left_hand': np.array([-6, 4]),
    'right_hand': np.array([6, 4]),
    'left_hip': np.array([-2, 4]),
    'right_hip': np.array([2, 4]),
    'left_knee': np.array([-2, 2]),
    'right_knee': np.array([2, 2]),
    'left_ankle': np.array([-2, 0]),
    'right_ankle': np.array([2, 0]),
    'torso': np.array([0, 6]),
    'weight': np.array([0, -2])
}

# Define the movement patterns for each joint
def move_head(frame):
    return joints['head'] + np.array([0, np.sin(frame / 10.0)])

def move_left_shoulder(frame):
    return joints['left_shoulder'] + np.array([-np.sin(frame / 10.0), np.cos(frame / 10.0)])

def move_right_shoulder(frame):
    return joints['right_shoulder'] + np.array([np.sin(frame / 10.0), np.cos(frame / 10.0)])

def move_left_elbow(frame):
    return joints['left_elbow'] + np.array([-np.sin(frame / 5.0), np.cos(frame / 5.0)])

def move_right_elbow(frame):
    return joints['right_elbow'] + np.array([np.sin(frame / 5.0), np.cos(frame / 5.0)])

def move_left_hand(frame):
    return joints['left_hand'] + np.array([-np.sin(frame / 2.0), np.cos(frame / 2.0)])

def move_right_hand(frame):
    return joints['right_hand'] + np.array([np.sin(frame / 2.0), np.cos(frame / 2.0)])

def move_left_hip(frame):
    return joints['left_hip'] + np.array([-np.sin(frame / 10.0), np.cos(frame / 10.0)])

def move_right_hip(frame):
    return joints['right_hip'] + np.array([np.sin(frame / 10.0), np.cos(frame / 10.0)])

def move_left_knee(frame):
    return joints['left_knee'] + np.array([-np.sin(frame / 5.0), np.cos(frame / 5.0)])

def move_right_knee(frame):
    return joints['right_knee'] + np.array([np.sin(frame / 5.0), np.cos(frame / 5.0)])

def move_left_ankle(frame):
    return joints['left_ankle'] + np.array([-np.sin(frame / 2.0), np.cos(frame / 2.0)])

def move_right_ankle(frame):
    return joints['right_ankle'] + np.array([np.sin(frame / 2.0), np.cos(frame / 2.0)])

def move_torso(frame):
    return joints['torso'] + np.array([0, np.sin(frame / 10.0)])

def move_weight(frame):
    return joints['weight'] + np.array([0, np.sin(frame / 10.0)])

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
point_lights = [
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0],
    ax.plot([], [], 'o', markersize=5, color='white')[0]
]

# Animation function
def animate(frame):
    point_lights[0].set_data(move_head(frame)[0], move_head(frame)[1])
    point_lights[1].set_data(move_left_shoulder(frame)[0], move_left_shoulder(frame)[1])
    point_lights[2].set_data(move_right_shoulder(frame)[0], move_right_shoulder(frame)[1])
    point_lights[3].set_data(move_left_elbow(frame)[0], move_left_elbow(frame)[1])
    point_lights[4].set_data(move_right_elbow(frame)[0], move_right_elbow(frame)[1])
    point_lights[5].set_data(move_left_hand(frame)[0], move_left_hand(frame)[1])
    point_lights[6].set_data(move_right_hand(frame)[0], move_right_hand(frame)[1])
    point_lights[7].set_data(move_left_hip(frame)[0], move_left_hip(frame)[1])
    point_lights[8].set_data(move_right_hip(frame)[0], move_right_hip(frame)[1])
    point_lights[9].set_data(move_left_knee(frame)[0], move_left_knee(frame)[1])
    point_lights[10].set_data(move_right_knee(frame)[0], move_right_knee(frame)[1])
    point_lights[11].set_data(move_left_ankle(frame)[0], move_left_ankle(frame)[1])
    point_lights[12].set_data(move_right_ankle(frame)[0], move_right_ankle(frame)[1])
    point_lights[13].set_data(move_torso(frame)[0], move_torso(frame)[1])
    point_lights[14].set_data(move_weight(frame)[0], move_weight(frame)[1])
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True, interval=50)

plt.show()
