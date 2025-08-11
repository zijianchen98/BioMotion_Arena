
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent:
# 0-Head, 1-Left Shoulder, 2-Right Shoulder, 3-Left Elbow, 4-Right Elbow,
# 5-Left Wrist, 6-Right Wrist, 7-Chest, 8-Spine, 9-Hips, 10-Left Hip,
# 11-Right Hip, 12-Left Knee, 13-Right Knee, 14-Left Ankle, 15-Right Ankle
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [1, -1],  # Right Shoulder
    [-2, -2], # Left Elbow
    [2, -2],  # Right Elbow
    [-3, -3], # Left Wrist
    [3, -3],  # Right Wrist
    [0, -1],  # Chest
    [0, -2],  # Spine
    [0, -3],  # Hips
    [-1, -4], # Left Hip
    [1, -4],  # Right Hip
    [-1, -5], # Left Knee
    [1, -5],  # Right Knee
    [-1, -6], # Left Ankle
    [1, -6]   # Right Ankle
])

# Define the range of motion for each joint
# This will simulate the woman lying down with slight movements
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Simulate slight breathing motion by moving the chest up and down
    chest_amplitude = 0.1
    chest_frequency = 0.1
    chest_offset = chest_amplitude * np.sin(frame * chest_frequency)
    positions[7][1] += chest_offset
    
    # Simulate slight leg movement (knees bending)
    knee_amplitude = 0.2
    knee_frequency = 0.05
    left_knee_offset = knee_amplitude * np.sin(frame * knee_frequency)
    right_knee_offset = knee_amplitude * np.cos(frame * knee_frequency)
    positions[12][1] += left_knee_offset
    positions[13][1] += right_knee_offset
    
    # Simulate slight arm movement (elbows bending)
    elbow_amplitude = 0.2
    elbow_frequency = 0.07
    left_elbow_offset = elbow_amplitude * np.sin(frame * elbow_frequency)
    right_elbow_offset = elbow_amplitude * np.cos(frame * elbow_frequency)
    positions[3][1] += left_elbow_offset
    positions[4][1] += right_elbow_offset
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
