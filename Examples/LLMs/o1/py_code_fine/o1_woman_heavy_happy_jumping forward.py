import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This program displays a point-light stimulus of a "happy woman with heavy weight"
# jumping forward in a biologically plausible manner. It uses 15 white points on
# a solid black background and animates their positions over time to represent
# the jumping sequence.

# ----------------------
# Global Settings
# ----------------------
FPS = 30            # Frames per second
DURATION = 2.0      # Total duration of the jump (seconds)
FRAMES = int(FPS * DURATION)
NUM_POINTS = 15
# Figure limits for the display
X_MIN, X_MAX = -1.0, 6.0
Y_MIN, Y_MAX = -0.5, 3.0

# ----------------------
# Helper Functions
# ----------------------

def get_joint_positions(t):
    """
    Returns the (x, y) positions of the 15 joints at time t (where t is in [0,1])
    to simulate a 'heavy' forward jump in a plausible manner.
    Joints (example labeling):
      0:  Head
      1:  Neck
      2:  Shoulder Left
      3:  Elbow Left
      4:  Hand Left
      5:  Shoulder Right
      6:  Elbow Right
      7:  Hand Right
      8:  Hip Left
      9:  Knee Left
      10: Foot Left
      11: Hip Right
      12: Knee Right
      13: Foot Right
      14: Pelvis/Body Center
    """

    # Horizontal progression (heavy jump, slower forward movement)
    # Let's move from x=0 to x=5 over one jump cycle (t in [0..1])
    pelvis_x = 5.0 * t
    
    # Vertical jump arc (heavier bounce, smaller amplitude, slower apex)
    # We can use a "sin" shaped jump for the pelvis:
    pelvis_y = 1.2 * np.sin(np.pi * t)  # peak in mid-jump

    # Basic stance parameters
    # Slight up-down shift to create a heavier landing effect
    vertical_offset = 0.5
    
    # Let's define angles or offsets for the limbs based on time t
    # We can simulate arms and legs bending differently through the jump.
    # For example, arms swing forward at mid jump, legs bend on landing.
    arm_swing = 0.5 - 0.5 * np.cos(2 * np.pi * t)
    leg_bend = 0.3 + 0.2 * np.cos(2 * np.pi * t)
    
    # The pelvis is the base of the body
    pelvis = np.array([pelvis_x, pelvis_y + vertical_offset])

    # Torso length
    torso_len = 0.45
    # Neck is above the pelvis by torso_len
    neck = pelvis + np.array([0.0, torso_len])
    # Head point a bit above the neck
    head = neck + np.array([0.0, 0.15])

    # Shoulders L/R from the neck
    shoulder_offset = 0.2
    shoulder_left = neck + np.array([-shoulder_offset, 0])
    shoulder_right = neck + np.array([ shoulder_offset, 0])

    # Arms (use arm_swing to pivot elbow positions)
    upper_arm_len = 0.25
    lower_arm_len = 0.25
    
    # Left arm
    elbow_left = shoulder_left + np.array([0, -upper_arm_len * (0.8 + 0.2*arm_swing)])
    hand_left = elbow_left + np.array([0, -lower_arm_len * (0.7 + 0.3*arm_swing)])
    
    # Right arm
    elbow_right = shoulder_right + np.array([0, -upper_arm_len * (0.8 - 0.2*arm_swing)])
    hand_right = elbow_right + np.array([0, -lower_arm_len * (0.7 - 0.3*arm_swing)])
    
    # Hips L/R from pelvis
    hip_offset = 0.15
    hip_left = pelvis + np.array([-hip_offset, 0])
    hip_right = pelvis + np.array([ hip_offset, 0])

    # Legs
    upper_leg_len = 0.4
    lower_leg_len = 0.4
    
    # Left leg
    knee_left = hip_left + np.array([0, -upper_leg_len * (1.0 - 0.5*leg_bend)])
    foot_left = knee_left + np.array([0, -lower_leg_len * (1.0 - 0.5*leg_bend)])
    
    # Right leg
    knee_right = hip_right + np.array([0, -upper_leg_len * (1.0 - 0.4*leg_bend)])
    foot_right = knee_right + np.array([0, -lower_leg_len * (1.0 - 0.4*leg_bend)])
    
    # Collect all points in order
    points = np.array([
        head,
        neck,
        shoulder_left,
        elbow_left,
        hand_left,
        shoulder_right,
        elbow_right,
        hand_right,
        hip_left,
        knee_left,
        foot_left,
        hip_right,
        knee_right,
        foot_right,
        pelvis
    ])
    
    return points

# ----------------------
# Animation Functions
# ----------------------

def init():
    scatter.set_offsets(np.zeros((NUM_POINTS, 2)))
    return (scatter,)

def animate(frame):
    # Convert frame index to a time value [0..1] for one jump cycle
    t = frame / (FRAMES - 1.0)
    pts = get_joint_positions(t)
    scatter.set_offsets(pts)
    return (scatter,)

# ----------------------
# Main Execution
# ----------------------
if __name__ == "__main__":
    plt.style.use('dark_background')

    fig, ax = plt.subplots()
    fig.set_dpi(100)
    fig.set_size_inches(6, 4)

    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)
    ax.set_aspect('equal')
    ax.axis('off')  # no axes for a clean black background

    # Create scatter for 15 white dots
    scatter = ax.scatter(
        np.zeros(NUM_POINTS),
        np.zeros(NUM_POINTS),
        c='white',
        s=40
    )

    ani = animation.FuncAnimation(
        fig, animate, init_func=init,
        frames=FRAMES, interval=1000/FPS, blit=True
    )

    plt.show()