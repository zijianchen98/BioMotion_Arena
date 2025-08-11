
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_point_positions(t):
    """
    Compute the 15 joint positions for a point-light walking figure at time t.
    Returns two arrays: xs (x-coordinates), ys (y-coordinates).
    """
    # Walking cycle frequency (Hz)
    freq = 1.0
    phase = 2 * np.pi * freq * t

    # Torso bobbing
    bob_amp = 0.05
    bob = bob_amp * np.sin(2 * phase)

    # Hip center
    hip_y = bob
    hip_x = 0.0

    # Torso points: spine, neck, head
    spine = np.array([0.0, hip_y + 0.25])
    neck = np.array([0.0, hip_y + 0.50 + 0.02 * np.sin(2 * phase)])
    head = np.array([0.0, neck[1] + 0.20])

    # Shoulder positions
    shoulder_offset = 0.20
    left_shoulder  = np.array([-shoulder_offset, neck[1]])
    right_shoulder = np.array([ shoulder_offset, neck[1]])

    # Hip positions
    hip_offset = 0.10
    left_hip  = np.array([-hip_offset, hip_y])
    right_hip = np.array([ hip_offset, hip_y])

    # Leg parameters
    upper_leg = 0.50
    lower_leg = 0.50
    leg_swing_amp = 0.5  # radians

    # Thigh swing angles
    left_thigh_ang  =  leg_swing_amp * np.sin(phase)
    right_thigh_ang =  leg_swing_amp * np.sin(phase + np.pi)

    # Knee bends occur during swing (when thigh is forward)
    left_knee_bend  = 0.5 * max(0.0,  np.sin(phase))
    right_knee_bend = 0.5 * max(0.0,  np.sin(phase + np.pi))

    # Left knee and ankle
    lk_dx = upper_leg * np.sin(left_thigh_ang)
    lk_dy = -upper_leg * np.cos(left_thigh_ang)
    left_knee = left_hip + np.array([lk_dx, lk_dy])
    la_dx = lower_leg * np.sin(left_thigh_ang - left_knee_bend)
    la_dy = -lower_leg * np.cos(left_thigh_ang - left_knee_bend)
    left_ankle = left_knee + np.array([la_dx, la_dy])

    # Right knee and ankle
    rk_dx = upper_leg * np.sin(right_thigh_ang)
    rk_dy = -upper_leg * np.cos(right_thigh_ang)
    right_knee = right_hip + np.array([rk_dx, rk_dy])
    ra_dx = lower_leg * np.sin(right_thigh_ang - right_knee_bend)
    ra_dy = -lower_leg * np.cos(right_thigh_ang - right_knee_bend)
    right_ankle = right_knee + np.array([ra_dx, ra_dy])

    # Arm parameters
    upper_arm = 0.35
    lower_arm = 0.25
    arm_swing_amp = 0.7

    # Shoulder rotation angles
    left_shoulder_ang  = -arm_swing_amp * np.sin(phase)
    right_shoulder_ang = -arm_swing_amp * np.sin(phase + np.pi)

    # Elbow bends (slight bend when arm is back)
    left_elbow_bend  = 0.3 * max(0.0, np.sin(phase + np.pi))
    right_elbow_bend = 0.3 * max(0.0, np.sin(phase))

    # Left elbow and wrist
    le_dx = upper_arm * np.sin(left_shoulder_ang)
    le_dy = -upper_arm * np.cos(left_shoulder_ang)
    left_elbow = left_shoulder + np.array([le_dx, le_dy])
    lw_dx = lower_arm * np.sin(left_shoulder_ang - left_elbow_bend)
    lw_dy = -lower_arm * np.cos(left_shoulder_ang - left_elbow_bend)
    left_wrist = left_elbow + np.array([lw_dx, lw_dy])

    # Right elbow and wrist
    re_dx = upper_arm * np.sin(right_shoulder_ang)
    re_dy = -upper_arm * np.cos(right_shoulder_ang)
    right_elbow = right_shoulder + np.array([re_dx, re_dy])
    rw_dx = lower_arm * np.sin(right_shoulder_ang - right_elbow_bend)
    rw_dy = -lower_arm * np.cos(right_shoulder_ang - right_elbow_bend)
    right_wrist = right_elbow + np.array([rw_dx, rw_dy])

    # Collect all 15 points
    points = [
        head,
        neck,
        left_shoulder, right_shoulder,
        spine,
        left_elbow, right_elbow,
        left_wrist, right_wrist,
        left_hip, right_hip,
        left_knee, right_knee,
        left_ankle, right_ankle
    ]

    pts = np.array(points)
    xs, ys = pts[:, 0], pts[:, 1]
    return xs, ys

def animate_point_lights(duration=10.0, fps=30):
    """
    Create and show the walking point-light animation.
    duration: length of animation in seconds.
    fps: frames per second.
    """
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.2, 1.5)

    # Initial scatter of 15 points
    xs, ys = get_point_positions(0)
    scat = ax.scatter(xs, ys, c='white', s=50)

    def update(frame):
        t = frame / fps
        xs, ys = get_point_positions(t)
        scat.set_offsets(np.c_[xs, ys])
        return scat,

    frames = int(duration * fps)
    anim = animation.FuncAnimation(fig, update, frames=frames,
                                   interval=1000/fps, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    animate_point_lights(duration=10.0, fps=30)
