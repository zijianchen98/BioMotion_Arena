
"""
This program displays a point‐light biological motion animation where a stick figure man waves his right hand.
The figure is represented by exactly 15 white “point‐lights” against a black background.
The animated right arm (right elbow and right wrist) is computed by a simple two‐segment inverse-kinematics
model so that the hand "waves" in a biomechanically plausible manner.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define fixed positions for the 15 markers.
# The markers are indexed as follows:
# 0: Head
# 1: Neck
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow (animated)
# 6: Left Wrist
# 7: Right Wrist (animated)
# 8: Torso (Chest)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# Fixed (static) coordinates for markers (x,y)
static_points = {
    0: np.array([0.0, 10.0]),      # Head
    1: np.array([0.0, 9.0]),       # Neck
    2: np.array([-1.0, 8.5]),      # Left Shoulder
    3: np.array([1.0, 8.5]),       # Right Shoulder (anchor for right arm)
    4: np.array([-1.5, 7.5]),      # Left Elbow
    # 5: Right Elbow (animated)
    6: np.array([-1.8, 7.0]),      # Left Wrist
    # 7: Right Wrist (animated)
    8: np.array([0.0, 8.0]),       # Torso (Chest)
    9: np.array([-0.5, 6.0]),      # Left Hip
    10: np.array([0.5, 6.0]),      # Right Hip
    11: np.array([-0.5, 4.0]),     # Left Knee
    12: np.array([0.5, 4.0]),      # Right Knee
    13: np.array([-0.5, 2.0]),     # Left Ankle
    14: np.array([0.5, 2.0])       # Right Ankle
}

# Arm segment lengths for the right arm (in arbitrary units)
L1 = 2.0  # upper arm length (shoulder to elbow)
L2 = 2.0  # lower arm length (elbow to wrist)

# Right shoulder fixed location from static_points index 3.
shoulder_R = static_points[3]

# Function to compute the inverse kinematics for the right arm.
def compute_right_arm(t):
    """
    Computes the positions of the right elbow and wrist at time t.
    The wrist follows a periodic oscillation (waving) and the elbow is computed
    to give a realistic two-segment arm configuration.
    """
    # Animation parameters:
    period = 2.0  # seconds; one full wave cycle every 2 seconds.
    omega = 2 * np.pi / period  # angular frequency
    
    # Define the target right wrist position W(t):
    # The idea: the wrist is held almost fully extended (distance ~ L1+L2 from shoulder)
    # with a small periodic oscillation in the horizontal direction.
    # Base offset from shoulder: mostly upward.
    base_dx = 0.0
    base_dy = L1 + L2  # almost fully extended upward from shoulder
    # Add a small oscillation (wave) horizontally and slight vertical modulation.
    osc_amp = 0.5  # amplitude of oscillation
    osc_x = osc_amp * np.sin(omega * t)      # horizontal oscillation
    osc_y = osc_amp * np.cos(omega * t)        # small vertical modulation

    # Target wrist position = shoulder + base offset + oscillation
    wrist_target = shoulder_R + np.array([base_dx + osc_x, base_dy + osc_y])
    
    # Compute the vector from shoulder to wrist target:
    v = wrist_target - shoulder_R
    d = np.linalg.norm(v)
    # Clamp d to avoid numerical issues (if d is very small, although not expected)
    if d < 1e-6:
        d = 1e-6
    v_norm = v / d
    
    # Use cosine law to compute the angle at shoulder for the first segment:
    # cos(theta) = (L1^2 + d^2 - L2^2) / (2*L1*d)
    cos_theta = (L1**2 + d**2 - L2**2) / (2 * L1 * d)
    # Clamp to valid range for arccos, in case of minor numerical issues.
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    
    # Determine a perpendicular direction to v_norm.
    # A perpendicular vector in 2D: (-v_y, v_x).
    perp = np.array([-v_norm[1], v_norm[0]])
    # Choose sign: we want the elbow to be in a plausible position.
    # For a hand raised upward, a natural elbow position is slightly downward relative to the line from shoulder to wrist.
    # We check the y-component; if positive, flip the perpendicular.
    if perp[1] > 0:
        perp = -perp

    # Compute elbow position along the two-segment solution:
    elbow = shoulder_R + L1 * (np.cos(theta) * v_norm + np.sin(theta) * perp)
    
    # Return the computed right elbow and wrist positions.
    return elbow, wrist_target

# Set up the matplotlib figure.
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("Point-Light Biological Motion: Hand Waving")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-3, 5)
ax.set_ylim(0, 13)

# Initialize 15 scatter points.
# We store the positions in a (15,2) array.
points = np.zeros((15, 2))

# Set initial positions for static markers.
for idx, pos in static_points.items():
    points[idx] = pos

# For right arm joints, initialize with current IK solution at t=0.
elbow_R, wrist_R = compute_right_arm(0)
points[5] = elbow_R  # index 5 is right elbow
points[7] = wrist_R  # index 7 is right wrist

# Create scatter plot for point-lights.
scat = ax.scatter(points[:, 0], points[:, 1], s=100, c="white")

# Optionally, remove axes ticks and labels.
ax.set_xticks([])
ax.set_yticks([])

# Animation update function.
def update(frame):
    # Convert frame number to time in seconds.
    # Adjust interval: here we assume 30 frames per second.
    t = frame / 30.0
    
    # Update right arm positions using IK.
    elbow_R, wrist_R = compute_right_arm(t)
    points[5] = elbow_R  # update right elbow
    points[7] = wrist_R  # update right wrist

    # (Optional) You could add subtle overall body motion here if desired.
    # For now, the rest of the markers remain static.
    
    # Update scatter plot data.
    scat.set_offsets(points)
    return scat,

# Create the animation.
anim = FuncAnimation(fig, update, frames=300, interval=33, blit=True)

plt.show()