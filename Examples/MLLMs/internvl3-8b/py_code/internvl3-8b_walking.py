
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
n_points = 15
n_frames = 100
frame_rate = 10  # Hz

# Generating initial positions (man walking)
positions = {
    'head': np.array([50, 50]),
    'upper_torso': np.array([60, 58]),
    'lower_torso': np.array([70, 68]),
    'right_upper_limb': np.array([80, 74]),
    'right_lower_limb': np.array([80, 88]),
    'left_upper_limb': np.array([70, 77]),
    'left_lower_limb': np.array([60, 90]),
    'right_arm': np.array([70, 82]),
    'right_knee': np.array([60, 82]),
    'left_arm': np.array([60, 70]),
    'left_knee': np.array([50, 74]),
    'right_wrist': np.array([70, 90]),
    'left_wrist': np.array([60, 70]),
}

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

# Function to update each frame
def update(frame):
    if frame > frame_rate * 0.3:
        positions['head'][1] += 2
    if frame > frame_rate * 0.5:
        positions['upper_torso'][1] += 2
    if frame > frame_rate * 0.7:
        positions['lower_torso'][1] += 2
    if frame > frame_rate * 0.9:
        positions['right_upper_limb'][1] += 2.5
        positions['upper_torso'][0] += 1
        positions['left_upper_limb'][1] += 2.5
        positions['upper_torso'][0] -= 1
    if frame > frame_rate * 1.2:
        positions['right_lower_limb'][1] += 1
        positions['right_upper_limb'][0] += 1
        positions['left_lower_limb'][1] += 1
        positions['left_upper_limb'][0] -= 1
    if frame > frame_rate * 1.5:
        positions['right_upper_limb'][0] -= 0.5
        positions['right_lower_limb'][0] -= 0.5
        positions['left_upper_limb'][0] += 0.5
        positions['left_lower_limb'][0] += 0.5
    if frame > frame_rate * 1.8:
        positions['right_knee'][1] += 1.3
        positions['right_wrist'][1] += 1.3
        positions['left_knee'][1] += 1
        positions['left_wrist'][1] += 1
        positions['right_wrist'][0] += 1
        positions['left_wrist'][0] -= 1
    ax.clear()
    for key, pos in positions.items():
        ax.scatter(pos[0], pos[1], color='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=1000/frame_rate, repeat=False)

# Display animation
plt.show()
