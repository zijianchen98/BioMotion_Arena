
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their indices
body_parts = {
    'head': 0,
    'neck': 1,
    'torso': 2,
    'upper_left_arm': 3,
    'lower_left_arm': 4,
    'upper_right_arm': 5,
    'lower_right_arm': 6,
    'upper_left_leg': 7,
    'lower_left_leg': 8,
    'upper_right_leg': 9,
    'lower_right_leg': 10,
    'left_hand': 11,
    'right_hand': 12,
    'left_foot': 13,
    'right_foot': 14
}

# Define initial positions of the body parts (centered at origin)
initial_positions = np.array([
    [0, 0.5],   # head
    [0, 0.3],   # neck
    [0, 0.1],   # torso
    [-0.2, 0.1], # upper_left_arm
    [-0.3, 0.05], # lower_left_arm
    [0.2, 0.1],  # upper_right_arm
    [0.3, 0.05], # lower_right_arm
    [-0.2, -0.2], # upper_left_leg
    [-0.3, -0.4], # lower_left_leg
    [0.2, -0.2], # upper_right_leg
    [0.3, -0.4], # lower_right_leg
    [-0.3, 0.05], # left_hand
    [0.3, 0.05], # right_hand
    [-0.3, -0.4], # left_foot
    [0.3, -0.4]  # right_foot
])

# Define the animation parameters
num_frames = 100
frame_duration = 50  # ms
speed_factor = 0.05

# Create the point lights
point_lights = [ax.plot([], [], 'o', color='white', markersize=10)[0] for _ in range(15)]

def update(frame):
    # Simulate a walking motion
    t = frame / num_frames
    # Simple sinusoidal motion for legs and arms
    leg_phase = t * 2 * np.pi * 2
    arm_phase = t * 2 * np.pi * 2

    # Update positions
    positions = initial_positions.copy()
    # Legs
    positions[7] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    positions[8] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    positions[9] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    positions[10] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    # Arms
    positions[3] += np.array([-0.1 * np.sin(arm_phase + np.pi/2), 0])
    positions[4] += np.array([-0.1 * np.sin(arm_phase + np.pi/2), 0])
    positions[5] += np.array([0.1 * np.sin(arm_phase + np.pi/2), 0])
    positions[6] += np.array([0.1 * np.sin(arm_phase + np.pi/2), 0])
    # Hands
    positions[11] += np.array([-0.1 * np.sin(arm_phase + np.pi/2), 0])
    positions[12] += np.array([0.1 * np.sin(arm_phase + np.pi/2), 0])
    # Feet
    positions[13] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    positions[14] += np.array([0, -0.1 * np.sin(leg_phase + np.pi/2)])
    # Head and torso
    positions[0] += np.array([0, -0.05 * np.sin(leg_phase)])
    positions[1] += np.array([0, -0.05 * np.sin(leg_phase)])
    positions[2] += np.array([0, -0.05 * np.sin(leg_phase)])

    # Update the point lights
    for i, light in enumerate(point_lights):
        light.set_data(positions[i][0], positions[i][1])

    return point_lights

ani = FuncAnimation(fig, update, frames=num_frames, interval=frame_duration, blit=True)

plt.show()
