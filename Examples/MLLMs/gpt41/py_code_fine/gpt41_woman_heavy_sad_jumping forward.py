
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
n_points = 15
frames = 80
fps = 30

# Point-light marker indices for a standard 15-point model
# 0: Head, 1/2: Shoulders (L/R), 3/4: Elbows (L/R), 5/6: Wrists (L/R),
# 7/8: Hips (L/R), 9/10: Knees (L/R), 11/12: Ankles (L/R), 13/14: Feet (L/R)
# We'll use the same mapping for movement

# Simple "sad" heavy woman body shape proportions (broad body, slumped)
joint_y = np.array([
    1.00,  # 0 : Head
    0.91,0.91,  # 1/2: Shoulders
    0.80,0.80,   # 3/4: Elbows
    0.70,0.70,   # 5/6: Wrists
    0.60,0.60,   # 7/8: Hips
    0.40,0.40,   # 9/10: Knees
    0.15,0.15,   # 11/12: Ankles
    0.05,0.05    # 13/14: Feet
])
joint_x = np.array([
    0.0,
    -0.16, 0.16,
    -0.26, 0.26,
    -0.32, 0.32,
    -0.14, 0.14,
    -0.16, 0.16,
    -0.12, 0.12,
    -0.16, 0.16
])

# The jumping forward: The body "squats", then pushes up and forward, feet push, arms lift and chest/head drop ("sad/heavy" style: slightly hunched, low amplitude)
def synth_pose(t):
    # t in [0,1]
    # t=0: ready, t=0.3: squat deep, t=0.5: push up, t=0.8: airborne apex, t=1: land
    pose_y = joint_y.copy()
    pose_x = joint_x.copy()

    # Horizontal: Move forward 0.28 body widths per full jump
    x_disp = 0.0 + 0.28*t   # move right

    # Sad/hunched: Torso/shoulders/head droop more when squatting/landing, less during apex
    hunched = 0.07*np.sin(np.pi*t)

    # "Squat" fraction (0 ready, 1 deepest)
    if t < 0.33:
        squat = 1.4*t
    elif t < 0.5:
        squat = 0.46 - 1.3*(t-0.33)
    elif t < 0.7:
        squat = 0
    else:
        squat = 2.5*(t-0.7)

    squat = np.clip(squat, 0, 0.43)

    # Center of mass arc: "Jump" parabola
    jump_height = 0.20     # increase for higher jump if desired
    if t < 0.2:
        arc = 0
    elif t < 0.8:
        arc = jump_height*np.sin(np.pi*(t-0.2)/0.6)
    else:
        arc = 0

    # Blend the changes:
    # Pelvis, knees, ankles, feet all lower when squatting
    # The full body is lifted by the jump (arc)
    for idx in [7,8,9,10,11,12,13,14]: # hips, knees, ankles, feet
        pose_y[idx] -= 0.13*squat

    # Hunched pose: Head, shoulders drop extra when squatting and at land (sad style)
    for idx in [0,1,2]: # head, shoulders
        pose_y[idx] -= hunched

    # Feet swing up at push-off and in air
    lift = 0
    if t>0.18 and t<0.7:
        lift = 0.19*np.sin(np.pi*(t-0.2)/0.5)
    for idx in [13,14]: # feet
        pose_y[idx] += lift

    # Arms: Start drooping, then as body jumps, swing up a little
    arm_swing = 0.09*np.sin(np.pi*min(1,t/0.6))
    for idx in [3,4,5,6]:
        if idx in [3,5]:  # left arm (slightly behind, lower for sad)
            pose_y[idx] += 0.03-0.08*np.sin(np.pi*t)
            pose_x[idx] -= 0.02 + 0.05*np.sin(np.pi*t)
        else:            # right arm
            pose_y[idx] += 0.03-0.07*np.sin(np.pi*t)
            pose_x[idx] += 0.02 + 0.05*np.sin(np.pi*t)

    # All points: add vertical COM arc ("arc" upward motion)
    pose_y += arc

    # All points: Add overall rightward displacement
    pose_x += x_disp

    # "Sag" the knees/ankles/feet a bit for "heavy" effect on landing
    if t>0.85 or t<0.15:
        add_sag = 0.06*np.exp(-25*(t-1)**2) if t>0.85 else 0.06*np.exp(-60*(t)**2)
        for idx in [9,10,11,12,13,14]:
            pose_y[idx] -= add_sag

    return pose_x, pose_y

# Prepare frames
poses_x = []
poses_y = []
for f in range(frames):
    t = f/(frames-1)
    px,py = synth_pose(t)
    poses_x.append(px)
    poses_y.append(py)
poses_x = np.stack(poses_x)
poses_y = np.stack(poses_y)

# Stretch scales for display (make proportions wider for 'heavy')
w, h = 2.0, 2.0

# Animate
fig, ax = plt.subplots(figsize=(4,8))
plt.style.use('dark_background')
ax.set_xlim(-0.45, 0.70)
ax.set_ylim(-0.08, 1.10)
ax.axis('off')

pts, = ax.plot([], [], 'wo', ms=10)
def animate(i):
    pts.set_data(w*poses_x[i], h*poses_y[i])
    return (pts,)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000//fps, blit=True)

plt.show()
