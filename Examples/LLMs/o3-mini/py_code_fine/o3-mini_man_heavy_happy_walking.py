
"""
This Python program creates an animation of 15 white point‐lights on a solid black background 
that together represent a “happyman with heavy weight” walking. The 15 points represent key joints 
of the body (head, shoulders, elbows, hands, torso, hips, knees, feet) plus one extra point for the 
heavy load. The walking motion is generated using smooth sinusoidal modulation for biomechanically‐plausible 
movement. The figure slowly moves from left to right while its limbs swing in opposing phase.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Animation parameters
fps = 30               # frames per second
duration = 8           # total duration in seconds
num_frames = duration * fps
period = 1.5           # gait cycle period in seconds
speed = 0.3            # horizontal walking speed

# Define base (local) coordinates for the 15 points.
# These coordinates approximate the human figure in an upright pose.
# Index mapping:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Hand
#  6: Right Hand
#  7: Mid Torso
#  8: Left Hip
#  9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Foot
# 13: Right Foot
# 14: Heavy weight (e.g., a point that indicates a carried mass)

def get_joint_positions(t):
    # Global horizontal translation simulating walking.
    dx = speed * t

    # Sinusoidal gait modulation over the cycle.
    cycle = 2 * np.pi * (t % period) / period
    
    # Head: Slight vertical bobbing.
    head = np.array([0, 1.50 + 0.05 * np.sin(cycle)])
    
    # Shoulders: small horizontal swing in opposite directions.
    left_shoulder = np.array([-0.20 + 0.02 * np.sin(cycle), 1.40])
    right_shoulder = np.array([0.20 - 0.02 * np.sin(cycle), 1.40])
    
    # Elbows: continue the arm swing.
    left_elbow = np.array([-0.40 + 0.03 * np.sin(cycle), 1.20])
    right_elbow = np.array([0.40 - 0.03 * np.sin(cycle), 1.20])
    
    # Hands: a bit more pronounced swing.
    left_hand = np.array([-0.50 + 0.04 * np.sin(cycle), 1.00])
    right_hand = np.array([0.50 - 0.04 * np.sin(cycle), 1.00])
    
    # Mid torso: slight vertical bobbing.
    torso = np.array([0, 1.00 + 0.03 * np.sin(cycle)])
    
    # Hips: small horizontal modulation.
    left_hip = np.array([-0.15 + 0.02 * np.sin(cycle), 0.80])
    right_hip = np.array([0.15 - 0.02 * np.sin(cycle), 0.80])
    
    # Legs: simulate a simple gait by lifting one leg while the other is down.
    # For realism with heavy weight, the knee and foot movements are less exaggerated.
    # Use absolute value of sine for the leg (positive phase indicates swing/lift).
    left_knee_lift = 0.10 * max(0, np.sin(cycle))
    right_knee_lift = 0.10 * max(0, np.sin(cycle + np.pi))
    
    left_foot_lift = 0.12 * max(0, np.sin(cycle))
    right_foot_lift = 0.12 * max(0, np.sin(cycle + np.pi))
    
    left_knee = np.array([-0.15, 0.50 + left_knee_lift])
    right_knee = np.array([0.15, 0.50 + right_knee_lift])
    
    left_foot = np.array([-0.15, 0.20 + left_foot_lift])
    right_foot = np.array([0.15, 0.20 + right_foot_lift])
    
    # Heavy weight point: represented as a point near the center-left of the torso.
    # It can simulate carrying a heavy object (or simply represent the heaviness of the man).
    # For added realism, let it have a slight lag relative to the torso motion.
    weight = np.array([-0.08, 0.70])
    
    # List of all joints in order.
    joints = [head, left_shoulder, right_shoulder,
              left_elbow, right_elbow,
              left_hand, right_hand,
              torso, left_hip, right_hip,
              left_knee, right_knee,
              left_foot, right_foot,
              weight]
              
    # Apply global translation (moving rightwards)
    joints = [joint + np.array([dx, 0]) for joint in joints]
    return np.array(joints)

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
scat = ax.scatter([], [], c='white', s=80)

# Setting fixed limits to see the motion across frames.
# You may adjust these limits depending on speed and duration.
ax.set_xlim(-1, speed * duration + 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    t = frame / fps
    joints = get_joint_positions(t)
    scat.set_offsets(joints)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init,
                              interval=1000 / fps, blit=True)

plt.show()