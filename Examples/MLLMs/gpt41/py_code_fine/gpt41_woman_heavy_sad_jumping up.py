
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------
# 15-point biological motion model (woman, front view):
# 0: head       1: left shoulder    2: right shoulder
# 3: left elbow 4: right elbow      5: left wrist   6: right wrist
# 7: center pelvis (mid-hip)
# 8: left hip   9: right hip 
# 10: left knee 11: right knee
# 12: left ankle 13: right ankle
# 14: heavy weight (dumbbell object)
# ------------------------------

# Base skeleton for 'heavy' woman (more width, hips, upper thighs, modest proportions)
# All coordinates in arbitrary units (y increases downward, as in drawing, so we'll invert later!)
base_pose = np.array([
    [ 0.0, 0.0],     # 0: head (just above shoulders)
    [-0.27, 0.30],   # 1: left shoulder
    [ 0.27, 0.30],   # 2: right shoulder
    [-0.38, 0.57],   # 3: left elbow
    [ 0.38, 0.57],   # 4: right elbow
    [-0.35, 0.83],   # 5: left wrist
    [ 0.35, 0.83],   # 6: right wrist
    [ 0.0, 0.66],    # 7: pelvis center (mid-hip)
    [-0.19, 0.70],   # 8: left hip
    [ 0.19, 0.70],   # 9: right hip
    [-0.23, 1.09],   # 10: left knee
    [ 0.23, 1.09],   # 11: right knee
    [-0.23, 1.48],   # 12: left ankle
    [ 0.24, 1.48],   # 13: right ankle
    [ 0.0, 0.95],    # 14: heavy weight (held at pelvis/knees area, between hands, drops slightly on squat)
])

# Utility: Interpolate between two skeletons
def interpolate_pose(pose1, pose2, alpha):
    return (1 - alpha) * pose1 + alpha * pose2

# Generate jump cycle (sagittal, frontal)
def jump_cycle(t):
    # t: phase in [0, 1), where 0 is start to takeoff, 0.2-0.8 is flight, 1 is landing
    # The movement has 3 main phases: crouch, takeoff (push up from bend), flight, land
    squat = base_pose.copy()
    squat[[1,2,8,9,7],1]   += 0.17       # shoulders, hips, pelvis lower
    squat[[3,4,5,6],1]     += 0.05       # elbows/wrists lower
    squat[[10,11],1]       += 0.10       # knees more bent
    squat[[12,13],1]       -= 0.07       # ankles slightly forward
    squat[[ 8],0]          -= 0.03
    squat[[ 9],0]          += 0.03
    squat[[ 3],0]          -= 0.01
    squat[[ 4],0]          += 0.01
    squat[14] = [(base_pose[7,0]), base_pose[7,1]+0.18]  # dumbbell/weight below pelvis
    
    full_stretch = base_pose.copy()
    full_stretch[[3,4],1]  -= 0.10      # elbows up
    full_stretch[[5,6],1]  -= 0.12      # wrists up
    full_stretch[[1,2],1]  -= 0.03      # shoulders up
    # Arms are less raised for sadness & heaviness
    full_stretch[[8,9,7],1] -= 0.07     # hips, pelvis up
    full_stretch[[10,11],1] -= 0.06     # knees less bent
    full_stretch[[12,13],1] -= 0.02
    # For sad/heavy, don't fully straighten
    full_stretch[14] = [0, base_pose[7,1]+0.01]   # weight stays near pelvis

    # 'Sad' gesture: head and shoulders droop, wrists and hands close to body,
    # less arm swing, chin tucked
    sad_offset = np.zeros_like(base_pose)
    sad_offset[0,1]  += 0.05           # head a bit lower (chin down)
    sad_offset[1,1]  += 0.02           # shoulders droop a bit
    sad_offset[2,1]  += 0.02
    sad_offset[3,0]  += 0.05           # elbows inwards
    sad_offset[4,0]  -= 0.05
    sad_offset[5,0]  += 0.10           # wrists close to hips
    sad_offset[6,0]  -= 0.10
    sad_offset[5,1]  += 0.04           # hands droop
    sad_offset[6,1]  += 0.04

    # Crouch to takeoff (0.0-0.12), push-up (0.13-0.21), flight (0.22-0.78), descend/land (0.79-1.0)
    if t < 0.13:   # crouching/squatting preparatory bending
        alpha = 1 - t/0.13
        pose = interpolate_pose(full_stretch, squat, alpha)
    elif t < 0.22: # push-off: straightening to jump
        alpha = (t-0.13) / (0.09)
        pose = interpolate_pose(squat, full_stretch, alpha)
    elif t < 0.78:  # flight
        a = np.sin(np.pi*(t-0.22)/(0.56))    # for arched in midair, knees/arms up slightly
        # legs/knees up slightly in the air, arms don't swing much
        airy = full_stretch.copy()
        airy[[10,11],1] -= 0.13*a       # knees lift
        airy[[12,13],1] -= 0.08*a       # ankles up
        # Hands tuck in for sadness and inertia
        airy[[5,6],1] -= 0.06*a
        airy[[3,4],1] -= 0.03*a 
        # Weight is briefly lifted some in air (arms flexed)
        airy[14,1] -= 0.12*a
        pose = airy
    else:  # descent/landing (bending knees, hands down), reverse of takeoff
        alpha = (t-0.78)/(1-0.78)
        pose = interpolate_pose(full_stretch, squat, alpha)

    # Gravity/jump path: subject moves up, then down in the air
    # Heavy = small vertical excursion
    jump_height = 0.16         # moderate, for heavy
    jump_duration = 0.6
    if t < 0.13:
        dz = 0.0
    elif t < 0.13 + jump_duration:    # airborne
        local_t = (t - 0.13)/jump_duration
        dz = - jump_height * np.sin(np.pi * local_t)
    else:
        dz = 0.0
    pose[:,1] = pose[:,1] + dz

    # Apply "sad" hunched gesture throughout
    pose += sad_offset

    return pose

# Animation setup
fig, ax = plt.subplots(figsize=(4,8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(1.7, -0.2)
ax.axis('off')
bg = fig.patch
bg.set_facecolor('black')

scatter = ax.scatter([], [], s=72, color='white')

# trail for the weight for realism
weight_trail, = ax.plot([], [], lw=2, color='gray', alpha=0.20)

n_frames = 60
def animate(i):
    phase = (i % n_frames) / n_frames
    pose = jump_cycle(phase)
    xs, ys = pose[:,0], pose[:,1]
    scatter.set_offsets(np.c_[xs, ys])

    # Weight trail during main jump (show trajectory visually)
    t0 = max(phase-0.08, 0)
    trail_t = np.linspace(t0, phase, 8)
    trail_pts = np.array([jump_cycle(t)[14] for t in trail_t])
    weight_trail.set_data(trail_pts[:,0], trail_pts[:,1])
    return scatter, weight_trail

ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=33, blit=True)

plt.show()
