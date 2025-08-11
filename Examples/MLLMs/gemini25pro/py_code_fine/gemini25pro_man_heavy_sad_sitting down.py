
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Configuration ---
NUM_FRAMES = 130  # Slower, more deliberate motion for "heavy" feel
FIG_SIZE = (5, 9)
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'
POINT_SIZE = 8
X_LIMITS = (-50, 50)
Y_LIMITS = (-100, 50)
GROUND_Y_LEVEL = -90

# --- Kinematic Parameters ---
# Body part lengths, chosen to create a plausible human figure
L_THORAX = 35
L_NECK = 10
L_UPPER_ARM = 22
L_FOREARM = 24
L_THIGH = 28
L_SHIN = 26
SHOULDER_WIDTH = 12
PELVIS_WIDTH = 8

def get_pose(progress, x_offset, y_offset):
    """
    Calculates the 2D coordinates of all 15 joints for a given progress.
    Applies grounding offsets to the final coordinates.
    Angles are in radians, with 0 pointing right (standard math convention).
    """
    # --- Core Body Motion ---
    # Pelvis moves down and slightly back as one sits
    pelvis_y = np.interp(progress, [0, 1], [0, -35])
    pelvis_x = np.interp(progress, [0, 1], [0, -10])

    # Torso leans forward for balance, then settles slightly.
    # 90 degrees is vertical. Start slumped (90+8), lean forward (90+30), settle (90+25)
    torso_angle_deg = np.interp(progress, [0, 0.75, 1], [98, 120, 115])
    torso_angle_rad = np.radians(torso_angle_deg)
    
    thorax_x = pelvis_x + L_THORAX * np.cos(torso_angle_rad)
    thorax_y = pelvis_y + L_THORAX * np.sin(torso_angle_rad)
    
    # Head remains bowed forward relative to the torso angle
    head_angle_rad = torso_angle_rad + np.radians(20)
    head_x = thorax_x + L_NECK * np.cos(head_angle_rad)
    head_y = thorax_y + L_NECK * np.sin(head_angle_rad)

    # --- Shoulder and Hip Attachments ---
    # Shoulders are slightly slumped down from the thorax anchor
    l_shoulder_x, r_shoulder_x = thorax_x - SHOULDER_WIDTH, thorax_x + SHOULDER_WIDTH
    l_shoulder_y, r_shoulder_y = thorax_y - 2, thorax_y - 2
    
    l_hip_x, r_hip_x = pelvis_x - PELVIS_WIDTH, pelvis_x + PELVIS_WIDTH
    l_hip_y, r_hip_y = pelvis_y, pelvis_y

    # --- Leg Kinematics (Forward) ---
    # Thigh flexion: starts almost straight (5 deg from vertical), ends at 95 deg
    hip_flex_deg = np.interp(progress, [0, 1], [5, 95])
    thigh_angle_deg = 270 - hip_flex_deg
    
    # Knee flexion: starts straight (5 deg), bends to 90 deg
    knee_flex_deg = np.interp(progress, [0, 1], [5, 90])
    
    # Right Leg
    r_thigh_angle_rad = np.radians(thigh_angle_deg)
    r_shin_angle_rad = r_thigh_angle_rad - np.radians(knee_flex_deg)
    
    r_knee_x = r_hip_x + L_THIGH * np.cos(r_thigh_angle_rad)
    r_knee_y = r_hip_y + L_THIGH * np.sin(r_thigh_angle_rad)
    r_ankle_x = r_knee_x + L_SHIN * np.cos(r_shin_angle_rad)
    r_ankle_y = r_knee_y + L_SHIN * np.sin(r_shin_angle_rad)

    # Left Leg (staggered slightly for depth)
    l_thigh_angle_rad = np.radians(thigh_angle_deg - 2)
    l_shin_angle_rad = l_thigh_angle_rad - np.radians(knee_flex_deg)

    l_knee_x = l_hip_x + L_THIGH * np.cos(l_thigh_angle_rad)
    l_knee_y = l_hip_y + L_THIGH * np.sin(l_thigh_angle_rad)
    l_ankle_x = l_knee_x + L_SHIN * np.cos(l_shin_angle_rad)
    l_ankle_y = l_knee_y + L_SHIN * np.sin(l_shin_angle_rad)

    # --- Arm Kinematics (Forward) ---
    # Arms move forward to balance and then rest on thighs
    shoulder_flex_deg = np.interp(progress, [0, 1], [10, 70])
    upper_arm_angle_deg = 270 - shoulder_flex_deg
    
    elbow_flex_deg = np.interp(progress, [0, 1], [15, 85])
    
    # Right Arm
    r_upper_arm_angle_rad = np.radians(upper_arm_angle_deg)
    r_forearm_angle_rad = r_upper_arm_angle_rad - np.radians(elbow_flex_deg)

    r_elbow_x = r_shoulder_x + L_UPPER_ARM * np.cos(r_upper_arm_angle_rad)
    r_elbow_y = r_shoulder_y + L_UPPER_ARM * np.sin(r_upper_arm_angle_rad)
    r_wrist_x = r_elbow_x + L_FOREARM * np.cos(r_forearm_angle_rad)
    r_wrist_y = r_elbow_y + L_FOREARM * np.sin(r_forearm_angle_rad)

    # Left Arm (staggered)
    l_upper_arm_angle_rad = np.radians(upper_arm_angle_deg - 4)
    l_forearm_angle_rad = l_upper_arm_angle_rad - np.radians(elbow_flex_deg)
    
    l_elbow_x = l_shoulder_x + L_UPPER_ARM * np.cos(l_upper_arm_angle_rad)
    l_elbow_y = l_shoulder_y + L_UPPER_ARM * np.sin(l_upper_arm_angle_rad)
    l_wrist_x = l_elbow_x + L_FOREARM * np.cos(l_forearm_angle_rad)
    l_wrist_y = l_elbow_y + L_FOREARM * np.sin(l_forearm_angle_rad)
    
    # --- Assemble and Apply Grounding ---
    coords = np.array([
        [head_x, head_y], [thorax_x, thorax_y], [pelvis_x, pelvis_y],
        [l_shoulder_x, l_shoulder_y], [r_shoulder_x, r_shoulder_y],
        [l_hip_x, l_hip_y], [r_hip_x, r_hip_y],
        [l_elbow_x, l_elbow_y], [r_elbow_x, r_elbow_y],
        [l_wrist_x, l_wrist_y], [r_wrist_x, r_wrist_y],
        [l_knee_x, l_knee_y], [r_knee_x, r_knee_y],
        [l_ankle_x, l_ankle_y], [r_ankle_x, r_ankle_y]
    ])
    
    # Apply the pre-calculated offsets to ground the figure
    coords += [x_offset, y_offset]
    return coords

# --- Main Animation Setup ---
fig, ax = plt.subplots(figsize=FIG_SIZE)
fig.patch.set_facecolor(BACKGROUND_COLOR)
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(X_LIMITS)
ax.set_ylim(Y_LIMITS)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# --- Calculate Grounding Offset ---
# Get the raw pose at the start (progress=0) without any offset
initial_coords = get_pose(0, 0, 0)
# Find the average initial position of the ankles
initial_ankle_y = (initial_coords[13, 1] + initial_coords[14, 1]) / 2.0
initial_ankle_x = (initial_coords[13, 0] + initial_coords[14, 0]) / 2.0
# Calculate the offset needed to move the feet to the ground level and center them
y_offset = GROUND_Y_LEVEL - initial_ankle_y
x_offset = 0 - initial_ankle_x

# Create the 15 point objects for the animation
points = [ax.plot([], [], 'o', color=POINT_COLOR, markersize=POINT_SIZE)[0] for _ in range(15)]

def init():
    """Initializes the plot for the animation."""
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    """Updates the positions of the points for each frame."""
    # Use a cosine easing function for smooth acceleration and deceleration
    progress = (1 - np.cos(np.pi * frame / NUM_FRAMES)) / 2.0
    
    # Get the coordinates for the current state of the animation
    coords = get_pose(progress, x_offset, y_offset)
    
    # Update the data for each point
    for i, point in enumerate(points):
        point.set_data(coords[i, 0], coords[i, 1])
        
    return points

# Create and run the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=NUM_FRAMES,
    init_func=init,
    blit=True,
    interval=40  # Corresponds to 25 FPS
)

plt.show()
