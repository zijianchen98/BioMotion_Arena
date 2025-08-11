
"""
This program shows a point‐light stimulus animation that represents a “happy heavy‐weight” woman running.
It uses exactly 15 white point‐lights (markers) on a solid black background. The 15 markers roughly
correspond to key joints/features of the body (head, shoulders, elbows, hands, hips, knees, ankles,
mid-torso and pelvis). Their motion is driven by a simple biomechanically plausible running cycle.
While the model is highly simplified, the cyclic swinging of the arms and legs produces a smooth,
life‐like run.
 
Run the script (e.g. “python3 point_light_run.py”) to see the animation.
 
Note: This is a minimal simulation; in a research context one might replace the kinematic model
with real human motion capture data.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the running simulation
v = 2.0                           # horizontal speed (units per second)
run_cycle = 1.0                   # period of one running cycle in seconds
arm_swing = 0.4                   # amplitude of arm swing displacement
leg_swing = 0.5                   # amplitude of leg swing displacement
bounce_amplitude = 0.05           # vertical bounce amplitude for the core

# Animation parameters
fps = 30                          # frames per second
total_time = 5                    # total simulation time in seconds
n_frames = int(total_time * fps)
dt = 1 / fps

# Set up the figure and axis
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# We will use a scatter plot to plot exactly 15 white dots
scatter = ax.scatter([], [], c='white', s=80)

# Set the axes limits large enough to show the motion as the figure runs
ax.set_xlim(-1, v * total_time + 2)
ax.set_ylim(-3, 4)
ax.set_aspect('equal')
ax.axis('off')


def get_marker_positions(t):
    """
    Compute the 15 marker positions for a given time t.
    The markers (joints) and their indices are:
      0: Head
      1: Left Shoulder
      2: Right Shoulder
      3: Left Elbow
      4: Right Elbow
      5: Left Hand
      6: Right Hand
      7: Left Hip
      8: Right Hip
      9: Left Knee
      10: Right Knee
      11: Left Ankle
      12: Right Ankle
      13: Mid-Torso (sternum)
      14: Pelvis (center)
    """
    # Phase variable for cyclic movement
    phase = 2 * np.pi * (t % run_cycle) / run_cycle

    # Horizontal displacement of the runner
    cx = v * t
    # A slight bounce in the vertical direction (small for heavy weight)
    cy = bounce_amplitude * np.sin(phase)
    
    # Base positions (relative to pelvis center at (cx, cy))
    head = np.array([cx, cy + 2.0])
    
    left_shoulder = np.array([cx - 0.5, cy + 1.8])
    right_shoulder = np.array([cx + 0.5, cy + 1.8])
    
    # Arms: elbows and hands swing in opposite phases for left and right
    left_elbow = np.array([cx - 0.8 + arm_swing * np.sin(phase), cy + 1.2])
    right_elbow = np.array([cx + 0.8 - arm_swing * np.sin(phase), cy + 1.2])
    
    left_hand = np.array([cx - 0.8 + arm_swing * np.sin(phase), cy + 0.6])
    right_hand = np.array([cx + 0.8 - arm_swing * np.sin(phase), cy + 0.6])
    
    # Hips
    left_hip = np.array([cx - 0.3, cy])
    right_hip = np.array([cx + 0.3, cy])
    
    # Legs: note that arms and legs swing in opposite phases (contralateral)
    # For biomechanical plausibility, when one arm swings forward, the opposite leg swings forward.
    # Here we simulate a horizontal swing and add a bit of vertical modulation based on cosine.
    left_knee = np.array([cx - 0.3 + leg_swing * np.sin(phase),
                           cy - 0.9 - 0.3 * leg_swing * np.abs(np.cos(phase))])
    right_knee = np.array([cx + 0.3 - leg_swing * np.sin(phase),
                            cy - 0.9 - 0.3 * leg_swing * np.abs(np.cos(phase))])
    
    left_ankle = np.array([cx - 0.3 + leg_swing * np.sin(phase),
                           cy - 1.8 - 0.5 * leg_swing * np.abs(np.cos(phase))])
    right_ankle = np.array([cx + 0.3 - leg_swing * np.sin(phase),
                            cy - 1.8 - 0.5 * leg_swing * np.abs(np.cos(phase))])
    
    # Mid-Torso (between head and pelvis)
    mid_torso = np.array([cx, cy + 1.0])
    
    # Pelvis center (redundant with cy but makes the marker count 15)
    pelvis = np.array([cx, cy])
    
    # Assemble the 15 markers in order:
    markers = np.array([
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_hand,
        right_hand,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        mid_torso,
        pelvis
    ])
    
    return markers


def init():
    scatter.set_offsets([])
    return scatter,


def update(frame):
    t = frame * dt
    points = get_marker_positions(t)
    scatter.set_offsets(points)
    return scatter,


# Create the animation
anim = animation.FuncAnimation(fig, update, frames=n_frames, init_func=init,
                               interval=1000/fps, blit=True)

plt.show()