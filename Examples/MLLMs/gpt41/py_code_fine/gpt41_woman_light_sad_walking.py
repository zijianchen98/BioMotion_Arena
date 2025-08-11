
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Biological motion marker template for "walking"
# Order: head, shoulders (L,R), elbows (L,R), wrists (L,R), torso (C), hips (L,R), knees (L,R), ankles (L,R)
# See: Johansson, "Visual Perception of Biological Motion", Science, 1973.

MARKER_NAMES = [
    'head',        # 0
    'shoulder_L',  # 1
    'shoulder_R',  # 2
    'elbow_L',     # 3
    'elbow_R',     # 4
    'wrist_L',     # 5
    'wrist_R',     # 6
    'torso',       # 7
    'hip_L',       # 8
    'hip_R',       # 9
    'knee_L',      # 10
    'knee_R',      # 11
    'ankle_L',     # 12
    'ankle_R',     # 13
    'pelvis',      # 14
]

N_MARKERS = 15

# Anthropomorphic segment lengths (arbitrary but plausible for biological motion)
segment = {
    'head_to_shoulder': 0.18,
    'shoulder_width': 0.27,
    'upperarm': 0.22,
    'forearm': 0.19,
    'shoulder_to_torso': 0.18,
    'torso_to_hip': 0.23,
    'pelvis_width': 0.20,
    'upperleg': 0.24,
    'lowerleg': 0.24,
    'foot_length': 0.09
}

def get_marker_positions(phase):
    """Returns a (15,2) array of marker XY positions for a single frame (phase: 0~2pi)"""
    # Sagittal view: X=hor (left-right), Y=vertical

    # Basic body structure
    head_Y = 1.55
    pelvis_Y = 1.00
    shoulder_Y = head_Y - segment['head_to_shoulder']
    torso_Y = (shoulder_Y + pelvis_Y) / 2

    # Lateral (left/right) offsets
    shoulder_off = segment['shoulder_width']/2
    pelvis_off = segment['pelvis_width']/2

    # "Sad" posture: Drooping head, shoulders forward/down, torso slightly hunched
    sad_shoulder_drop = 0.06
    sad_head_angle = np.deg2rad(17)
    sad_shoulders_forward = -0.06

    # Walking cycle (all params in meters)
    walk_cycle = phase
    stride = 0.26      # stride length
    hip_sway = 0.04    # hips shift L/R modulating gait

    # Left/right acts in counterphase (left=0, right=pi)
    # Angles: positive is forward flexion (for legs), backward extension (for arms)
    hip_L_angle = 0.42*np.sin(walk_cycle)
    hip_R_angle = 0.42*np.sin(walk_cycle+np.pi)

    knee_L_angle = 0.75*np.maximum(0, np.sin(walk_cycle + np.pi/2))   # only flex during swing
    knee_R_angle = 0.75*np.maximum(0, np.sin(walk_cycle + 3*np.pi/2))

    ankle_L_angle = -0.38*np.maximum(0, np.sin(walk_cycle + np.pi/2))
    ankle_R_angle = -0.38*np.maximum(0, np.sin(walk_cycle + 3*np.pi/2))

    # Arm swing counterphase to legs, and slightly less in amplitude (sad arms=lower swing)
    shoulder_L_angle = 0.34 * np.sin(walk_cycle + np.pi)
    shoulder_R_angle = 0.34 * np.sin(walk_cycle)

    elbow_L_angle = 0.78 - 0.11*np.abs(np.sin(walk_cycle + np.pi))
    elbow_R_angle = 0.78 - 0.11*np.abs(np.sin(walk_cycle))

    # Shoulder positions (slouch/rounded forward, sag down)
    shoulder_L = np.array([-shoulder_off + sad_shoulders_forward, shoulder_Y - sad_shoulder_drop])
    shoulder_R = np.array([ shoulder_off + sad_shoulders_forward, shoulder_Y - sad_shoulder_drop])

    # Head (depressed slightly forward and down)
    head = np.array([0, head_Y]) + 0.07*np.array([np.sin(sad_head_angle), -np.cos(sad_head_angle)])

    # Torso/pelvis center
    pelvis = np.array([0, pelvis_Y])
    torso = np.array([0, torso_Y])

    # Hip positions
    hip_L = pelvis + np.array([-pelvis_off+hip_sway*np.sin(walk_cycle), 0])
    hip_R = pelvis + np.array([pelvis_off+hip_sway*np.sin(walk_cycle+np.pi), 0])

    # Torso marker closer to shoulder than pelvis
    torso = (shoulder_L + shoulder_R)/2*0.5 + pelvis*0.5

    # Shoulders to elbows
    def limb_from_shoulder(base, shoulder_angle, seg1, elbow_angle, seg2):
        # Shoulder_angle: relative to vertical (downwards=0), negative: backward, positive: forward
        sh_th = np.deg2rad(90) + shoulder_angle      # from +y axis
        elbow_d = seg1 * np.array([np.sin(sh_th), -np.cos(sh_th)])
        elbow = base + elbow_d
        el_th = sh_th + elbow_angle
        wrist = elbow + seg2 * np.array([np.sin(el_th), -np.cos(el_th)])
        return elbow, wrist

    elbow_L, wrist_L = limb_from_shoulder(
        shoulder_L, shoulder_L_angle, segment['upperarm'],
        elbow_L_angle, segment['forearm'])
    elbow_R, wrist_R = limb_from_shoulder(
        shoulder_R, shoulder_R_angle, segment['upperarm'],
        elbow_R_angle, segment['forearm'])

    # Sad arms: arms lower and less swing, wrists closer to hips on down phase
    # No explicit revision since angles above are already "sadder" (less amplitude)

    # Hips to knees to ankles
    def leg_chain(hip, hip_angle, upperleg, knee_angle, lowerleg, ankle_angle, foot_length):
        # All relative to vertical (downwards)
        hip_th = -hip_angle
        knee = hip + upperleg*np.array([np.sin(hip_th), -np.cos(hip_th)])
        knee_th = hip_th + knee_angle
        ankle = knee + lowerleg*np.array([np.sin(knee_th), -np.cos(knee_th)])
        foot_th = knee_th + ankle_angle
        foot = ankle + foot_length*np.array([np.sin(foot_th), -np.cos(foot_th)]) # (not displayed)
        return knee, ankle, foot

    knee_L, ankle_L, _ = leg_chain(
        hip_L, hip_L_angle, segment['upperleg'],
        knee_L_angle, segment['lowerleg'], ankle_L_angle, segment['foot_length'])
    knee_R, ankle_R, _ = leg_chain(
        hip_R, hip_R_angle, segment['upperleg'],
        knee_R_angle, segment['lowerleg'], ankle_R_angle, segment['foot_length'])

    marker_positions = np.stack([
        head,            # 0
        shoulder_L,      # 1
        shoulder_R,      # 2
        elbow_L,         # 3
        elbow_R,         # 4
        wrist_L,         # 5
        wrist_R,         # 6
        torso,           # 7
        hip_L,           # 8
        hip_R,           # 9
        knee_L,          # 10
        knee_R,          # 11
        ankle_L,         # 12
        ankle_R,         # 13
        pelvis           # 14
    ])

    # Lateral translation: The walker moves at slow, light pace (pace for light/sad walk)
    walker_speed = 0.018
    X_offset = walker_speed * phase
    marker_positions[:, 0] += X_offset

    # "Sad": head and body moves lower in the walk, less bounce and more downward pitch
    body_bounce = 0.018 * np.sin(walk_cycle) - 0.032 * np.abs(np.sin(walk_cycle/2))
    marker_positions[:, 1] += body_bounce

    return marker_positions

# Animation function
def animate_walk():
    fig = plt.figure(figsize=(3.5, 5.6), dpi=100)
    ax = plt.axes(xlim=(-0.55, 0.75), ylim=(0.55, 1.79))
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    plt.axis('off')

    scat = ax.scatter([], [], color='white', s=41)

    frame_cnt = 48   # frames per cycle
    walk_phases = np.linspace(0, 2*np.pi, frame_cnt, endpoint=False)

    def init():
        scat.set_offsets(np.zeros((N_MARKERS, 2)))
        return (scat,)

    def animate(i):
        phase = walk_phases[i % frame_cnt]
        points = get_marker_positions(phase)
        scat.set_offsets(points)
        return (scat,)

    ani = animation.FuncAnimation(
        fig, animate, frames=frame_cnt, interval=1000/30, blit=True, init_func=init, repeat=True)

    plt.show()

if __name__ == "__main__":
    animate_walk()
