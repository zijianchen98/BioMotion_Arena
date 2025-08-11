
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of frames for one running cycle
N_FRAMES = 60

# 15 marker points (same general model as example image)
# 0: Head
# 1-2: Shoulders (L,R)
# 3-4: Elbows
# 5-6: Wrists
# 7-8: Hips
# 9-10: Knees
# 11-12: Ankles
# 13-14: Feet

# Segment lengths (longer/shorter to suggest 'heavy' woman)
#             Torso   UpperArm  ForeArm   Thigh   Shin   Foot
L_torso   = .24      # Head to hip
L_shoul   = .23      # Shoulder-to-shoulder
L_hip     = .13      # Hip width
L_uarm    = .13      # Upper arm
L_larm    = .13      # Forearm (a bit stubbier)
L_thigh   = .19
L_shin    = .165
L_foot    = .10

# Offsets and proportions (to subtly suggest 'happy' & 'heavy'):
smile_lift = .018  # head bob + smile
shoulder_bounce = .014  # happy bounce

# Root (hip midpoint) goes (X,Y) across the screen:
def hip_trajectory(frame):
    t = frame / N_FRAMES * 2 * np.pi
    speed = 1.4  # m/s 
    amplitude = 0.20
    y_base = 0.27
    y = y_base + amplitude*0.07*np.sin(2*t)
    x = 0.15 + 0.45 * (frame / N_FRAMES)
    return np.array([x, y])

# Limb angles (simple sinusoidal model for running)
def joint_angles(side, frame):
    t = frame / N_FRAMES * 2 * np.pi
    # phase per side (L, R alternates)
    ph = 0 if side=='L' else np.pi
    # Arm swing
    sh_ang = np.deg2rad(45) * np.sin(t+ph)
    el_ang = np.deg2rad(32) * np.sin(t+ph-np.pi/8)
    # Leg movement (larger for heavy running, knees higher, ankles lower)
    hip_ang = np.deg2rad(40) * np.sin(t+ph+np.pi/5)
    knee_ang = np.deg2rad(66) * abs(np.sin(t+ph+np.pi/6))
    ankle_ang = np.deg2rad(15) * np.sin(1.5*t+ph+np.pi/4)
    return sh_ang, el_ang, hip_ang, knee_ang, ankle_ang

# Stick figure function
def get_marker_positions(frame):
    pos = np.zeros((15,2))
    hip_c = hip_trajectory(frame)

    # Torso and head
    # Hip midpoint: points 7,8 average
    L_R_HIP = hip_c + np.array([-L_hip/2, 0])
    R_R_HIP = hip_c + np.array([ L_hip/2, 0])
    pos[7] = L_R_HIP
    pos[8] = R_R_HIP

    # Shoulder mid (above hip)
    torso_dx = 0; torso_dy = L_torso
    shoulder_c = hip_c + np.array([torso_dx, torso_dy])
    # For "happy bounce", shoulders bob side-to-side
    shoulder_c[0] += shoulder_bounce * np.sin(2*np.pi*frame/N_FRAMES)
    # Shoulders
    L_SHOULDER = shoulder_c + np.array([-L_shoul/2,0])
    R_SHOULDER = shoulder_c + np.array([ L_shoul/2,0])
    pos[1] = L_SHOULDER
    pos[2] = R_SHOULDER

    # Head (above midpoint of shoulders)
    head_top = shoulder_c + np.array([0, 0.087+smile_lift*np.sin(2*np.pi*frame/N_FRAMES)])
    pos[0] = head_top

    # Left arm
    l_sh_ang, l_el_ang, *_ = joint_angles('L', frame)
    l_elb = L_SHOULDER + [ L_uarm*np.sin(l_sh_ang), -L_uarm*np.cos(l_sh_ang)]
    pos[3] = l_elb
    l_wrist = l_elb + [ L_larm*np.sin(l_sh_ang+l_el_ang), -L_larm*np.cos(l_sh_ang+l_el_ang)]
    pos[5] = l_wrist

    # Right arm
    r_sh_ang, r_el_ang, *_ = joint_angles('R', frame)
    r_elb = R_SHOULDER + [ L_uarm*np.sin(r_sh_ang), -L_uarm*np.cos(r_sh_ang)]
    pos[4] = r_elb
    r_wrist = r_elb + [ L_larm*np.sin(r_sh_ang+r_el_ang), -L_larm*np.cos(r_sh_ang+r_el_ang)]
    pos[6] = r_wrist

    # Left leg
    _, _, l_hip_ang, l_knee_ang, l_ankle_ang = joint_angles('L', frame)
    l_knee = L_R_HIP + [ L_thigh*np.sin(l_hip_ang), -L_thigh*np.cos(l_hip_ang)]
    pos[9] = l_knee
    l_ankle = l_knee + [ L_shin*np.sin(l_hip_ang+l_knee_ang), -L_shin*np.cos(l_hip_ang+l_knee_ang)]
    pos[11] = l_ankle
    l_foot = l_ankle + [ L_foot*np.sin(l_hip_ang+l_knee_ang+l_ankle_ang), -L_foot*np.cos(l_hip_ang+l_knee_ang+l_ankle_ang)]
    pos[13] = l_foot

    # Right leg
    _, _, r_hip_ang, r_knee_ang, r_ankle_ang = joint_angles('R', frame)
    r_knee = R_R_HIP + [ L_thigh*np.sin(r_hip_ang), -L_thigh*np.cos(r_hip_ang)]
    pos[10] = r_knee
    r_ankle = r_knee + [ L_shin*np.sin(r_hip_ang+r_knee_ang), -L_shin*np.cos(r_hip_ang+r_knee_ang)]
    pos[12] = r_ankle
    r_foot = r_ankle + [ L_foot*np.sin(r_hip_ang+r_knee_ang+r_ankle_ang), -L_foot*np.cos(r_hip_ang+r_knee_ang+r_ankle_ang)]
    pos[14] = r_foot

    # Now, markers for the trunk (4 points = sternum, stomach, 2 sides for chest/abdomen)
    # Chest center: between shoulders, down a bit (sternum)
    sternum = shoulder_c + np.array([0, -0.05])
    pos[3] = sternum  # over-write left elbow, but we want this marker included
    # Belly (lower torso, hint of bulge)
    belly = hip_c + np.array([0, .034])
    pos[4] = belly    # over-write right elbow

    # Two lateral trunk: in between, horizontal deviation
    pos[5] = shoulder_c + np.array([-0.07, -0.020])  # L lateral trunk
    pos[6] = shoulder_c + np.array([ 0.07, -0.020])  # R lateral trunk

    return pos

# Set up the figure
fig, ax = plt.subplots(figsize=(4,8))
ax.set_facecolor('black')
plt.axis('off')
ln, = plt.plot([], [], 'wo', ms=10)  # White points

# Animation function
def animate(frame):
    pts = get_marker_positions(frame % N_FRAMES)
    ln.set_data(pts[:,0], pts[:,1])
    return ln,

# Set axis limits to encompass all running motion:
ax.set_xlim(0,0.75)
ax.set_ylim(0,0.75)
ax.set_aspect('equal')

ani = animation.FuncAnimation(fig, animate, frames=240, interval=1000/60, blit=True)

plt.show()
