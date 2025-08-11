
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 point labels for a biological 'sad woman, heavy, lying down'
# (Head, Shoulders L/R, Elbows L/R, Wrists L/R, Hips L/R, Knees L/R, Ankles L/R)
LABELS = [
    "Head",
    "Shoulder_L", "Shoulder_R",
    "Elbow_L", "Elbow_R",
    "Wrist_L", "Wrist_R",
    "Spine",
    "Hip_L", "Hip_R",
    "Knee_L", "Knee_R",
    "Ankle_L", "Ankle_R",
    "Chest",
]

# Define "lying down" initial static pose (side-view: X-horizontal, Y-vertical)
def lying_down_pose():
    # Centered horizontally, head on left (low X), feet on right (high X), Y is up-down
    # Units in "arbitrary" anthropometric proportions
    #           X     Y
    points = np.array([
        [0.1,  0.25],  # Head
        [0.2,  0.30],  # Shoulder_L
        [0.2,  0.20],  # Shoulder_R
        [0.35, 0.32],  # Elbow_L
        [0.35, 0.18],  # Elbow_R
        [0.52, 0.34],  # Wrist_L
        [0.52, 0.16],  # Wrist_R
        [0.22, 0.25],  # Spine
        [0.28, 0.27],  # Hip_L
        [0.28, 0.23],  # Hip_R
        [0.46, 0.29],  # Knee_L
        [0.46, 0.21],  # Knee_R
        [0.62, 0.30],  # Ankle_L
        [0.62, 0.20],  # Ankle_R
        [0.16, 0.25],  # Chest
    ])
    return points

def sad_woman_lie_anim(t, base):
    """Return 15x2 points, modified from base according to frame t (t in [0,1])"""
    points = base.copy()

    # Sad pose: head droops, shoulders slouch, knees bend up, wrists slack
    sadness = 0.2 + 0.1*np.sin(2*np.pi*t)  # sadness slouch amplitude
    weight = 0.1 + 0.02*np.cos(2*np.pi*t)  # slight body heavy movement

    # Head droop
    points[0,1] -= sadness*0.09
    points[0,0] += sadness*0.10

    # Shoulder slouch (come closer to center, drop forward/down)
    for idx in [1,2]:
        points[idx,0] += 0.02*weight
        points[idx,1] -= 0.02*weight

    # Spine curves forward (arches)
    points[7,0] += 0.03*weight

    # Chest sinks
    points[14,0] += 0.05*sadness

    # Hips move down (heavy sink)
    for idx in [8,9]:
        points[idx,1] -= 0.09*weight

    # Knees bent toward body (pull up)
    points[10,0] -= 0.05*sadness
    points[10,1] += 0.10*sadness
    points[11,0] -= 0.05*sadness
    points[11,1] += 0.07*sadness

    # Ankles sag down more due to weight
    points[12,1] -= 0.11*weight
    points[13,1] -= 0.13*weight

    # Elbows move back slightly
    points[3,0] -= 0.03*weight
    points[4,0] -= 0.03*weight

    # Wrists flop toward ground from elbow, then sway gently
    sway = 0.015*np.sin(2*np.pi*t)
    points[5,0] -= 0.10*sadness - sway
    points[6,0] -= 0.08*sadness + sway
    points[5,1] -= 0.07*sadness + sway
    points[6,1] -= 0.07*sadness - sway

    # Body gentle breathing (whole body lifts and falls slowly: gravity/fatigue)
    breath = 0.012*np.sin(2*np.pi*t)
    points[:,1] += breath

    # Small trembling for "heaviness" effect, esp. wrists & ankles
    tremor = 0.004*np.sin(10*2*np.pi*t)
    for idx in [5,6,12,13]:
        points[idx,:] += np.array([tremor, -tremor])

    return points

# Visualization boilerplate
fig, ax = plt.subplots(figsize=(6,4))
plt.axis('off')
ax.set_facecolor('black')
ax.set_xlim(0, 0.75)
ax.set_ylim(0, 0.48)

scat = ax.scatter([], [], s=100, c='white', edgecolors='none')

base_pose = lying_down_pose()

def animate(i):
    t = (i % 100) / 100.0  # t in [0, 1]
    pts = sad_woman_lie_anim(t, base_pose)
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=200, interval=50, blit=True
)
plt.show()
