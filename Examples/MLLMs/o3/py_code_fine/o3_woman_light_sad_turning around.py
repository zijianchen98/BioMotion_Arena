
"""
Point-light stimulus: 15 white dots depicting a sad woman (light-weight build)
slowly turning around.  The animation is saved as a GIF called
`sadwoman_turning.gif`.

The code is entirely self-contained, uses only the Python standard library
plus matplotlib, and works in a head-less environment (Agg backend).
"""

import numpy as np
import matplotlib

# Use a non-interactive backend so the script works head-less
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def build_base_skeleton() -> np.ndarray:
    """
    Returns a (15, 3) array with the default 3-D coordinates for the joints
    of a (light-weight) human figure in a slightly slouched, 'sad' pose.

        index  joint
        -----  -------------------------
          0    head top
          1    neck
          2    left shoulder
          3    right shoulder
          4    left elbow
          5    right elbow
          6    left wrist
          7    right wrist
          8    pelvis (root / centre of mass)
          9    left hip
         10    right hip
         11    left knee
         12    right knee
         13    left ankle
         14    right ankle
    """
    #                     x,   y,   z
    joints = np.array(
        [
            [0.00, 1.70, 0.15],   # head top (slightly forward -> sad feeling)
            [0.00, 1.50, 0.10],   # neck
            [-0.20, 1.45, 0.05],  # L shoulder (a bit lower than neutral)
            [0.20, 1.45, 0.05],   # R shoulder
            [-0.35, 1.20, 0.05],  # L elbow
            [0.35, 1.20, 0.05],   # R elbow
            [-0.40, 0.95, 0.05],  # L wrist
            [0.40, 0.95, 0.05],   # R wrist
            [0.00, 1.00, 0.00],   # pelvis
            [-0.15, 1.00, 0.00],  # L hip
            [0.15, 1.00, 0.00],   # R hip
            [-0.15, 0.55, 0.00],  # L knee
            [0.15, 0.55, 0.00],   # R knee
            [-0.15, 0.10, 0.00],  # L ankle
            [0.15, 0.10, 0.00],   # R ankle
        ],
        dtype=float,
    )
    return joints


def rotate_y(points: np.ndarray, angle: float) -> np.ndarray:
    """
    Rigid rotation of points about the (global) Y axis by 'angle' radians.
    """
    c, s = np.cos(angle), np.sin(angle)
    rot = np.array([[c, 0.0, s], [0.0, 1.0, 0.0], [-s, 0.0, c]])
    return points @ rot.T  # (N,3) • (3,3)^T  -> (N,3)


def project_to_2d(points: np.ndarray, distance: float = 4.0) -> np.ndarray:
    """
    Simple perspective projection onto the 2-D image plane.
    """
    # Avoid division by zero if any z >= distance
    z = distance - points[:, 2]
    z[z < 1e-3] = 1e-3
    proj = points[:, :2] / z[:, None]
    return proj


def make_animation(filename: str = "sadwoman_turning.gif",
                   frames: int = 90,
                   fps: int = 30) -> None:
    """
    Create and save the point-light animation as an animated GIF.
    """
    base = build_base_skeleton()          # (15, 3)
    fig, ax = plt.subplots(figsize=(4, 6))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    scatter = ax.scatter([], [], s=30, c="white")
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(0.0, 1.9)
    ax.invert_yaxis()                     # conventional: y up -> y down for image
    ax.axis("off")                        # remove axes / ticks

    # Pre-compute all frames (helps tests that may analyse coordinates)
    projected_frames = []
    for i in range(frames):
        # Full 360° turn
        theta = 2 * np.pi * (i / frames)
        rot_points = rotate_y(base, theta)

        # Add a very subtle sway (weight shift) for realism (±2 cm side-to-side)
        sway = 0.02 * np.sin(2 * np.pi * (i / frames))
        rot_points[:, 0] += sway

        projected = project_to_2d(rot_points)
        projected_frames.append(projected)

    def update(frame_idx: int):
        coords = projected_frames[frame_idx]
        scatter.set_offsets(coords)
        return (scatter,)

    anim = FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=1000 / fps,
        blit=True,
    )

    # Save
    writer = PillowWriter(fps=fps)
    anim.save(filename, writer=writer)

    plt.close(fig)  # prevent resource warning on some systems


if __name__ == "__main__":
    make_animation()
