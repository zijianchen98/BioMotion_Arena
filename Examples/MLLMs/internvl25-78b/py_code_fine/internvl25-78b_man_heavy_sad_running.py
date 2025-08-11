
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and the axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Joint indices
joints = np.array([
    [0, 0],  # head
    [-3, -3], [3, -3],  # shoulders
    [-3, -5], [3, -5],  # elbows
    [-3, -7], [3, -7],  # wrists
    [0, -4],  # waist
    [-2, -6], [2, -6],  # hips
    [-2, -8], [2, -8],  # knees
    [-2, -10], [2, -10],  # ankles
    [0, -8],  # center of weight effect
])

# Create the initial scatter plot
sc = ax.scatter(joints[:, 0], joints[:, 1], c='white')

def update(frame):
    global joints
    angle = 0.05 * np.sin(frame * 0.1)  # Varying angle for rotation
    shift = 0.5 * np.sin(frame * 0.1)  # Varying shift for running motion

    # Update joints positions
    joints[0] = [shift, 0]  # head moves forward slightly

    shoulders = np.array([-3 + shift, -3 + shift])
    elbows = np.array([-3 + shift, -5 + shift])
    wrists = np.array([-3 + shift, -7 + shift])
    hips = np.array([-2 + shift, -6 + shift])
    knees = np.array([-2 + shift, -8 + shift])
    ankles = np.array([-2 + shift, -10 + shift])

    joints[1:3] = [shoulders, shoulders] * [[1, -1]]
    joints[3:5] = [elbows, elbows] * [[1, -1]]
    joints[5:7] = [wrists, wrists] * [[1, -1]]
    joints[7:9] = [hips, hips] * [[1, -1]]
    joints[9:11] = [knees, knees] * [[1, -1]]
    joints[11:13] = [ankles, ankles] * [[1, -1]]

    joints[13] = [0 + shift, -8]  # adjust weight effect position

    # Rotate joints for the running motion
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    joints = np.dot(joints, rotation_matrix)

    sc.set_offsets(joints)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.axis('off')
plt.show()
