
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint order (top to bottom, symmetrical around midline for biological motion)
# 15 Points: Head, L&R Shoulder, L&R Elbow, L&R Wrist, Chest, Hip, L&R Knee, L&R Ankle, L&R Foot
JOINT_NAMES = [
    'head', 'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow', 'l_wrist', 'r_wrist',
    'chest', 'pelvis', 'l_hip', 'r_hip', 'l_knee', 'r_knee', 'l_ankle', 'r_ankle'
]

# Skeleton: list of [parent, child] for reference (not used for display but helps parametrize motion)
SKELETON = [
    ('head', 'chest'), ('chest', 'l_shoulder'), ('chest', 'r_shoulder'),
    ('l_shoulder', 'l_elbow'), ('r_shoulder', 'r_elbow'),
    ('l_elbow', 'l_wrist'), ('r_elbow', 'r_wrist'),
    ('chest', 'pelvis'), ('pelvis', 'l_hip'), ('pelvis', 'r_hip'),
    ('l_hip', 'l_knee'), ('r_hip', 'r_knee'), ('l_knee', 'l_ankle'), ('r_knee', 'r_ankle')
]

# "Neutral" body configuration in standing pose (in image coordinates, approx)
# Units: arbitrary, adapted to fit [0,1] for both axes in plot
JOINT_OFFSETS = {
    'head':      np.array([0.0, 1.00]),
    'chest':     np.array([0.0, 0.90]),
    'pelvis':    np.array([0.0, 0.68]),
    'l_shoulder':np.array([-0.10, 0.93]),
    'r_shoulder':np.array([+0.10, 0.93]),
    'l_elbow':   np.array([-0.20, 0.82]),
    'r_elbow':   np.array([+0.20, 0.82]),
    'l_wrist':   np.array([-0.25, 0.72]),
    'r_wrist':   np.array([+0.25, 0.72]),
    'l_hip':     np.array([-0.08, 0.68]),
    'r_hip':     np.array([+0.08, 0.68]),
    'l_knee':    np.array([-0.10, 0.46]),
    'r_knee':    np.array([+0.10, 0.46]),
    'l_ankle':   np.array([-0.11, 0.24]),
    'r_ankle':   np.array([+0.11, 0.24])
}

# For a 'sitting down' action, specify joint angles over T frames
FRAMES = 60
FPS = 30

# Movement parameterization
def sitting_down_motion(t, total_frames):
    """Returns dict of joint positions at frame t (0..total_frames-1) for 'sitting down'."""
    # Sit progress (0=stand, 1=sit)
    progress = (t / (total_frames - 1))
    progress = np.clip(progress, 0, 1)
    # This progress curve makes it smooth at start/end
    progress = 0.5 * (1 - np.cos(np.pi * progress))

    # Main trunk downward and back shift
    chest_y = 0.90 - 0.28 * progress
    pelvis_y = 0.68 - 0.18 * progress
    chest_x = 0.0 - 0.06 * progress     # slight backward shift for biomechanical plausibility
    pelvis_x = 0.0 - 0.08 * progress

    # Legs bend at hip/knee/ankle
    hip_angle = np.deg2rad(10 + 85*progress)      # from 10° (standing) to ~95° (sitting)
    knee_angle = np.deg2rad(4 + 95*progress)      # from 4° to ~99°
    ankle_angle = np.deg2rad(-5 + 12*progress)    # from -5° to 7° (slight dorsiflexion)

    # Arms: happy/energetic: hands move a bit up/swing out
    shoulder_angle = np.deg2rad(-12 + 45*progress)   # relative to downwards, swing outward a bit
    elbow_angle = np.deg2rad(10 + 55*progress)       # bent more w/ movement
    wrist_lift = 0.03 * np.sin(np.pi * progress)     # a "happy" lift at midpoint

    # Helper: joint positions, filled in
    pos = {}

    # Pelvis
    pos['pelvis'] = np.array([pelvis_x, pelvis_y])

    # Chest is above pelvis (spine)
    spine_vec = np.array([chest_x - pelvis_x, chest_y - pelvis_y])
    spine_len = np.linalg.norm(spine_vec)
    spine_dir = spine_vec / (spine_len + 1e-8)
    # On initial frame: spine is vert, len ~0.22
    pos['chest'] = pos['pelvis'] + spine_dir * 0.22

    # Head above chest (always vertical up, very short "neck")
    head = pos['chest'] + np.array([0, 0.10])
    # For 'happy', bob head a bit
    head = head + np.array([0.00, 0.01*np.sin(np.pi*progress)])
    pos['head'] = head

    # Shoulders (outwards left/right from chest)
    sh_span = 0.21
    sh_angle = np.deg2rad(0)    # should line up with x axis even as trunk leans
    sh_x_off = sh_span/2 * np.cos(sh_angle)
    sh_y_off = sh_span/2 * np.sin(sh_angle)
    pos['l_shoulder'] = pos['chest'] + np.array([-sh_x_off, sh_y_off])
    pos['r_shoulder'] = pos['chest'] + np.array([+sh_x_off, sh_y_off])

    # Hips (below pelvis, slightly outward)
    hip_span = 0.16
    pos['l_hip'] = pos['pelvis'] + np.array([-hip_span/2, 0])
    pos['r_hip'] = pos['pelvis'] + np.array([+hip_span/2, 0])

    # Left Arm (shoulder -> elbow -> wrist)
    sh = pos['l_shoulder']
    # Shoulder to elbow
    upper_len = 0.135
    th = np.pi/2 + shoulder_angle + 0.10             # out from shoulder, a bit forward
    el = sh + upper_len * np.array([np.cos(th), np.sin(th)])
    pos['l_elbow'] = el
    # Elbow to wrist
    fore_len = 0.135
    el_th = th - elbow_angle
    wr = el + fore_len * np.array([np.cos(el_th), np.sin(el_th)])
    wr[1] += wrist_lift  # lift wrist out for "happy"
    pos['l_wrist'] = wr

    # Right Arm (mirrored)
    sh = pos['r_shoulder']
    th = np.pi/2 - shoulder_angle - 0.10
    el = sh + upper_len * np.array([np.cos(th), np.sin(th)])
    pos['r_elbow'] = el
    el_th = th + elbow_angle
    wr = el + fore_len * np.array([np.cos(el_th), np.sin(el_th)])
    wr[1] += wrist_lift
    pos['r_wrist'] = wr

    # LEFT Leg (pelvis->knee->ankle)
    phip = pos['l_hip']
    # Hip to knee
    upper_leg = 0.22
    # Hip angle: from vertical downward, trunk is leaning backward slightly!
    thigh_angle = -np.pi/2 + hip_angle - (progress*0.22)
    knee = phip + upper_leg * np.array([np.cos(thigh_angle), np.sin(thigh_angle)])
    pos['l_knee'] = knee
    # Knee to ankle
    lower_leg = 0.21
    shank_angle = thigh_angle + knee_angle
    ank = knee + lower_leg * np.array([np.cos(shank_angle), np.sin(shank_angle)])
    pos['l_ankle'] = ank

    # RIGHT Leg (pelvis->knee->ankle)
    phip = pos['r_hip']
    thigh_angle = -np.pi/2 + hip_angle - (progress*0.22)
    knee = phip + upper_leg * np.array([np.cos(thigh_angle), np.sin(thigh_angle)])
    pos['r_knee'] = knee
    shank_angle = thigh_angle + knee_angle
    ank = knee + lower_leg * np.array([np.cos(shank_angle), np.sin(shank_angle)])
    pos['r_ankle'] = ank

    # Return all 15 joints as numpy array (x, y) in correct order
    coords = []
    for name in JOINT_NAMES:
        coords.append(pos[name])
    return np.array(coords)

# Prepare animation frames
frames = [sitting_down_motion(t, FRAMES) for t in range(FRAMES)]

# Set up plot
fig, ax = plt.subplots(figsize=(3.5, 5.5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.45, 0.45)
ax.set_ylim(0.02, 1.13)
ax.set_aspect('equal')
ax.axis('off')

# Draw points
points, = ax.plot([], [], 'wo', ms=13)  # white circles, size matches reference image

# Animation update function
def animate(i):
    d = frames[i]
    points.set_data(d[:,0], d[:,1])
    return points,

# Animate!
ani = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS, blit=True, repeat=True)

plt.show()
