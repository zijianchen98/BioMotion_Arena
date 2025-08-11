import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This program creates a minimalistic 2D point-light display (15 points) of a
# "sad woman with heavy weight" walking. The figure is hunched and moves slowly
# to convey a sad, heavy gait. White points on a black background are used.

# Number of frames in one walking cycle
FRAMES = 200

def get_joint_positions(t):
    """
    Return an array of shape (15, 2) giving the (x, y) positions of
    15 point-lights for a single frame at time t in [0, 2*pi].
    
    Joint indices (15 total):
     0  - Head
     1  - Neck
     2  - Left Shoulder
     3  - Right Shoulder
     4  - Left Elbow
     5  - Right Elbow
     6  - Left Wrist
     7  - Right Wrist
     8  - Left Hip
     9  - Right Hip
     10 - Left Knee
     11 - Right Knee
     12 - Left Ankle
     13 - Right Ankle
     14 - Pelvis Center
    """
    # Base offsets and posture
    # Slight forward lean for a sad/heavy posture
    trunk_lean = np.deg2rad(10)  
    base_x = 0.0
    base_y = 1.0
    # Vertical bounce amplitude (small, slow bounce to indicate heaviness)
    bounce = 0.05 * np.sin(t * 0.5)
    
    # Sinusoidal swing for arms/legs: slow frequency to appear heavy
    swing_freq = 0.6
    arm_swing = 0.15 * np.sin(t * swing_freq)
    opp_arm_swing = 0.15 * np.sin(t * swing_freq + np.pi)
    leg_swing = 0.20 * np.sin(t * swing_freq)
    opp_leg_swing = 0.20 * np.sin(t * swing_freq + np.pi)
    
    # Forward progress (slow horizontal translation)
    progress = 0.05 * t
    
    # Helper to rotate a point around (0,0) by trunk_lean
    def rotate(px, py, angle=trunk_lean):
        rx = px * np.cos(angle) - py * np.sin(angle)
        ry = px * np.sin(angle) + py * np.cos(angle)
        return rx, ry
    
    # Define base positions (unshifted, unrotated), roughly measuring in meters
    # Pelvis center is the origin for this local coordinate system
    positions_local = np.array([
        [0.0,  0.8],   # 0  Head (above pelvis)
        [0.0,  0.6],   # 1  Neck
        [-0.2, 0.6],   # 2  Left Shoulder
        [ 0.2, 0.6],   # 3  Right Shoulder
        [-0.3, 0.4],   # 4  Left Elbow
        [ 0.3, 0.4],   # 5  Right Elbow
        [-0.35,0.2],   # 6  Left Wrist
        [ 0.35,0.2],   # 7  Right Wrist
        [-0.15,0.0],   # 8  Left Hip
        [ 0.15,0.0],   # 9  Right Hip
        [-0.15,-0.4],  # 10 Left Knee
        [ 0.15,-0.4],  # 11 Right Knee
        [-0.15,-0.8],  # 12 Left Ankle
        [ 0.15,-0.8],  # 13 Right Ankle
        [ 0.0,  0.0]   # 14 Pelvis Center
    ])
    
    # Apply simple swinging for arms: left side (2,4,6) vs right side (3,5,7)
    # In a heavy/sad walk, amplitude is not too large.
    # Adjust x-coords to simulate swing; keep y the same for simplicity.
    positions_local[2,0] += arm_swing   # left shoulder
    positions_local[4,0] += arm_swing   # left elbow
    positions_local[6,0] += arm_swing   # left wrist
    
    positions_local[3,0] += opp_arm_swing  # right shoulder
    positions_local[5,0] += opp_arm_swing  # right elbow
    positions_local[7,0] += opp_arm_swing  # right wrist
    
    # Apply swing for legs: left side (8,10,12) vs right side (9,11,13)
    positions_local[8,0] += leg_swing    # left hip
    positions_local[10,0] += leg_swing   # left knee
    positions_local[12,0] += leg_swing   # left ankle
    
    positions_local[9,0] += opp_leg_swing   # right hip
    positions_local[11,0] += opp_leg_swing  # right knee
    positions_local[13,0] += opp_leg_swing  # right ankle

    # Rotate entire skeleton around pelvis center to simulate forward lean
    # Then shift to base offset, add vertical bounce, and forward progress
    rotated_positions = []
    for i, (px, py) in enumerate(positions_local):
        # Shift local coords so pelvis is at origin for rotation
        px_shifted = px - positions_local[14,0]
        py_shifted = py - positions_local[14,1]
        rx, ry = rotate(px_shifted, py_shifted, trunk_lean)
        
        # Now move pelvis to global coords
        gx = base_x + progress + rx
        gy = base_y + bounce     + ry
        
        rotated_positions.append([gx, gy])
    
    return np.array(rotated_positions)

def animate(frame):
    """
    Update function for FuncAnimation.
    """
    t = 2.0 * np.pi * (frame / FRAMES)
    pts = get_joint_positions(t)
    scat.set_offsets(pts)
    return (scat,)

# Set up the plotting environment (black background, white dots).
fig = plt.figure(figsize=(5,5), facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')

# Create a scatter plot for 15 points.
pts_init = get_joint_positions(0)
scat = ax.scatter(pts_init[:,0], pts_init[:,1], c='white', s=30)

# Remove axes for a more realistic point-light display.
plt.axis('off')

# Fix the view limits so the figure remains in view.
ax.set_xlim(-1.5, 2.5)
ax.set_ylim(-1.5, 2.0)

# Create and start the animation
ani = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=50,
                              blit=True, repeat=True)

plt.show()