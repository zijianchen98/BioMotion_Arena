
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of joint (point-light) markers (15: Head, shoulders, elbows, wrists, hips, knees, ankles, chest, pelvis)
JOINT_NAMES = [
    "Head",               #0
    "Left Shoulder",      #1
    "Right Shoulder",     #2
    "Left Elbow",         #3
    "Right Elbow",        #4
    "Left Wrist",         #5
    "Right Wrist",        #6
    "Chest",              #7 (sternum)
    "Pelvis",             #8
    "Left Hip",           #9
    "Right Hip",          #10
    "Left Knee",          #11
    "Right Knee",         #12
    "Left Ankle",         #13
    "Right Ankle"         #14
]

FIGSIZE = (4, 7)
DOT_SIZE = 100

def build_sad_curl_frame(t, n_joints=15, cycle=2):
    """
    Generate the 2D joint coordinates for a sad woman with heavy weight forward rolling motion
    t: time parameter (in [0, 1])
    cycle: number of rolling cycles to do
    Returns: (n_joints, 2) array
    """

    # Stick figure settings (units arbitrary)
    head_rad = 0.15
    trunk_len = 0.55
    neck_len = 0.08
    pelvis_len = 0.20
    shoulder_width = 0.23
    hip_width = 0.19
    upper_arm = 0.22
    lower_arm = 0.20
    upper_leg = 0.33
    lower_leg = 0.35

    # Curl path radius & progression
    roll_R = 1.05  # body curl path radius
    roll_center = np.array([0, 0.2])  # center of the rolling circle
    # We want a sad, heavy motion, so roll slowly; for sad effect, head and arms kind of "hang"

    theta = 2 * np.pi * cycle * t   # main angle for the body position in roll

    # The position of the pelvis in global coords (circle path for rolling)
    pelv_x = roll_center[0] + roll_R * np.sin(theta)
    pelv_y = roll_center[1] + roll_R * np.cos(theta)

    # Body curl direction (tangent to trajectory), rotate body accordingly
    body_angle = theta - np.pi/2
    # Sad body pose: curl more, chin down, arms tucked, knees kept closer
    curl = 0.75 * np.pi  # fixed trunk-hip curl angle for somersault

    # Spine: pelvis (origin), chest, head
    pelvis = np.array([pelv_x, pelv_y])
    chest = pelvis + trunk_len * np.array([np.cos(body_angle + curl/2), np.sin(body_angle + curl/2)])
    neck = chest + neck_len * np.array([np.cos(body_angle + curl), np.sin(body_angle + curl)])
    head = neck + (head_rad + 0.05) * np.array([np.cos(body_angle + curl + 0.2), np.sin(body_angle + curl + 0.2)])

    # Shoulders (offset from chest)
    left_shoulder  = chest + (shoulder_width/2) * np.array([np.cos(body_angle + curl + np.pi/2),
                                                            np.sin(body_angle + curl + np.pi/2)])
    right_shoulder = chest + (shoulder_width/2) * np.array([np.cos(body_angle + curl - np.pi/2),
                                                            np.sin(body_angle + curl - np.pi/2)])
    # Hips (offset from pelvis)
    left_hip  = pelvis + (hip_width/2) * np.array([np.cos(body_angle + np.pi/2), np.sin(body_angle + np.pi/2)])
    right_hip = pelvis + (hip_width/2) * np.array([np.cos(body_angle - np.pi/2), np.sin(body_angle - np.pi/2)])

    # Sad, heavy arms: tucked, bent, wrists a bit "droopy"
    # Arms rotate with body, then bend at elbows, then bend at wrists with extra "sad" droop
    arm_base_angle = body_angle + curl + 0.13  # forward curling

    # Left arm (shape: shoulder -> elbow -> wrist)
    la_shoulder_to_elbow = upper_arm * np.array([np.cos(arm_base_angle + 0.8), np.sin(arm_base_angle + 0.8)])
    la_elbow = left_shoulder + la_shoulder_to_elbow

    la_wrist_angle = 1.2    # forearm curled tightly, wrist drooping
    la_elbow_to_wrist = lower_arm * np.array([np.cos(arm_base_angle + 0.8 + la_wrist_angle),
                                              np.sin(arm_base_angle + 0.8 + la_wrist_angle)])
    la_wrist = la_elbow + la_elbow_to_wrist

    # Right arm
    ra_shoulder_to_elbow = upper_arm * np.array([np.cos(arm_base_angle - 0.8), np.sin(arm_base_angle - 0.8)])
    ra_elbow = right_shoulder + ra_shoulder_to_elbow
    ra_wrist_angle = 1.2
    ra_elbow_to_wrist = lower_arm * np.array([np.cos(arm_base_angle - 0.8 - ra_wrist_angle),
                                              np.sin(arm_base_angle - 0.8 - ra_wrist_angle)])
    ra_wrist = ra_elbow + ra_elbow_to_wrist

    # Sad woman with heavy weight: hands are close together, suggest holding a weight (~below head)
    # Put the wrists close to each other, slightly ahead of head:
    wrists_center = (la_wrist + ra_wrist) / 2
    weight_pos = head + 0.19 * np.array([np.cos(body_angle + curl + 0.6), np.sin(body_angle + curl + 0.6)])
    la_wrist = weight_pos + np.array([-0.028, -0.01])
    ra_wrist = weight_pos + np.array([ 0.028, +0.007])

    # Legs: knees bent, feet tucked, suggest weight and curling
    leg_base_angle = body_angle - 0.22  # legs slightly trailing trunk
    knee_bend = 0.93 * np.pi  # heavy knee bend

    # Left leg
    ll_hip_to_knee = upper_leg * np.array([np.cos(leg_base_angle + 0.26), np.sin(leg_base_angle + 0.26)])
    ll_knee = left_hip + ll_hip_to_knee
    ll_knee_to_ankle = lower_leg * np.array([np.cos(leg_base_angle + 0.26 + knee_bend),
                                             np.sin(leg_base_angle + 0.26 + knee_bend)])
    ll_ankle = ll_knee + ll_knee_to_ankle

    # Right leg
    rl_hip_to_knee = upper_leg * np.array([np.cos(leg_base_angle - 0.26), np.sin(leg_base_angle - 0.26)])
    rl_knee = right_hip + rl_hip_to_knee
    rl_knee_to_ankle = lower_leg * np.array([np.cos(leg_base_angle - 0.26 + knee_bend),
                                             np.sin(leg_base_angle - 0.26 + knee_bend)])
    rl_ankle = rl_knee + rl_knee_to_ankle

    # Stack all joints in required order
    j = np.zeros((15, 2))
    j[0 ] = head
    j[1 ] = left_shoulder
    j[2 ] = right_shoulder
    j[3 ] = la_elbow
    j[4 ] = ra_elbow
    j[5 ] = la_wrist
    j[6 ] = ra_wrist
    j[7 ] = chest
    j[8 ] = pelvis
    j[9 ] = left_hip
    j[10] = right_hip
    j[11] = ll_knee
    j[12] = rl_knee
    j[13] = ll_ankle
    j[14] = rl_ankle

    return j

# Animation setup
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Prepare blank scatter plot for 15 points
scat = ax.scatter([], [], s=DOT_SIZE, color='white')

# Framing: set limits such that the figure is centered and rolling fits in window
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.1, 2.1)

# Animate
N_FRAMES = 75
DURATION = 3.6 # seconds
def update(frame):
    t = frame / N_FRAMES
    joints = build_sad_curl_frame(t)
    scat.set_offsets(joints)
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=N_FRAMES, interval=1000*DURATION/N_FRAMES, blit=True
)

plt.show()
