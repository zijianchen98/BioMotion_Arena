
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
rcParams['lines.linewidth'] = 2

# Number of points
num_points = 15

# Initialize the point lights
points, = ax.plot([], [], 'wo', markersize=8)

# Function to generate the trajectory of a waving hand with a sad, heavy motion
def generate_trajectory(num_frames=100):
    t = np.linspace(0, 2 * np.pi, num_frames)
    
    # Body points (torso, head, legs - relatively fixed)
    body_x = np.zeros(num_frames)
    body_y = np.zeros(num_frames)
    
    head_x = body_x
    head_y = body_y + 0.8
    
    # Shoulders
    left_shoulder_x = body_x - 0.3
    left_shoulder_y = body_y + 0.5
    right_shoulder_x = body_x + 0.3
    right_shoulder_y = body_y + 0.5
    
    # Arms (right arm is waving)
    right_upper_arm_x = right_shoulder_x + 0.1 * np.sin(t * 2)  # slight movement
    right_upper_arm_y = right_shoulder_y - 0.2 * np.cos(t * 2)
    
    # Waving motion for the forearm (exaggerated for sad, heavy motion)
    right_forearm_x = right_upper_arm_x + 0.3 * np.sin(0.5 * t + np.pi/4)
    right_forearm_y = right_upper_arm_y - 0.3 * (1 + 0.3 * np.sin(t)) * np.cos(0.5 * t + np.pi/4)
    
    right_hand_x = right_forearm_x + 0.2 * np.sin(0.5 * t + np.pi/2)
    right_hand_y = right_forearm_y - 0.2 * (1 + 0.2 * np.sin(t)) * np.cos(0.5 * t + np.pi/2)
    
    # Left arm (hanging down, minimal movement)
    left_upper_arm_x = left_shoulder_x - 0.1
    left_upper_arm_y = left_shoulder_y - 0.2
    
    left_forearm_x = left_upper_arm_x - 0.2
    left_forearm_y = left_upper_arm_y - 0.2
    
    left_hand_x = left_forearm_x - 0.1
    left_hand_y = left_forearm_y - 0.1
    
    # Hips
    left_hip_x = body_x - 0.2
    left_hip_y = body_y - 0.2
    right_hip_x = body_x + 0.2
    right_hip_y = body_y - 0.2
    
    # Legs (slightly bent, heavy motion)
    left_thigh_x = left_hip_x
    left_thigh_y = left_hip_y - 0.4 - 0.05 * np.sin(t)
    
    left_shin_x = left_thigh_x
    left_shin_y = left_thigh_y - 0.4 - 0.05 * np.sin(t + np.pi/4)
    
    left_foot_x = left_shin_x - 0.1
    left_foot_y = left_shin_y - 0.1
    
    right_thigh_x = right_hip_x
    right_thigh_y = right_hip_y - 0.4 - 0.05 * np.sin(t + np.pi/2)
    
    right_shin_x = right_thigh_x
    right_shin_y = right_thigh_y - 0.4 - 0.05 * np.sin(t + 3*np.pi/4)
    
    right_foot_x = right_shin_x + 0.1
    right_foot_y = right_shin_y - 0.1
    
    # Combine all points
    x = np.vstack([
        body_x, head_x,
        left_shoulder_x, right_shoulder_x,
        left_upper_arm_x, right_upper_arm_x,
        left_forearm_x, right_forearm_x,
        left_hand_x, right_hand_x,
        left_hip_x, right_hip_x,
        left_thigh_x, right_thigh_x,
        left_shin_x, right_shin_x,
        left_foot_x, right_foot_x
    ])
    
    y = np.vstack([
        body_y, head_y,
        left_shoulder_y, right_shoulder_y,
        left_upper_arm_y, right_upper_arm_y,
        left_forearm_y, right_forearm_y,
        left_hand_y, right_hand_y,
        left_hip_y, right_hip_y,
        left_thigh_y, right_thigh_y,
        left_shin_y, right_shin_y,
        left_foot_y, right_foot_y
    ])
    
    # Select 15 points (some points are combined or omitted for simplicity)
    selected_indices = [0, 1, 2, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    x_selected = x[selected_indices, :]
    y_selected = y[selected_indices, :]
    
    return x_selected, y_selected

# Generate the trajectory
x, y = generate_trajectory(100)

# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.title('Biological Motion: Sad Man Waving Hand', color='white')
plt.show()
