import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---------------
# Helper function
# ---------------
def rotation(origin, angle_deg, length):
    """
    Returns the endpoint of a segment (length) rotated by angle_deg (from vertical) 
    relative to 'origin'.
    'angle_deg' is measured clockwise from the vertical axis.
    'origin' is a 2D tuple (x, y).
    """
    # Convert angle to radians
    angle_rad = np.radians(angle_deg)
    # Endpoint relative to origin
    dx = length * np.sin(angle_rad)
    dy = -length * np.cos(angle_rad)
    return (origin[0] + dx, origin[1] + dy)

def get_joints(t):
    """
    Computes 15 joint coordinates (x, y) at time t for a running motion.
    Joints (in order):
     1. head
     2. chest
     3. left_shoulder
     4. right_shoulder
     5. left_elbow
     6. right_elbow
     7. left_wrist
     8. right_wrist
     9. pelvis
    10. left_hip
    11. right_hip
    12. left_knee
    13. right_knee
    14. left_ankle
    15. right_ankle
    """
    # Base body lengths
    trunk_len = 0.5
    head_offset = 0.25
    shoulder_offset = 0.15
    arm_upper_len = 0.25
    arm_lower_len = 0.25
    hip_offset = 0.12
    leg_upper_len = 0.35
    leg_lower_len = 0.35
    
    # Small bounce to simulate running vertical displacement
    pelvis_y = 0.05 * np.sin(2.0 * t)
    pelvis = (0.0, pelvis_y)  # (9) pelvis
    
    # Chest (2) is trunk_len above pelvis (vertical trunk)
    chest = (pelvis[0], pelvis[1] + trunk_len)
    
    # Head (1) slightly tilted forward to depict sadness: tilt ~ 15 deg
    head_angle = 15.0
    # Treat chest as the origin for the head
    head = rotation(chest, head_angle, head_offset)
    
    # Shoulders (3) left, (4) right
    left_shoulder = (chest[0] - shoulder_offset, chest[1])
    right_shoulder = (chest[0] + shoulder_offset, chest[1])
    
    # Hips (10) left, (11) right
    left_hip = (pelvis[0] - hip_offset, pelvis[1])
    right_hip = (pelvis[0] + hip_offset, pelvis[1])
    
    # --------------------
    # Running kinematics
    # --------------------
    # For simple plausibility, arms and legs swing out of phase
    # Angles measured from vertical (0 deg means straight down)
    # Frequencies set to 2 for a quicker running cycle
    arm_swing_amp = 30.0
    leg_swing_amp = 35.0
    
    # Left arm angle + left elbow bend
    alpha_la = arm_swing_amp * np.sin(2.0 * t)  # upper arm angle
    bend_la = 0.5 * alpha_la                   # elbow bend
    # Right arm angle + right elbow bend (phase-shift by pi)
    alpha_ra = arm_swing_amp * np.sin(2.0 * t + np.pi)
    bend_ra = 0.5 * alpha_ra
    
    # Left leg angle + left knee bend (phase-shift by pi)
    alpha_ll = leg_swing_amp * np.sin(2.0 * t + np.pi)
    bend_ll = 0.5 * alpha_ll
    # Right leg angle + right knee bend
    alpha_rl = leg_swing_amp * np.sin(2.0 * t)
    bend_rl = 0.5 * alpha_rl
    
    # --------------------
    # Upper Arms -> Elbows -> Wrists
    # --------------------
    # Left elbow (5)
    left_elbow = rotation(left_shoulder, alpha_la, arm_upper_len)
    # Left wrist (7)
    left_wrist = rotation(left_elbow, alpha_la + bend_la, arm_lower_len)
    
    # Right elbow (6)
    right_elbow = rotation(right_shoulder, alpha_ra, arm_upper_len)
    # Right wrist (8)
    right_wrist = rotation(right_elbow, alpha_ra + bend_ra, arm_lower_len)

    # --------------------
    # Upper Legs -> Knees -> Ankles
    # --------------------
    # Left knee (12)
    left_knee = rotation(left_hip, alpha_ll, leg_upper_len)
    # Left ankle (14)
    left_ankle = rotation(left_knee, alpha_ll + bend_ll, leg_lower_len)
    
    # Right knee (13)
    right_knee = rotation(right_hip, alpha_rl, leg_upper_len)
    # Right ankle (15)
    right_ankle = rotation(right_knee, alpha_rl + bend_rl, leg_lower_len)
    
    # Collect all 15 points for plotting
    return np.array([
        head,         # 1
        chest,        # 2
        left_shoulder,# 3
        right_shoulder,#4
        left_elbow,   # 5
        right_elbow,  # 6
        left_wrist,   # 7
        right_wrist,  # 8
        pelvis,       # 9
        left_hip,     #10
        right_hip,    #11
        left_knee,    #12
        right_knee,   #13
        left_ankle,   #14
        right_ankle   #15
    ])

# ---------------
# Animation setup
# ---------------
fig = plt.figure(facecolor='black')
ax = plt.axes(xlim=(-1.0, 1.0), ylim=(-1.0, 1.0))
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Create a scatter plot for the 15 points (white on black)
scatter_plot = ax.scatter([], [], c='white', s=30)

def init():
    scatter_plot.set_offsets([])
    return (scatter_plot,)

def animate(frame):
    # One cycle is 2*pi; let's map frame -> t in [0..2*pi]
    # e.g. 60 frames per cycle
    t = 2.0 * np.pi * (frame / 60.0)
    coords = get_joints(t)
    scatter_plot.set_offsets(coords)
    return (scatter_plot,)

ani = animation.FuncAnimation(
    fig, 
    animate, 
    init_func=init, 
    frames=120,   # run for 2 cycles 
    interval=40,  # delay between frames in ms (~25 fps)
    blit=True
)

plt.show()