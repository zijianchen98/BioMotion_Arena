
"""
This program creates an animation of a point‐light stimulus representing a “sadwoman” in a running motion.
It uses 15 white points on a solid black background to depict key joints of a human figure.
The joints (point lights) represent:
  0  Head
  1  Left Shoulder
  2  Right Shoulder
  3  Left Elbow
  4  Right Elbow
  5  Left Wrist
  6  Right Wrist
  7  Pelvis (center hip)
  8  Left Hip
  9  Right Hip
 10  Left Knee
 11  Right Knee
 12  Left Ankle
 13  Right Ankle
 14  Chest (mid-torso)
  
The animation uses biomechanically plausible sinusoidal motions for swinging arms and legs
as well as a slight vertical bobbing (and “sad” head droop) to simulate a realistic running cycle.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Global parameters for the animation
v = 1.0                # horizontal speed in m/s
T_cycle = 1.0          # running cycle period (seconds)
arm_amp = np.deg2rad(30)   # amplitude of arm swing (radians)
leg_amp = np.deg2rad(30)   # amplitude of leg swing (radians)
fps = 30               # frames per second
duration = 5           # total duration of animation in seconds

# Body segment lengths (in meters)
arm_upper = 0.35  # shoulder to elbow
arm_lower = 0.35  # elbow to wrist
thigh = 0.45      # hip to knee
shank = 0.45      # knee to ankle

def get_pose(t):
    """
    Given time t in seconds, returns a (15,2) array of the (x,y) positions
    of the 15 points representing the joints.
    The overall body is translated horizontally at constant speed.
    A small vertical bob and head droop is added.
    """
    phase = 2 * np.pi * (t / T_cycle)
    bob = 0.03 * np.sin(2 * phase)   # vertical bobbing for body
    head_droop = 0.04 * (1 - np.cos(phase))  # head droop (more droop on impact)

    # Overall translation (running along x axis)
    trans = np.array([v * t, 0])
    
    # Base positions for the static (neutral) pose 
    # (all positions are relative; we add body translation and bob at the end)
    head_base      = np.array([0.0, 1.75])
    left_shoulder  = np.array([-0.15, 1.60])
    right_shoulder = np.array([0.15, 1.60])
    chest          = np.array([0.0, 1.55])    # extra joint (mid-torso)
    pelvis         = np.array([0.0, 1.20])
    left_hip       = np.array([-0.10, 1.20])
    right_hip      = np.array([0.10, 1.20])
    
    # Arm swing angles: arms swing in opposite phase
    left_arm_angle = arm_amp * np.sin(phase)
    right_arm_angle = arm_amp * np.sin(phase + np.pi)
    
    # Leg swing angles: legs swing in opposite phase (relative to pelvis)
    left_leg_angle = leg_amp * np.sin(phase + np.pi)
    right_leg_angle = leg_amp * np.sin(phase)
    
    # Calculate arm joints positions
    # For left arm: starting from left shoulder
    # The default is vertical down; swing rotates around shoulder.
    left_elbow = left_shoulder + np.array([arm_upper * np.sin(left_arm_angle),
                                            -arm_upper * np.cos(left_arm_angle)])
    left_wrist = left_elbow + np.array([arm_lower * np.sin(left_arm_angle),
                                         -arm_lower * np.cos(left_arm_angle)])
    
    # For right arm: starting from right shoulder
    right_elbow = right_shoulder + np.array([arm_upper * np.sin(right_arm_angle),
                                              -arm_upper * np.cos(right_arm_angle)])
    right_wrist = right_elbow + np.array([arm_lower * np.sin(right_arm_angle),
                                           -arm_lower * np.cos(right_arm_angle)])
    
    # Calculate leg joints positions:
    # For left leg: starting from left hip
    left_knee = left_hip + np.array([thigh * np.sin(left_leg_angle),
                                      -thigh * np.cos(left_leg_angle)])
    left_ankle = left_knee + np.array([shank * np.sin(left_leg_angle),
                                        -shank * np.cos(left_leg_angle)])
    
    # For right leg: starting from right hip
    right_knee = right_hip + np.array([thigh * np.sin(right_leg_angle),
                                        -thigh * np.cos(right_leg_angle)])
    right_ankle = right_knee + np.array([shank * np.sin(right_leg_angle),
                                         -shank * np.cos(right_leg_angle)])
    
    # Adjust head with bobbing and droop (subtly lower the head to reinforce “sad” mood)
    head = head_base + np.array([0, bob - head_droop])
    
    # Add bobbing to the shoulders, chest, pelvis and hips
    left_shoulder = left_shoulder + np.array([0, bob])
    right_shoulder = right_shoulder + np.array([0, bob])
    chest = chest + np.array([0, bob])
    pelvis = pelvis + np.array([0, bob])
    left_hip = left_hip + np.array([0, bob])
    right_hip = right_hip + np.array([0, bob])
    
    # Assemble the 15 points in the prescribed order
    pts = np.zeros((15, 2))
    pts[0, :] = head
    pts[1, :] = left_shoulder
    pts[2, :] = right_shoulder
    pts[3, :] = left_elbow
    pts[4, :] = right_elbow
    pts[5, :] = left_wrist
    pts[6, :] = right_wrist
    pts[7, :] = pelvis
    pts[8, :] = left_hip
    pts[9, :] = right_hip
    pts[10, :] = left_knee
    pts[11, :] = right_knee
    pts[12, :] = left_ankle
    pts[13, :] = right_ankle
    pts[14, :] = chest

    # Apply overall translation (running)
    pts += trans

    return pts

def animate():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.set_facecolor('black')
    plt.axis('off')
    
    # Set limits to view the motion comfortably.
    # Since the figure moves horizontally, we set xlim dynamically.
    x_margin = 1.0
    y_margin = 0.3
    ax.set_xlim(0, 5*v + 2)
    ax.set_ylim(0.8, 2.0)

    # Create scatter plot with 15 points.
    scatter = ax.scatter([], [], c='white', s=80)

    time_template = 'Time = %.2fs'
    time_text = ax.text(0.05, 0.92, '', transform=ax.transAxes, color='white')
    
    def init():
        scatter.set_offsets([])
        time_text.set_text('')
        return scatter, time_text
    
    def update(frame):
        t = frame / fps
        pts = get_pose(t)
        scatter.set_offsets(pts)
        time_text.set_text(time_template % t)
        return scatter, time_text

    frames = int(duration * fps)
    anim = FuncAnimation(fig, update, init_func=init, frames=frames, interval=1000/fps, blit=True)
    plt.show()

if __name__ == '__main__':
    animate()