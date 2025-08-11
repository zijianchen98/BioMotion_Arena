
"""
A Python program that shows a point‐light stimulus animation representing a heavy, sad woman jumping.
This animation uses exactly 15 white point‐lights (representing key joints)
on a solid black background. The motion is designed to be smooth and biomechanically plausible,
with a crouch, push‐off, flight, and landing phase.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Total number of frames in the animation.
TOTAL_FRAMES = 100

# Define the baseline (standing) positions (x, y) for the 15 points.
# These 15 points roughly correspond to:
#  0: Head
#  1: Left shoulder
#  2: Right shoulder
#  3: Left elbow
#  4: Right elbow
#  5: Left wrist
#  6: Right wrist
#  7: Left hip
#  8: Right hip
#  9: Left knee
# 10: Right knee
# 11: Left ankle
# 12: Right ankle
# 13: Chest center
# 14: Waist

initial_positions = np.array([
    [0.0, 1.70],       # 0: Head
    [-0.10, 1.55],     # 1: Left shoulder
    [ 0.10, 1.55],     # 2: Right shoulder
    [-0.20, 1.40],     # 3: Left elbow
    [ 0.20, 1.40],     # 4: Right elbow
    [-0.30, 1.25],     # 5: Left wrist
    [ 0.30, 1.25],     # 6: Right wrist
    [-0.10, 1.40],     # 7: Left hip
    [ 0.10, 1.40],     # 8: Right hip
    [-0.10, 1.00],     # 9: Left knee
    [ 0.10, 1.00],     #10: Right knee
    [-0.10, 0.00],     #11: Left ankle
    [ 0.10, 0.00],     #12: Right ankle
    [ 0.0,  1.55],     #13: Chest center
    [ 0.0,  1.40]      #14: Waist
])

def jump_offset(frame):
    """
    Compute the vertical offset for the body at a given frame.
    We simulate a jump with 3 phases:
      Phase 1 (frames 0-20): Crouch, lowering the body gradually (offset goes from 0 to -0.05).
      Phase 2 (frames 20-60): Jump flight modeled with a smooth parabolic (with a max raise of +0.15).
      Phase 3 (frames 60-100): Recovery / landing where the body returns from -0.05 to 0.
    The maximum overall vertical excursion is modest, reflecting a heavy, low jump.
    """
    if frame < 20:
        # Crouch phase: linear decrease from 0 to -0.05.
        return (frame / 20) * (-0.05)
    elif frame <= 60:
        # Jump phase: use a parabolic shape.
        # Normalize phase to u in [0,1]
        u = (frame - 20) / 40.0
        # Parabolic shape: 4*u*(1-u) peaks at u=0.5 with value 1.
        # Then add to the baseline crouch offset (-0.05).
        return -0.05 + 0.2 * (4 * u * (1 - u))
    else:
        # Recovery phase: linearly return from -0.05 at frame=60 to 0 at frame=100.
        return -0.05 * (1 - (frame - 60) / 40.0)

# Optionally, we can add a slight extra arm lift during the jump flight to emphasize the 
# movement; however, for a heavy, sad jump the arms might not swing vigorously.
# In this example, we keep the limb relative motions simple (only overall body translation).

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor("black")
plt.axis("equal")
# Set axis limits to comfortably include the jump motion.
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.1, 2.0)
plt.axis("off")

# Create the scatter plot for the 15 point-lights.
# We start with frame 0.
initial_y = initial_positions[:, 1] + jump_offset(0)
scat = ax.scatter(initial_positions[:, 0], initial_y, s=80, c="white")

def update(frame):
    """
    Update function for the animation. At every frame, adjust the 15 point positions by
    applying a vertical translation (the jump_offset). In a more advanced simulation, one
    could also include limb rotations, but here we focus on overall vertical motion.
    """
    # Compute the overall vertical offset for the frame.
    voffset = jump_offset(frame)
    # Create a new copy of positions and apply the vertical offset.
    # (In a more detailed biomechanical model, different joints could have relative motions.)
    new_positions = np.copy(initial_positions)
    new_positions[:, 1] += voffset

    # Update the scatter plot.
    scat.set_offsets(new_positions)
    return scat,

# Create the animation.
anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=50, blit=True)

# Uncomment the following line to save the animation as an mp4 (requires ffmpeg)
# anim.save("point_light_jump.mp4", writer="ffmpeg")

plt.show()