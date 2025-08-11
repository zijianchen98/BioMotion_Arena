
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 marker order, as in the image (top to bottom):
# 0: Head
# 1-2: Left/Right Shoulder
# 3-4: Left/Right Elbow
# 5-6: Left/Right Wrist
# 7: Spine/Base of neck
# 8: Pelvis/Hip (center)
# 9-10: Left/Right Hip
# 11-12: Left/Right Knee
# 13-14: Left/Right Ankle

# We create a lightly stylized skeleton. A "sadman" (head low, slouched a bit)
# For the jump: subject bends knees, crouches, then springs upward; arms might swing a little.

# Limb lengths (all normalized units, torso is about 1.0)
SCALE = 1.0
HEAD_RADIUS = 0.15 * SCALE
NECK_LEN = 0.13 * SCALE
TORSO_LEN = 0.45 * SCALE
PELVIS_WIDTH = 0.28 * SCALE
SHOULDER_WIDTH = 0.36 * SCALE
UPPER_ARM = 0.23 * SCALE
FORE_ARM = 0.23 * SCALE
UPPER_LEG = 0.28 * SCALE
LOWER_LEG = 0.30 * SCALE

# Joint rest locations, in a neutral standing pose (not yet animated), origin at pelvis center
def skeleton_pose(q_knees=0, q_hips=0, q_ankles=0, q_shoulders=0, q_elbows=0, q_wrist=0,
                  root_x=0, root_y=0, root_theta=0, q_head=0, q_spine=0):
    # Returns 15x2 array (x, y) for all point-light markers
    # Angles in radians

    c = np.cos
    s = np.sin

    # Root position is at pelvis center (x, y), with torso rotated by root_theta 
    # The angle system: y-up, x-right, 0 is upright, positive is counterclockwise ("matplotlib" Y axis up)
    pts = np.zeros((15, 2))

    # --- Pelvis center
    pelvis = np.array([root_x, root_y])
    # --- Pelvis left/right
    left_hip = pelvis + ( -PELVIS_WIDTH/2 * c(root_theta),  -PELVIS_WIDTH/2 * s(root_theta))
    right_hip = pelvis + (  PELVIS_WIDTH/2 * c(root_theta),   PELVIS_WIDTH/2 * s(root_theta))
    # --- Spine up 
    spine_dir = root_theta + q_spine
    base_neck = pelvis + (TORSO_LEN * s(spine_dir), TORSO_LEN * c(spine_dir))
    # --- Shoulder left/right
    left_shoulder = base_neck + (-SHOULDER_WIDTH/2 * c(spine_dir + np.pi/2), -SHOULDER_WIDTH/2 * s(spine_dir + np.pi/2))
    right_shoulder = base_neck + (SHOULDER_WIDTH/2 * c(spine_dir + np.pi/2), SHOULDER_WIDTH/2 * s(spine_dir + np.pi/2))
    # --- Head 
    head_dir = spine_dir + q_head
    head_center = base_neck + (NECK_LEN * s(head_dir), NECK_LEN * c(head_dir))
    # --- Arms (from shoulders)
    l_upper = q_shoulders[0]
    r_upper = q_shoulders[1]
    l_upper_arm = left_shoulder + (UPPER_ARM * s(spine_dir + l_upper), UPPER_ARM * c(spine_dir + l_upper))
    r_upper_arm = right_shoulder + (UPPER_ARM * s(spine_dir + r_upper), UPPER_ARM * c(spine_dir + r_upper))
    l_elbow_angle = l_upper + q_elbows[0]
    r_elbow_angle = r_upper + q_elbows[1]
    l_forearm = l_upper_arm + (FORE_ARM * s(spine_dir + l_elbow_angle), FORE_ARM * c(spine_dir + l_elbow_angle))
    r_forearm = r_upper_arm + (FORE_ARM * s(spine_dir + r_elbow_angle), FORE_ARM * c(spine_dir + r_elbow_angle))
    l_wrist_angle = l_elbow_angle + q_wrist[0]
    r_wrist_angle = r_elbow_angle + q_wrist[1]
    l_wrist = l_forearm + (0.00 * s(spine_dir + l_wrist_angle), 0.00 * c(spine_dir + l_wrist_angle))   # Mark at wrist
    r_wrist = r_forearm + (0.00 * s(spine_dir + r_wrist_angle), 0.00 * c(spine_dir + r_wrist_angle))   # Mark at wrist

    # --- Legs (from hips)
    l_hip_angle = q_hips[0]
    r_hip_angle = q_hips[1]
    l_knee = left_hip + (UPPER_LEG * s(root_theta + l_hip_angle), -UPPER_LEG * c(root_theta + l_hip_angle))
    r_knee = right_hip + (UPPER_LEG * s(root_theta + r_hip_angle), -UPPER_LEG * c(root_theta + r_hip_angle))
    l_ankle_angle = l_hip_angle + q_knees[0]
    r_ankle_angle = r_hip_angle + q_knees[1]
    l_ankle = l_knee + (LOWER_LEG * s(root_theta + l_ankle_angle), -LOWER_LEG * c(root_theta + l_ankle_angle))
    r_ankle = r_knee + (LOWER_LEG * s(root_theta + r_ankle_angle), -LOWER_LEG * c(root_theta + r_ankle_angle))

    # Now assign to output
    # Order: Head, L-Shoulder, R-Shoulder, L-Elbow, R-Elbow, L-Wrist, R-Wrist, Spine/BaseN, Pelvis center, L-Hip, R-Hip, L-Knee, R-Knee, L-Ankle, R-Ankle
    pts[0] = head_center
    pts[1] = left_shoulder
    pts[2] = right_shoulder
    pts[3] = l_upper_arm
    pts[4] = r_upper_arm
    pts[5] = l_forearm
    pts[6] = r_forearm
    pts[7] = base_neck
    pts[8] = pelvis
    pts[9] = left_hip
    pts[10] = right_hip
    pts[11] = l_knee
    pts[12] = r_knee
    pts[13] = l_ankle
    pts[14] = r_ankle

    return pts

# Biomechanical motion definition for jumping up

def jump_motion(t, T=1.25):
    """
    Returns all joint angles and root positions for time t in [0, T]
    - T: period/length of the jump cycle
    t=0: stand
    t=0.3: crouch
    t=0.42: rapid extension (takeoff)
    t=0.5: maximum upward velocity
    t~0.7: airborne, arms raised, knees bent
    t~0.9: descending, arms down
    t~1.10: landing
    t~1.20: recover
    """
    t = t % T
    # Timings of phases
    t_crouch = 0.30 * T
    t_launch = 0.42 * T
    t_apex = 0.74 * T
    t_land = 1.08 * T

    # 1. Standing (neutral) pose
    # 2. Crouch phase: hips flexed, knees bent, spine leans forward, arms swing back
    # 3. Take-off: rapid extension of legs/spine, arms swing up
    # 4. Airborne: knees/hips slightly flexed, arms above head
    # 5. Descend/landing: arms come down, knees flex
    # We'll interpolate biomechanically plausible trajectories

    # Encode the phase ("stand", "crouch", "extend", "air", "land") for each t
    if t < t_crouch:
        # Standing -> crouch
        ph = (t) / (t_crouch)
        # Interpolate key poses
        spine = 0.0 + ph*(-0.25)                 # radians, forward lean
        q_head = 0.0 + ph*(-0.10)
        q_hips = np.array([0.0, 0.0]) + ph*np.array([0.50, 0.40])  # L, R (flexion, + is forward)
        q_knees = np.array([0.0, 0.0]) + ph*np.array([1.15, 1.15])
        q_ankles = np.array([0.0,0.0]) + ph*np.array([-0.58, -0.56])
        q_shoulders = np.array([0.0, 0.0]) + ph*np.array([-0.55, 0.55])
        q_elbows = np.array([0.0, 0.0]) + ph*np.array([-1.0, 1.0])
        q_wrist = np.array([0.0, 0.0])
        dy = ph*(-0.28)      # pelvis drops

    elif t < t_launch:
        # Crouch hold, arms further back
        ph = (t - t_crouch) / (t_launch - t_crouch)
        spine = -0.25
        q_head = -0.10
        q_hips = np.array([0.50, 0.40])  + ph*np.array([-0.10,-0.10])
        q_knees = np.array([1.15,1.15])  + ph*np.array([ 0.10,0.10])
        q_ankles = np.array([-0.58,-0.56])+ ph*np.array([-0.08,-0.08])
        q_shoulders = np.array([-0.55, 0.55]) + ph*np.array([-0.30, 0.30])
        q_elbows = np.array([-1.0, 1.0]) + ph*np.array([-0.30,0.30])
        q_wrist = np.array([0.0, 0.0])
        dy = -0.28

    elif t < t_apex:
        # Launch (rapid extension) to air
        ph = (t - t_launch)/(t_apex - t_launch)
        # From crouch to "airborne" pose
        spine = -0.25 + ph*0.4
        q_head = -0.10 + ph*0.12
        q_hips = np.array([0.40,0.30]) + ph*np.array([-0.35,-0.22])
        q_knees = np.array([1.25,1.25]) + ph*np.array([-0.75,-0.83])
        q_ankles = np.array([-0.66,-0.64]) + ph*np.array([ 0.38, 0.30])
        q_shoulders = np.array([-0.85, 0.85]) + ph*np.array([1.35, -1.13])
        q_elbows = np.array([-1.3, 1.3]) + ph*np.array([1.50,-1.70])
        q_wrist = np.array([0.0, 0.0])
        # Vertical velocity is highest (simulate a ballistic jump arc):
        t0, t1 = t_launch, t_apex
        h0, h1 = -0.28, 0.16
        dy = h0 + (h1-h0)*(ph) - 0.27*0.5*(1-np.cos(ph*np.pi))  # parabola for apex

    elif t < t_land:
        # In air: flexed knees/hips, arms overhead. Back to down
        ph = (t - t_apex)/(t_land - t_apex)
        spine = 0.15 - ph*0.2
        q_head = 0.02 - ph*0.05
        q_hips = np.array([0.05,0.08]) + ph*np.array([0.25,0.20])
        q_knees = np.array([0.35,0.42]) + ph*np.array([0.55,0.55])
        q_ankles = np.array([-0.28,-0.34]) + ph*np.array([-0.17,-0.15])
        q_shoulders = np.array([0.5, -0.28]) + ph*np.array([-0.95, 0.92])
        q_elbows = np.array([0.20,-0.40]) + ph*np.array([-1.2, 1.2])
        q_wrist = np.array([0.0, 0.0])
        # Parabola path: apex (h=0.16) back to -0.18
        t0, t1 = t_apex, t_land
        ph2 = (t-t_apex)/(t_land-t_apex)
        dy = 0.16 + (-0.18-0.16)*ph2 - 0.22*0.5*(1-np.cos(ph2*np.pi)) # parabola fall

    else:
        # Landing: knees deep flexed, arms swing down, spine forward, then recover
        ph = (t - t_land)/(T-t_land)
        spine = -0.05 + ph*0.05
        q_head = -0.03 + ph*0.08
        q_hips = np.array([0.30,0.28]) + ph*np.array([-0.30,-0.28])
        q_knees = np.array([0.97,0.97]) + ph*np.array([-0.97,-0.97])
        q_ankles = np.array([-0.45,-0.45]) + ph*np.array([0.45,0.45])
        q_shoulders = np.array([-0.45,0.40]) + ph*np.array([0.45,-0.40])
        q_elbows = np.array([-1.0,1.0]) + ph*np.array([1.0,-1.0])
        q_wrist = np.array([0.0, 0.0])
        dy = -0.18 + (0.0+0.18)*ph

    # Add optional root motion: slight forward swing
    root_x = 0.0
    # Calculate vertical jump arc; model as: y(t) = v0*t - 0.5*g*t^2, but we use canonical profile above
    root_y = dy
    # Slight tilt? (simulate forward lean in crouch/land)
    if spine < -0.15:
        root_theta = -0.03
    elif spine > 0.15:
        root_theta = 0.02
    else:
        root_theta = 0.0

    return (q_knees, q_hips, q_ankles, q_shoulders, q_elbows, q_wrist, root_x, root_y, root_theta, q_head, spine)

# Visualization
def animate_jump():
    np.random.seed(0)
    fig, ax = plt.subplots(figsize=(4, 8))
    ax.set_facecolor("black")
    plt.axis("off")
    # aspect ratio
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.5, 2.1)
    # For smooth animation
    N_FRAMES = 90
    T = 1.25
    dt = T / N_FRAMES

    # Initial position
    pts = skeleton_pose(*jump_motion(0.0, T))
    scat = ax.scatter(pts[:,0], pts[:,1], s=60, c='white', edgecolors='none')

    def update(frame):
        t = frame * dt
        pts = skeleton_pose(*jump_motion(t, T))
        scat.set_offsets(pts)
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=N_FRAMES, interval=1000*dt, blit=True, repeat=True)
    plt.show()

if __name__ == "__main__":
    animate_jump()
