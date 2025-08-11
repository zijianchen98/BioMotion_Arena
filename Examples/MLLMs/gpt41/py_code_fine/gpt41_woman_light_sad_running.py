
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 keypoints: head, shoulders (L,R), elbows (L,R), wrists (L,R), hips (L,R), knees (L,R), ankles (L,R)
JOINTS = [
    "Head",          # 0
    "Shoulder_L",    # 1
    "Shoulder_R",    # 2
    "Elbow_L",       # 3
    "Elbow_R",       # 4
    "Wrist_L",       # 5
    "Wrist_R",       # 6
    "Hip_L",         # 7
    "Hip_R",         # 8
    "Knee_L",        # 9
    "Knee_R",        #10
    "Ankle_L",       #11
    "Ankle_R",       #12
    "Pelvis",        #13
    "Chest"          #14
]

# Helper function to ensure female, sad posture, and running: 
def sadwoman_running_pose(t, stride_length=0.7, body_height=2):
    # t: time in [0,1]
    # stride_length: horizontal run stride
    # body_height: overall body length
    
    # Running cycle (using two phase: left and right, offset pi)
    omega = 2 * np.pi
    phase = omega * t

    # Sag in shoulders/head for sad posture (shoulders rounded, head forward/droop), slightly bent knees
    sad_head_drop = 0.11 * body_height
    sad_shoulder_drop = 0.08 * body_height
    sad_shoulder_curve = 0.06 * body_height
    sad_chest_curl = 0.06 * body_height

    # Joint base positions (relative to 0,0 at pelvis)
    pelvis_y = 0
    chest_y = pelvis_y + 0.25 * body_height - sad_chest_curl
    head_y = chest_y + 0.30 * body_height - sad_head_drop

    # side-to-side distance
    shoulder_span = 0.24 * body_height
    hip_span = 0.18 * body_height
    elbow_span = 0.39 * body_height
    wrist_span = 0.49 * body_height

    # Joints - we will compute L and R with phase difference
    joints = np.zeros((15,2))

    # HORIZONTAL movement of body
    pelvis_x = stride_length * (t)    # move right at constant speed

    # Pelvis
    joints[13] = [pelvis_x, pelvis_y]
    
    # Chest
    chest_x = pelvis_x
    joints[14] = [chest_x, chest_y]
    
    # Head (drooped, forward for sadness)
    head_x = chest_x + 0.03 * body_height
    joints[0] = [head_x, head_y]

    # Shoulders (curved and dropped a bit)
    shoulder_drop = sad_shoulder_drop
    shoulder_curve = sad_shoulder_curve
    joints[1] = [chest_x - shoulder_span/2 + shoulder_curve, chest_y - shoulder_drop]
    joints[2] = [chest_x + shoulder_span/2 - shoulder_curve, chest_y - shoulder_drop]
    
    # Running: legs swing with phase offset, arms opposite phase
    # KNEES/ANKLES phase
    leg_phase_L = phase
    leg_phase_R = phase + np.pi

    # Hip positions
    hip_y = pelvis_y
    joints[7] = [pelvis_x - hip_span/2, hip_y]
    joints[8] = [pelvis_x + hip_span/2, hip_y]

    # Thigh (hip to knee)
    thigh = 0.28 * body_height
    # Shin (knee to ankle)
    shin = 0.29 * body_height

    # Simulate sad running: legs never fully extend, body is low, arms little drive (sad)
    knee_L_y = hip_y - thigh * np.cos(0.55 + 0.20 * np.sin(leg_phase_L))
    knee_L_x = joints[7,0] + thigh * np.sin(0.55 + 0.70 * np.sin(leg_phase_L))
    knee_R_y = hip_y - thigh * np.cos(0.55 + 0.20 * np.sin(leg_phase_R))
    knee_R_x = joints[8,0] + thigh * np.sin(0.55 + 0.70 * np.sin(leg_phase_R))

    joints[9] = [knee_L_x, knee_L_y]
    joints[10]= [knee_R_x, knee_R_y]

    # Ankle positions
    ankle_L_y = knee_L_y - shin * np.cos(0.80 + 0.50 * np.sin(leg_phase_L + 0.2))
    ankle_L_x = knee_L_x + shin * np.sin(0.80 + 0.45 * np.sin(leg_phase_L + 0.1))
    ankle_R_y = knee_R_y - shin * np.cos(0.80 + 0.50 * np.sin(leg_phase_R + 0.2))
    ankle_R_x = knee_R_x + shin * np.sin(0.80 + 0.45 * np.sin(leg_phase_R + 0.1))

    joints[11] = [ankle_L_x, ankle_L_y]
    joints[12] = [ankle_R_x, ankle_R_y]

    # Arms swing opposite legs, but muted (sad mood, low amplitude, little drive)
    arm_swing_amp = 0.22 * np.pi
    arm_phase_L = phase + np.pi
    arm_phase_R = phase

    elbow_L_angle = 1.1 + arm_swing_amp * np.sin(arm_phase_L) - 0.18 # arms down and in front
    elbow_R_angle = 1.1 + arm_swing_amp * np.sin(arm_phase_R) - 0.18 

    # shoulder y is chest_y - shoulder_drop
    elbow_y_L = joints[1,1] - 0.26 * body_height * np.cos(elbow_L_angle)
    elbow_x_L = joints[1,0] - 0.18 * body_height * np.sin(elbow_L_angle)
    elbow_y_R = joints[2,1] - 0.26 * body_height * np.cos(elbow_R_angle)
    elbow_x_R = joints[2,0] - 0.18 * body_height * np.sin(elbow_R_angle)

    joints[3] = [elbow_x_L, elbow_y_L]
    joints[4] = [elbow_x_R, elbow_y_R]

    # Wrists, with a bent forearm, hanging
    wrist_L_angle = elbow_L_angle + 0.90
    wrist_R_angle = elbow_R_angle + 0.90

    wrist_L_y = elbow_y_L - 0.21 * body_height * np.cos(wrist_L_angle)
    wrist_L_x = elbow_x_L - 0.11 * body_height * np.sin(wrist_L_angle)
    wrist_R_y = elbow_y_R - 0.21 * body_height * np.cos(wrist_R_angle)
    wrist_R_x = elbow_x_R - 0.11 * body_height * np.sin(wrist_R_angle)

    joints[5] = [wrist_L_x, wrist_L_y]
    joints[6] = [wrist_R_x, wrist_R_y]

    return joints

# Animation parameters
FPS = 60
DURATION = 2.7  # seconds, short but enough to loop a run
FRAMES = int(DURATION * FPS)

# Prepare the figure
fig, ax = plt.subplots(figsize=(4, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')

# Set aspect ratio and axis limits (room for horizontal running loop)
H, W = 8, 4
ax.set_xlim(-1, 3)  # so you can see the running movement
ax.set_ylim(-1, H-1)
ax.set_aspect('equal')

# Scatter plot for 15 white point-lights
points, = ax.plot([],[], 'o', color='white', markersize=10)

# Draw stick connections to help visualization (optional, comment out if PURE point-light required)
SKELETON = [
    (0,14),          # Head to chest
    (14,1),(14,2),   # Chest to shoulders
    (13,7),(13,8),   # Pelvis to hips
    (14,13),         # Chest to pelvis
    (1,3),(3,5),     # Left arm
    (2,4),(4,6),     # Right arm
    (7,9),(9,11),    # Left leg
    (8,10),(10,12),  # Right leg
]
lines = []
for s in SKELETON:
    l, = ax.plot([], [], '-', color='white', linewidth=1.4, alpha=0.10)
    lines.append(l)

# Sad face mark (optional, subtle)
sad_face, = ax.plot([], [], 'o', color='white', markersize=3, alpha=0.9)

def animate(frame):
    t = (frame % FRAMES) / FRAMES    # in [0,1)
    joints = sadwoman_running_pose(t, stride_length=1.1, body_height=4.8)

    # Loop jump for horizontal movement
    x = joints[:,0] % 2.4 - 0.5
    y = joints[:,1]
    points.set_data(x, y)

    # Draw lines for reference (subtle)
    for i, (a, b) in enumerate(SKELETON):
        lines[i].set_data([x[a], x[b]], [y[a], y[b]])
    
    # Draw a subtle sad face
    head = [x[0], y[0]]
    face_dx = 0.10
    sad_face.set_data([head[0] - face_dx, head[0], head[0] + face_dx],
                      [head[1] - 0.03, head[1] - 0.08, head[1] - 0.03])
    return [points] + lines + [sad_face]

ani = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS, blit=True)

plt.show()
