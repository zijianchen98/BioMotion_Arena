
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define segment lengths (approximate proportions)
L_upper = 1.0   # Upper arm length
L_forearm = 1.0 # Forearm length
L_thigh = 1.5   # Thigh length
L_shank = 1.5   # Shank length

# Base positions for a lying-down figure (oriented vertically for visibility)
base_positions = {
    'torso_center': (0, 5),
    'neck': (0, 6),
    'head': (0, 7),
    'left_shoulder': (-0.5, 6.5),
    'right_shoulder': (0.5, 6.5),
    'left_hip': (-0.3, 4.5),
    'right_hip': (0.3, 4.5),
}

# Calculate joint angles and positions at each time step
def get_angles(t):
    # Breathing motion (period = 4 seconds)
    breathing = 0.2 * np.sin(2 * np.pi * t / 4)
    
    # Left arm angles (degrees converted to radians)
    theta_arm_left = 10 * np.pi / 180 + 5 * np.pi / 180 * np.sin(2 * np.pi * t / 5)
    theta_elbow_left = 20 * np.pi / 180 + 5 * np.pi / 180 * np.sin(2 * np.pi * t / 5)
    
    # Right arm angles (mirrored, with phase offset)
    theta_arm_right = -10 * np.pi / 180 + 5 * np.pi / 180 * np.sin(2 * np.pi * t / 5 + np.pi)
    theta_elbow_right = -20 * np.pi / 180 + 5 * np.pi / 180 * np.sin(2 * np.pi * t / 5 + np.pi)
    
    # Leg angles (small movements)
    theta_hip_left = 3 * np.pi / 180 * np.sin(2 * np.pi * t / 6)
    theta_knee_left = 3 * np.pi / 180 * np.sin(2 * np.pi * t / 6)
    theta_hip_right = 3 * np.pi / 180 * np.sin(2 * np.pi * t / 6 + np.pi)
    theta_knee_right = 3 * np.pi / 180 * np.sin(2 * np.pi * t / 6 + np.pi)
    
    return (breathing, theta_arm_left, theta_elbow_left, theta_arm_right, 
            theta_elbow_right, theta_hip_left, theta_knee_left, theta_hip_right, theta_knee_right)

# Compute positions of all 15 points based on time t
def calculate_positions(t):
    breathing, theta_arm_left, theta_elbow_left, theta_arm_right, theta_elbow_right, \
    theta_hip_left, theta_knee_left, theta_hip_right, theta_knee_right = get_angles(t)
    
    positions = {}
    
    # Core body points with breathing motion
    positions['torso_center'] = (0, 5 + breathing)
    positions['neck'] = (0, 6 + breathing)
    positions['head'] = (0 + 0.1 * np.sin(2 * np.pi * t / 3), 7 + breathing)  # Slight head tilt
    positions['left_shoulder'] = (-0.5, 6.5 + breathing)
    positions['right_shoulder'] = (0.5, 6.5 + breathing)
    positions['left_hip'] = (-0.3, 4.5 + breathing / 2)
    positions['right_hip'] = (0.3, 4.5 + breathing / 2)
    
    # Left arm
    x_ls, y_ls = positions['left_shoulder']
    positions['left_elbow'] = (x_ls - L_upper * np.sin(theta_arm_left), 
                               y_ls - L_upper * np.cos(theta_arm_left))
    x_le, y_le = positions['left_elbow']
    positions['left_wrist'] = (x_le - L_forearm * np.sin(theta_elbow_left), 
                               y_le - L_forearm * np.cos(theta_elbow_left))
    
    # Right arm
    x_rs, y_rs = positions['right_shoulder']
    positions['right_elbow'] = (x_rs + L_upper * np.sin(theta_arm_right), 
                                y_rs - L_upper * np.cos(theta_arm_right))
    x_re, y_re = positions['right_elbow']
    positions['right_wrist'] = (x_re + L_forearm * np.sin(theta_elbow_right), 
                                y_re - L_forearm * np.cos(theta_elbow_right))
    
    # Left leg
    x_lh, y_lh = positions['left_hip']
    positions['left_knee'] = (x_lh - L_thigh * np.sin(theta_hip_left), 
                              y_lh - L_thigh * np.cos(theta_hip_left))
    x_lk, y_lk = positions['left_knee']
    positions['left_ankle'] = (x_lk - L_shank * np.sin(theta_knee_left), 
                               y_lk - L_shank * np.cos(theta_knee_left))
    
    # Right leg
    x_rh, y_rh = positions['right_hip']
    positions['right_knee'] = (x_rh + L_thigh * np.sin(theta_hip_right), 
                               y_rh - L_thigh * np.cos(theta_hip_right))
    x_rk, y_rk = positions['right_knee']
    positions['right_ankle'] = (x_rk + L_shank * np.sin(theta_knee_right), 
                                y_rk - L_shank * np.cos(theta_knee_right))
    
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
points = ax.scatter([], [], color='white', s=50)  # White points

# Update function for animation
def update(t):
    positions = calculate_positions(t)
    x = [positions[key][0] for key in positions]
    y = [positions[key][1] for key in positions]
    points.set_offsets(np.c_[x, y])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 200), interval=50, blit=True)

plt.axis('off')  # Hide axes for cleaner look
plt.show()
