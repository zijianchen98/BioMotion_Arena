
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Marker order (15): Head, R Shoulder, L Shoulder, R Elbow, L Elbow,
# R Wrist, L Wrist, Hip, R Hip, L Hip,
# R Knee, L Knee, R Ankle, L Ankle, Weight (in both hands)
# The "center of mass" is roughly between the hips.

def rolling_happyman_pose(t, radius=1.35):
    # t: phase in [0, 2pi]
    # Circle center for rolling: (cx, cy)
    cx, cy = 0, 0
    # The full loop represents a roll, period = 2pi
    theta = t
    # The body rotates as a stiff stick, legs and arms bend correctly

    # Torso length (shoulder to hip)
    torso = 0.45
    head_r = 0.14
    shoulder_w = 0.33
    hip_w = 0.26

    upper_arm = 0.27
    lower_arm = 0.26

    upper_leg = 0.41
    lower_leg = 0.37
    ankle_gap = 0.16

    # Place circle positions for rolling
    # Let's imagine the center of mass traces a circle, height is radius above ground
    # Head is further above

    # Find center of mass
    body_theta = theta
    body_x = cx + radius * np.sin(body_theta)
    body_y = cy + radius * np.cos(body_theta)

    # The body is rotated by "body_theta"
    # Compute orientation vector (unit vector from hip to head)
    orient = -body_theta
    orient_vec = np.array([np.sin(orient), np.cos(orient)])  # up direction

    # Place hips (centered at body_x, body_y)
    hip_center = np.array([body_x, body_y])
    hip_r = orient + np.pi/2
    hip_L = hip_center + hip_w/2 * np.array([np.cos(hip_r), np.sin(hip_r)])
    hip_R = hip_center - hip_w/2 * np.array([np.cos(hip_r), np.sin(hip_r)])

    # Place shoulders (above hips along body axis)
    shoulder_center = hip_center + torso*orient_vec
    shoulder_r = orient + np.pi/2
    shoulder_L = shoulder_center + shoulder_w/2 * np.array([np.cos(shoulder_r), np.sin(shoulder_r)])
    shoulder_R = shoulder_center - shoulder_w/2 * np.array([np.cos(shoulder_r), np.sin(shoulder_r)])

    # Head
    head = shoulder_center + head_r*1.2*orient_vec

    # Arms: individual shoulders to wrist (elbow bends)
    # To carry "heavy weight", both hands are held together at chest center, arms bent, "hugging" the weight.

    # The "weight" is an extra marker, in front of chest.
    weight_offset = orient_vec * 0.12 + np.array([np.cos(orient + np.pi/2), np.sin(orient + np.pi/2)]) * 0.05
    weight = shoulder_center + torso*0.37*orient_vec + weight_offset

    def bent_arm(shoulder, target, elbow_angle):
        # Compute elbow position given angle, shoulder, target (hand)
        vec = target - shoulder
        len_total = np.linalg.norm(vec)
        if len_total > upper_arm + lower_arm:
            elbow = shoulder + (upper_arm/len_total)*(vec)
            return elbow, target
        # Law of cosines for the triangle
        a = upper_arm
        b = lower_arm
        c = len_total
        # Find intersection of two circles around shoulder and hand (arm lengths)
        mid = shoulder + 0.5 * vec
        dir_perp = np.array([-vec[1], vec[0]]) / (np.linalg.norm(vec) + 1e-8)
        h = np.sqrt(max(0, a**2 - (c/2)**2))
        elbow = mid + h * dir_perp * (-1 if elbow_angle == "up" else 1)
        return elbow, target

    # Arms toward the "weight"
    elbow_R, wrist_R = bent_arm(shoulder_R, weight, "up")
    elbow_L, wrist_L = bent_arm(shoulder_L, weight, "up")

    # Legs: Hips to ankles (with knee bend)
    # In a roll, the legs are pulled close in a tuck, and alternately extend as the body rolls.
    leg_tuck = 0.45 + 0.25 * np.cos(theta+np.pi)
    # Phase for each leg for plausible rolling
    phase_L = theta
    phase_R = theta + np.pi
    knee_ang_L = np.deg2rad(80 + 30*np.sin(phase_L))
    knee_ang_R = np.deg2rad(80 + 30*np.sin(phase_R))
    # "Knee forward" vector
    def bent_leg(hip, foot, knee_ang, out_sign):
        vec = foot - hip
        d = np.linalg.norm(vec)
        if d > upper_leg + lower_leg:
            knee = hip + (upper_leg/d)*(vec)
            return knee, foot
        # Law of cosines
        a = upper_leg
        b = lower_leg
        c = d
        mid = hip + 0.5*vec
        dir_perp = np.array([-vec[1], vec[0]]) / (np.linalg.norm(vec) + 1e-8)
        h = np.sqrt(max(0, a**2 - (c/2)**2))
        knee = mid + out_sign * h * dir_perp
        return knee, foot

    # Ankle positions: closely tucked in a rolling ball, opening and closing cyclically
    ankle_L = hip_L + (-0.19*orient_vec
                       + ankle_gap/2 * np.array([np.cos(orient+np.pi/2), np.sin(orient+np.pi/2)])
                       -0.19 * np.array([np.cos(orient), np.sin(orient)])
                       + 0.17*np.array([np.cos(orient-np.pi/2), np.sin(orient-np.pi/2)]) * np.sin(theta)*0.6)
    ankle_R = hip_R + (-0.19*orient_vec
                       - ankle_gap/2 * np.array([np.cos(orient+np.pi/2), np.sin(orient+np.pi/2)])
                       -0.19 * np.array([np.cos(orient), np.sin(orient)])
                       - 0.17*np.array([np.cos(orient-np.pi/2), np.sin(orient-np.pi/2)]) * np.sin(theta)*0.6)

    knee_L, _ = bent_leg(hip_L, ankle_L, knee_ang_L, +1)
    knee_R, _ = bent_leg(hip_R, ankle_R, knee_ang_R, -1)

    # Hip (center), L hip, R hip, L knee, R knee, L ankle, R ankle

    # Order: Head, R Shoulder, L Shoulder, R Elbow, L Elbow,
    # R Wrist, L Wrist, Hip(center), R Hip, L Hip,
    # R Knee, L Knee, R Ankle, L Ankle, Weight
    return np.array([
        head,
        shoulder_R, shoulder_L,
        elbow_R, elbow_L,
        wrist_R, wrist_L,
        hip_center, hip_R, hip_L,
        knee_R, knee_L,
        ankle_R, ankle_L,
        weight
    ])

# Visualization
fig, ax = plt.subplots(figsize=(3.2, 5.6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.axis('off')

# Set animation bounds. We'll "roll" forward horizontally
xlim = (-1.2, 1.2)
ylim = (-1.6, 1.5)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

scatter = ax.scatter([], [], s=39, c='w', edgecolors='none')

# main animation loop
frames = 120
# Full roll period = 2pi; stride forward per roll = 1.1 units
stride = 1.1

def init():
    scatter.set_offsets(np.zeros((15,2)))
    return scatter,

def animate(i):
    t = (2*np.pi) * (i / frames)
    # Advance horizontally to create forward rolling
    # The "roll" is actually a translation as well as a rotation
    x_offset = (stride / (2*np.pi)) * t
    positions = rolling_happyman_pose(t)
    # Apply forward translation
    positions[:,0] += x_offset
    scatter.set_offsets(positions)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=25, init_func=init, blit=True)

plt.show()
