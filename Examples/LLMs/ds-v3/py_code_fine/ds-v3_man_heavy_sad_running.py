
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the running motion (simplified)
# Each keyframe is a list of (x, y) positions for the 15 points
# The points represent: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso, and 2 additional points for the back
keyframes = []

# Parameters for the running motion
stride_length = 1.5
leg_swing = 0.8
arm_swing = 0.6
torso_height = 0.2

# Generate keyframes for one running cycle (8 phases)
for phase in np.linspace(0, 2 * np.pi, 16):
    # Head
    head_x = 0
    head_y = 1.5 + 0.1 * np.sin(phase * 2)
    
    # Shoulders (shoulders)
    shoulder_left_x = -0.3
    shoulder_left_y = 1.3 + 0.05 * np.sin(phase * 2)
    shoulder_right_x = 0.3
    shoulder_right_y = 1.3 + 0.05 * np.sin(phase * 2)
    
    # Elbows
    elbow_left_x = -0.3 - 0.3 * np.sin(phase * 2 + np.pi/2)
    elbow_left_y = 1.0 + 0.1 * np.sin(phase * 2)
    elbow_right_x = 0.3 + 0.3 * np.sin(phase * 2 + np.pi/2)
    elbow_right_y = 1.0 + 0.1 * np.sin(phase * 2)
    
    # Hands
    hand_left_x = elbow_left_x - 0.2 * np.sin(phase * 2 + np.pi/2)
    hand_left_y = elbow_left_y - 0.2 * np.cos(phase * 2 + np.pi/2)
    hand_right_x = elbow_right_x + 0.2 * np.sin(phase * 2 + np.pi/2)
    hand_right_y = elbow_right_y - 0.2 * np.cos(phase * 2 + np.pi/2)
    
    # Hips
    hip_left_x = -0.2
    hip_left_y = 0.8 + 0.05 * np.sin(phase * 2)
    hip_right_x = 0.2
    hip_right_y = 0.8 + 0.05 * np.sin(phase * 2)
    
    # Knees
    knee_left_x = -0.2 - 0.1 * np.sin(phase * 2)
    knee_left_y = 0.4 - 0.2 * np.cos(phase * 2)
    knee_right_x = 0.2 + 0.1 * np.sin(phase * 2)
    knee_right_y = 0.4 + 0.2 * np.cos(phase * 2)
    
    # Feet
    foot_left_x = knee_left_x - 0.1 * np.sin(phase * 2)
    foot_left_y = 0.1 - 0.1 * np.cos(phase * 2)
    foot_right_x = knee_right_x + 0.1 * np.sin(phase * 2)
    foot_right_y = 0.1 + 0.1 * np.cos(phase * 2)
    
    # Torso (midpoint between shoulders and hips)
    torso_x = 0
    torso_y = 1.3 + 0.8 / 2
    
    # Back points (to give more body structure)
    back1_x = 0
    back1_y = 1.1
    back2_x = 0
    back2_y = 0.9
    
    # Collect all points in order
    frame = np.array([
        [head_x, head_y],
        [shoulder_left_x, shoulder_left_y],
        [shoulder_right_x, shoulder_right_y],
        [elbow_left_x, elbow_left_y],
        [elbow_right_x, elbow_right_y],
        [hand_left_x, hand_left_y],
        [hand_right_x, hand_right_y],
        [hip_left_x, hip_left_y],
        [hip_right_x, hip_right_y],
        [knee_left_x, knee_left_y],
        [knee_right_x, knee_right_y],
        [foot_left_x, foot_left_y],
        [foot_right_x, foot_right_y],
        [back1_x, back1_y],
        [back2_x, back2_y]
    ])
    
    keyframes.append(frame)

# Convert keyframes to a numpy array
keyframes = np.array(keyframes)

# Animation function
def update(frame):
    points.set_data(keyframes[frame % len(keyframes)][:, 0], 
                    keyframes[frame % len(keyframes)][:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(keyframes), interval=100, blit=True)

plt.tight_layout()
plt.show()
