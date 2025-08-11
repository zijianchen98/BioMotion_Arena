import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program uses matplotlib to display a point-light stimulus (15 points)
# of a heavy-set "happy man" performing a sitting-down motion. The background
# is solid black and the points are white.

# Number of points in the stimulus
NUM_POINTS = 15

# Animation settings
FPS = 30           # frames per second
DURATION = 4       # total duration of the sitting-down and returning-up cycle (seconds)
TOTAL_FRAMES = FPS * DURATION

# Define body segment lengths (in arbitrary units)
HEAD_RADIUS = 0.1
NECK_TO_SHOULDER = 0.2
SHOULDER_TO_ELBOW = 0.3
ELBOW_TO_HAND = 0.3
NECK_TO_HIP = 0.7
HIP_TO_KNEE = 0.5
KNEE_TO_ANKLE = 0.5

# A helper function to interpolate angles or distances over the motion parameter
def interp_value(param, start_val, end_val):
    return start_val + (end_val - start_val) * param

def get_joint_positions(frame):
    """
    Compute the (x,y) positions of the 15 point-lights (joints/markers)
    for the current animation frame.
    """

    # Param goes 0 -> 1 over the first half of the cycle (stand to sit),
    # and 1 -> 0 over the second half (sit back to stand).
    # This creates a smooth up-and-down cycle.
    half_frames = TOTAL_FRAMES // 2
    if frame < half_frames:
        param = frame / (half_frames - 1)
    else:
        param = 1.0 - (frame - half_frames) / (half_frames - 1)

    # Angles (in radians) for key joints, interpolated from standing to sitting
    # Standing: knee=0°, hip=0°, trunk upright
    # Sitting: knee=90°, hip=70°, trunk leaning forward ~30°
    knee_angle = np.radians(interp_value(param, 0, 90))   # 0->90
    hip_angle = np.radians(interp_value(param, 0, 70))    # 0->70
    trunk_angle = np.radians(interp_value(param, 0, 30))  # 0->30

    # Basic side-view skeleton:
    # We'll place the hip joint around y=1.0 (standing), and shift it downward
    # as the person sits. We'll also add a slight horizontal displacement
    # for the trunk leaning.
    # For a heavier person, the belly point will move slightly more forward.

    # Base hip center
    # Move the hips down by up to 0.4 units as sitting (param=1).
    hip_y = 1.0 - 0.4 * param
    hip_x = 0.0 + 0.2 * np.sin(trunk_angle)  # small forward shift with trunk angle

    # Neck position relative to hip, trunk leaning by trunk_angle
    # trunk length = NECK_TO_HIP
    # trunk is angled. We'll consider hip as pivot for trunk rotation.
    trunk_len = NECK_TO_HIP
    neck_x = hip_x + trunk_len * np.sin(trunk_angle)
    neck_y = hip_y + trunk_len * np.cos(trunk_angle)

    # Head (above neck)
    head_x = neck_x
    head_y = neck_y + HEAD_RADIUS

    # Shoulders: let's define them near the neck with a small offset
    # We'll treat the shoulders as 0.2 units below neck for a heavier build,
    # but also affected slightly by trunk angle.
    shoulder_offset = NECK_TO_SHOULDER
    shoulder_x = neck_x
    shoulder_y = neck_y - shoulder_offset

    # Arms: We'll do a simple approach, each shoulder -> elbow -> hand
    # We'll place R-arm and L-arm at a small +/- horizontal offset
    arm_angle = np.radians(15)  # Just a slight angle outward
    # Right shoulder
    r_shoulder_x = shoulder_x + 0.05
    r_shoulder_y = shoulder_y
    # Left shoulder
    l_shoulder_x = shoulder_x - 0.05
    l_shoulder_y = shoulder_y

    # Elbows (just a fixed angle for a relaxed posture)
    # We'll place elbows ~0.3 units down from shoulders
    r_elbow_x = r_shoulder_x + SHOULDER_TO_ELBOW * np.sin(arm_angle)
    r_elbow_y = r_shoulder_y - SHOULDER_TO_ELBOW * np.cos(arm_angle)
    l_elbow_x = l_shoulder_x - SHOULDER_TO_ELBOW * np.sin(arm_angle)
    l_elbow_y = l_shoulder_y - SHOULDER_TO_ELBOW * np.cos(arm_angle)

    # Hands
    r_hand_x = r_elbow_x + ELBOW_TO_HAND * np.sin(arm_angle)
    r_hand_y = r_elbow_y - ELBOW_TO_HAND * np.cos(arm_angle)
    l_hand_x = l_elbow_x - ELBOW_TO_HAND * np.sin(arm_angle)
    l_hand_y = l_elbow_y - ELBOW_TO_HAND * np.cos(arm_angle)

    # Knees: from hips, angle = hip_angle + knee_angle for the thigh + shin
    # We'll define the thigh angle = hip_angle relative to trunk (which is trunk_angle from vertical).
    # So total angle from vertical for thigh is trunk_angle + hip_angle
    thigh_angle = trunk_angle + hip_angle
    knee_x = hip_x + HIP_TO_KNEE * np.sin(thigh_angle)
    knee_y = hip_y + HIP_TO_KNEE * np.cos(thigh_angle)

    # Knees to ankles: angle = thigh_angle + knee_angle (the "shin" rotates further)
    shin_angle = thigh_angle + knee_angle
    ankle_x = knee_x + KNEE_TO_ANKLE * np.sin(shin_angle)
    ankle_y = knee_y + KNEE_TO_ANKLE * np.cos(shin_angle)

    # We'll define a belly point protruding out in front of the trunk
    # halfway between neck and hip but offset horizontally by about 0.15
    mid_y = (neck_y + hip_y) / 2.0
    mid_x = (neck_x + hip_x) / 2.0
    belly_offset = 0.15 + 0.05 * param  # gets a bit more forward in sitting
    belly_angle = trunk_angle
    belly_x = mid_x + belly_offset * np.sin(belly_angle)
    belly_y = mid_y + belly_offset * np.cos(belly_angle)

    # Collect all 15 points in (x,y) form:
    points = [
        (head_x, head_y),          # 1 Head
        (neck_x, neck_y),          # 2 Neck
        (r_shoulder_x, r_shoulder_y),  # 3 Right Shoulder
        (l_shoulder_x, l_shoulder_y),  # 4 Left Shoulder
        (r_elbow_x, r_elbow_y),    # 5 Right Elbow
        (l_elbow_x, l_elbow_y),    # 6 Left Elbow
        (r_hand_x, r_hand_y),      # 7 Right Hand
        (l_hand_x, l_hand_y),      # 8 Left Hand
        (hip_x, hip_y),            # 9 Hip center
        (knee_x, knee_y),          # 10 Knee (we'll assume single-limb side view)
        (ankle_x, ankle_y),        # 11 Ankle (same reasoning)
        (belly_x, belly_y),        # 12 Belly point
        # Add a few more (fake) reference points for additional "visual clarity"
        # so we total 15 white points.
        # We'll place them near the trunk line or around to mimic a heavier build.
        (hip_x + 0.1*np.sin(trunk_angle), hip_y + 0.2*np.cos(trunk_angle)),  # 13
        (neck_x + 0.1*np.sin(trunk_angle), neck_y + 0.1*np.cos(trunk_angle)),# 14
        (hip_x - 0.1*np.sin(trunk_angle), hip_y + 0.2*np.cos(trunk_angle)),  # 15
    ]

    return np.array(points)

# Setup figure and axis
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter([], [], s=40, c='white')

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    pts = get_joint_positions(frame)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(
    fig,
    update,
    frames=TOTAL_FRAMES,
    init_func=init,
    blit=True,
    interval=1000/FPS,
    repeat=True
)

plt.show()