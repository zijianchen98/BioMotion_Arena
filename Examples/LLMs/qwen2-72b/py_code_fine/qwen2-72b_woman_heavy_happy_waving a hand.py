
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define joint positions at rest
joint_positions = {
    'neck': [0, 0],
    'right_shoulder': [-0.5, -0.5],
    'left_shoulder': [0.5, -0.5],
    'right_elbow': [-0.75, -1],
    'left_elbow': [0.75, -1],
    'right_wrist': [-0.85, -1.5],
    'left_wrist': [0.85, -1.5],
}

# Define initial light positions
light_positions = list(joint_positions.values())

# Animation parameters
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 0.5)
ax.set_facecolor('black')

# Create scatter plot for lights
scatter = ax.scatter(*zip(*light_positions), color='white', s=100)

def update(frame):
    # Update the position of the left arm to simulate a wave
    angle = np.sin(frame / 50) * np.pi / 4
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Rotate the left arm
    left_elbow_pos = np.array(joint_positions['left_elbow'])
    left_wrist_pos = np.array(joint_positions['left_wrist'])
    new_left_wrist_pos = np.dot(rotation_matrix, left_wrist_pos - left_elbow_pos) + left_elbow_pos
    
    # Update the light positions
    light_positions[joint_positions.keys().index('left_wrist')] = new_left_wrist_pos.tolist()
    
    # Update the scatter plot
    scatter.set_offsets(light_positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
