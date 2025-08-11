import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ----------------------------------------------------------------------------
# This program displays a point-light stimulus (15 points) of a "sad man"
# with light weight, performing a jumping motion against a black background.
# ----------------------------------------------------------------------------

# Base skeleton (x, y) coordinates for a sad/neutral standing pose (15 points).
# The figure is slightly hunched forward, arms drooped, etc.
base_skeleton = np.array([
    [0.0, 5.0],   # 0: Head
    [0.0, 4.5],   # 1: Neck
    [0.6, 4.0],   # 2: Right shoulder
    [0.8, 3.2],   # 3: Right elbow
    [0.8, 2.4],   # 4: Right wrist
    [-0.6, 4.0],  # 5: Left shoulder
    [-0.8, 3.2],  # 6: Left elbow
    [-0.8, 2.4],  # 7: Left wrist
    [0.0, 3.0],   # 8: Spine
    [0.4, 2.5],   # 9: Right hip
    [0.4, 1.5],   # 10: Right knee
    [0.4, 0.5],   # 11: Right ankle
    [-0.4, 2.5],  # 12: Left hip
    [-0.4, 1.5],  # 13: Left knee
    [-0.4, 0.5],  # 14: Left ankle
])

def lerp(a, b, x):
    """Linear interpolation from value a to b by fraction x."""
    return a + (b - a) * x

def piecewise_interpolate(t, segments):
    """
    Given t in [0,1] and a list of segments = [(t0, t1, start_val, end_val), ...],
    returns a linear interpolation of the value for the segment that contains t.
    """
    for (t0, t1, v0, v1) in segments:
        if t0 <= t <= t1:
            frac = (t - t0) / (t1 - t0) if (t1 - t0) > 0 else 0
            return lerp(v0, v1, frac)
    # If out of range (numerical edge), clamp to last segment's end_val
    return segments[-1][3]

def get_skeleton_positions(t):
    """
    Returns a 15x2 array of (x,y) coordinates for the skeleton at time fraction t in [0,1].
    The motion simulates a sad man jumping:
        1) 0   -> 0.2 : Crouch down
        2) 0.2 -> 0.5 : Accelerate upward to apex
        3) 0.5 -> 0.8 : Come down from apex
        4) 0.8 -> 1.0 : Return to standing
    """

    # Vertical offset for the entire body
    # Piecewise: (t0, t1, start_val, end_val)
    #   0.0 -> 0.2: from 0.0 down to -0.5
    #   0.2 -> 0.5: from -0.5 up to 2.0
    #   0.5 -> 0.8: from 2.0 down to -0.5
    #   0.8 -> 1.0: from -0.5 back to 0.0
    y_shift_segments = [
        (0.0, 0.2, 0.0, -0.5),
        (0.2, 0.5, -0.5, 2.0),
        (0.5, 0.8, 2.0, -0.5),
        (0.8, 1.0, -0.5, 0.0),
    ]
    y_offset = piecewise_interpolate(t, y_shift_segments)

    # A simple "knee bend" angle factor for realism.
    # We'll just shift knees/ankles a bit in y to simulate bending and straightening.
    # 0.0 -> 0.2 : goes from 0 to 0.3 (crouch)
    # 0.2 -> 0.5 : goes back to 0 (fully extended in jump)
    # 0.5 -> 0.8 : goes to 0.3 again (landing crouch)
    # 0.8 -> 1.0 : goes back to 0 (stand)
    knee_segments = [
        (0.0, 0.2, 0.0, 0.3),
        (0.2, 0.5, 0.3, 0.0),
        (0.5, 0.8, 0.0, 0.3),
        (0.8, 1.0, 0.3, 0.0),
    ]
    knee_bend = piecewise_interpolate(t, knee_segments)

    # Copy the base skeleton so we can modify it
    skel = base_skeleton.copy()

    # Shift whole skeleton by y_offset
    skel[:, 1] += y_offset

    # Adjust right knee and ankle by "knee_bend"
    # Right knee is index 10, right ankle is index 11
    skel[10, 1] -= knee_bend  # bend knees downward
    skel[11, 1] -= knee_bend

    # Adjust left knee and ankle by "knee_bend"
    # Left knee is index 13, left ankle is index 14
    skel[13, 1] -= knee_bend
    skel[14, 1] -= knee_bend

    return skel

# Set up figure and animation
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# We'll animate over 60 frames for a single jump cycle
num_frames = 60

# Create scatter plot for 15 white points
scatter = ax.scatter([], [], color="white", s=20)

# Remove axes ticks and set a suitable view range
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(-1.0, 6.0)
ax.set_xticks([])
ax.set_yticks([])

def init():
    """Initialize the scatter plot."""
    scatter.set_offsets(np.zeros((15, 2)))
    return (scatter,)

def update(frame):
    """Update function for each animation frame."""
    t = frame / (num_frames - 1)
    positions = get_skeleton_positions(t)
    scatter.set_offsets(positions)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

plt.show()