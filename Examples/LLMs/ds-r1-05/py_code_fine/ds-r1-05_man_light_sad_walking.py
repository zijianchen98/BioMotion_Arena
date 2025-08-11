
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')  # Ensure TkAgg backend is used for display

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-8, 8)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')
ax.axis('off')

# Initial joint positions (in a standing pose)
initial_positions = [
    [0.0, 10.0],    # 0: head
    [-2.0, 8.0],     # 1: left shoulder
    [2.0, 8.0],      # 2: right shoulder
    [-2.0, 6.0],     # 3: left elbow
    [2.0, 6.0],      # 4: right elbow
    [-2.0, 4.0],     # 5: left wrist
    [2.0, 4.0],      # 6: right wrist
    [-1.5, 5.0],     # 7: left hip
    [1.5, 5.0],      # 8: right hip
    [-1.5, 3.0],     # 9: left knee
    [1.5, 3.0],      # 10: right knee
    [-1.5, 1.0],     # 11: left ankle
    [1.5, 1.0],      # 12: right ankle
    [-2.0, 0.0],     # 13: left foot (toe)
    [2.0, 0.0]       # 14: right foot (toe)
]

positions = np.array(initial_positions)
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white', edgecolors='none')

def update(frame):
    t = frame * 0.05  # Incremental time for smooth motion
    body_oscillation = 0.25 * np.sin(2 * np.pi * t)
    lateral_sway = 0.6 * np.sin(2 * np.pi * t)
    
    # Body movement: vertical oscillation applied to all points
    positions[:, 1] = [p[1] - 5.0 + 5.0 for p in initial_positions]  # Reset to initial Y
    positions[:, 1] += body_oscillation
    
    # Lateral sway for the hips and shoulders
    positions[[1, 2, 7, 8], 0] = [p[0] for p in initial_positions][1:9]  # Reset shoulders and hips X
    positions[[1, 7], 0] -= lateral_sway * 0.5
    positions[[2, 8], 0] += lateral_sway * 0.5
    
    # Limb motion: arms (elbows and wrists)
    arm_angle = 0.9 * np.sin(2 * np.pi * t)
    positions[3, 0] = positions[1, 0] - 0.5 * np.sin(arm_angle)
    positions[3, 1] = positions[1, 1] - 0.5 * np.cos(arm_angle)
    positions[5, 0] = positions[1, 0] - np.sin(arm_angle)
    positions[5, 1] = positions[1, 1] - np.cos(arm_angle)
    positions[4, 0] = positions[2, 0] + 0.5 * np.sin(arm_angle)
    positions[4, 1] = positions[2, 1] - 0.5 * np.cos(arm_angle)
    positions[6, 0] = positions[2, 0] + np.sin(arm_angle)
    positions[6, 1] = positions[2, 1] - np.cos(arm_angle)
    
    # Feet positions to simulate stepping
    positions[[13, 14], 1] += 0.5 * np.cos(4 * np.pi * t)
    positions[13, 0] = initial_positions[13][0] - 0.5 * np.sin(2 * np.pi * t)
    positions[14, 0] = initial_positions[14][0] + 0.5 * np.sin(2 * np.pi * t)
    
    # Leg motion: set knee positions based on hip and ankle positions
    positions[9] = (positions[7] + positions[11]) / 2
    positions[10] = (positions[8] + positions[12]) / 2
    
    scat.set_offsets(positions)
    return scat,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
