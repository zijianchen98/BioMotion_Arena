import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of frames in the animation
NUM_FRAMES = 90
# Frames per second
FPS = 30

# Base (average) coordinates for 15 point-lights in a lying-down pose.
# Indices reference:
# 0 - Head
# 1 - Neck
# 2 - Left Shoulder
# 3 - Right Shoulder
# 4 - Left Elbow
# 5 - Right Elbow
# 6 - Left Wrist
# 7 - Right Wrist
# 8 - Pelvis
# 9 - Left Hip
# 10 - Right Hip
# 11 - Left Knee
# 12 - Right Knee
# 13 - Left Ankle
# 14 - Right Ankle
base_positions = np.array([
    [0.20,  0.14],  # Head
    [0.28,  0.10],  # Neck
    [0.33,  0.08],  # Left Shoulder
    [0.38,  0.08],  # Right Shoulder
    [0.30,  0.06],  # Left Elbow
    [0.41,  0.06],  # Right Elbow
    [0.27,  0.04],  # Left Wrist
    [0.44,  0.04],  # Right Wrist
    [0.50,  0.05],  # Pelvis
    [0.55,  0.04],  # Left Hip
    [0.60,  0.04],  # Right Hip
    [0.65,  0.03],  # Left Knee
    [0.70,  0.03],  # Right Knee
    [0.68,  0.01],  # Left Ankle
    [0.73,  0.01]   # Right Ankle
])

def get_positions(frame):
    """
    Returns the 2D coordinates of each of the 15 point-lights
    for the specified animation frame. We add slight sinusoidal 
    movement to simulate a slow, sad breathing motion.
    """
    t = frame / NUM_FRAMES
    # A simple sinusoidal parameter for subtle movement
    alpha = 2 * np.pi * t
    # Amplitude of small vertical motion
    amp = 0.02 * np.sin(alpha)
    
    # Copy the base positions so we don't modify the global array
    pts = base_positions.copy()
    
    # Simulate slight "breathing" or "sobbing" by shifting
    # neck, shoulders, elbows, wrists, and pelvis in y-direction
    idx_to_move = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in idx_to_move:
        pts[i, 1] += amp * (1.0 - 0.05 * i)  # diminishing offsets
    
    # Optionally, a bit of wave in the legs for slight fidgeting
    leg_amp = 0.01 * np.sin(2 * alpha)
    idx_legs = [9, 10, 11, 12, 13, 14]
    for i in idx_legs:
        pts[i, 1] += leg_amp * 0.5
    
    return pts

# Set up the figure
fig, ax = plt.subplots(figsize=(5, 4))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 0.2)
ax.axis('off')

# Scatter plot for the 15 points (white on black)
scat = ax.scatter([], [], c='white', s=30)

def init():
    scat.set_offsets([])
    return (scat,)

def update(frame):
    positions = get_positions(frame)
    scat.set_offsets(positions)
    return (scat,)

ani = FuncAnimation(
    fig, update, frames=NUM_FRAMES, init_func=init,
    interval=1000 / FPS, blit=True, repeat=True
)

plt.show()