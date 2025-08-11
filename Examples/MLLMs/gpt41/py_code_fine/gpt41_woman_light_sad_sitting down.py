
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- PARAMETERS ----
NUM_POINTS = 15
FIGSIZE = (5, 8)
BG_COLOR = 'black'
POINT_COLOR = 'white'
POINT_SIZE = 70

# -- BODY MODEL: 15 points, standard convention --
# 0: Head (top of skull)
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Wrist
# 6: Left Wrist
# 7: Spine (upper, sternum)
# 8: Hip (pelvis/center)
# 9: Right Hip
#10: Left Hip
#11: Right Knee
#12: Left Knee
#13: Right Ankle
#14: Left Ankle

# coordinate arrays: (NUM_JOINTS, 2)
def base_pose():
    # approximate upright standing pose (woman, slightly narrower shoulders/hips, light, head slightly lowered)
    pose = np.array([
        [0.0, 7.5],    # 0 head (top)
        [-0.6, 6.7],   # 1 right shoulder
        [ 0.6, 6.7],   # 2 left shoulder
        [-1.0, 6.0],   # 3 right elbow
        [ 1.0, 6.0],   # 4 left elbow
        [-1.0, 5.3],   # 5 right wrist
        [ 1.0, 5.3],   # 6 left wrist
        [ 0.0, 6.3],   # 7 upper back/sternum
        [ 0.0, 5.5],   # 8 center pelvis
        [-0.4, 5.5],   # 9 right hip
        [ 0.4, 5.5],   #10 left hip
        [-0.5, 4.2],   #11 right knee
        [ 0.5, 4.2],   #12 left knee
        [-0.6, 2.7],   #13 right ankle
        [ 0.6, 2.7],   #14 left ankle
    ])
    return pose

# SAD woman: head tilted down, slumping spine, arms limp in front, overall dropped posture
def sad_pose():
    pose = base_pose()
    # head tilt
    pose[0, 1] -= 0.3
    pose[0, 0] -= 0.15
    # slouch spine: move upper back and head forward
    pose[7, 0] -= 0.15
    pose[0, 0] -= 0.1
    # shoulders slightly raised and forward
    pose[1, 1] += 0.08
    pose[2, 1] += 0.08
    pose[1, 0] += 0.08
    pose[2, 0] += -0.08
    # limp arms, wrists brought closer together in front
    pose[5, 0] = -0.36
    pose[5, 1] = 5.12
    pose[6, 0] =  0.36
    pose[6, 1] = 5.12
    pose[3, 0] = -0.6
    pose[3, 1] = 5.8
    pose[4, 0] = 0.6
    pose[4, 1] = 5.8
    # drop pelvis ever so slightly
    pose[8, 1] -= 0.13
    pose[9, 1] -= 0.13
    pose[10, 1] -= 0.13
    # knees and ankles inwards, feet together
    pose[11, 0] = -0.25
    pose[12, 0] = 0.25
    pose[13, 0] = -0.19
    pose[14, 0] = 0.19
    return pose

# SITTING motion: interpolate from standing sad to sitting
def interpolate_pose(t):
    # 't': 0 (start, upright) -> 1 (end, sitting)
    # For keyframes, interpolate between base and sitting pose
    sad = sad_pose()
    # Sitting pose: knees/hips ~ 90 degrees, torso bent forward, arms on knees, ankles under knees
    sit = np.copy(sad)
    # shift pelvis/knees/ankles down and forward, so thighs/humerus at ~horizontal, shank/tibia vertical
    # Pelvis (hips): down and forward
    pelvis_shift_y = -2.8
    pelvis_shift_x = 1.4
    sit[8, :] += [pelvis_shift_x, pelvis_shift_y]
    sit[9, :] += [pelvis_shift_x, pelvis_shift_y]
    sit[10, :] += [pelvis_shift_x, pelvis_shift_y]
    # Knees: forward, down
    sit[11, 0] += pelvis_shift_x + 0.18
    sit[11, 1] += pelvis_shift_y - 0.26
    sit[12, 0] += pelvis_shift_x - 0.18
    sit[12, 1] += pelvis_shift_y - 0.26
    # Ankles: almost under knees
    sit[13, 0] = sit[11, 0] - 0.05
    sit[13, 1] = sit[11, 1] - 1.0
    sit[14, 0] = sit[12, 0] + 0.05
    sit[14, 1] = sit[12, 1] - 1.0
    # Torso: spine and head bent more forward (to look downward: sad, hunched sitting)
    sit[7, 0] += 1.2
    sit[7, 1] += -1.6
    sit[0, 0] += 1.3
    sit[0, 1] += -1.6
    # Shoulders: forward, down
    sit[1, 0] += 1.2
    sit[1, 1] += -1.6
    sit[2, 0] += 1.2
    sit[2, 1] += -1.6
    # Elbows: forward, almost above knees
    sit[3, 0] = (sit[11, 0] + sit[1, 0]) / 2 - 0.12
    sit[3, 1] = (sit[11, 1] + sit[1, 1]) / 2 + 0.35
    sit[4, 0] = (sit[12, 0] + sit[2, 0]) / 2 + 0.12
    sit[4, 1] = (sit[12, 1] + sit[2, 1]) / 2 + 0.35
    # Wrists: on knees
    sit[5, 0] = sit[11, 0]
    sit[5, 1] = sit[11, 1] + 0.05
    sit[6, 0] = sit[12, 0]
    sit[6, 1] = sit[12, 1] + 0.05
    # Interpolate between sad and sitting
    pose = (1 - t) * sad + t * sit
    return pose

# -- ANIMATION FUNCTION --
def animate_point_light_sitting(num_frames=80, duration=3.5):
    fig, ax = plt.subplots(figsize=FIGSIZE)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    plt.xlim(-2, 4.5)
    plt.ylim(0, 8.4)

    # Remove axes
    ax.axis('off')

    # init
    scatter = ax.scatter([], [], s=POINT_SIZE, c=POINT_COLOR, edgecolors='none')

    # for smooth vel profile (ease out/in), use sigmoid curves
    def ease_curve(x):
        # smoothstep, 0-1
        return 3*x**2 - 2*x**3

    def update(frame):
        t = frame / (num_frames - 1)
        t_motion = ease_curve(min(t*1.1, 1.0))  # slight overshoot for pause at end
        pose = interpolate_pose(t_motion)
        x = pose[:, 0]
        y = pose[:, 1]
        scatter.set_offsets(np.c_[x, y])
        return scatter,

    ani = animation.FuncAnimation(
        fig, update, frames=num_frames, interval=duration * 1000 / num_frames,
        blit=True, repeat=True
    )

    plt.show()

# -- RUN ANIMATION --
if __name__ == "__main__":
    animate_point_light_sitting()
