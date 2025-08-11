
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import collections as mc

# Parameters for the animation
R = 0.8       # Radius of the body circle during roll
T_crouch = 1.0  # Crouching phase duration (seconds)
T_roll = 3.0    # Rolling phase duration
T_stand = 1.0   # Standing phase duration
T_total = T_crouch + T_roll + T_stand
fps = 30        # Frames per second
total_frames = int(T_total * fps)
w = 2*np.pi / T_roll  # Angular velocity for rolling

# Define 15 body joints with identifiers
joints = [
    "head", "neck", "shoulderR", "elbowR", "handR",
    "shoulderL", "elbowL", "handL", "chest", "hipC",
    "hipR", "kneeR", "footR", "hipL", "kneeL", "footL"
]

# Initial crouching positions (x, y)
key_crouch = np.array([
    [ 0.00, 1.20],  # head
    [ 0.00, 1.10],  # neck
    [-0.15, 1.00],  # shoulderR
    [-0.30, 0.90],  # elbowR
    [-0.40, 0.75],  # handR
    [ 0.15, 1.00],  # shoulderL
    [ 0.30, 0.90],  # elbowL
    [ 0.40, 0.75],  # handL
    [ 0.00, 0.95],  # chest
    [ 0.00, 0.75],  # hipC
    [-0.15, 0.70],  # hipR
    [-0.15, 0.40],  # kneeR
    [-0.15, 0.10],  # footR
    [ 0.15, 0.70],  # hipL
    [ 0.15, 0.40],  # kneeL
    [ 0.15, 0.10]   # footL
])

# Final standing positions
key_stand = np.array([
    [ 0.00, 1.70],  # head
    [ 0.00, 1.55],  # neck
    [-0.20, 1.40],  # shoulderR
    [-0.35, 1.20],  # elbowR
    [-0.45, 1.00],  # handR
    [ 0.20, 1.40],  # shoulderL
    [ 0.35, 1.20],  # elbowL
    [ 0.45, 1.00],  # handL
    [ 0.00, 1.25],  # chest
    [ 0.00, 0.95],  # hipC
    [-0.20, 0.90],  # hipR
    [-0.20, 0.50],  # kneeR
    [-0.20, 0.10],  # footR
    [ 0.20, 0.90],  # hipL
    [ 0.20, 0.50],  # kneeL
    [ 0.20, 0.10]   # footL
])

# Body angles for circular rolling motion
angles = np.array([
    np.pi/2,        # head
    1.8*np.pi/3,    # neck
    1.6*np.pi/3,    # shoulderR
    1.4*np.pi/3,    # elbowR
    np.pi/3,        # handR
    1.4*np.pi/3,    # shoulderL
    1.6*np.pi/3,    # elbowL
    2*np.pi/3,      # handL
    1.7*np.pi/3,    # chest
    np.pi,          # hipC
    4.5*np.pi/3,    # hipR
    5*np.pi/3,      # kneeR
    5.5*np.pi/3,    # footR
    1.5*np.pi/3,    # hipL
    np.pi/3,        # kneeL
    0.5*np.pi/3     # footL
])

# Set up the figure
plt.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(8, 5), facecolor='black')
ax = fig.add_subplot(111, xlim=(-1, 6), ylim=(-0.5, 2.0))
ax.set_axis_off()
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize point lights
points = ax.scatter([], [], s=50, c='white', edgecolors='none')

def get_positions(t):
    """Calculate joint positions at time t"""
    if t <= T_crouch:  # Crouch phase
        s = t / T_crouch
        return key_crouch * (1 - s) + key_crouch * s
        
    elif t <= T_crouch + T_roll:  # Rolling phase
        t_roll = t - T_crouch
        phase = w * t_roll
        center_x = R * phase  # Center moves horizontally
        return np.array([[
            center_x + R * np.cos(a - phase),
            R + R * np.sin(a - phase)
        ] for a in angles])
        
    else:  # Standing phase
        t_stand = t - T_crouch - T_roll
        s = t_stand / T_stand
        final_roll_pos = get_positions(T_crouch + T_roll)
        return final_roll_pos * (1 - s) + key_stand * s

def update(frame):
    """Update function for animation"""
    t = frame * T_total / total_frames
    positions = get_positions(t)
    points.set_offsets(positions)
    return points,

# Create and show the animation
ani = FuncAnimation(fig, update, frames=total_frames, 
                    interval=1000/fps, blit=True)
plt.tight_layout()
plt.show()
