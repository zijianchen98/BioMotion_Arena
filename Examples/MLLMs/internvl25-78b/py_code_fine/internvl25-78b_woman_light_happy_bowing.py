
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint structure for a bowing motion
def init():
    for body_part in body_parts.values():
        body_part.set_data([], [])
    return body_parts.values()

def update(frame):
    # Angles and positions based on a simplified model
    head_pos = np.array([0, 2])
    neck_pos = np.array([0, 1])
    torso_pos = np.array([0, 0])
    pelvis_pos = np.array([0, -1])
    
    # Define arms and legs positions
    arms_pos = [np.array([0.3, 0]), np.array([-0.3, 0]), np.array([0.6, -0.2]), np.array([-0.6, -0.2])]
    legs_pos = [np.array([0.2, -1]), np.array([-0.2, -1]), np.array([0.4, -1.5]), np.array([-0.4, -1.5])]
    
    # Bowing motion
    angle = np.radians(frame * 2)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    head_pos = np.dot(rotation_matrix, head_pos)
    neck_pos = np.dot(rotation_matrix, neck_pos)
    torso_pos = np.dot(rotation_matrix, torso_pos)
    
    # Update points
    body_parts['head'].set_data(*head_pos)
    body_parts['neck'].set_data(*neck_pos)
    body_parts['torso'].set_data(*torso_pos)
    body_parts['pelvis'].set_data(*pelvis_pos)
    
    for i, arm in enumerate(arms_pos):
        arm = np.dot(rotation_matrix, arm)
        body_parts[f'arm_{i}'].set_data(*arm)
    
    for i, leg in enumerate(legs_pos):
        leg = np.dot(rotation_matrix, leg)
        body_parts[f'leg_{i}'].set_data(*leg)
    
    return body_parts.values()

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')

body_parts = {
    'head': plt.plot([], [], 'wo')[0],
    'neck': plt.plot([], [], 'wo')[0],
    'torso': plt.plot([], [], 'wo')[0],
    'pelvis': plt.plot([], [], 'wo')[0],
    'arm_0': plt.plot([], [], 'wo')[0],
    'arm_1': plt.plot([], [], 'wo')[0],
    'arm_2': plt.plot([], [], 'wo')[0],
    'arm_3': plt.plot([], [], 'wo')[0],
    'leg_0': plt.plot([], [], 'wo')[0],
    'leg_1': plt.plot([], [], 'wo')[0],
    'leg_2': plt.plot([], [], 'wo')[0],
    'leg_3': plt.plot([], [], 'wo')[0]
}

# Animation
ani = animation.FuncAnimation(fig, update, frames=30, init_func=init, blit=True)

plt.axis('off')
plt.show()
