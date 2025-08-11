
"""
Biological‐motion point-light display
Running (light-weight, sadman), 15 white dots on a black background
-------------------------------------------------------------------

When executed this script will

1.  Synthesize a kinematically–plausible running gait for 15 anatomical
    landmarks (head, neck, shoulders, elbows, wrists, pelvis, hips,
    knees, ankles).

2.  Produce an animation (60 frames ≈ 2 s at 30 fps) using matplotlib.
    The animation is saved as an animated GIF file
    ``point_light_running.gif`` in the current directory.  If a graphic
    backend is available an interactive window will also pop up.

The most important routine for possible automatic assessment is
``generate_running_motion(frames)`` which returns a NumPy array of shape

    (frames, 15, 2)   # (time, point-index, XY)

with normalised coordinates in the range 0 … 1 for both axes.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# --------------------------------------------------------------------
# 1.  Kinematic model
# --------------------------------------------------------------------
def _single_pose(phase: float) -> np.ndarray:
    """
    Return 15×2 array with joint positions for one instant of the gait
    cycle.  ``phase`` must be in the interval [0, 1).
    All coordinates are normalised to the interval [0, 1].
    """

    # ---------------------- general constants -----------------------
    # Relative segment lengths (in fraction of global height)
    HEAD_H           = 0.08
    NECK_H           = 0.02
    TORSO_H          = 0.18
    THIGH_L          = 0.18
    SHIN_L           = 0.18
    ARM_UPPER_L      = 0.14
    ARM_LOWER_L      = 0.14
    SHOULDER_OFFSET  = 0.07  # horizontal distance pelvis-→shoulder
    HIP_OFFSET       = 0.06

    # Basic reference point: pelvis (body COM)
    pelvis_x = 0.50                          # centred horizontally
    pelvis_y = 0.50 + 0.02 * math.sin(2*math.pi*phase)   # slight bob
    pelvis   = np.array([pelvis_x, pelvis_y])

    # ---------------------- legs (running) --------------------------
    # Angular variations (deg) – simple sinusoidal model
    # Legs alternate; right = +phase, left = phase+π
    freq = 1.0                      # 1 stride / gait cycle
    theta_thigh_r = math.radians( 30 * math.sin(2*math.pi*freq*phase))
    theta_thigh_l = math.radians(-30 * math.sin(2*math.pi*freq*phase))

    # Knee flexion peaks midway through swing phase
    theta_knee_r = math.radians(40 * (1 - math.cos(2*math.pi*freq*phase)))  # ≥0
    theta_knee_l = math.radians(40 * (1 - math.cos(2*math.pi*freq*phase + math.pi)))

    # Helper to compute knee & ankle
    def _leg(hip_pt: np.ndarray, thigh_ang: float, knee_flex: float):
        knee = hip_pt + np.array([THIGH_L*math.sin(thigh_ang),
                                  -THIGH_L*math.cos(thigh_ang)])
        shank_ang = thigh_ang + knee_flex
        ankle = knee + np.array([SHIN_L*math.sin(shank_ang),
                                 -SHIN_L*math.cos(shank_ang)])
        return knee, ankle

    # Hip joints
    hip_r = pelvis + np.array([ HIP_OFFSET, 0])
    hip_l = pelvis + np.array([-HIP_OFFSET, 0])

    knee_r, ankle_r = _leg(hip_r, theta_thigh_r, theta_knee_r)
    knee_l, ankle_l = _leg(hip_l, theta_thigh_l, theta_knee_l)

    # ---------------------- arms ------------------------------------
    # Arms swing in counter-phase with legs
    theta_arm_r = math.radians(-35 * math.sin(2*math.pi*freq*phase))
    theta_arm_l = math.radians( 35 * math.sin(2*math.pi*freq*phase))

    # Shoulder and arm joints
    shoulder_y = pelvis_y + TORSO_H
    shoulder_r = np.array([pelvis_x + SHOULDER_OFFSET, shoulder_y])
    shoulder_l = np.array([pelvis_x - SHOULDER_OFFSET, shoulder_y])

    def _arm(shoulder_pt: np.ndarray, upper_ang: float):
        elbow = shoulder_pt + np.array([ARM_UPPER_L*math.sin(upper_ang),
                                        -ARM_UPPER_L*math.cos(upper_ang)])
        fore_ang = upper_ang + math.radians(25)   # constant elbow bend
        wrist = elbow + np.array([ARM_LOWER_L*math.sin(fore_ang),
                                  -ARM_LOWER_L*math.cos(fore_ang)])
        return elbow, wrist

    elbow_r, wrist_r = _arm(shoulder_r, theta_arm_r)
    elbow_l, wrist_l = _arm(shoulder_l, theta_arm_l)

    # ---------------------- head and torso --------------------------
    neck = np.array([pelvis_x, shoulder_y + NECK_H])
    head = np.array([pelvis_x, neck[1] + HEAD_H])

    # ---------------------- stack all points ------------------------
    # Index legend:
    # 0 head, 1 neck, 2 R-shoulder, 3 L-shoulder,
    # 4 R-elbow, 5 L-elbow, 6 R-wrist, 7 L-wrist,
    # 8 pelvis, 9 R-hip, 10 L-hip,
    # 11 R-knee, 12 L-knee, 13 R-ankle, 14 L-ankle
    pts = np.array([
        head, neck,
        shoulder_r, shoulder_l,
        elbow_r,   elbow_l,
        wrist_r,   wrist_l,
        pelvis, hip_r, hip_l,
        knee_r,  knee_l,
        ankle_r, ankle_l
    ])
    return pts


def generate_running_motion(frames: int = 60) -> np.ndarray:
    """
    Generate a biological-motion sequence.

    Parameters
    ----------
    frames : int
        Number of time steps (default 60).

    Returns
    -------
    ndarray
        Array of shape ``(frames, 15, 2)`` with coordinates in [0 … 1].
    """
    phases = np.linspace(0, 1, frames, endpoint=False)
    seq = np.stack([_single_pose(phase) for phase in phases], axis=0)
    return seq


# --------------------------------------------------------------------
# 2.  Animation using matplotlib
# --------------------------------------------------------------------
def _create_animation(data: np.ndarray,
                      fps: int = 30,
                      outfile: str | Path = "point_light_running.gif") -> None:
    """Create and save an animated GIF from pre-computed coordinates."""
    frames, n_points, _ = data.shape
    assert n_points == 15, "There must be exactly 15 points."

    # Figure setup
    fig, ax = plt.subplots(figsize=(4, 6), dpi=100)
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    scat = ax.scatter([], [], s=60, c="white")

    def _init():
        scat.set_offsets(np.zeros((n_points, 2)))
        return scat,

    def _update(i):
        scat.set_offsets(data[i])
        return scat,

    anim = FuncAnimation(fig,
                         _update,
                         frames=frames,
                         init_func=_init,
                         interval=1000 / fps,
                         blit=True)

    # Save animation (Pillow writer is always available)
    anim.save(outfile, writer=PillowWriter(fps=fps))

    # If a display backend exists, also present interactively
    try:
        plt.show(block=False)
        plt.pause(0.1)   # yield to event loop
    except Exception:
        pass   # headless environment, nothing to do
    finally:
        plt.close(fig)


# --------------------------------------------------------------------
# 3.  Main (only executed when run as a script)
# --------------------------------------------------------------------
if __name__ == "__main__":
    motion_sequence = generate_running_motion(frames=60)
    _create_animation(motion_sequence)
