
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint index legend for 15 points:
# 0: Head
# 1: L Shoulder, 2: R Shoulder
# 3: L Elbow,   4: R Elbow
# 5: L Wrist,   6: R Wrist
# 7: Chest
# 8: Pelvis (hips)
# 9: L Hip,    10: R Hip
# 11: L Knee,  12: R Knee
# 13: L Ankle, 14: R Ankle

# Bone connectivities for sadman figure (as in example image)
BONES = [
    (0,1), (0,2),       # Head-Shoulders
    (1,3), (2,4),       # Shoulders-Elbows
    (3,5), (4,6),       # Elbows-Wrists
    (1,7), (2,7),       # Shoulders-Chest
    (7,8),              # Chest-Pelvis(Hips)
    (8,9),   (8,10),    # Pelvis-Hips
    (9,11),  (10,12),   # Hips-Knees
    (11,13), (12,14),   # Knees-Ankles
]

# Skeleton lengths (meters)
SKELETON = {
    'head': 0.13,
    'neck': 0.10,
    'shoulder_to_elbow': 0.23,
    'elbow_to_wrist': 0.23,
    'shoulder_width': 0.36,
    'chest_height': 0.14,
    'torso_height': 0.30,
    'hip_width': 0.25,
    'hip_to_knee': 0.40,
    'knee_to_ankle': 0.41
}

def base_pose():
    """Returns the initial pose as (15,2) ndarray, centered at (0,0)."""
    sk = SKELETON
    # y: up, x: right
    pelvis = np.array([0.0, 0.0])

    # Hips
    l_hip = pelvis + np.array([-sk['hip_width']/2, 0])
    r_hip = pelvis + np.array([ sk['hip_width']/2, 0])

    # Chest is above pelvis
    chest = pelvis + np.array([0, sk['torso_height']])
    # Shoulders above chest
    l_shoulder = chest + np.array([-sk['shoulder_width']/2, sk['chest_height']])
    r_shoulder = chest + np.array([ sk['shoulder_width']/2, sk['chest_height']])
    # Head above midpoint of shoulders/neck
    neck = (l_shoulder + r_shoulder)/2
    head = neck + np.array([0, sk['neck'] + sk['head']])

    # Elbows and Wrists: hanging down (neutral)
    l_elbow = l_shoulder + np.array([-0.02, -sk['shoulder_to_elbow']])
    r_elbow = r_shoulder + np.array([ 0.02, -sk['shoulder_to_elbow']])
    l_wrist = l_elbow + np.array([-0.01, -sk['elbow_to_wrist']])
    r_wrist = r_elbow + np.array([ 0.01, -sk['elbow_to_wrist']])

    # Knees
    l_knee = l_hip + np.array([0, -sk['hip_to_knee']])
    r_knee = r_hip + np.array([0, -sk['hip_to_knee']])
    # Ankles
    l_ankle = l_knee + np.array([0, -sk['knee_to_ankle']])
    r_ankle = r_knee + np.array([0, -sk['knee_to_ankle']])

    # Order matches index legend
    joints = np.stack([
        head,      # 0
        l_shoulder,# 1
        r_shoulder,# 2
        l_elbow,   # 3
        r_elbow,   # 4
        l_wrist,   # 5
        r_wrist,   # 6
        chest,     # 7
        pelvis,    # 8
        l_hip,     # 9
        r_hip,     #10
        l_knee,    #11
        r_knee,    #12
        l_ankle,   #13
        r_ankle    #14
    ])
    return joints

def jump_motion(frac, with_weight=True):
    """
    Return all joint positions (15,2) at a frame in the jump cycle (frac: 0-1)

    - "with_weight" makes attempted jump look more effortful (arms, posture)
    - frac = 0: about to crouch; 0.2: deepest crouch; 0.4: start takeoff; 0.55: highest; 0.85: landing; 1: ready to start again
    """

    # Kinematic envelope
    joints = base_pose()

    # -- Rough jump timing (fractions of total cycle) --
    t_crouch1 = 0.18  # descend into crouch
    t_push = 0.30     # push-off (bottom to takeoff)
    t_rise = 0.47     # ascend to apex
    t_apex = 0.58     # apex of jump
    t_fall1 = 0.78    # downward flight to ground-contact
    t_land = 1.0      # return to stand

    # Predefine vertical displacement for pelvis
    if frac < t_crouch1:  # Pre-crouch: go down a bit
        pelvis_y = 0.0 - 0.12 * (frac/t_crouch1)
    elif frac < t_rise:   # Crouched, then stretching up for jump
        # Crouch to takeoff to apex: up
        #0: deepest, 1: apex
        up_phase = (frac-t_crouch1)/(t_rise-t_crouch1)
        # Pelvis up: initial crouch, then takeoff, then rising up
        pelvis_y = -0.12 + (0.12+0.24)*up_phase    # total jump ~0.24m
        if pelvis_y > 0.24:
            pelvis_y = 0.24
    elif frac < t_fall1:  # In the air; start falling
        fall_phase = (frac-t_rise)/(t_fall1-t_rise)
        pelvis_y = 0.24 - 0.21*fall_phase
    else: # Land and return to standing
        land_phase = (frac-t_fall1)/(t_land-t_fall1)
        pelvis_y = 0.03 - 0.03*land_phase

    # Shift all points vertically with pelvis (hips)
    y_shift = pelvis_y - joints[8,1]
    joints[:,1] += y_shift

    # -- Key postures for the jump --
    # Arm swing, knee bend, torso tilt, effort
    # All in biomech plausible ranges.

    # Crouch: knees forward, torso bends, arms behind
    if frac < t_crouch1:
        crouch = frac/t_crouch1
    elif frac < t_push:
        crouch = 1
    elif frac < t_rise:
        crouch = 1 - (frac-t_push)/(t_rise-t_push)
    else:
        crouch = 0

    # Arms swing: arms go back, then swing up
    # Swing timing: start at crouch, sweep up at takeoff, peak near apex
    if frac < t_push:
        arms_up = 0
    elif frac < t_apex:
        arms_up = (frac-t_push)/(t_apex-t_push)
    else:
        arms_up = 1-(frac-t_apex)/(t_land-t_apex)
    arms_up = np.clip(arms_up, 0, 1)

    # -- Motion modifiers for heavy weight (sadman wants to jump, but is weighed down) --
    # 1. Arms don't swing as high (arms_up amplitude < 1).
    # 2. Torso bends more forward (head/chest lower).
    # 3. Knees bend more in crouch.
    # 4. Jump height reduced.
    # 5. Slight foot drag in air.

    weight_arms = 0.57 if with_weight else 1.0
    weight_jump = 0.66 if with_weight else 1.0
    weight_knee = 1.2 if with_weight else 1.0
    weight_torso = 1.25 if with_weight else 1.0

    # --- Animate arms: swing back at crouch, then throw forward on takeoff ---
    # L, R: indices 1-6
    shL = joints[1][:].copy()
    shR = joints[2][:].copy()
    elL = joints[3][:].copy()
    elR = joints[4][:].copy()
    wrL = joints[5][:].copy()
    wrR = joints[6][:].copy()

    # - Shoulder: default down/side; swing = rotate at shoulder
    shoulder_angle0 = -np.pi/2  # arms down
    # Back swing (crouch): go back (shoulder behind), say -2.2rad (back-down)
    crouch_angle = -2.2
    # Up swing: arms, after takeoff, go forward-up (shoulder ~+10° front/up)
    up_angle = -np.pi/3 + (0.5*arms_up*weight_arms)
    # Interpolate: crouch->up
    shL_angle = crouch*(crouch_angle)+(1-crouch)*up_angle
    shR_angle = shL_angle + 0.06   # tiny L/R offset

    # - Elbow: flex in crouch, straighten when in air
    elbow_flex_crouch = np.deg2rad(55 +20*weight_knee) # more bend when crouched
    elbow_flex_air = np.deg2rad(22)
    elbowL_angle = (crouch)*elbow_flex_crouch + (1-crouch)*elbow_flex_air
    elbowR_angle = elbowL_angle + np.deg2rad(2) # small offset

    len_up = SKELETON['shoulder_to_elbow']
    len_lo = SKELETON['elbow_to_wrist']

    # Left arm
    elL = shL + [len_up*np.cos(shL_angle), len_up*np.sin(shL_angle)]
    wrL = elL + [len_lo*np.cos(shL_angle-elbowL_angle), len_lo*np.sin(shL_angle-elbowL_angle)]
    # Right arm
    elR = shR + [len_up*np.cos(shR_angle), len_up*np.sin(shR_angle)]
    wrR = elR + [len_lo*np.cos(shR_angle-elbowR_angle), len_lo*np.sin(shR_angle-elbowR_angle)]
    joints[3] = elL
    joints[4] = elR
    joints[5] = wrL
    joints[6] = wrR

    # --- Animate legs: knee flexion in crouch, extend on takeoff ---
    # Hip/knee/ankle: swing more when heavy, knees track forwards
    hipL = joints[9]
    hipR = joints[10]
    # Knees forward at crouch, then extend
    knee_flex_crouch = np.deg2rad(95+25*weight_knee)    # deep crouch with heavy weight
    knee_flex_air = np.deg2rad(28)                     # mid-air
    kneeL_angle = crouch*knee_flex_crouch + (1-crouch)*knee_flex_air
    kneeR_angle = kneeL_angle

    # Hip angle: torso tilts forward on crouch, rebounds upright after
    torso_angle_crouch = -np.deg2rad(38*weight_torso)
    torso_angle_air = np.deg2rad(6)
    torso_angle = crouch*torso_angle_crouch + (1-crouch)*torso_angle_air

    # Set chest (7) and head (0)
    # Chest is above pelvis at torso_angle, torso length
    pelvis = joints[8]
    chest = pelvis + [SKELETON['torso_height']*np.sin(torso_angle),
                     SKELETON['torso_height']*np.cos(torso_angle)]
    neck = chest + [0, SKELETON['chest_height']*1.0] # vertical up from chest
    head = neck + [0, SKELETON['neck']+SKELETON['head']] # vertical up
    joints[7] = chest
    joints[0] = head

    # Shoulders: at top of chest, spread left/right
    shoulders_center = neck
    shL = neck + np.array([-SKELETON['shoulder_width']/2, 0])
    shR = neck + np.array([ SKELETON['shoulder_width']/2, 0])
    joints[1] = shL
    joints[2] = shR

    # Left leg (9->11->13)
    hip_angle_L = torso_angle - np.deg2rad(4)
    k_posL = hipL + [SKELETON['hip_to_knee']*np.sin(hip_angle_L),
                  -SKELETON['hip_to_knee']*np.cos(hip_angle_L)]
    joints[11] = k_posL

    # Calculate ankle from knee and knee angle (relative)
    knee_vec_L = np.array([SKELETON['knee_to_ankle']*np.sin(hip_angle_L-kneeL_angle),
                           -SKELETON['knee_to_ankle']*np.cos(hip_angle_L-kneeL_angle)])
    a_posL = k_posL + knee_vec_L
    joints[13] = a_posL

    # Right leg (10->12->14)
    hip_angle_R = torso_angle + np.deg2rad(4)
    k_posR = hipR + [SKELETON['hip_to_knee']*np.sin(hip_angle_R),
                  -SKELETON['hip_to_knee']*np.cos(hip_angle_R)]
    joints[12] = k_posR

    knee_vec_R = np.array([SKELETON['knee_to_ankle']*np.sin(hip_angle_R-kneeR_angle),
                           -SKELETON['knee_to_ankle']*np.cos(hip_angle_R-kneeR_angle)])
    a_posR = k_posR + knee_vec_R
    joints[14] = a_posR

    # -- Optional: Feet dragging when heavy, slight up lag on takeoff, down on land
    if with_weight:
        foot_drag = max(0, 0.11 - abs(0.5-frac))
        joints[13,1] -= foot_drag*0.08
        joints[14,1] -= foot_drag*0.08

    # Final jump scale
    center_x = 0.0
    overall_scale = 1.7
    jump_y = -0.19*SKELETON['torso_height']
    joints[:,0] = overall_scale * (joints[:,0] - center_x)
    joints[:,1] = overall_scale * (joints[:,1] + jump_y) * weight_jump + (1-weight_jump)*joints[:,1]

    return joints

# --- Animation code ---

fig, ax = plt.subplots(figsize=(3,6), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

NUM_POINTS = 15
POINT_SIZE = 96

# For "fixed" ground
GROUND_Y = -1.85

# Set axes ranges (meters, roughly)
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-2.2, 0.9)

# Draw point-lights
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Draw bones for context (optional, dashed so as not to distract)
bones_artists = []
for (i0, i1) in BONES:
    ln, = ax.plot([],[], color='white', lw=0.7, alpha=0.10, linestyle='-')
    bones_artists.append(ln)

# Draw "ground"
ground_line, = ax.plot([-1,1],[GROUND_Y,GROUND_Y],'w-',lw=1, alpha=0.16)

def animate(frame):
    # Cycle smoothly (slow, for realism)
    loop_frames = 50
    frac = (frame % loop_frames) / loop_frames

    joints = jump_motion(frac, with_weight=True)
    xs, ys = joints[:,0], joints[:,1]

    # Points
    points.set_data(xs, ys)

    # Bones
    for (i,(j0,j1)) in enumerate(BONES):
        bx = [xs[j0], xs[j1]]
        by = [ys[j0], ys[j1]]
        bones_artists[i].set_data(bx,by)

    return [points] + bones_artists + [ground_line]

ani = animation.FuncAnimation(fig, animate, frames=300, interval=28, blit=True)
plt.show()
