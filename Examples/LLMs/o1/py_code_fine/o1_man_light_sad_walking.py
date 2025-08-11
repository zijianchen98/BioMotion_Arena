#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This program displays a point-light stimulus of a "sadman" with light weight walking.
There are exactly 15 white point-lights on a solid black background. The motion is
designed to appear plausibly biomechanical for a walking cycle. The figure displays
the animation in real-time.
"""

# Number of frames in one walking cycle
FRAMES_PER_CYCLE = 60
# Frames per second for the animation
FPS = 30
# Total number of cycles to show
NUM_CYCLES = 2
# Total frames in the animation
TOTAL_FRAMES = FRAMES_PER_CYCLE * NUM_CYCLES

# Number of point-lights
NUM_POINTS = 15

def get_joint_positions(frame_idx):
    """
    Given the current frame index, return an array of shape (NUM_POINTS, 2)
    containing x,y positions for each of the 15 point-lights representing
    the 'sadman' walker. 
    """

    # Normalize time parameter [0..1] across one gait cycle
    t_normalized = (frame_idx % FRAMES_PER_CYCLE) / FRAMES_PER_CYCLE
    # This will be our main phase angle that completes one cycle (2*pi)
    phase = 2.0 * np.pi * t_normalized

    # We'll define a forward progression along x plus a small vertical bounce.
    # The factor 0.05 in x controls step size per cycle; 
    # the factor 0.1 for y controls bounce amplitude.
    # The negative offset in y simulates a slight forward-lean "sad" posture.
    pelvis_x = 0.05 * frame_idx  
    pelvis_y = -0.1 + 0.1 * np.sin(2.0 * phase)

    # Let’s create a base array of zeros for the 15 joints
    joint_positions = np.zeros((NUM_POINTS, 2))

    # Indices of the points for reference:
    # 0: Head
    # 1: Neck
    # 2: Right Shoulder
    # 3: Right Elbow
    # 4: Right Wrist
    # 5: Left Shoulder
    # 6: Left Elbow
    # 7: Left Wrist
    # 8: Right Hip
    # 9: Right Knee
    # 10: Right Ankle
    # 11: Left Hip
    # 12: Left Knee
    # 13: Left Ankle
    # 14: Pelvis center

    # Pelvis center (base reference)
    joint_positions[14] = [pelvis_x, pelvis_y]

    # Hips: Slight lateral motion out of phase
    hip_offset = 0.1
    hip_lateral_amp = 0.02
    joint_positions[8] = [pelvis_x + hip_offset + hip_lateral_amp*np.sin(2*phase),  pelvis_y]       # Right Hip
    joint_positions[11] = [pelvis_x - hip_offset - hip_lateral_amp*np.sin(2*phase), pelvis_y]       # Left Hip

    # Knees: hinged under hips, amplitude for swinging
    knee_y_offset = -0.15
    knee_amp = 0.08
    # Right knee swings with +phase, left with -phase
    joint_positions[9]  = [joint_positions[8,0], joint_positions[8,1] + knee_y_offset +
                           knee_amp * np.sin(phase)]
    joint_positions[12] = [joint_positions[11,0], joint_positions[11,1] + knee_y_offset +
                           knee_amp * np.sin(phase + np.pi)]

    # Ankles: further down, also out of phase
    ankle_y_offset = -0.15
    ankle_amp = 0.06
    joint_positions[10] = [joint_positions[9,0], joint_positions[9,1] + ankle_y_offset +
                           ankle_amp * np.sin(phase)]
    joint_positions[13] = [joint_positions[12,0], joint_positions[12,1] + ankle_y_offset +
                           ankle_amp * np.sin(phase + np.pi)]

    # Shoulders: Slight slump forward. We place them above pelvis, with small wave.
    shoulder_y_offset = 0.2
    shoulder_forward_offset = 0.05  # to simulate "sad, drooping" posture
    shoulder_amp = 0.01
    joint_positions[2] = [pelvis_x + shoulder_forward_offset + 0.1 + 
                          shoulder_amp * np.sin(phase),
                          pelvis_y + shoulder_y_offset]
    joint_positions[5] = [pelvis_x + shoulder_forward_offset - 0.1 -
                          shoulder_amp * np.sin(phase),
                          pelvis_y + shoulder_y_offset]

    # Elbows: below shoulders, small amplitude swing out of phase with legs
    elbow_y_offset = -0.1
    elbow_amp = 0.03
    joint_positions[3] = [joint_positions[2,0], 
                          joint_positions[2,1] + elbow_y_offset - 
                          elbow_amp * np.sin(phase + np.pi/2)]
    joint_positions[6] = [joint_positions[5,0], 
                          joint_positions[5,1] + elbow_y_offset - 
                          elbow_amp * np.sin(phase - np.pi/2)]

    # Wrists: further down from elbows
    wrist_y_offset = -0.1
    wrist_amp = 0.02
    joint_positions[4] = [joint_positions[3,0],
                          joint_positions[3,1] + wrist_y_offset - 
                          wrist_amp * np.sin(phase + np.pi/2)]
    joint_positions[7] = [joint_positions[6,0],
                          joint_positions[6,1] + wrist_y_offset - 
                          wrist_amp * np.sin(phase - np.pi/2)]

    # Neck and Head: above shoulders, slightly forward
    neck_y_offset = 0.05
    head_y_offset = 0.07
    joint_positions[1] = [pelvis_x + shoulder_forward_offset,
                          pelvis_y + shoulder_y_offset + neck_y_offset]
    joint_positions[0] = [pelvis_x + shoulder_forward_offset,
                          pelvis_y + shoulder_y_offset + neck_y_offset + head_y_offset]

    return joint_positions

def init():
    """
    Initialize the scatter object for animation.
    """
    scat.set_offsets([])
    return (scat,)

def update(frame_idx):
    """
    Update function for animation. Moves the 15 white points to their new positions.
    """
    points = get_joint_positions(frame_idx)
    scat.set_offsets(points)
    return (scat,)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-1, 3)   # Adjust as needed for forward motion
ax.set_ylim(-1.5, 1) # Vertical limits
ax.set_aspect('equal', 'box')
ax.set_facecolor('black')
ax.axis('off')

# Create scatter plot (white points)
scat = ax.scatter([], [], c='white', s=50)

# Create animation
anim = FuncAnimation(
    fig, 
    update,
    frames=TOTAL_FRAMES,
    init_func=init,
    blit=True,
    interval=1000.0/FPS
)

if __name__ == "__main__":
    plt.show()