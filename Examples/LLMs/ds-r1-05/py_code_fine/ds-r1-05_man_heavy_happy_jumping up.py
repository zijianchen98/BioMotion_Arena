
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuration parameters
num_points = 15
amplitude = 0.8
period = 2.0
fps = 30
interval = 50

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.axis('off')

# Initialize scatter plot with 15 white points
scat = ax.scatter([], [], c='white', s=50, edgecolors='none')

def init():
    scat.set_offsets(np.zeros((num_points, 2)))
    return scat,

def update(frame):
    t = frame / fps  # Current time in seconds
    
    # Calculate vertical position for body core
    core_y = amplitude * np.sin(2 * np.pi * t / period)
    positions = np.zeros((num_points, 2))
    
    # Head (0)
    positions[0] = [0, core_y + 0.7]
    
    # Shoulders (1, 2)
    positions[1] = [-0.5, core_y + 0.5]
    positions[2] = [0.5, core_y + 0.5]
    
    # Arms (3-6)
    arm_phase = np.sin(2 * np.pi * t / period - np.pi/2)
    # Left arm
    positions[3] = [positions[1][0] + 0.4*np.cos(arm_phase), 
                    positions[1][1] + 0.4*np.sin(arm_phase)]
    positions[5] = [positions[3][0] + 0.3*np.cos(arm_phase - np.pi/4),
                    positions[3][1] + 0.3*np.sin(arm_phase - np.pi/4)]
    # Right arm
    positions[4] = [positions[2][0] + 0.4*np.cos(-arm_phase),
                    positions[2][1] + 0.4*np.sin(-arm_phase)]
    positions[6] = [positions[4][0] + 0.3*np.cos(-arm_phase + np.pi/4),
                    positions[4][1] + 0.3*np.sin(-arm_phase + np.pi/4)]
    
    # Hips (7, 8)
    positions[7] = [-0.3, core_y]
    positions[8] = [0.3, core_y]
    
    # Legs (9-14)
    leg_phase = np.sin(2 * np.pi * t / period + np.pi/2)
    # Left leg
    positions[9] = [positions[7][0] + 0.4*np.cos(leg_phase),
                    positions[7][1] - 0.4*np.sin(leg_phase)]
    positions[11] = [positions[9][0] + 0.4*np.cos(leg_phase - np.pi/4),
                     positions[9][1] - 0.4*np.sin(leg_phase - np.pi/4)]
    positions[13] = [positions[11][0] + 0.2*np.cos(leg_phase - np.pi/3),
                     positions[11][1] - 0.2*np.sin(leg_phase - np.pi/3)]
    # Right leg
    positions[10] = [positions[8][0] + 0.4*np.cos(-leg_phase),
                     positions[8][1] - 0.4*np.sin(-leg_phase)]
    positions[12] = [positions[10][0] + 0.4*np.cos(-leg_phase + np.pi/4),
                     positions[10][1] - 0.4*np.sin(-leg_phase + np.pi/4)]
    positions[14] = [positions[12][0] + 0.2*np.cos(-leg_phase + np.pi/3),
                     positions[12][1] - 0.2*np.sin(-leg_phase + np.pi/3)]
    
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, init_func=init, frames=fps*period,
                    interval=interval, blit=True)

plt.show()
