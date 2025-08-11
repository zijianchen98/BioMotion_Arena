
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define point indices for 15-point biological motion figure:
# 0: Head
# 1-2: Shoulders (L/R)
# 3-4: Elbows (L/R)
# 5-6: Wrists (L/R)
# 7: Torso (pelvis, center)
# 8-9: Hips (L/R)
# 10-11: Knees (L/R)
# 12-13: Ankles (L/R)
# 14: Chest (upper torso center)

# Base skeleton (Y increases upwards)
SKELETON_OFFSETS = np.array([
    [ 0.0,  1.75], # 0 Head
    [-0.25, 1.50], # 1 L Shoulder
    [ 0.25, 1.50], # 2 R Shoulder
    [-0.45, 1.10], # 3 L Elbow
    [ 0.45, 1.10], # 4 R Elbow
    [-0.55, 0.75], # 5 L Wrist
    [ 0.55, 0.75], # 6 R Wrist
    [ 0.0,  1.00], # 7 Pelvis
    [-0.15, 1.00], # 8 L Hip
    [ 0.15, 1.00], # 9 R Hip
    [-0.17, 0.55], #10 L Knee
    [ 0.17, 0.55], #11 R Knee
    [-0.18, 0.10], #12 L Ankle
    [ 0.18, 0.10], #13 R Ankle
    [ 0.0,  1.60], #14 Chest
])

# Heavier figure: make joints a bit further from center/torso thicker
HEAVY_SCALE = np.array([
    [ 0.00, 0.00], # head no change
    [-0.32, 0.00], # L shoulder broader
    [ 0.32, 0.00], # R shoulder broader
    [-0.52, 0.00], # elbows farther
    [ 0.52, 0.00],
    [-0.66, 0.00], # wrists wider apart
    [ 0.66, 0.00],
    [ 0.00, 0.00], # pelvis center
    [-0.23, 0.00], # L hip wider
    [ 0.23, 0.00], # R hip wider
    [-0.30, 0.00], # L knee
    [ 0.30, 0.00], # R knee
    [-0.36, 0.00], # L ankle
    [ 0.36, 0.00], # R ankle
    [ 0.00, 0.00], # chest no change
])

# Motion parameters
n_frames = 80
fps = 30
dt = 1.0 / fps
t = np.linspace(0, 1, n_frames)

# Jumping forward: hop motion with raising/falling CoM, swinging arms
def get_frame(jump_prog):
    # Center-of-mass vertical trajectory (parabolic jump) and horizontal displacement
    jump_height = 0.50 # meters
    jump_length = 1.0 # meters
    y0 = 0.0 # base ground level

    # Vertical CoM (parabola: jump up then down)
    phase = jump_prog * 2 * np.pi
    y_offset = y0 + jump_height*np.sin(np.pi*jump_prog)

    # Forward (to the right) horizontal movement: begin at x=0
    x_offset = -0.3 + jump_length*jump_prog
    
    # Bounces: Arms up during takeoff, legs bent before, arms swing up and legs extend during apex
    # To exaggerate: at heavy weight, motion is extra bouncy.
    # Key phases: crouch (0), takeoff (0.1), apex (0.5), landing (0.9), land (1)
    # Smooth movements: interpolate with sinusoids

    # Torso lean (forward lean at takeoff/landing)
    torso_angle = 0.10 * np.sin(phase-np.pi/2)

    # Legs bend at crouch/landing
    leg_bend = 0.50 * np.cos(phase)
    left_knee_offset = 0.13 * (1-np.sin(phase/2)) # more bent at landing
    right_knee_offset = 0.11 * (1-np.sin(phase/2 + 0.7))
    left_ankle_y = 0.08 * (1-np.sin(phase/2 + 0.4))
    right_ankle_y = 0.07 * (1-np.sin(phase/2 + 1.2))

    # Arms swing: up at takeoff, forward at apex, down at landing
    # Shoulders rotate arms up and out
    LARM = 1.0 - 0.6*np.cos(phase)
    RARM = 1.0 - 0.7*np.cos(phase + np.pi/7)
    lelbow_y = 1.36 + 0.16*LARM
    relbow_y = 1.36 + 0.16*RARM
    lwrist_y = 1.13 + 0.20*LARM
    rwrist_y = 1.13 + 0.20*RARM
    lelbow_x = -0.52 - 0.27*np.cos(phase-1.0)
    relbow_x = 0.52 + 0.27*np.cos(phase+1.0)
    lwrist_x = -0.66 - 0.37*np.cos(phase-1.5)
    rwrist_x = 0.66 + 0.37*np.cos(phase+1.5)

    # Head bob
    head_y = 1.73 + 0.03*np.sin(phase-0.2)
    head_x = 0.0 + 0.027*np.sin(phase+0.9)

    # Shoulders: raise a bit at takeoff
    sh_raise = 0.03*np.sin(phase)
    lshoulder_x = -0.32 - 0.01*np.cos(phase)
    rshoulder_x = 0.32 + 0.01*np.cos(phase)
    lshoulder_y = 1.54 + sh_raise
    rshoulder_y = 1.54 + sh_raise

    # Chest, pelvis slight rise/fall, sway for happiness
    chest_x = 0.0 + 0.012*np.sin(phase+2.6)
    chest_y = 1.61 + 0.025*np.sin(phase+1.7)
    pelvis_x = .00+0.015*np.sin(phase+2.6)
    pelvis_y = 1.02 + 0.05*np.sin(phase+0.6)
    lhip_x = -0.23 - 0.017*np.cos(phase)
    rhip_x =  0.23 + 0.015*np.cos(phase)
    lhip_y = 1.01 + 0.01*np.sin(phase+1.2)
    rhip_y = 1.01 + 0.01*np.sin(phase+0.9)

    # Knees, ankles more bent at crouch and landing
    lknee_x = -0.28 - left_knee_offset
    rknee_x = 0.28 + right_knee_offset
    lknee_y = 0.63 - 0.06*np.cos(phase)
    rknee_y = 0.63 - 0.09*np.cos(phase)
    lankle_x = -0.36 - 0.09*np.cos(phase + 0.4)
    rankle_x = 0.36 + 0.08*np.cos(phase + 1.3)
    lankle_y = 0.12 + left_ankle_y
    rankle_y = 0.12 + right_ankle_y

    # Compose all marker positions
    p = np.zeros((15,2))
    # Head
    p[0] = [head_x, head_y]
    # L, R Shoulders
    p[1] = [lshoulder_x, lshoulder_y]
    p[2] = [rshoulder_x, rshoulder_y]
    # L, R Elbows
    p[3] = [lelbow_x, lelbow_y]
    p[4] = [relbow_x, relbow_y]
    # L, R Wrists
    p[5] = [lwrist_x, lwrist_y]
    p[6] = [rwrist_x, rwrist_y]
    # Pelvis
    p[7] = [pelvis_x, pelvis_y]
    # L, R Hip
    p[8] = [lhip_x, lhip_y]
    p[9] = [rhip_x, rhip_y]
    # L, R Knee
    p[10] = [lknee_x, lknee_y]
    p[11] = [rknee_x, rknee_y]
    # L, R Ankle
    p[12] = [lankle_x, lankle_y]
    p[13] = [rankle_x, rankle_y]
    # Chest
    p[14] = [chest_x, chest_y]
    
    # Add happy subtle bouncing: vertical oscillation
    happy_bounce = 0.012*np.sin(4*phase)
    p[:,1] += happy_bounce

    # "Forward" movement: shift all x/y by jump position
    p[:,0] += x_offset
    p[:,1] += y_offset

    return p

# Animation
fig = plt.figure(figsize=(4.2,7.5), facecolor='black')
ax = plt.gca()
plt.axis('off')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-0.6, 1.25)
ax.set_ylim(-0.15, 2.2)

points, = ax.plot([], [],
                  'o',
                  color='white',
                  markersize=10, # increase for better visualization
                  markeredgewidth=0)

def init():
    points.set_data([], [])
    return (points,)

def animate(i):
    jump_prog = (i % n_frames) / n_frames
    p = get_frame(jump_prog)
    points.set_data(p[:,0], p[:,1])
    return (points,)

ani = FuncAnimation(fig, animate, frames=n_frames, interval=1000*dt, blit=True, init_func=init)

plt.show()
