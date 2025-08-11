
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Define keyframes for the lying down motion
def get_keyframes(t):
    # Time is normalized between 0 and 1 for the animation cycle
    # The motion is periodic, so we use sine/cosine for smoothness
    
    # Head (1 point)
    head_x = 0.0
    head_y = 0.8 + 0.05 * np.sin(2 * np.pi * t)  # slight breathing motion
    
    # Shoulders (2 points)
    shoulder_left_x = -0.3
    shoulder_left_y = 0.7 + 0.02 * np.sin(2 * np.pi * t + 0.2)
    shoulder_right_x = 0.3
    shoulder_right_y = 0.7 + 0.02 * np.sin(2 * np.pi * t + 0.2)
    
    # Elbows (2 points)
    elbow_left_x = -0.4
    elbow_left_y = 0.5 + 0.03 * np.sin(2 * np.pi * t + 0.3)
    elbow_right_x = 0.4
    elbow_right_y = 0.5 + 0.03 * np.sin(2 * np.pi * t + 0.3)
    
    # Hands (2 points)
    hand_left_x = -0.5
    hand_left_y = 0.3 + 0.04 * np.sin(2 * np.pi * t + 0.4)
    hand_right_x = 0.5
    hand_right_y = 0.3 + 0.04 * np.sin(2 * np.pi * t + 0.4)
    
    # Torso (1 point - center)
    torso_x = 0.0
    torso_y = 0.5 + 0.02 * np.sin(2 * np.pi * t)
    
    # Hips (2 points)
    hip_left_x = -0.2
    hip_left_y = 0.3 + 0.02 * np.sin(2 * np.pi * t + 0.1)
    hip_right_x = 0.2
    hip_right_y = 0.3 + 0.02 * np.sin(2 * np.pi * t + 0.1)
    
    # Knees (2 points)
    knee_left_x = -0.25
    knee_left_y = 0.0 + 0.03 * np.sin(2 * np.pi * t + 0.2)
    knee_right_x = 0.25
    knee_right_y = 0.0 + 0.03 * np.sin(2 * np.pi * t + 0.2)
    
    # Feet (2 points)
    foot_left_x = -0.3
    foot_left_y = -0.3 + 0.04 * np.sin(2 * np.pi * t + 0.3)
    foot_right_x = 0.3
    foot_right_y = -0.3 + 0.04 * np.sin(2 * np.pi * t + 0.3)
    
    # Heaviness: slight downward shift and slower movement
    heaviness_factor = 0.1 * np.sin(np.pi * t)  # slower oscillation
    
    # Apply heaviness to y-coordinates
    head_y -= heaviness_factor * 0.2
    shoulder_left_y -= heaviness_factor * 0.2
    shoulder_right_y -= heaviness_factor * 0.2
    elbow_left_y -= heaviness_factor * 0.15
    elbow_right_y -= heaviness_factor * 0.15
    hand_left_y -= heaviness_factor * 0.1
    hand_right_y -= heaviness_factor * 0.1
    torso_y -= heaviness_factor * 0.15
    hip_left_y -= heaviness_factor * 0.1
    hip_right_y -= heaviness_factor * 0.1
    knee_left_y -= heaviness_factor * 0.05
    knee_right_y -= heaviness_factor * 0.05
    foot_left_y -= heaviness_factor * 0.05
    foot_right_y -= heaviness_factor * 0.05
    
    # Return all points in order
    return np.array([
        [head_x, head_y],  # 0: head
        [shoulder_left_x, shoulder_left_y],  # 1: left shoulder
        [shoulder_right_x, shoulder_right_y],  # 2: right shoulder
        [elbow_left_x, elbow_left_y],  # 3: left elbow
        [elbow_right_x, elbow_right_y],  # 4: right elbow
        [hand_left_x, hand_left_y],  # 5: left hand
        [hand_right_x, hand_right_y],  # 6: right hand
        [torso_x, torso_y],  # 7: torso
        [hip_left_x, hip_left_y],  # 8: left hip
        [hip_right_x, hip_right_y],  # 9: right hip
        [knee_left_x, knee_left_y],  # 10: left knee
        [knee_right_x, knee_right_y],  # 11: right knee
        [foot_left_x, foot_left_y],  # 12: left foot
        [foot_right_x, foot_right_y],  # 13: right foot
        [torso_x - 0.1, torso_y + 0.1]  # 14: additional point for heaviness (e.g., belly)
    ])

# Update function for animation
def update(frame):
    t = frame / 30  # 30 frames per cycle
    keyframes = get_keyframes(t)
    for i, point in enumerate(points):
        point.set_data(keyframes[i, 0], keyframes[i, 1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=30, interval=50, blit=True)

plt.tight_layout()
plt.show()
