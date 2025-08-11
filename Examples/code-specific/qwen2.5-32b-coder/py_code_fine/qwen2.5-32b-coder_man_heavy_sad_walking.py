
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
dt = 0.1
g = 9.81
mass = 70  # kg
weight = mass * g
step_length = 0.6  # meters
step_height = 0.1  # meters
fps = 30

# Initialize positions
positions = np.zeros((num_lights, 2))
angles = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)

# Define joint indices for a simplified walking model
joints = {
    'head': 0,
    'neck': 1,
    'torso_top': 2,
    'torso_bottom': 3,
    'left_shoulder': 4,
    'left_elbow': 5,
    'left_hand': 6,
    'right_shoulder': 7,
    'right_elbow': 8,
    'right_hand': 9,
    'left_hip': 10,
    'left_knee': 11,
    'left_foot': 12,
    'right_hip': 13,
    'right_knee': 14,
    'right_foot': 15
}

# Define lengths of body segments
lengths = {
    'head_neck': 0.15,
    'neck_torso': 0.25,
    'torso_upper_leg': 0.3,
    'upper_leg_lower_leg': 0.35,
    'lower_leg_foot': 0.25,
    'torso_shoulder': 0.15,
    'shoulder_elbow': 0.25,
    'elbow_hand': 0.2
}

# Initialize angles
angle_head_neck = np.deg2rad(15)
angle_neck_torso = np.deg2rad(-10)
angle_torso_upper_leg_left = np.deg2rad(-20)
angle_torso_upper_leg_right = np.deg2rad(-20)
angle_upper_leg_lower_leg_left = np.deg2rad(-40)
angle_upper_leg_lower_leg_right = np.deg2rad(-40)
angle_torso_shoulder_left = np.deg2rad(15)
angle_torso_shoulder_right = np.deg2rad(-15)
angle_shoulder_elbow_left = np.deg2rad(-30)
angle_shoulder_elbow_right = np.deg2rad(30)
angle_elbow_hand_left = np.deg2rad(45)
angle_elbow_hand_right = np.deg2rad(-45)

def update(frame):
    t = frame / fps
    
    # Walking motion
    phase_left = t
    phase_right = t + np.pi
    
    # Update angles for walking
    angle_torso_upper_leg_left = -np.pi/4 + step_height * np.sin(phase_left)
    angle_torso_upper_leg_right = -np.pi/4 + step_height * np.sin(phase_right)
    angle_upper_leg_lower_leg_left = -3*np.pi/4 + step_height * np.sin(phase_left)
    angle_upper_leg_lower_leg_right = -3*np.pi/4 + step_height * np.sin(phase_right)
    
    # Update positions based on angles
    positions[joints['head']] = [lengths['neck_torso'] * np.cos(angle_neck_torso), lengths['neck_torso'] * np.sin(angle_neck_torso)]
    positions[joints['neck']] = [0, 0]
    positions[joints['torso_top']] = [lengths['neck_torso'] * np.cos(angle_neck_torso), lengths['neck_torso'] * np.sin(angle_neck_torso)]
    positions[joints['torso_bottom']] = [positions[joints['torso_top']][0] + lengths['torso_upper_leg_left'] * np.cos(angle_torso_upper_leg_left),
                                        positions[joints['torso_top']][1] + lengths['torso_upper_leg_left'] * np.sin(angle_torso_upper_leg_left)]
    positions[joints['left_hip']] = positions[joints['torso_bottom']]
    positions[joints['left_knee']] = [positions[joints['left_hip']][0] + lengths['upper_leg_lower_leg_left'] * np.cos(angle_upper_leg_lower_leg_left),
                                      positions[joints['left_hip']][1] + lengths['upper_leg_lower_leg_left'] * np.sin(angle_upper_leg_lower_leg_left)]
    positions[joints['left_foot']] = [positions[joints['left_knee']][0] + lengths['lower_leg_foot'] * np.cos(angle_upper_leg_lower_leg_left),
                                      positions[joints['left_knee']][1] + lengths['lower_leg_foot'] * np.sin(angle_upper_leg_lower_leg_left)]
    positions[joints['right_hip']] = positions[joints['torso_bottom']]
    positions[joints['right_knee']] = [positions[joints['right_hip']][0] + lengths['upper_leg_lower_leg_right'] * np.cos(angle_upper_leg_lower_leg_right),
                                       positions[joints['right_hip']][1] + lengths['upper_leg_lower_leg_right'] * np.sin(angle_upper_leg_lower_leg_right)]
    positions[joints['right_foot']] = [positions[joints['right_knee']][0] + lengths['lower_leg_foot'] * np.cos(angle_upper_leg_lower_leg_right),
                                       positions[joints['right_knee']][1] + lengths['lower_leg_foot'] * np.sin(angle_upper_leg_lower_leg_right)]
    positions[joints['left_shoulder']] = [positions[joints['torso_top']][0] + lengths['torso_shoulder_left'] * np.cos(angle_torso_shoulder_left),
                                          positions[joints['torso_top']][1] + lengths['torso_shoulder_left'] * np.sin(angle_torso_shoulder_left)]
    positions[joints['left_elbow']] = [positions[joints['left_shoulder']][0] + lengths['shoulder_elbow_left'] * np.cos(angle_shoulder_elbow_left),
                                        positions[joints['left_shoulder']][1] + lengths['shoulder_elbow_left'] * np.sin(angle_shoulder_elbow_left)]
    positions[joints['left_hand']] = [positions[joints['left_elbow']][0] + lengths['elbow_hand_left'] * np.cos(angle_elbow_hand_left),
                                       positions[joints['left_elbow']][1] + lengths['elbow_hand_left'] * np.sin(angle_elbow_hand_left)]
    positions[joints['right_shoulder']] = [positions[joints['torso_top']][0] + lengths['torso_shoulder_right'] * np.cos(angle_torso_shoulder_right),
                                           positions[joints['torso_top']][1] + lengths['torso_shoulder_right'] * np.sin(angle_torso_shoulder_right)]
    positions[joints['right_elbow']] = [positions[joints['right_shoulder']][0] + lengths['shoulder_elbow_right'] * np.cos(angle_shoulder_elbow_right),
                                         positions[joints['right_shoulder']][1] + lengths['shoulder_elbow_right'] * np.sin(angle_shoulder_elbow_right)]
    positions[joints['right_hand']] = [positions[joints['right_elbow']][0] + lengths['elbow_hand_right'] * np.cos(angle_elbow_hand_right),
                                        positions[joints['right_elbow']][1] + lengths['elbow_hand_right'] * np.sin(angle_elbow_hand_right)]
    
    # Shift positions to simulate walking forward
    x_offset = step_length * np.sin(t)
    positions[:, 0] += x_offset
    
    scatter.set_offsets(positions)
    return scatter,

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
