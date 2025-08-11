
"""
This program animates a biological motion “point‐light” display of a sad woman jumping up.
It uses 15 white points on a black background to indicate key joints of the body.
The figure’s “skeleton” is defined by 15 points representing:
  0: Head
  1: Left Shoulder
  2: Right Shoulder
  3: Left Elbow
  4: Right Elbow
  5: Left Hand
  6: Right Hand
  7: Spine
  8: Left Hip
  9: Right Hip
 10: Left Knee
 11: Right Knee
 12: Left Ankle
 13: Right Ankle
 14: Belly
During the jump the legs extend (in flight) and then quickly flex on landing;
similarly, the arms swing upward a bit in flight.
The animation uses simple physics (a parabolic vertical displacement)
with custom interpolation for limbs so that the motion is smooth and biomechanically plausible.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Helper function: linear interpolation between two 2D points.
def lerp(p0, p1, a):
    # p0, p1 are tuples or numpy arrays (x, y)
    return (1 - a) * np.array(p0) + a * np.array(p1)

# Animation parameters
total_animation_time = 2.0  # seconds
fps = 30
nframes = int(total_animation_time * fps)
dt = total_animation_time / nframes

# Define jump physics parameters.
# We simulate a jump using vertical displacement: y = v0*t - 0.5*g*t^2,
# with effective gravity chosen to slow the motion.
v0 = 1.4       # initial upward velocity (units/sec)
g_eff = 1.96   # effective gravitational acceleration (units/sec^2)
T_flight = 2 * v0 / g_eff  # total flight time (~1.43 sec)

# For t within flight, global vertical displacement.
def jump_displacement(t):
    if t <= T_flight:
        return v0 * t - 0.5 * g_eff * t**2
    else:
        return 0.0

# Leg bending factor: during the flight phase the legs extend, and on the ground (start & end) they are bent.
# We define a factor b that smoothly goes from 0 at take-off, to 1 at mid-flight, back to 0 at landing.
def leg_extension_factor(t):
    if t <= T_flight:
        t_norm = t / T_flight  # normalized time in [0,1]
        # Using cosine: at t=0: cos(pi*(-1)) = -1 -> b = 0; at t=0.5: cos(0)=1 -> b=1; at t=1: cos(pi)= -1 -> b=0.
        return 0.5 + 0.5 * np.cos(np.pi * (2 * t_norm - 1))
    else:
        return 0.0

# Arm swing factor: arms go upward in flight.
def arm_swing_factor(t):
    if t <= T_flight:
        t_norm = t / T_flight
        # Sine gives 0 at beginning and end with a maximum (1) at mid-flight.
        return np.sin(np.pi * t_norm)
    else:
        return 0.0

# Define the base (landing) positions of the 15 joints (in a 2D plane).
# For a sad posture, the shoulders and head are slightly drooped.
# Coordinates are chosen so that when y-displacement is 0 the figure is on the ground.
# Note: y axis is vertical, positive upward.
base_joints = {
    0: (0.0, 0.8),          # Head
    1: (-0.2, 0.6),         # Left Shoulder
    2: (0.2, 0.6),          # Right Shoulder
    3: (-0.4, 0.4),         # Left Elbow (landing)
    4: (0.4, 0.4),          # Right Elbow (landing)
    5: (-0.5, 0.2),         # Left Hand (landing)
    6: (0.5, 0.2),          # Right Hand (landing)
    7: (0.0, 0.4),          # Spine
    8: (-0.15, 0.2),        # Left Hip
    9: (0.15, 0.2),         # Right Hip
    10: (-0.15, 0.0),       # Left Knee (landing)
    11: (0.15, 0.0),        # Right Knee (landing)
    12: (-0.15, -0.3),      # Left Ankle (landing)
    13: (0.15, -0.3),       # Right Ankle (landing)
    14: (0.0, 0.35)         # Belly (mid-torso)
}

# Define the "flight" positions (when extended or swinging) for the limbs.
# Legs: when extended in flight, the knees and ankles drop a little more.
leg_flight = {
    'left_knee': (-0.15, -0.1),
    'right_knee': (0.15, -0.1),
    'left_ankle': (-0.15, -0.4),
    'right_ankle': (0.15, -0.4)
}

# Arms: when swung upward in flight.
arm_flight = {
    'left_elbow': (-0.45, 0.5),
    'right_elbow': (0.45, 0.5),
    'left_hand': (-0.55, 0.3),
    'right_hand': (0.55, 0.3)
}

# The shoulders remain fixed at their base positions.
# For convenience, list the joint indices that will be updated using interpolation:
# Left arm: joint 3 (elbow) and 5 (hand)
# Right arm: joint 4 (elbow) and 6 (hand)
# Left leg: joint 10 (knee) and 12 (ankle)
# Right leg: joint 11 (knee) and 13 (ankle)

# Set up the matplotlib figure.
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')  # hide axes

# Initialize the scatter plot for 15 points.
scat = ax.scatter([], [], s=100, c='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    t = frame * dt
    y_disp = jump_displacement(t)
    b = leg_extension_factor(t)   # For legs: 0 -> bent (landing), 1 -> extended (in flight)
    a = arm_swing_factor(t)       # For arms: 0 -> landing, 1 -> swung upward

    # Compute updated joint positions.
    joints = {}

    # Head (joint 0)
    joints[0] = np.array(base_joints[0]) + np.array([0, y_disp])
    
    # Left Shoulder (1) and Right Shoulder (2) (no interpolation; remain constant relative to body)
    joints[1] = np.array(base_joints[1]) + np.array([0, y_disp])
    joints[2] = np.array(base_joints[2]) + np.array([0, y_disp])
    
    # Left Elbow (3): interpolate between landing and flight positions with factor a.
    landing_left_elbow = np.array(base_joints[3])
    flight_left_elbow = np.array(arm_flight['left_elbow'])
    joints[3] = lerp(landing_left_elbow, flight_left_elbow, a) + np.array([0, y_disp])
    
    # Right Elbow (4)
    landing_right_elbow = np.array(base_joints[4])
    flight_right_elbow = np.array(arm_flight['right_elbow'])
    joints[4] = lerp(landing_right_elbow, flight_right_elbow, a) + np.array([0, y_disp])
    
    # Left Hand (5)
    landing_left_hand = np.array(base_joints[5])
    flight_left_hand = np.array(arm_flight['left_hand'])
    joints[5] = lerp(landing_left_hand, flight_left_hand, a) + np.array([0, y_disp])
    
    # Right Hand (6)
    landing_right_hand = np.array(base_joints[6])
    flight_right_hand = np.array(arm_flight['right_hand'])
    joints[6] = lerp(landing_right_hand, flight_right_hand, a) + np.array([0, y_disp])
    
    # Spine (7)
    joints[7] = np.array(base_joints[7]) + np.array([0, y_disp])
    
    # Left Hip (8) and Right Hip (9) remain the same (relative to body)
    joints[8] = np.array(base_joints[8]) + np.array([0, y_disp])
    joints[9] = np.array(base_joints[9]) + np.array([0, y_disp])
    
    # Left Knee (10): interpolate between landing and flight versions.
    landing_left_knee = np.array(base_joints[10])
    flight_left_knee = np.array(leg_flight['left_knee'])
    joints[10] = lerp(landing_left_knee, flight_left_knee, b) + np.array([0, y_disp])
    
    # Right Knee (11)
    landing_right_knee = np.array(base_joints[11])
    flight_right_knee = np.array(leg_flight['right_knee'])
    joints[11] = lerp(landing_right_knee, flight_right_knee, b) + np.array([0, y_disp])
    
    # Left Ankle (12)
    landing_left_ankle = np.array(base_joints[12])
    flight_left_ankle = np.array(leg_flight['left_ankle'])
    joints[12] = lerp(landing_left_ankle, flight_left_ankle, b) + np.array([0, y_disp])
    
    # Right Ankle (13)
    landing_right_ankle = np.array(base_joints[13])
    flight_right_ankle = np.array(leg_flight['right_ankle'])
    joints[13] = lerp(landing_right_ankle, flight_right_ankle, b) + np.array([0, y_disp])
    
    # Belly (14)
    joints[14] = np.array(base_joints[14]) + np.array([0, y_disp])
    
    # Create an array of shape (15,2) for scatter positions.
    pos = np.array([joints[i] for i in range(15)])
    scat.set_offsets(pos)
    return scat,

# Create the animation.
anim = FuncAnimation(fig, update, frames=nframes, init_func=init, interval=1000/fps, blit=True)

plt.show()