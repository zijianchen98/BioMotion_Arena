
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def build_skeleton():
    """
    Returns a (15, 3) numpy array with the 3-D coordinates of a thin / “sad” figure.
    Coordinates are in an arbitrary unit space with:
        y – vertical (up),
        x – horizontal (right),
        z – depth (toward the observer is +z).
    """
    #                    x,     y,     z
    joints = np.array([
        [0.00, 1.00,  0.05],   # 0 – head      (slightly forward – sad posture)
        [0.00, 0.80,  0.00],   # 1 – neck
        [-0.20, 0.80, 0.10],   # 2 – R shoulder
        [ 0.20, 0.80,-0.10],   # 3 – L shoulder
        [-0.30, 0.60, 0.10],   # 4 – R elbow
        [ 0.30, 0.60,-0.10],   # 5 – L elbow
        [-0.35, 0.40, 0.10],   # 6 – R wrist
        [ 0.35, 0.40,-0.10],   # 7 – L wrist
        [0.00, 0.40,  0.00],   # 8 – pelvis / mid-hip
        [-0.20, 0.40, 0.08],   # 9 – R hip
        [ 0.20, 0.40,-0.08],   # 10 – L hip
        [-0.20, 0.20, 0.08],   # 11 – R knee
        [ 0.20, 0.20,-0.08],   # 12 – L knee
        [-0.20, 0.00, 0.08],   # 13 – R ankle
        [ 0.20, 0.00,-0.08],   # 14 – L ankle
    ], dtype=float)

    return joints


def rotate_y(points, angle):
    """
    Rotates an (N, 3) array of points around the Y-axis by <angle> radians.
    """
    c, s = np.cos(angle), np.sin(angle)
    rot = np.array([[ c, 0.0, s],
                    [0.0, 1.0, 0.0],
                    [-s, 0.0, c]])
    return points @ rot.T


def project(points):
    """
    Very simple perspective projection.  Points further away (–z)
    are slightly smaller; closer points (+z) slightly larger.
    """
    # Camera parameters
    d = 2.0           # distance of viewer from projection plane
    z = points[:, 2]
    factor = d / (d - z)          # little bigger if z > 0 (toward the viewer)
    x2d = points[:, 0] * factor
    y2d = points[:, 1] * factor
    return np.column_stack([x2d, y2d])


def animate_sadman():
    # Build basic skeleton
    base = build_skeleton()

    # Matplotlib setup
    fig, ax = plt.subplots(figsize=(4, 6), dpi=100)
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.axis("off")

    # Scatter containing 15 white points
    scatter = ax.scatter([], [], s=36, c="white")

    # Limits so the figure stays centred regardless of rotation
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.1, 1.1)

    def init():
        scatter.set_offsets(np.zeros((15, 2)))
        return scatter,

    def update(frame):
        # Rotation angle: full turn every 240 frames
        angle = 2 * np.pi * frame / 240.0
        rotated = rotate_y(base, angle)

        # Optional small bobbing (sad shuffle) to make it look alive
        bob = 0.02 * np.sin(2 * np.pi * frame / 120.0)
        rotated[:, 1] += bob

        # Project to 2-D canvas & update scatter
        pts2d = project(rotated)
        scatter.set_offsets(pts2d)
        return scatter,

    ani = animation.FuncAnimation(
        fig, update, init_func=init, interval=40, blit=True, frames=240, repeat=True
    )

    plt.show()


if __name__ == "__main__":
    animate_sadman()
