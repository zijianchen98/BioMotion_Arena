
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Point-light marker indices (15 total)
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Wrist
# 6: Left Wrist
# 7: Chest
# 8: Hip Center
# 9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Ankle
# 14: Left Ankle

def forward_roll_motion(n_frames, amplitude=1.2, y0=2):
    """
    Simulate a biologically plausible forward roll using 15 point-lights.
    Returns: array of shape (n_frames, 15, 2)
    """
    angle_step = 2 * np.pi / n_frames
    head_radius = 0.22   # head to shoulder/hip radius
    spine_length = 0.44  # shoulder to hip (torso)
    pelvis_width = 0.22
    shoulder_width = 0.25
    arm_length = 0.33
    forearm_length = 0.27
    thigh_length = 0.45
    shin_length = 0.43
    ankle_offset = 0.10

    # Place markers according to human morphology, rolling along +x axis.
    all_positions = []
    for t in range(n_frames):
        theta = angle_step * t
        cx = amplitude * np.sin(theta) + t * (0.025)  # x center of body follows a rolling path
        cy = y0 + amplitude * np.cos(theta)           # y center of body

        # The main "roll": treat the body as a rotating stick with articulated limbs.
        # The 'spine axis' rotates as a whole; head/torso follows the circle.
        rot = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

        # Hip center and chest center
        spine_axis = np.array([0, -spine_length/2])
        hip_center = np.array([cx, cy]) + rot @ spine_axis
        chest_center = np.array([cx, cy]) + rot @ (-spine_axis)

        # Head (above chest)
        head = chest_center + rot @ np.array([0, head_radius + 0.10])

        # Shoulders, hips (perpendicular to spine axis)
        spine_dir = rot @ np.array([0,1])  # from hip to chest
        right = rot @ np.array([1,0])
        left = rot @ np.array([-1,0])

        right_shoulder = chest_center + right * shoulder_width/2
        left_shoulder = chest_center + left * shoulder_width/2
        right_hip = hip_center + right * pelvis_width/2
        left_hip = hip_center + left * pelvis_width/2

        # Elbows/wrists - arms swing as she rolls (simulate happy energy)
        arm_angle = 0.7 * np.sin(2*theta + 1)
        right_elbow = right_shoulder + rot @ np.array([np.cos(-np.pi/2 + arm_angle), np.sin(-np.pi/2 + arm_angle)]) * arm_length
        left_elbow = left_shoulder + rot @ np.array([np.cos(-np.pi/2 - arm_angle), np.sin(-np.pi/2 - arm_angle)]) * arm_length

        right_wrist = right_elbow + rot @ np.array([np.cos(-np.pi/2 + 2*arm_angle), np.sin(-np.pi/2 + 2*arm_angle)]) * forearm_length
        left_wrist = left_elbow + rot @ np.array([np.cos(-np.pi/2 - 2*arm_angle), np.sin(-np.pi/2 - 2*arm_angle)]) * forearm_length

        # Knees/ankles - legs tucked in rollover (simulate tucking)
        knee_angle = 1.2 + 0.2 * np.sin(theta)
        right_knee = right_hip + rot @ np.array([np.cos(-np.pi/2 + knee_angle), np.sin(-np.pi/2 + knee_angle)]) * thigh_length * 0.77
        left_knee = left_hip + rot @ np.array([np.cos(-np.pi/2 - knee_angle), np.sin(-np.pi/2 - knee_angle)]) * thigh_length * 0.77

        right_ankle = right_knee + rot @ np.array([np.cos(-np.pi/2 + knee_angle + 0.7), np.sin(-np.pi/2 + knee_angle + 0.7)]) * shin_length * 0.78
        left_ankle = left_knee + rot @ np.array([np.cos(-np.pi/2 - knee_angle - 0.7), np.sin(-np.pi/2 - knee_angle - 0.7)]) * shin_length * 0.78

        # Chest (center)
        chest = chest_center

        # Hip (center)
        hip = hip_center

        points = np.stack([
            head,
            right_shoulder,
            left_shoulder,
            right_elbow,
            left_elbow,
            right_wrist,
            left_wrist,
            chest,
            hip,
            right_hip,
            left_hip,
            right_knee,
            left_knee,
            right_ankle,
            left_ankle
        ], axis=0)
        all_positions.append(points)
    return np.array(all_positions)


# Parameters for animation
n_frames = 48
dt = 1/30.  # 30 FPS

positions = forward_roll_motion(n_frames, amplitude=1.2, y0=2)

# Happy facial expression: make head bob (marker 0) with a little bounce
for i in range(n_frames):
    offset = 0.04 * np.sin(4*np.pi*i/n_frames)
    positions[i,0,1] += offset

fig, ax = plt.subplots(figsize=(4, 7))
ax.set_facecolor('black')
plt.axis('off')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(0.2, 3.4)

# Draw point-lights
scats = ax.plot([], [], 'wo', ms=9)[0]

def init():
    scats.set_data([], [])
    return scats,

def animate(i):
    data = positions[i%positions.shape[0]]
    scats.set_data(data[:,0], data[:,1])
    return scats,

ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=1000*dt, blit=True, init_func=init)

plt.show()
