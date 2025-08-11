
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

# Define keyframes for a running motion (simplified)
def get_keyframe(t):
    # Time-dependent parameters
    phase = 2 * np.pi * t / 20  # Running cycle
    
    # Body motion (torso)
    torso_x = 0.5 * np.sin(phase)
    torso_y = 0.1 * np.sin(2 * phase)
    
    # Head
    head_x = torso_x
    head_y = torso_y + 0.3
    
    # Arms (left and right)
    arm_amplitude = 0.4
    left_arm_x = torso_x - 0.2 - arm_amplitude * np.sin(phase + np.pi/2)
    left_arm_y = torso_y + 0.2 + 0.1 * np.sin(2 * phase)
    right_arm_x = torso_x + 0.2 + arm_amplitude * np.sin(phase + np.pi/2)
    right_arm_y = torso_y + 0.2 + 0.1 * np.sin(2 * phase)
    
    # Hands
    left_hand_x = left_arm_x - 0.1 * np.sin(phase + np.pi/2)
    left_hand_y = left_arm_y - 0.1
    right_hand_x = right_arm_x + 0.1 * np.sin(phase + np.pi/2)
    right_hand_y = right_arm_y - 0.1
    
    # Legs (left and right)
    leg_amplitude = 0.5
    left_leg_x = torso_x - 0.15 - 0.1 * np.sin(phase)
    left_leg_y = torso_y - 0.3 - leg_amplitude * np.sin(phase)
    right_leg_x = torso_x + 0.15 + 0.1 * np.sin(phase)
    right_leg_y = torso_y - 0.3 + leg_amplitude * np.sin(phase)
    
    # Feet
    left_foot_x = left_leg_x - 0.1 * np.sin(phase)
    left_foot_y = left_leg_y - 0.2
    right_foot_x = right_leg_x + 0.1 * np.sin(phase)
    right_foot_y = right_leg_y - 0.2
    
    # Additional points for heavier appearance (e.g., broader shoulders, hips)
    left_shoulder_x = torso_x - 0.3
    left_shoulder_y = torso_y + 0.15
    right_shoulder_x = torso_x + 0.3
    right_shoulder_y = torso_y + 0.15
    left_hip_x = torso_x - 0.25
    left_hip_y = torso_y - 0.1
    right_hip_x = torso_x + 0.25
    right_hip_y = torso_y - 0.1
    
    # Combine all points
    x = np.array([
        head_x, 
        left_shoulder_x, right_shoulder_x,
        left_arm_x, right_arm_x,
        left_hand_x, right_hand_x,
        torso_x,
        left_hip_x, right_hip_x,
        left_leg_x, right_leg_x,
        left_foot_x, right_foot_x,
        torso_x - 0.1 * np.sin(phase)  # Additional point for heaviness
    ])
    
    y = np.array([
        head_y,
        left_shoulder_y, right_shoulder_y,
        left_arm_y, right_arm_y,
        left_hand_y, right_hand_y,
        torso_y,
        left_hip_y, right_hip_y,
        left_leg_y, right_leg_y,
        left_foot_y, right_foot_y,
        torso_y - 0.2  # Additional point for heaviness
    ])
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_keyframe(frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.linspace(0, 20, 100), 
    interval=50, blit=True
)

plt.tight_layout()
plt.show()
