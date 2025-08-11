
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint angles for sitting down (normalized to 0-1)
# These are simplified representations and could be refined with biomechanical models
joint_angles = {
    'head': [0.1, 0.1],  # Initial and final angles
    'neck': [0.2, 0.1],
    'shoulder_left': [0.3, 0.2],
    'shoulder_right': [0.3, 0.2],
    'elbow_left': [0.4, 0.3],
    'elbow_right': [0.4, 0.3],
    'wrist_left': [0.5, 0.4],
    'wrist_right': [0.5, 0.4],
    'hip_left': [0.6, 0.5],
    'hip_right': [0.6, 0.5],
    'knee_left': [0.7, 0.6],
    'knee_right': [0.7, 0.6],
    'ankle_left': [0.8, 0.7],
    'ankle_right': [0.8, 0.7],
    'toe_left': [0.9, 0.8],
    'toe_right': [0.9, 0.8]
}

# Define the number of frames in the animation
num_frames = 100

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the points
points = []
for joint_name, angles in joint_angles.items():
    x = 0.5 * (angles[0] + angles[1])
    y = 0.5 * (angles[0] + angles[1])
    points.append([x, y])

# Create the line object
line, = ax.plot([0, points[0][0]], [0, points[0][1]], 'w', lw=2)

# Initialize the animation
def init():
    line.set_data([], [])
    return line,

def animate(i):
    # Update the positions of the points
    for j, joint_name in enumerate(joint_angles):
        x = 0.5 * (joint_angles[joint_name][0] + joint_angles[joint_name][1])
        y = 0.5 * (joint_angles[joint_name][0] + joint_angles[joint_name][1])
        points[j] = [x, y]
    
    line.set_data([points[0][0], points[1][0]], [points[0][1], points[1][1]]) # simplified to 2 points
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("sitting_down.gif", writer='pillow', fps=30)

# Display the animation
plt.show()
