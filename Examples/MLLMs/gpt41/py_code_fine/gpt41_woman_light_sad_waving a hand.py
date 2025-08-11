
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Skeleton Model (Female, Sad Posture) ---

# Each point: [name, parent_index, (x,y) offset at rest]
# Units are arbitrary; coordinates are for constructing the initial pose.
# Indices:
# 0 Head, 1 Neck, 2 RShoulder, 3 LShoulder, 4 RElbow, 5 LElbow,
# 6 RWrist, 7 LWrist, 8 Torso, 9 RHip, 10 LHip, 11 RKnee, 12 LKnee, 13 RAnkle, 14 LAnkle

JOINTS = [
    ("Head",    1, np.array([ 0.,   12.])),  # 0
    ("Neck",    8, np.array([ 0.,    9.])),  # 1
    ("RShoulder",1, np.array([ 1.5,  9.])),  # 2
    ("LShoulder",1, np.array([-1.5,  9.])),  # 3
    ("RElbow",   2, np.array([ 2.5,  7.])),  # 4
    ("LElbow",   3, np.array([-2.5,  7.])),  # 5
    ("RWrist",   4, np.array([ 3.5,  5.])),  # 6
    ("LWrist",   5, np.array([-2.5,  5.])),  # 7
    ("Torso",   9, np.array([ 0.,    5.])),  # 8
    ("RHip",    8, np.array([ 0.8,   5.])),  # 9
    ("LHip",    8, np.array([-0.8,   5.])),  #10
    ("RKnee",   9, np.array([ 1.,    2.3])), #11
    ("LKnee",  10, np.array([-1.,   2.3])),  #12
    ("RAnkle", 11, np.array([ 1.1,   0.])),  #13
    ("LAnkle", 12, np.array([-1.1,   0.])),  #14
]

# -- Parameters for animation --

FPS = 40         # frames per second
DURATION = 4     # seconds
NFRAMES = int(FPS * DURATION)

# Biological parameters for biomechanics (motion ranges, freq, etc.),
# for a subtle, sad, light-weighted female waving with left hand.

def get_joint_positions(t):
    # t: time in seconds

    # SAD posture: Head down, torso and hips a bit slouched,
    # all joints held slightly lower, shoulders "drooped", no excessive motion EXCEPT left arm.
    # Waving: Only the LEFT arm (indices 3 (shoulder), 5 (elbow), 7 (wrist)) moves actively.

    base = np.array([
        [ 0 , 12],       # Head
        [ 0 ,  9],       # Neck
        [ 1.5, 9],       # RShoulder
        [-1.5, 9],       # LShoulder
        [ 2.4, 7],       # RElbow
        [-2.6, 7],       # LElbow -- will wave
        [ 3.1, 5.4],     # RWrist
        [-2.6, 5],       # LWrist -- will wave
        [ 0 ,  5],       # Torso
        [ 0.8, 5],       # RHip
        [-0.8, 5],       # LHip
        [ 0.9, 2.2],     # RKnee
        [-1.1,2.15],     # LKnee
        [ 1.0, 0.2],     # RAnkle
        [-1.1, 0.1],     # LAnkle
    ])
    # Apply global translation for figure's 'sadness'
    base[:,1] -= 1.5  # Compress vertically

    # Head/neck drop, rounded shoulder
    base[0,1] -= 0.5  # head lower
    base[1,1] -= 0.4  # neck lower
    base[2,1] -= 0.25 # RShoulder drop
    base[3,1] -= 0.32 # LShoulder more drooped

    # Add slight body bob (lightweight sad affect: body "weighted downward")
    bob = 0.10 * np.sin(2*np.pi*t/1.8)
    base[:,1] += bob

    # -- Animate ARM WAVE: left arm (shoulder 3, elbow 5, wrist 7) --
    # Model the shoulder, elbow and wrist joints as a simple 2-link (upper/lower arm),
    # with shoulder rotating a bit, more pronounced elbow motion, wrist accentuates wave.
    # Wave phase: slow, small, underarm (sad).
    # We'll wave with left arm (the subject's left == our right on plot).

    # Parameters
    upper_arm = 2.3   # shoulder->elbow
    fore_arm  = 2.0   # elbow->wrist

    # Shoulder origin
    lshoulder = base[3].copy()

    # Waving: (l-arm moves in a mostly y-plane "wave" with some flexion/extension)
    freq = 0.8   # slower wave (low affect)
    phase = (2*np.pi*freq*t)
    wave_angle = np.deg2rad(60) + 0.23*np.sin(phase)  # up; neutral plus small up/down
    elbow_angle = -np.deg2rad(70) + 0.37*np.sin(phase+0.8)  # mostly extended, slight curve
    wrist_off_angle = 0.27*np.sin(3*phase+1.3)   # repeated wrist bends

    # Arm rotates downward (sad) and more forward
    # Shoulder angle is w.r.t vertical downward (so -90° = up, 0 = sideways, +90° = down)
    angle0 = -np.pi/2 + wave_angle - 0.28  # a bit below horizontal

    # Elbow pos
    lelbow = lshoulder + upper_arm * np.array([np.cos(angle0), np.sin(angle0)])
    # Wrist pos
    angle1 = angle0 + elbow_angle
    lwrist = lelbow + fore_arm * np.array([np.cos(angle1), np.sin(angle1)])
    # Tiny wrist waggle for lifelike effect:
    lwrist += 0.22 * np.array([np.cos(angle1 + wrist_off_angle), np.sin(angle1 + wrist_off_angle)])

    # Apply to skeleton
    base[5] = lelbow
    base[7] = lwrist

    # Animate light rocking for "sadness"
    sad_slouch = 0.18 * np.sin(2*np.pi*t/2)
    base[8:,0] -= sad_slouch  # hips, knees, ankles

    # For lightness, add a slight random "tremble" to hand and wrist points
    np.random.seed(int(t*100)%10000)
    tremble = 0.06 * (np.random.rand(2)-0.5)
    base[7] += tremble

    # Animate very slightly the right hand for realism (less than the left!)
    # Model with small elbow and wrist flexion
    rshoulder = base[2]
    rupper_arm = 2.3
    rfore_arm = 1.7
    rangle0 = np.pi + 0.1*np.sin(phase/2)
    relbow = rshoulder + rupper_arm * np.array([np.cos(rangle0), np.sin(rangle0)])
    rangle1 = rangle0 - 0.15 + 0.12*np.sin(phase/1.7+2)
    rwrist = relbow + rfore_arm * np.array([np.cos(rangle1), np.sin(rangle1)])
    base[4] = relbow
    base[6] = rwrist

    # And a little right hand tremble
    tremble2 = 0.025 * (np.random.rand(2)-0.5)
    base[6] += tremble2

    return base

# --- Plotting and Animation ---
fig, ax = plt.subplots(figsize=(3,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_aspect('equal')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_xlim(-7, 7)
ax.set_ylim(-2, 14)

# Scatter (for 15 white points, big enough as in the stimulus; all points)
points = ax.scatter([], [], c='w', s=60, edgecolors='none')

def init():
    points.set_offsets(np.zeros((15,2)))
    return (points,)

def animate(i):
    t = (i / FPS)
    xy = get_joint_positions(t)
    points.set_offsets(xy)
    return (points,)

ani = animation.FuncAnimation(
    fig, animate, frames=NFRAMES, init_func=init,
    interval=1000/FPS, blit=True, repeat=True)

plt.show()
