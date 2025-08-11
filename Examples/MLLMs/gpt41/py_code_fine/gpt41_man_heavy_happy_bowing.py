
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 point body model (happyman) -- keypoints
# Based on Johansson's biological motion model, example image, and bowing action

# Keypoint indices:
# 0: Head
# 1,2: Shoulders (L, R)
# 3,4: Elbows (L, R)
# 5,6: Hands (L, R)
# 7,8: Hips (L, R)
# 9,10: Knees (L, R)
# 11,12: Feet (L, R)
# 13,14: "Heavy weight" (L, R) in hands

# Basic skeleton definition (static pose, anatomical directions)
BASE = {
    0:  np.array([0,  6.2]),      # Head (center)
    1:  np.array([-1, 5.4]),      # Left shoulder
    2:  np.array([1, 5.4]),       # Right shoulder
    3:  np.array([-2, 4.0]),      # Left elbow
    4:  np.array([2, 4.0]),       # Right elbow
    5:  np.array([-2.5, 2.7]),    # Left hand
    6:  np.array([2.5, 2.7]),     # Right hand
    7:  np.array([-1, 3.5]),      # Left hip
    8:  np.array([1, 3.5]),       # Right hip
    9:  np.array([-1, 1.75]),     # Left knee
    10: np.array([1, 1.75]),      # Right knee
    11: np.array([-1.2, 0.2]),    # Left foot
    12: np.array([1.2, 0.2]),     # Right foot
    13: np.array([-3.1, 2.5]),    # Left weight (in hand)
    14: np.array([3.1, 2.5]),     # Right weight (in hand)
}

# Limb definitions (for future construction)
LIMBS = [
    (0,1),(0,2),(1,3),(3,5),(2,4),(4,6),
    (1,7),(2,8),(7,8),
    (7,9),(9,11),(8,10),(10,12),
    (5,13),(6,14)
]

# Return joint positions for given bow angle (anim_param in [0,1]):
def bowing_joint_positions(anim_param):
    # anim_param: 0 to 1; 0: upright, 1: max bow
    
    # Bow parameters
    bow_angle_max = np.radians(65) # Maximum trunk bow (from vertical)
    bow_angle = bow_angle_max * anim_param

    # Pelvis (hips) stays about the same place, but trunk/head rotate forward
    pelvis = (BASE[7] + BASE[8]) / 2
    pelvis_y = pelvis[1] + 0.10*np.sin(anim_param*np.pi)  # small updown motion

    # Define a local coordinate "trunk": origin=pelvis, y-up is back, x lateral
    # Rotation is about the hip (pelvis)
    def rotate(p, angle):
        """Rotate point around pelvis by angle [rads]"""
        R = np.array([[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle),  np.cos(angle)]])
        return pelvis + R @ (p - pelvis)

    # Move upper body points (head, shoulders, elbows, hands) around pelvis
    model = {}

    # Torso: rotate head, shoulders, elbows, hands collectively
    for k in [0,1,2,3,4,5,6]:
        model[k] = rotate(BASE[k], -bow_angle)  # negative=bow forward

    # Sway the head/shoulder area slightly down as the bow proceeds
    for k in [0,1,2]:
        model[k][1] -= 0.15 * anim_param

    # The hips remain largely at their base (with a slight vertical displacement)
    model[7] = np.array([BASE[7][0], pelvis_y])
    model[8] = np.array([BASE[8][0], pelvis_y])

    # Legs: gently flex at knees/ankles as part of bowing
    knee_flex = np.radians(15) * anim_param
    ankle_flex = np.radians(8) * anim_param

    # Left leg
    hip = model[7]
    thigh = BASE[9] - BASE[7]
    thigh_len = np.linalg.norm(thigh)
    knee_angle = knee_flex
    # knee
    thigh_vec = np.array([0, -1]) * thigh_len  # downward
    thigh_vec = rotate_vec(thigh_vec, knee_angle)
    model[9] = hip + thigh_vec

    # foot
    shank = BASE[11] - BASE[9]
    shank_len = np.linalg.norm(shank)
    shank_angle = ankle_flex
    shank_vec = np.array([0, -1]) * shank_len  # downward
    shank_vec = rotate_vec(shank_vec, knee_angle + shank_angle)
    model[11] = model[9] + shank_vec

    # Right leg
    hip = model[8]
    # knee
    thigh_vec = np.array([0, -1]) * thigh_len
    thigh_vec = rotate_vec(thigh_vec, knee_angle)
    model[10] = hip + thigh_vec

    # foot
    shank_vec = np.array([0, -1]) * shank_len
    shank_vec = rotate_vec(shank_vec, knee_angle + shank_angle)
    model[12] = model[10] + shank_vec

    # HANDS/WEIGHTS: The hands carry a "heavy weight" that drags the shoulder/elbow/hand line a bit lower and forward as the bow progresses.
    # Let the weight be attached to each hand, slightly forward, with some swinging motion depending on bow and time.
    for i, kh, kw in [(5, 13, BASE[13]), (6, 14, BASE[14])]:
        # Place weight slightly forward and lower compared to hand
        dvec = model[kh] - pelvis
        dvec = dvec / np.linalg.norm(dvec)
        weight_offset = 0.6 * dvec - np.array([0, 0.35 + 0.12*anim_param])  # slightly forward and down
        # Also add a small swinging motion
        swing_mag = 0.13 * anim_param
        swing = swing_mag * np.sin(anim_param * np.pi * 2)
        weight_pos = model[kh] + weight_offset + np.array([swing * (-1 if i==5 else +1), 0])
        model[kw] = weight_pos

    return np.stack([model[i] for i in range(15)])

def rotate_vec(vec, angle):
    c,s = np.cos(angle), np.sin(angle)
    return np.array([c*vec[0]-s*vec[1], s*vec[0]+c*vec[1]])

# Animation function
def animate_bowing():
    # Prepare canvas
    fig, ax = plt.subplots(figsize=(3.5,6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor("black")
    plt.axis('equal')
    plt.axis('off')
    ax.set_xlim(-4.1, 4.1)
    ax.set_ylim(-0.5, 7.0)

    # Draw 15 point-lights as white circles
    pts, = ax.plot([], [], 'wo', ms=8)
    
    # For smooth loop, bow down and up
    n_frames = 70
    def get_param(f):
        # f in [0, ..., n_frames-1]
        t = f / n_frames
        return 0.5 - 0.5 * np.cos(t * 2 * np.pi)  # cosine ease in/out

    # Animation function
    def update(frame):
        anim_param = get_param(frame)
        pos = bowing_joint_positions(anim_param)
        pts.set_data(pos[:,0], pos[:,1])
        return pts,

    ani = animation.FuncAnimation(
        fig, update, frames=n_frames, interval=30, blit=True
    )

    plt.show()

if __name__ == '__main__':
    animate_bowing()
