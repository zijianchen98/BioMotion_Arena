
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Define the number of points and frames
num_points = 15
num_frames = 60  # Number of frames in the animation cycle

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize the point lights
points = ax.scatter([], [], color='white', s=50)

# Define the key positions for the running motion (simplified)
def get_key_positions(frame):
    t = 2 * np.pi * frame / num_frames
    # Main body points (e.g., head, torso, hips)
    head_x = 0.1 * np.sin(t)
    head_y = 1.5 + 0.1 * np.cos(t)
    
    torso_x = 0.05 * np.sin(t + 0.2)
    torso_y = 1.0 + 0.05 * np.cos(t + 0.2)
    
    hip_x = 0.0
    hip_y = 0.5 + 0.05 * np.cos(t)
    
    # Legs (thighs and shins)
    left_thigh_x = -0.2 + 0.1 * np.sin(t * 2)
    left_thigh_y = 0.3 + 0.1 * np.cos(t * 2)
    
    right_thigh_x = 0.2 - 0.1 * np.sin(t * 2)
    right_thigh_y = 0.3 - 0.1 * np.cos(t * 2)
    
    left_shin_x = left_thigh_x - 0.1 * np.sin(t * 2 + np.pi/4)
    left_shin_y = left_thigh_y - 0.3 * np.cos(t * 2 + np.pi/4)
    
    right_shin_x = right_thigh_x + 0.1 * np.sin(t * 2 + np.pi/4)
    right_shin_y = right_thigh_y - 0.3 * np.cos(t * 2 + np.pi/4)
    
    # Arms (upper and lower)
    left_upper_arm_x = -0.3 - 0.1 * np.sin(t * 2 + np.pi/2)
    left_upper_arm_y = 1.2 + 0.1 * np.cos(t * 2 + np.pi/2)
    
    right_upper_arm_x = 0.3 + 0.1 * np.sin(t * 2 + np.pi/2)
    right_upper_arm_y = 1.2 - 0.1 * np.cos(t * 2 + np.pi/2)
    
    left_lower_arm_x = left_upper_arm_x - 0.1 * np.sin(t * 2 + np.pi)
    left_lower_arm_y = left_upper_arm_y - 0.2 * np.cos(t * 2 + np.pi)
    
    right_lower_arm_x = right_upper_arm_x + 0.1 * np.sin(t * 2 + np.pi)
    right_lower_arm_y = right_upper_arm_y - 0.2 * np.cos(t * 2 + np.pi)
    
    # Feet and hands
    left_foot_x = left_shin_x - 0.05 * np.sin(t * 2 + np.pi/2)
    left_foot_y = left_shin_y - 0.1 * np.cos(t * 2 + np.pi/2)
    
    right_foot_x = right_shin_x + 0.05 * np.sin(t * 2 + np.pi/2)
    right_foot_y = right_shin_y - 0.1 * np.cos(t * 2 + np.pi/2)
    
    left_hand_x = left_lower_arm_x - 0.05 * np.sin(t * 2 + np.pi/2)
    left_hand_y = left_lower_arm_y - 0.05 * np.cos(t * 2 + np.pi/2)
    
    right_hand_x = right_lower_arm_x + 0.05 * np.sin(t * 2 + np.pi/2)
    right_hand_y = right_lower_arm_y - 0.05 * np.cos(t * 2 + np.pi/2)
    
    # Combine all points
    x = np.array([
        head_x, torso_x, hip_x,
        left_thigh_x, right_thigh_x,
        left_shin_x, right_shin_x,
        left_upper_arm_x, right_upper_arm_x,
        left_lower_arm_x, right_lower_arm_x,
        left_foot_x, right_foot_x,
        left_hand_x, right_hand_x
    ])
    
    y = np.array([
        head_y, torso_y, hip_y,
        left_thigh_y, right_thigh_y,
        left_shin_y, right_shin_y,
        left_upper_arm_y, right_upper_arm_y,
        left_lower_arm_y, right_lower_arm_y,
        left_foot_y, right_foot_y,
        left_hand_y, right_hand_y
    ])
    
    return x, y

# Update function for animation
def update(frame):
    x, y = get_key_positions(frame)
    points.set_offsets(np.column_stack([x, y]))
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=50, blit=True
)

plt.tight_layout()
plt.show()
