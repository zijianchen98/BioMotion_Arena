
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation parameters
fps = 30
duration = 6             # total duration in seconds
frames = int(fps * duration)
wave_freq = 0.5          # waves per second (slow, heavy movement)
wave_amp = 0.5           # elbow swing amplitude in radians
breath_freq = 0.25       # slow trunk bobbing frequency
breath_amp = 0.02        # trunk bobbing amplitude

# Limb segment lengths
L_upper = 0.25   # length of upper arm
L_lower = 0.25   # length of forearm

def get_joint_positions(t):
    """
    Returns a (15,2) array of xy-coordinates for the 15 point-lights
    at time t (in seconds).
    Joint indexing:
      0 head top
      1 neck
      2 left shoulder
      3 right shoulder
      4 left elbow
      5 right elbow
      6 left wrist
      7 right wrist
      8 pelvis
      9 left hip
     10 right hip
     11 left knee
     12 right knee
     13 left ankle
     14 right ankle
    """
    # Trunk bobbing (simulating heavy breathing/sway)
    y_bob = breath_amp * np.sin(2 * np.pi * breath_freq * t)
    
    # Base (static) joint positions, plus trunk bob for head/neck/shoulders/hips
    J = np.zeros((15, 2))
    J[0]  = [ 0.00, 0.60 + y_bob]   # head top
    J[1]  = [ 0.00, 0.40 + y_bob]   # neck
    J[2]  = [-0.15, 0.35 + y_bob]   # left shoulder
    J[3]  = [ 0.15, 0.35 + y_bob]   # right shoulder
    J[8]  = [ 0.00, 0.00        ]   # pelvis
    J[9]  = [-0.10, 0.00 + y_bob]   # left hip (slightly move with trunk)
    J[10] = [ 0.10, 0.00 + y_bob]   # right hip
    
    # Legs static
    J[11] = [-0.10, -0.40]  # left knee
    J[12] = [ 0.10, -0.40]  # right knee
    J[13] = [-0.10, -0.80]  # left ankle
    J[14] = [ 0.10, -0.80]  # right ankle
    
    # Left arm static (arm hanging down)
    J[4] = [-0.35,  0.10 + y_bob]   # left elbow
    J[6] = [-0.45, -0.20 + y_bob]   # left wrist
    
    # Right arm: waving
    shoulder = J[3]
    # Upper arm fixed out to the side (horizontal)
    theta_sh = 0.0  # radians (0 = horizontally to the right)
    elbow_pos = shoulder + L_upper * np.array([np.cos(theta_sh), np.sin(theta_sh)])
    
    # Elbow swing for waving motion
    delta = wave_amp * np.sin(2 * np.pi * wave_freq * t)
    lower_ang = theta_sh + delta
    wrist_pos = elbow_pos + L_lower * np.array([np.cos(lower_ang), np.sin(lower_ang)])
    
    J[5] = elbow_pos
    J[7] = wrist_pos
    
    return J

# Set up the figure and scatter plot
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_aspect('equal', 'box')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

points = ax.scatter([], [], c='white', s=100)

def init():
    points.set_offsets(np.zeros((15,2)))
    return (points,)

def update(frame):
    t = frame / fps
    J = get_joint_positions(t)
    points.set_offsets(J)
    return (points,)

anim = FuncAnimation(
    fig, update, frames=frames, init_func=init,
    interval=1000/fps, blit=True
)

plt.show()
