
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
num_point_lights = 15
num_frames = 100

# Define the joints and their initial positions
joints = {
    'head': np.array([0, 10]),
    'left_shoulder': np.array([-2, 8]),
    'right_shoulder': np.array([2, 8]),
    'left_elbow': np.array([-4, 6]),
    'right_elbow': np.array([4, 6]),
    'left_hand': np.array([-6, 4]),
    'right_hand': np.array([6, 4]),
    'left_hip': np.array([-2, 2]),
    'right_hip': np.array([2, 2]),
    'left_knee': np.array([-2, 0]),
    'right_knee': np.array([2, 0]),
    'left_ankle': np.array([-2, -2]),
    'right_ankle': np.array([2, -2]),
    'left_foot': np.array([-2, -4]),
    'right_foot': np.array([2, -4])
}

# Define the movement of each joint over time
def get_joint_position(joint, frame):
    if joint == 'head':
        return np.array([0, 10 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_shoulder':
        return np.array([-2, 8 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_shoulder':
        return np.array([2, 8 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_elbow':
        return np.array([-4, 6 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_elbow':
        return np.array([4, 6 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_hand':
        return np.array([-6, 4 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_hand':
        return np.array([6, 4 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_hip':
        return np.array([-2, 2 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_hip':
        return np.array([2, 2 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_knee':
        return np.array([-2, 0 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_knee':
        return np.array([2, 0 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_ankle':
        return np.array([-2, -2 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_ankle':
        return np.array([2, -2 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'left_foot':
        return np.array([-2, -4 + 2 * np.sin(2 * np.pi * frame / num_frames)])
    elif joint == 'right_foot':
        return np.array([2, -4 + 2 * np.sin(2 * np.pi * frame / num_frames)])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 20)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
point_lights = []
for joint in joints:
    point_light, = ax.plot(joints[joint][0], joints[joint][1], 'o', markersize=5, color='white')
    point_lights.append(point_light)

# Define the animation function
def animate(frame):
    for i, joint in enumerate(joints):
        point_lights[i].set_data(get_joint_position(joint, frame)[0], get_joint_position(joint, frame)[1])
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

plt.show()
