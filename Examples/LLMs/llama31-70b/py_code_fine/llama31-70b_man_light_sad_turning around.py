
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the sad man's joints
joints = {
    'head': [0, 0],
    'left_shoulder': [-0.2, 0.2],
    'right_shoulder': [0.2, 0.2],
    'left_elbow': [-0.3, 0],
    'right_elbow': [0.3, 0],
    'left_hand': [-0.4, -0.2],
    'right_hand': [0.4, -0.2],
    'left_hip': [-0.1, -0.3],
    'right_hip': [0.1, -0.3],
    'left_knee': [-0.1, -0.5],
    'right_knee': [0.1, -0.5],
    'left_foot': [-0.1, -0.7],
    'right_foot': [0.1, -0.7],
    'torso': [0, -0.1],
    'waist': [0, -0.4]
}

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the new joint positions based on the frame number
    head = [joints['head'][0], joints['head'][1] + np.sin(frame / 10.0) * 0.1]
    left_shoulder = [joints['left_shoulder'][0], joints['left_shoulder'][1] + np.sin(frame / 10.0) * 0.05]
    right_shoulder = [joints['right_shoulder'][0], joints['right_shoulder'][1] + np.sin(frame / 10.0) * 0.05]
    left_elbow = [joints['left_elbow'][0] + np.sin(frame / 5.0) * 0.1, joints['left_elbow'][1] + np.cos(frame / 5.0) * 0.1]
    right_elbow = [joints['right_elbow'][0] + np.sin(frame / 5.0) * 0.1, joints['right_elbow'][1] + np.cos(frame / 5.0) * 0.1]
    left_hand = [joints['left_hand'][0] + np.sin(frame / 2.0) * 0.1, joints['left_hand'][1] + np.cos(frame / 2.0) * 0.1]
    right_hand = [joints['right_hand'][0] + np.sin(frame / 2.0) * 0.1, joints['right_hand'][1] + np.cos(frame / 2.0) * 0.1]
    left_hip = [joints['left_hip'][0], joints['left_hip'][1] + np.sin(frame / 10.0) * 0.05]
    right_hip = [joints['right_hip'][0], joints['right_hip'][1] + np.sin(frame / 10.0) * 0.05]
    left_knee = [joints['left_knee'][0] + np.sin(frame / 5.0) * 0.1, joints['left_knee'][1] + np.cos(frame / 5.0) * 0.1]
    right_knee = [joints['right_knee'][0] + np.sin(frame / 5.0) * 0.1, joints['right_knee'][1] + np.cos(frame / 5.0) * 0.1]
    left_foot = [joints['left_foot'][0] + np.sin(frame / 2.0) * 0.1, joints['left_foot'][1] + np.cos(frame / 2.0) * 0.1]
    right_foot = [joints['right_foot'][0] + np.sin(frame / 2.0) * 0.1, joints['right_foot'][1] + np.cos(frame / 2.0) * 0.1]
    torso = [joints['torso'][0], joints['torso'][1] + np.sin(frame / 10.0) * 0.05]
    waist = [joints['waist'][0], joints['waist'][1] + np.sin(frame / 10.0) * 0.05]

    # Plot the joints
    ax.plot(head[0], head[1], 'o', markersize=5, color='white')
    ax.plot(left_shoulder[0], left_shoulder[1], 'o', markersize=5, color='white')
    ax.plot(right_shoulder[0], right_shoulder[1], 'o', markersize=5, color='white')
    ax.plot(left_elbow[0], left_elbow[1], 'o', markersize=5, color='white')
    ax.plot(right_elbow[0], right_elbow[1], 'o', markersize=5, color='white')
    ax.plot(left_hand[0], left_hand[1], 'o', markersize=5, color='white')
    ax.plot(right_hand[0], right_hand[1], 'o', markersize=5, color='white')
    ax.plot(left_hip[0], left_hip[1], 'o', markersize=5, color='white')
    ax.plot(right_hip[0], right_hip[1], 'o', markersize=5, color='white')
    ax.plot(left_knee[0], left_knee[1], 'o', markersize=5, color='white')
    ax.plot(right_knee[0], right_knee[1], 'o', markersize=5, color='white')
    ax.plot(left_foot[0], left_foot[1], 'o', markersize=5, color='white')
    ax.plot(right_foot[0], right_foot[1], 'o', markersize=5, color='white')
    ax.plot(torso[0], torso[1], 'o', markersize=5, color='white')
    ax.plot(waist[0], waist[1], 'o', markersize=5, color='white')

    # Plot the lines connecting the joints
    ax.plot([head[0], left_shoulder[0]], [head[1], left_shoulder[1]], color='white')
    ax.plot([head[0], right_shoulder[0]], [head[1], right_shoulder[1]], color='white')
    ax.plot([left_shoulder[0], left_elbow[0]], [left_shoulder[1], left_elbow[1]], color='white')
    ax.plot([right_shoulder[0], right_elbow[0]], [right_shoulder[1], right_elbow[1]], color='white')
    ax.plot([left_elbow[0], left_hand[0]], [left_elbow[1], left_hand[1]], color='white')
    ax.plot([right_elbow[0], right_hand[0]], [right_elbow[1], right_hand[1]], color='white')
    ax.plot([torso[0], left_hip[0]], [torso[1], left_hip[1]], color='white')
    ax.plot([torso[0], right_hip[0]], [torso[1], right_hip[1]], color='white')
    ax.plot([left_hip[0], left_knee[0]], [left_hip[1], left_knee[1]], color='white')
    ax.plot([right_hip[0], right_knee[0]], [right_hip[1], right_knee[1]], color='white')
    ax.plot([left_knee[0], left_foot[0]], [left_knee[1], left_foot[1]], color='white')
    ax.plot([right_knee[0], right_foot[0]], [right_knee[1], right_foot[1]], color='white')
    ax.plot([torso[0], waist[0]], [torso[1], waist[1]], color='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
