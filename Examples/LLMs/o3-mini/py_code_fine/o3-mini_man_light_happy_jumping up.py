
"""
This program displays an animation of a “happy man” jumping up,
represented by 15 white point‐lights against a black background.
Each point represents a key body marker of the human figure.
The motion is biomechanically plausible, with a parabolic (projectile)
jump trajectory combined with small coordinated limb movements.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------
# Define the base (resting) positions for 15 markers.
# Coordinates are given relative to an internal body frame.
# (x, y) positions in meters.
# The “ground” is at y = 0. We assume the person stands roughly
# 0.8 m tall (head) and the base positions are relative to center-of-mass.
#
# Markers:
# 1. head
# 2. left_shoulder
# 3. right_shoulder
# 4. left_elbow
# 5. right_elbow
# 6. left_wrist
# 7. right_wrist
# 8. torso (chest)
# 9. left_hip
# 10. right_hip
# 11. left_knee
# 12. right_knee
# 13. left_ankle
# 14. right_ankle
# 15. belly (between torso and hips)
# -------------------------------

base_markers = [
    ("head",         0.00, 0.80),
    ("left_shoulder",-0.15, 0.75),
    ("right_shoulder", 0.15, 0.75),
    ("left_elbow",   -0.30, 0.65),
    ("right_elbow",   0.30, 0.65),
    ("left_wrist",   -0.35, 0.55),
    ("right_wrist",   0.35, 0.55),
    ("torso",         0.00, 0.40),
    ("left_hip",     -0.10, 0.30),
    ("right_hip",     0.10, 0.30),
    ("left_knee",    -0.10, 0.10),
    ("right_knee",    0.10, 0.10),
    ("left_ankle",   -0.10, 0.00),
    ("right_ankle",   0.10, 0.00),
    ("belly",         0.00, 0.35)
]

# -------------------------------
# Jump parameters for a realistic parabolic jump.
# We'll assume the man performs a jump with a desired (approximate)
# vertical takeoff velocity corresponding to a moderate jump.
# Using v0 = sqrt(2*g*h) where we set h = 0.5 m (jump height)
# g is gravitational acceleration (9.81 m/s^2).
# The total flight duration = 2*v0/g.
# -------------------------------
g = 9.81  # gravitational acceleration (m/s^2)
jump_height = 0.5  # desired max jump height (m)
v0 = np.sqrt(2 * g * jump_height)  # initial vertical velocity needed
T_flight = 2 * v0 / g  # total flight time (s)

# For continuous animation, we set the cycle period to T_flight.
cycle_period = T_flight

# -------------------------------
# Limb modulation functions
# We add small time-dependent modulation terms to simulate
# a coordinated, happy jump:
#  - Arms are raised more at the peak of the jump.
#  - The elbows and wrists add vertical and slight horizontal offsets.
#  - The knees extend (move upward) as the jump progresses.
# A phase parameter p (0 -> 1 -> 0) is defined such that:
#   p = 0: contact / crouch before take-off or after landing.
#   p = 1: jump apex.
# -------------------------------
def phase_parameter(t_mod):
    # t_mod is in [0, cycle_period]
    # p increases linearly from 0 at t=0 to 1 at mid-flight,
    # then decreases back to 0 at landing.
    if t_mod <= cycle_period/2:
        p = 2 * t_mod / cycle_period
    else:
        p = 2 * (cycle_period - t_mod) / cycle_period
    return p

# -------------------------------
# Function to compute positions of markers for time t (seconds).
# This function returns two arrays: xs and ys of length 15.
# -------------------------------
def compute_marker_positions(t):
    # t_mod is the time within the current jump cycle.
    t_mod = t % cycle_period
    p = phase_parameter(t_mod)
    
    # The center-of-mass vertical offset following the projectile trajectory.
    # y_cm = v0*t_mod - 0.5*g*t_mod**2.
    y_cm = v0 * t_mod - 0.5 * g * t_mod**2
    # Additional small horizontal translation due to body lean (simulate happy energy)
    x_cm = 0.02 * np.sin(2 * np.pi * t_mod / cycle_period)
    
    xs = []
    ys = []
    
    for name, base_x, base_y in base_markers:
        # Start with base relative coordinate.
        x = base_x
        y = base_y
        
        # Apply limb specific modulation:
        if name in ("left_elbow", "right_elbow"):
            # Slight upward raise as the jump peaks.
            y += 0.05 * p
        if name in ("left_wrist", "right_wrist"):
            # More pronounced raise in the wrists and a slight horizontal swing.
            y += 0.10 * p
            # For horizontal swing, add a small sine modulation.
            # left_wrist moves slightly left, right_wrist moves right.
            if name == "left_wrist":
                x -= 0.02 * np.sin(2 * np.pi * t_mod / cycle_period)
            else:
                x += 0.02 * np.sin(2 * np.pi * t_mod / cycle_period)
        if name in ("left_knee", "right_knee"):
            # Knees extend as jump proceeds.
            y += 0.10 * p
        # Optionally, you can add other modulations for more realism.
        
        # Now add the center-of-mass offset.
        x += x_cm
        y += y_cm
        
        xs.append(x)
        ys.append(y)
    
    return xs, ys

# -------------------------------
# Set up the matplotlib figure and axis.
# The background is black and the markers will be white.
# -------------------------------
fig, ax = plt.subplots(figsize=(5, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
scat = ax.scatter([], [], s=100, c="white")

# Set fixed axis limits so that the figure remains in view.
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 2.0)
ax.set_aspect("equal")
ax.axis("off")  # Hide axes

# -------------------------------
# Animation update function.
# -------------------------------
def update(frame):
    # frame is in milliseconds (or arbitrary time steps). 
    # We'll assume frame rate ~ 30 fps so t in seconds:
    t = frame / 30.0
    xs, ys = compute_marker_positions(t)
    scat.set_offsets(np.column_stack((xs, ys)))
    return scat,

# -------------------------------
# Create the animation using FuncAnimation.
# -------------------------------
anim = FuncAnimation(fig, update, frames=np.linspace(0, 300, 300), interval=33, blit=True)

# Uncomment the following line to save the animation as an mp4 (requires ffmpeg)
# anim.save('point_light_jump.mp4', writer='ffmpeg', fps=30)

plt.show()