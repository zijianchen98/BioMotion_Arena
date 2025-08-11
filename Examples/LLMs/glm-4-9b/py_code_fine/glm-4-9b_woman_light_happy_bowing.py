
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Constants
NUM_LIGHTS = 15
DURATION = 10  # seconds
FPS = 30
TOTAL_FRAMES = DURATION * FPS
BOWING_MIN_ANGLE = -30  # degrees
BOWING_MAX_ANGLE = -90  # degrees
BODY_PARTS = {
    'torso': (0, 0, 2, 1),  # (x, y, width, height)
    'head': (0, -2, 1, 1),
    'left_arm': (-1.5, 0, 1, 2),
    'right_arm': (1.5, 0, 1, 2),
    'left_leg': (-1, 2, 1, 3),
    'right_leg': (1, 2, 1, 3)
}
ARM_AND_LEG_LENGTH = 2

def generate_bowing_motion(frame_idx, total_frames):
    """Calculate the angle of the bowing motion for a given frame."""
    t = frame_idx / total_frames
    angle = np.interp(t, [0, 0.5, 1], [BOWING_MIN_ANGLE, (BOWING_MIN_ANGLE + BOWING_MAX_ANGLE) / 2, BOWING_MAX_ANGLE])
    return angle

def calculate_light_positions(body_parts, angle):
    """Calculate the positions of the light points based on the bowing angle."""
    angle_rad = np.deg2rad(angle)
    positions = []
    
    # Define some example positions for the lights
    light_distribution = [
        (-1.5, -1), (-1, -1), (-0.5, -1), (0, -1), (0.5, -1), (1, -1), (1.5, -1),
        (-1, 0), (-0.5, 0), (0, 0), (0.5, 0), (1, 0), (-1, 1), (-0.5, 1), (0.5, 1)
    ]
    
    for x, y in light_distribution:
        # Rotate the light positions based on the bowing angle
        x_rotated = x * np.cos(angle_rad) - y * np.sin(angle_rad)
        y_rotated = x * np.sin(angle_rad) + y * np.cos(angle_rad)
        positions.append((x_rotated, y_rotated))
    
    return positions

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-4, 2)
    ax.set_facecolor('black')
    ax.axis('off')
    return []

def update(frame):
    ax.clear()
    init()
    
    angle = generate_bowing_motion(frame, TOTAL_FRAMES)
    light_positions = calculate_light_positions(BODY_PARTS, angle)
    
    # Draw the lights
    for x, y in light_positions:
        ax.add_patch(patches.Circle((x, y), radius=0.08, color='white'))
    
    # Optional: Draw the outline of the person for better context
    angle_rad = np.deg2rad(angle)
    x_torso = 0
    y_torso = 0
    
    # Draw torso
    ax.add_patch(patches.Rectangle(
        (x_torso - BODY_PARTS['torso'][2] / 2, y_torso - BODY_PARTS['torso'][3] / 2),
        BODY_PARTS['torso'][2], BODY_PARTS['torso'][3],
        edgecolor='white', facecolor='none', linewidth=1
    ))
    
    # Draw arms
    for x_offset, y_offset, width, height in [BODY_PARTS['left_arm'], BODY_PARTS['right_arm']]:
        x_arm = x_offset * np.cos(angle_rad) - y_offset * np.sin(angle_rad)
        y_arm = x_offset * np.sin(angle_rad) + y_offset * np.cos(angle_rad)
        ax.add_patch(patches.Rectangle(
            (x_arm - width / 2, y_arm - height / 2),
            width, height,
            edgecolor='white', facecolor='none', linewidth=1
        ))
    
    # Draw legs
    for x_offset, y_offset, width, height in [BODY_PARTS['left_leg'], BODY_PARTS['right_leg']]:
        x_leg = x_offset * np.cos(angle_rad) - y_offset * np.sin(angle_rad)
        y_leg = x_offset * np.sin(angle_rad) + y_offset * np.cos(angle_rad)
        ax.add_patch(patches.Rectangle(
            (x_leg - width / 2, y_leg - height / 2),
            width, height,
            edgecolor='white', facecolor='none', linewidth=1
        ))
    
    # Draw head
    x_head = BODY_PARTS['head'][0] * np.cos(angle_rad) - BODY_PARTS['head'][1] * np.sin(angle_rad)
    y_head = BODY_PARTS['head'][0] * np.sin(angle_rad) + BODY_PARTS['head'][1] * np.cos(angle_rad)
    ax.add_patch(patches.Rectangle(
        (x_head - BODY_PARTS['head'][2] / 2, y_head - BODY_PARTS['head'][3] / 2),
        BODY_PARTS['head'][2], BODY_PARTS['head'][3],
        edgecolor='white', facecolor='none', linewidth=1
    ))
    
    return []

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, init_func=init, blit=True, interval=1000/FPS)
plt.show()
