
"""
This program creates an animation of a point‐light “sadman” running,
using exactly 15 white point‐lights against a solid black background.
The 15 points correspond to:
  0: Head
  1: Neck
  2: Left Shoulder
  3: Right Shoulder
  4: Left Elbow
  5: Right Elbow
  6: Left Hand
  7: Right Hand
  8: Torso
  9: Left Hip
 10: Right Hip
 11: Left Knee
 12: Right Knee
 13: Left Foot
 14: Right Foot

The running motion is implemented with smooth sinusoidal oscillations for a biomechanically plausible movement.
While not a full biomechanical model, the motion mimics natural swings of the arms and legs plus a gentle body “bounce.”
Note that the “sadman” is portrayed only by the point‐lights and no additional facial information is available.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Global parameters for the animation
fps = 30
duration = 10  # seconds
frames = fps * duration

# Speed: horizontal displacement per second
speed = 0.5

def compute_positions(t):
    """
    Compute the positions (x,y) of the 15 point-lights at time t.
    The base (static) pose is defined for an upright figure.
    Running motion is simulated via sinusoidal modulations on the limbs and a subtle bounce.
    A common horizontal offset is added to simulate overall forward progression.
    """
    # Common horizontal displacement for running
    dx = speed * t

    # Body bounce (simulating vertical oscillation of the torso)
    bounce = 0.05 * np.sin(2 * np.pi * t)
    
    # The base positions (without running motion) for the joints:
    # Format: (base_x, base_y)
    base = {
        0: (0.0, 1.8),     # Head
        1: (0.0, 1.6),     # Neck
        2: (-0.2, 1.6),    # Left Shoulder
        3: (0.2, 1.6),     # Right Shoulder
        4: (-0.5, 1.4),    # Left Elbow
        5: (0.5, 1.4),     # Right Elbow
        6: (-0.7, 1.2),    # Left Hand
        7: (0.7, 1.2),     # Right Hand
        8: (0.0, 1.2),     # Torso (center)
        9: (-0.2, 1.0),    # Left Hip
        10: (0.2, 1.0),    # Right Hip
        11: (-0.2, 0.6),   # Left Knee
        12: (0.2, 0.6),    # Right Knee
        13: (-0.2, 0.2),   # Left Foot
        14: (0.2, 0.2)     # Right Foot
    }
    
    # Create a dictionary to hold modulated positions
    pos = {}
    
    # Head and Neck simply follow the bounce and horizontal translation.
    pos[0] = (base[0][0] + dx, base[0][1] + bounce)
    pos[1] = (base[1][0] + dx, base[1][1] + bounce)
    
    # Shoulders (attached to the neck and following bounce)
    pos[2] = (base[2][0] + dx, base[2][1] + bounce)
    pos[3] = (base[3][0] + dx, base[3][1] + bounce)
    
    # Arms: the upper and lower arms swing.
    # Left arm swings forward/backward with phase t; right arm swings oppositely.
    armSwing = 0.3 * np.sin(2 * np.pi * t)  # swing amplitude for elbows
    handSwing = 0.35 * np.sin(2 * np.pi * t)  # swing amplitude for hands
    extraArmLiftLeft = 0.1 * np.sin(4 * np.pi * t)
    extraArmLiftRight = 0.1 * np.sin(4 * np.pi * t + np.pi)
    
    pos[4] = (base[4][0] + armSwing + dx, base[4][1] + bounce)
    pos[5] = (base[5][0] - armSwing + dx, base[5][1] + bounce)
    
    pos[6] = (base[6][0] + handSwing + dx, base[6][1] + bounce + extraArmLiftLeft)
    pos[7] = (base[7][0] - handSwing + dx, base[7][1] + bounce + extraArmLiftRight)
    
    # Torso: follows bounce and translation.
    pos[8] = (base[8][0] + dx, base[8][1] + bounce)
    
    # Hips: follow torso
    pos[9] = (base[9][0] + dx, base[9][1] + bounce)
    pos[10] = (base[10][0] + dx, base[10][1] + bounce)
    
    # Legs: simulate running by swinging the legs.
    # Left leg swings with phase t; right leg swings in opposite phase.
    legSwingLeft = 0.3 * np.sin(2 * np.pi * t)
    legSwingRight = 0.3 * np.sin(2 * np.pi * t + np.pi)
    
    kneeLiftLeft = -0.1 * np.cos(2 * np.pi * t)
    kneeLiftRight = -0.1 * np.cos(2 * np.pi * t + np.pi)
    
    pos[11] = (base[11][0] + legSwingLeft + dx, base[11][1] + kneeLiftLeft)
    pos[12] = (base[12][0] + legSwingRight + dx, base[12][1] + kneeLiftRight)
    
    # For feet we simulate a short upward lift when the foot is advancing.
    # Use max(0, sin(...)) so that the lift occurs only when the leg is in a swinging phase.
    footLiftLeft = 0.1 * max(0, np.sin(2 * np.pi * t))
    footLiftRight = 0.1 * max(0, np.sin(2 * np.pi * t + np.pi))
    
    pos[13] = (base[13][0] + 0.35 * np.sin(2 * np.pi * t) + dx, base[13][1] + footLiftLeft)
    pos[14] = (base[14][0] + 0.35 * np.sin(2 * np.pi * t + np.pi) + dx, base[14][1] + footLiftRight)
    
    # Return the positions as two numpy arrays: xs and ys in order of indices 0 to 14.
    xs = []
    ys = []
    for i in range(15):
        x, y = pos[i]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

# Set up the matplotlib figure and axes.
fig, ax = plt.subplots(figsize=(8, 6))
fig.canvas.set_window_title("Point-Light Biological Motion: Running Sadman")
ax.set_facecolor('black')
plt.style.use('dark_background')
# Make sure the axis is off for a stimulus presentation.
ax.axis('off')

# Initial positions for scatter plot.
xs_init, ys_init = compute_positions(0)
scat = ax.scatter(xs_init, ys_init, c='white', s=80)

# Set axis limits so that the full motion is visible.
# We account for horizontal translation over the animation duration.
x_margin = 1.0
y_margin = 0.5
ax.set_xlim(-1 + 0, speed * duration + 1)
ax.set_ylim(0, 2.2)

def update(frame):
    # t in seconds
    t = frame / fps
    xs, ys = compute_positions(t)
    offsets = np.column_stack((xs, ys))
    scat.set_offsets(offsets)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()