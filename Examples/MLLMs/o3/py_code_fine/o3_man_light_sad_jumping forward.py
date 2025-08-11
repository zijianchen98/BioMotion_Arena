
"""
Point-light biological motion stimulus
15 white dots on a black background representing a light-weight sadman jumping forward.
The animation is saved as GIF “point_light_jump.gif”.
"""

import numpy as np
import matplotlib

# Use a non-interactive backend so the code also runs on headless machines / CI servers
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


class JumpingPointLight:
    """
    Generate the 2-D coordinates (x, y) of 15 anatomical markers describing
    a person jumping forward.  All distances are in arbitrary units.
    
    Marker order (15):
        0  head
        1  neck
        2  L shoulder   3  R shoulder
        4  L elbow      5  R elbow
        6  L wrist      7  R wrist
        8  pelvis (mid-hip)
        9  L hip        10 R hip
        11 L knee       12 R knee
        13 L ankle      14 R ankle
    """

    def __init__(self):
        # constant body segment lengths
        self.torso = 1.0      # pelvis->neck
        self.head  = 0.30     # neck->head
        self.upper_arm = 0.45
        self.fore_arm  = 0.45
        self.thigh = 0.80
        self.shank = 0.80

        # lateral widths
        self.shoulder_w = 0.60
        self.hip_w      = 0.50

        # global parameters
        self.jump_height = 0.50    # COM vertical excursion
        self.forward_stride = 2.0  # how far the jumper travels (x direction)
        self.frames = 120          # total number of frames in the cycle

    def frame(self, n: int):
        """
        Compute the 15×2 array of (x, y) coordinates for frame index n.
        """
        # phase value in [0,1]
        t = n / (self.frames - 1)

        # ------------------------------------------------------------------ #
        #  global (pelvis / COM) translation
        # ------------------------------------------------------------------ #
        # Forward movement (x) – linear
        pelvis_x = self.forward_stride * t
        # Vertical movement – single jump: smooth take-off, flight, landing
        pelvis_y = 0.90 + self.jump_height * np.sin(np.pi * t)

        # ------------------------------------------------------------------ #
        #  posture parameters that vary over the jump
        # ------------------------------------------------------------------ #
        # Knee/hip bending (0 = fully extended, 1 = fully flexed)
        bend = np.cos(np.pi * t) ** 2                      # bent at start & end
        # Arm swing (–1 = backwards, +1 = forwards)
        arm_swing = np.sin(np.pi * t)                      # back->front->back

        # Thigh + shank effective (vertical) lengths as a function of bend
        thigh_eff  = self.thigh  * (0.6 + 0.4 * (1 - bend))   # 60–100 % length
        shank_eff  = self.shank  * (0.6 + 0.4 * (1 - bend))

        # Height of knees and ankles
        knee_y   = pelvis_y - thigh_eff
        ankle_y  = knee_y   - shank_eff

        # Amount the knees come forward when bending
        knee_forward_offset = 0.20 * bend        # small forward shift

        # ------------------------------------------------------------------ #
        #  Assemble all 15 joint coordinates
        # ------------------------------------------------------------------ #
        pts = np.zeros((15, 2))

        # Head / neck / shoulders
        neck_y = pelvis_y + self.torso
        head_y = neck_y + self.head

        pts[0]  = (pelvis_x,                head_y)             # head
        pts[1]  = (pelvis_x,                neck_y)             # neck
        pts[2]  = (pelvis_x - self.shoulder_w/2, neck_y)        # L shoulder
        pts[3]  = (pelvis_x + self.shoulder_w/2, neck_y)        # R shoulder

        # Arms – simple hinged two-segment model in the sagittal plane
        # Angle (in radians) relative to negative y (down) axis
        # Backwards swing = negative angle, forward swing = positive
        arm_angle = 0.8 * arm_swing     # ⁓ ± 0.8 rad

        # Left arm (mirrored right arm)
        for side, shoulder_idx, elbow_idx, wrist_idx, sign in (
            ("L", 2, 4, 6, -1),
            ("R", 3, 5, 7, +1),
        ):
            shoulder_x, shoulder_y = pts[shoulder_idx]
            # Upper arm end (elbow)
            elbow_x = shoulder_x + sign * self.upper_arm * np.sin(arm_angle)
            elbow_y = shoulder_y - self.upper_arm * np.cos(arm_angle)
            # Forearm end (wrist)
            wrist_x = elbow_x + sign * self.fore_arm * np.sin(arm_angle)
            wrist_y = elbow_y - self.fore_arm * np.cos(arm_angle)
            pts[elbow_idx] = (elbow_x, elbow_y)
            pts[wrist_idx] = (wrist_x, wrist_y)

        # Pelvis & hips
        pts[8]  = (pelvis_x,                pelvis_y)           # pelvis
        pts[9]  = (pelvis_x - self.hip_w/2, pelvis_y)           # L hip
        pts[10] = (pelvis_x + self.hip_w/2, pelvis_y)           # R hip

        # Knees & ankles
        # Knees move forward slightly when flexed (bend)
        for hip_idx, knee_idx, ankle_idx, sign in (
            (9, 11, 13, -1),
            (10, 12, 14, +1),
        ):
            hip_x, _ = pts[hip_idx]
            knee_x  = hip_x + sign * knee_forward_offset
            pts[knee_idx] = (knee_x, knee_y)
            pts[ankle_idx] = (knee_x, ankle_y)

        return pts


def create_animation():
    model = JumpingPointLight()

    # ---------- Matplotlib figure & axis ----------
    fig, ax = plt.subplots(figsize=(4, 6), facecolor="black")
    ax.set_facecolor("black")

    # Initial scatter plot (15 points)
    scatter = ax.scatter([], [], s=30, c="white")

    # Nice axis limits so the jumper remains centred
    ax.set_xlim(-1.5, model.forward_stride + 1.5)
    ax.set_ylim(-0.5, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # ---------- Animation callback ----------
    def init():
        scatter.set_offsets(np.zeros((15, 2)))
        return scatter,

    def update(frame):
        pts = model.frame(frame)
        scatter.set_offsets(pts)
        return scatter,

    ani = FuncAnimation(
        fig,
        update,
        frames=model.frames,
        init_func=init,
        interval=1000 / 30,  # 30 fps
        blit=True
    )

    # Save as GIF (works everywhere – no extra codecs needed)
    ani.save("point_light_jump.gif", writer=PillowWriter(fps=30))


if __name__ == "__main__":
    create_animation()
