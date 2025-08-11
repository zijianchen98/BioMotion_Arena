
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Description of the 15 points:
# 0: Head
# 1: Right Shoulder, 2: Left Shoulder
# 3: Right Elbow,    4: Left Elbow
# 5: Right Wrist,    6: Left Wrist
# 7: Hip (center)
# 8: Right Hip,      9: Left Hip
# 10: Right Knee,    11: Left Knee
# 12: Right Ankle,   13: Left Ankle
# 14: Chest

# Lying down position; y=up, x=right
# All coordinates in arbitrary units for a figure about 2 units "tall"

def get_static_pose():
    pose = np.array([
        [ 1.0,  0.0],   # 0 - Head (centered)
        [ 0.6, -0.17],  # 1 - R Shoulder
        [ 1.4, -0.13],  # 2 - L Shoulder
        [ 0.3, -0.37],  # 3 - R Elbow
        [ 1.7, -0.35],  # 4 - L Elbow
        [ 0.1, -0.65],  # 5 - R Wrist
        [ 1.9, -0.67],  # 6 - L Wrist
        [ 1.0, -0.6],   # 7 - Hip center
        [ 0.8, -0.58],  # 8 - R Hip
        [ 1.2, -0.62],  # 9 - L Hip
        [ 0.75, -1.11], # 10 - R Knee
        [ 1.25, -1.13], # 11 - L Knee
        [ 0.7, -1.6],   # 12 - R Ankle
        [ 1.3, -1.62],  # 13 - L Ankle
        [ 1.0, -0.35],  # 14 - Chest
    ])
    return pose

def get_lying_motion(T, fps=30):
    # T: Number of frames; returns (T, 15, 2) array
    pose0 = get_static_pose()
    poses = np.zeros((T, 15, 2))
    t = np.linspace(0, 1, T)
    for i in range(T):
        phase = 2*np.pi * t[i]
        pose = pose0.copy()
        # Simulate very subtle "happy" movement and heavy weight "breathe"
        # 1. Torso (shoulders/chest/hips) moves up/down to simulate breathing
        # Amplitude higher (heavy weight); small movement in x for happy 'wiggle'
        breathe_y = 0.04 * np.sin(phase)
        breathe_x = 0.02 * np.sin(0.5 * phase)
        torso_idx = [0,1,2,14,7,8,9]
        pose[torso_idx,0] += breathe_x
        pose[torso_idx,1] += breathe_y
        # 2. Arms wag subtly as if relaxed/happy
        # move wrists and elbows in slow, small arcs
        for L,R,iE,iW in [(2,1,4,6,),(1,2,3,5,)]:  # (shoulder L/R, elbow L/R, wrist L/R)
            # angle offset for left/right to offset movement
            angle = 0.18 * np.sin(phase + (0 if L==2 else np.pi))
            # move elbow out/in
            pose[iE,0] += 0.04 * np.cos(phase + (0 if iE==4 else np.pi/2))
            pose[iE,1] += 0.02 * np.sin(phase + (0 if iE==4 else np.pi/2))
            # wrists swing further
            pose[iW,0] += 0.07 * np.cos(phase*0.7 + (0 if iW==6 else np.pi/2))
            pose[iW,1] += 0.03 * np.sin(phase*0.7 + (0 if iW==6 else np.pi/2))
        # 3. Legs: move a little as if adjusting for comfort
        # knees and ankles, legs spread a bit with sinusoidal cycle
        leg_spread = 0.05 * np.sin(phase * 0.8)
        knee_idxs = [10,11]
        ankle_idxs = [12,13]
        pose[knee_idxs,0] += [-leg_spread, leg_spread]
        pose[ankle_idxs,0] += [-leg_spread*1.6, leg_spread*1.6]
        # 4. Very slight side-to-side undulation of the whole body (happy mood)
        undu_x = 0.012 * np.sin(phase*1.7)
        pose[:,0] += undu_x
        poses[i] = pose
    # (Optional: Add minimal random jitter for "life" - but keep smooth)
    return poses

# ------------------------------------------------------------------------------
# Visualization -- use matplotlib.animation
def animate_biomotion():
    fps = 30
    duration = 2.5 # seconds
    T = int(fps*duration)
    poses = get_lying_motion(T, fps)

    # vertical translation to center in black screen
    poses[:,:,1] += 1.5

    fig, ax = plt.subplots(figsize=(4,6))
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_facecolor('black')
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 3)

    scatter = ax.scatter([], [], s=50, facecolors='white', edgecolors='none')
    ax.axis('off')

    def update(frame):
        data = poses[frame]
        scatter.set_offsets(data)
        return scatter,

    ani = animation.FuncAnimation(
        fig, update, frames=T, interval=1000/fps, blit=True, repeat=True
    )

    plt.show()

if __name__ == '__main__':
    animate_biomotion()
