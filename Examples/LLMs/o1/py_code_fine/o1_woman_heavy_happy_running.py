import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_joint_positions(t):
    """
    Returns a (15, 2) numpy array with the (x, y) positions of 15 point-lights
    representing a running "happy woman with heavy weight". This is a simplified
    2D side-view approximation using basic sine-wave kinematics for demonstration.
    """
    # Time parameters
    freq = 2.0               # Stride frequency (cycles per second)
    phase = 2 * np.pi * freq * t
    
    # Body segment lengths (approximate, in arbitrary units)
    torso_len = 0.4
    head_len = 0.1
    upper_arm_len = 0.25
    lower_arm_len = 0.25
    upper_leg_len = 0.4
    lower_leg_len = 0.4
    
    # Horizontal movement speed (units per second)
    speed = 0.5
    
    # Vertical bounce parameters
    bounce_amplitude = 0.05
    base_height = 0.55  # base offset so feet stay above y=0

    # Angles (radians) driven by sine waves to simulate running
    # (Heavier running can be emulated by slightly lower frequency + pronounced bounce)
    # Leg angles
    max_leg_swing = 0.8
    left_leg_angle = max_leg_swing * np.sin(phase)
    right_leg_angle = -max_leg_swing * np.sin(phase)
    
    # Knee angles (bending more when the leg is forward/back)
    # Attempting a simple relation: knee angle ~ half the thigh angle, but offset to emulate flexion
    left_knee_angle =  0.5 * left_leg_angle - 0.3
    right_knee_angle = 0.5 * right_leg_angle - 0.3
    
    # Arms move roughly out of phase with the legs
    max_arm_swing = 0.4
    left_arm_angle = max_arm_swing * np.sin(phase + np.pi)
    right_arm_angle = max_arm_swing * np.sin(phase)
    
    # Elbow bending
    left_elbow_angle =  0.5 * left_arm_angle - 0.2
    right_elbow_angle = 0.5 * right_arm_angle - 0.2
    
    # Horizontal and vertical position of the pelvis (base of torso)
    pelvis_x = speed * t
    pelvis_y = base_height + bounce_amplitude * np.sin(phase)
    
    # Build the chain of coordinates for each of the 15 points.
    # 1) Pelvis
    pelvis = np.array([pelvis_x, pelvis_y])

    # 2) Torso (above pelvis)
    torso = pelvis + np.array([0.0, torso_len])

    # 3) Head (above torso)
    head = torso + np.array([0.0, head_len])

    # Shoulders (approximate width offset from torso center)
    shoulder_offset = 0.15
    left_shoulder = torso + np.array([-shoulder_offset, 0.0])
    right_shoulder = torso + np.array([ shoulder_offset, 0.0])

    # Hips similarly offset from pelvis center (slightly narrower than shoulders)
    hip_offset = 0.1
    left_hip = pelvis + np.array([-hip_offset, 0.0])
    right_hip = pelvis + np.array([ hip_offset, 0.0])

    # Compute elbow coordinates:
    # For left elbow, pivot from left shoulder with angle left_arm_angle
    # Direction is somewhat forward/back. We'll treat "forward" as negative x from side-view angle.
    def rotate(point, center, angle, length):
        """Rotate a 'length' 2D vector from center by 'angle' (counterclockwise),
           here we assume we rotate around negative x for forward swing in side-view."""
        # In side-view, negative angle in x means forward on the screen, so adjust sign as needed.
        # For simplicity, treat angle as rotating around the (x) axis in the plane. We just do 2D rotation.
        dx = length * np.sin(angle)
        dy = length * np.cos(angle)
        return center + np.array([dx, dy])
    
    left_elbow = rotate(left_shoulder, left_shoulder, left_arm_angle,  upper_arm_len)
    left_wrist = rotate(left_elbow,    left_elbow,    left_elbow_angle, lower_arm_len)
    
    right_elbow = rotate(right_shoulder, right_shoulder, right_arm_angle,  upper_arm_len)
    right_wrist = rotate(right_elbow,     right_elbow,    right_elbow_angle, lower_arm_len)
    
    # Compute knees and ankles for legs
    left_knee = rotate(left_hip, left_hip, left_leg_angle, upper_leg_len)
    left_ankle = rotate(left_knee, left_knee, left_knee_angle, lower_leg_len)
    
    right_knee = rotate(right_hip, right_hip, right_leg_angle, upper_leg_len)
    right_ankle = rotate(right_knee, right_knee, right_knee_angle, lower_leg_len)
    
    # Middle of shoulders (approx torso top center) as an extra "torso center" point
    torso_center = 0.5 * (left_shoulder + right_shoulder)
    
    # Combine all 15 points in a consistent order
    points = np.array([
        head,            # 1
        pelvis,          # 2
        torso,           # 3
        left_shoulder,   # 4
        left_elbow,      # 5
        left_wrist,      # 6
        right_shoulder,  # 7
        right_elbow,     # 8
        right_wrist,     # 9
        left_hip,        # 10
        left_knee,       # 11
        left_ankle,      # 12
        right_hip,       # 13
        right_knee,      # 14
        right_ankle      # 15
    ])
    return points

def update(frame):
    # Compute the time in seconds for current frame
    t = frame / float(fps)
    pts = get_joint_positions(t)
    scatter.set_offsets(pts)
    return scatter,

# Set up the figure and animation
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')  # Black background
ax.set_facecolor('black')
ax.set_xlim(-1, 3)
ax.set_ylim(0, 1.5)
ax.axis('off')

# Prepare scatter plot for 15 white points
initial_positions = get_joint_positions(0)
scatter = ax.scatter(initial_positions[:,0], initial_positions[:,1],
                     s=50, c='white', edgecolors='none')

# Animation parameters
fps = 30
frames = 180  # ~6 seconds of animation 
anim = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()