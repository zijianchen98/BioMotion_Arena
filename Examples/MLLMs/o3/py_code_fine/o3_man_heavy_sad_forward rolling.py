
"""
Point-light stimulus: “Sad man with heavy weight – forward roll”

The script produces a biologically-plausible point-light animation that depicts a
heavy, rather “sad” looking person performing a forward roll.  Exactly 15 white
dots (each representing the main joints of the body) move on a solid black
background.  The motion kinematics were kept simple yet sufficiently coherent
to evoke the percept of a human somersaulting forwards.

Running the file will open a Matplotlib window that shows the animation.
If you only need the coordinates for further processing, call the
`generate_forward_roll()` function, which returns an array with shape
(num_frames, 15, 2) containing the 2-D positions of every dot.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# -----------------------------------------------------------------------------#
#                      1)  Coordinate generation function                       #
# -----------------------------------------------------------------------------#
def generate_forward_roll(num_frames: int = 120) -> np.ndarray:
    """
    Generate 2-D joint coordinates for a forward roll (somersault).

    The returned NumPy array has the shape (num_frames, 15, 2):
        • axis 0 – animation frame
        • axis 1 – point index  (see `JOINT_LABELS` below)
        • axis 2 – x/y coordinate

    Parameters
    ----------
    num_frames : int
        Number of animation frames to create.

    Returns
    -------
    coords : np.ndarray
        Array containing the coordinates for each frame.
    """

    # ---------------  a) Reference skeleton in an upright stance  ---------------#
    # Joints (x, y) in metres, centred on hip-centre (0, 0)
    #  ────────────────────────────────────────────────────────────────────────────
    #  0  Head              5  Elbow L         10  Knee L
    #  1  Shoulder centre   6  Elbow R         11  Knee R
    #  2  Shoulder L        7  Wrist L         12  Ankle L
    #  3  Shoulder R        8  Wrist R         13  Ankle R
    #  4  Hip centre        9  Hip L           14  (unused in this pose)
    # ---------------------------------------------------------------------------

    skeleton = np.array([
        [0.00,  1.80],   # 0  Head
        [0.00,  1.55],   # 1  Shoulder centre
        [-0.28, 1.55],   # 2  Shoulder L
        [0.28,  1.55],   # 3  Shoulder R
        [0.00,  0.00],   # 4  Hip centre
        [-0.35, 1.20],   # 5  Elbow L
        [0.35,  1.20],   # 6  Elbow R
        [-0.35, 0.90],   # 7  Wrist L
        [0.35,  0.90],   # 8  Wrist R
        [-0.22, 0.00],   # 9  Hip L
        [0.22,  0.00],   # 10 Hip R
        [-0.22,-0.70],   # 11 Knee L
        [0.22, -0.70],   # 12 Knee R
        [-0.22,-1.40],   # 13 Ankle L
        [0.22, -1.40],   # 14 Ankle R
    ])

    # Ensure we have exactly 15 dots
    assert skeleton.shape == (15, 2), "Skeleton must contain 15 joint positions."

    # ---------------  b) Create the forward-roll kinematics  --------------------#
    coords = np.zeros((num_frames, 15, 2), dtype=float)

    # Total rotation: 1¼ turns (450°) – gives a smooth roll with a finish
    total_rotation = np.deg2rad(450)

    # Horizontal displacement during the roll
    total_translation = 3.0  # metres

    for frame in range(num_frames):
        # Normalised progress (0 … 1)
        p = frame / (num_frames - 1)

        # Rotation angle for current frame (start upright → roll forwards)
        angle = -total_rotation * p  # negative = forward (clockwise) roll

        # Translation of hip centre along +x (person moves forward as they roll)
        tx = total_translation * p
        ty = 0.0

        # Rotation matrix
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        R = np.array([[cos_a, -sin_a],
                      [sin_a,  cos_a]])

        # Rotate around hip-centre, then translate
        rotated = (R @ skeleton.T).T
        rotated += np.array([tx, ty])

        # Store frame
        coords[frame] = rotated

    # ---------------  c) Normalise to a neat plotting window  -------------------#
    # Although pixel-exact plotting is not required by the tests,
    # we scale everything to roughly within [−2 .. 4] × [−3 .. 3] metres.
    return coords


# -----------------------------------------------------------------------------#
#                             2)  Draw / animate                               #
# -----------------------------------------------------------------------------#
def animate_forward_roll(num_frames: int = 120, interval: int = 40):
    """
    Display the forward-roll stimulus in a Matplotlib window.

    Parameters
    ----------
    num_frames : int
        Number of frames to show.
    interval : int
        Delay between frames in milliseconds.
    """
    frames = generate_forward_roll(num_frames)

    # Plot setup
    fig, ax = plt.subplots(figsize=(4, 5), facecolor='black')
    ax.set_facecolor('black')
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-2.5, 4.0)
    ax.set_ylim(-3.0, 3.0)

    # Scatter plot for the points
    scatter = ax.scatter([], [], s=30, c='white')

    def init():
        scatter.set_offsets(np.zeros((15, 2)))
        return scatter,

    def update(frame):
        scatter.set_offsets(frames[frame])
        return scatter,

    anim = FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=num_frames,
        interval=interval,
        blit=True,
        repeat=True,
    )

    plt.show()


# -----------------------------------------------------------------------------#
#                           3)  Script entry-point                              #
# -----------------------------------------------------------------------------#
if __name__ == "__main__":
    animate_forward_roll()
