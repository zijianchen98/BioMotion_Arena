
"""
Point–light biological–motion stimulus
--------------------------------------

A minimal script that generates a 15–dot point–light walker (biological
motion stimulus).  The walker is produced procedurally from a very simple
biomechanical model and animated with matplotlib.

Run this file and a window will open that shows an endlessly looping,
realistic(ish) walking cycle consisting of 15 white dots on a black
background.
"""

import numpy as np
import matplotlib                                               # noqa: E402
import matplotlib.pyplot as plt                                  # noqa: E402
from matplotlib.animation import FuncAnimation                   # noqa: E402


# -----------------------------------------------------------------------------
#  Simple (yet plausible) kinematic model
# -----------------------------------------------------------------------------
class WalkerModel:
    """A crude, but coherent 2-D biomechanical walker model."""
    # Segment lengths (all values in (arbitrary) metres)
    HEAD            = 0.25
    SPINE           = 0.25      # Neck → pelvis
    SHOULDER_WIDTH  = 0.30
    PELVIS_WIDTH    = 0.22
    UPPER_ARM       = 0.30
    LOWER_ARM       = 0.30
    THIGH           = 0.45
    SHIN            = 0.45

    STEP_LENGTH     = 0.30      # ±z range for feet
    STEP_HEIGHT     = 0.08      # how high the foot lifts
    ARM_SWING       = 0.35      # ±z range for wrists
    PERIOD          = 1.2       # walking cycle duration (sec)

    def __init__(self, fps: int = 60):
        self.fps = fps

    # ----- helpers -----------------------------------------------------------
    @staticmethod
    def _ik_2d(a_len, b_len, root_yz, end_yz, bend_sign: float = 1.0):
        """
        2-D (y–z plane) two-segment inverse kinematics.
        Gives joint (knee/elbow) co-ordinates for a limb with lengths a_len and
        b_len going from `root_yz` (hip/shoulder) to `end_yz` (ankle/wrist).

        Parameters
        ----------
        a_len, b_len : float
            Segment lengths (thigh+shin or upper+lower arm).
        root_yz, end_yz : ndarray shape (2,)
            y,z co-ordinates of root and end effector.
        bend_sign : float
            +1 => bend "forwards" (knee in front), ‑1 => bend backwards.

        Returns
        -------
        ndarray shape (2,)
            y,z co-ordinates of the joint (knee / elbow).
        """
        root = np.asarray(root_yz, dtype=float)
        end  = np.asarray(end_yz,  dtype=float)
        diff = end - root
        dist = np.linalg.norm(diff)

        # Clamp distance so that triangle can be formed
        dist = np.clip(dist, 1e-6, a_len + b_len - 1e-6)

        # Law of cosines
        a = (a_len**2 - b_len**2 + dist**2) / (2 * dist)
        h = np.sqrt(max(a_len**2 - a**2, 1e-9))

        # Unit vector hip→ankle
        u = diff / dist
        # Perpendicular vector (rotate by 90° in y–z plane)
        perp = np.array([-u[1], u[0]])     # (y,z)   (-z, y)

        joint = root + a * u + bend_sign * h * perp
        return joint

    # ----- core --------------------------------------------------------------
    def pose(self, t: float):
        """
        Compute 3-D positions for 15 key points at time `t` (seconds).

        Returns
        -------
        ndarray, shape (15, 3)
            x, y, z coordinates of the 15 dots.
        """
        # -----------------------------------------------------------------
        #  Global/root motion
        # -----------------------------------------------------------------
        phase = 2 * np.pi * (t % self.PERIOD) / self.PERIOD       # [0, 2π)
        hip_y = 1.0 + 0.05 * np.sin(2 * phase)                    # vertical bob
        hip_z = 0.0                                               # in-place walk

        # left/right phase offset
        phi_L = phase
        phi_R = phase + np.pi

        # -----------------------------------------------------------------
        #  Feet (ankles)
        # -----------------------------------------------------------------
        def foot_pos(phi):
            """Ankle world position in y-z plane."""
            z = self.STEP_LENGTH * np.sin(phi)
            lift = np.clip(np.sin(phi), 0, 1)                     # only positive half
            y = 0.0 + self.STEP_HEIGHT * lift
            return np.array([y, z])                               # (y, z)

        L_ankle_yz = foot_pos(phi_L)
        R_ankle_yz = foot_pos(phi_R)

        # -----------------------------------------------------------------
        #  Hips, knees (inverse kinematics)
        # -----------------------------------------------------------------
        hip_offset_z = 0.5 * self.PELVIS_WIDTH
        L_hip_yz = np.array([hip_y, hip_z - hip_offset_z])
        R_hip_yz = np.array([hip_y, hip_z + hip_offset_z])

        L_knee_yz = self._ik_2d(self.THIGH, self.SHIN,
                                L_hip_yz, L_ankle_yz, bend_sign=1)
        R_knee_yz = self._ik_2d(self.THIGH, self.SHIN,
                                R_hip_yz, R_ankle_yz, bend_sign=1)

        # -----------------------------------------------------------------
        #  Upper body
        # -----------------------------------------------------------------
        neck_y  = hip_y + self.SPINE
        head_y  = neck_y + self.HEAD

        shoulder_offset_z = 0.5 * self.SHOULDER_WIDTH
        L_sh_yz = np.array([neck_y, hip_z - shoulder_offset_z])
        R_sh_yz = np.array([neck_y, hip_z + shoulder_offset_z])

        # Wrists trajectory (arm swing opposite to legs)
        def wrist_traj(phi, side_sign):
            z = side_sign * 0.02 + self.ARM_SWING * np.sin(phi + np.pi)  # opposite phase
            drop = 0.25
            y = hip_y - drop + 0.04 * np.sin(phi + np.pi/2)              # slight bounce
            return np.array([y, z])

        L_wrist_yz = wrist_traj(phi_L, -1)
        R_wrist_yz = wrist_traj(phi_R, +1)

        # Elbows via IK
        L_elb_yz = self._ik_2d(self.UPPER_ARM, self.LOWER_ARM,
                               L_sh_yz, L_wrist_yz, bend_sign=-1)
        R_elb_yz = self._ik_2d(self.UPPER_ARM, self.LOWER_ARM,
                               R_sh_yz, R_wrist_yz, bend_sign=-1)

        # -----------------------------------------------------------------
        #  Assemble all 15 points  (x,y,z) – we keep x constant (=depth into screen)
        # -----------------------------------------------------------------
        # A small constant left/right x-offset gives us proper separation
        # in projection so that symmetric joints don’t overlap perfectly.
        SEP = 0.06
        pts = np.zeros((15, 3))
        #     idx   x                     y        z
        pts[0]  = [0.0,         head_y,           hip_z]                 # head
        pts[1]  = [0.0,         neck_y,           hip_z]                 # neck/sternum
        pts[2]  = [0.0,         hip_y,            hip_z]                 # pelvis (mid)
        # shoulders
        pts[3]  = [-SEP,        L_sh_yz[0],       L_sh_yz[1]]            # L shoulder
        pts[4]  = [+SEP,        R_sh_yz[0],       R_sh_yz[1]]            # R shoulder
        # elbows
        pts[5]  = [-SEP,        L_elb_yz[0],      L_elb_yz[1]]           # L elbow
        pts[6]  = [+SEP,        R_elb_yz[0],      R_elb_yz[1]]           # R elbow
        # wrists
        pts[7]  = [-SEP,        L_wrist_yz[0],    L_wrist_yz[1]]         # L wrist
        pts[8]  = [+SEP,        R_wrist_yz[0],    R_wrist_yz[1]]         # R wrist
        # hips
        pts[9]  = [-SEP,        L_hip_yz[0],      L_hip_yz[1]]           # L hip
        pts[10] = [+SEP,        R_hip_yz[0],      R_hip_yz[1]]           # R hip
        # knees
        pts[11] = [-SEP,        L_knee_yz[0],     L_knee_yz[1]]          # L knee
        pts[12] = [+SEP,        R_knee_yz[0],     R_knee_yz[1]]          # R knee
        # ankles
        pts[13] = [-SEP,        L_ankle_yz[0],    L_ankle_yz[1]]         # L ankle
        pts[14] = [+SEP,        R_ankle_yz[0],    R_ankle_yz[1]]         # R ankle

        return pts


# -----------------------------------------------------------------------------
#  Matplotlib animation / visualisation
# -----------------------------------------------------------------------------
def main():
    # Make sure we use a dark background
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(4, 6))
    fig.canvas.manager.set_window_title("Point-light Walker")

    # Axes aesthetics
    ax.set_facecolor("black")
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 2)
    ax.set_aspect("equal")
    ax.axis("off")

    model = WalkerModel(fps=60)
    dots  = ax.scatter([], [], s=40, c="white")

    def init():
        dots.set_offsets(np.zeros((15, 2)))
        return (dots,)

    def update(frame):
        t   = frame / model.fps
        pts = model.pose(t)

        # orthographic projection: (x, y, z) → (z, y)
        xy  = np.stack([pts[:, 2], pts[:, 1]], axis=1)
        dots.set_offsets(xy)
        return (dots,)

    # 3 seconds of animation, looped
    frames = int(model.fps * 3)
    anim = FuncAnimation(fig, update, init_func=init,
                         frames=frames, interval=1000 / model.fps,
                         blit=True)

    plt.show()


if __name__ == "__main__":
    main()
