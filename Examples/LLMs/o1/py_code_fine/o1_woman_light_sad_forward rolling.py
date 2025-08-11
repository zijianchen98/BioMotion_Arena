import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------------------------
# A NOTE TO THE READER:
# ------------------------------------------------------------------------------
# The following code provides a simplified example of animating 15 point-lights
# in 2D to approximate a "sad" figure performing a forward roll. In reality,
# achieving truly realistic, biomechanically plausible motion often involves
# motion-capture data, inverse kinematics, and more sophisticated modeling.
# This script is a basic illustration of how one might build a point-light
# stimulus in Python using matplotlib for demonstration purposes only.
# ------------------------------------------------------------------------------

# Number of point-lights
NUM_POINTS = 15

# Total frames in the animation
NUM_FRAMES = 60

# Duration of the animation in seconds (for timing reference)
DURATION = 4.0

# Frames per second
FPS = NUM_FRAMES / DURATION

# ------------------------------------------------------------------------------
# 1. Define a "base posture" of the figure (15 points) in a neutral pose.
#    We'll treat (0,0) as the center of mass (COM).
#
#    The arrangement below is a rough, 2D "skeleton" with a somewhat "slumped"
#    upper torso to suggest a sad pose. Each row is [x, y] for one joint/light.
# ------------------------------------------------------------------------------

base_pose = np.array([
    [ 0.0,  0.15],  # 1  Head (slightly forward to look sad)
    [ 0.0,  0.10],  # 2  Neck
    [-0.05, 0.10],  # 3  Left shoulder
    [ 0.05, 0.10],  # 4  Right shoulder
    [-0.08, 0.05],  # 5  Left elbow
    [ 0.08, 0.05],  # 6  Right elbow
    [-0.10, 0.00],  # 7  Left wrist
    [ 0.10, 0.00],  # 8  Right wrist
    [ 0.0,   0.05], # 9  Upper torso (chest)
    [ 0.0,   0.00], # 10 Mid torso
    [ 0.0,  -0.05], # 11 Lower torso (waist)
    [-0.05, -0.06], # 12 Left hip
    [ 0.05, -0.06], # 13 Right hip
    [-0.05, -0.12], # 14 Left knee
    [ 0.05, -0.12], # 15 Right knee
])

# ------------------------------------------------------------------------------
# 2. Define a function to generate the position of each of the 15 points over
#    time as the figure performs a forward roll. We'll do this by:
#    - Rotating the entire "base_pose" around an imaginary pivot to simulate
#      a roll.
#    - Adding minor flexion/extension changes in arms/legs to give some motion
#      variation.
# ------------------------------------------------------------------------------
def get_frame_positions(frame_index):
    """
    Returns an array of shape (15, 2) containing (x,y) positions
    for each point-light at the specified frame index.
    """
    # Time parameter in [0, 1] across the entire roll
    t = frame_index / float(NUM_FRAMES - 1)
    
    # Angle of the full-body rotation (one full revolution ~ 2*pi)
    # We'll do slightly more than one roll to be sure it completes.
    full_rolls = 1.2
    rotation_angle = 2.0 * np.pi * full_rolls * t
    
    # We'll revolve the figure forward along an arc. The center of this rotation
    # will move forward slightly over time to simulate traveling forward.
    radius = 0.1  # approximate radius for the forward roll
    pivot_x = -0.2 + 0.4 * t  # move left to right across the screen
    pivot_y = -0.05           # slight vertical offset for the pivot

    # Rotation matrix around (0,0)
    R = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle)],
        [np.sin(rotation_angle),  np.cos(rotation_angle)]
    ])
    
    # Copy the base pose for manipulation
    points = base_pose.copy()

    # Minor "flexion/extension" in arms/legs:
    # We'll modulate elbow and knee positions with small sinusoidal offsets.
    # Indices in base_pose: 
    #   left elbow = 4, right elbow = 5, left wrist = 6, right wrist = 7
    #   left knee = 13, right knee = 14
    arm_leg_offset = 0.02 * np.sin(2.0 * np.pi * 2.0 * t)  # 2 cycles of flex
    # Apply to left elbow, right elbow
    points[4,1] += arm_leg_offset
    points[5,1] += arm_leg_offset
    # Apply to left knee, right knee
    points[13,1] -= arm_leg_offset
    points[14,1] -= arm_leg_offset

    # First translate each point so that COM is at the origin, then rotate, then
    # shift by the pivot location.
    # We'll treat the COM as roughly the midpoint among the torso points (indices 8,9,10).
    torso_indices = [8, 9, 10]
    com = points[torso_indices].mean(axis=0)
    # Shift so COM is at origin
    shifted = points - com
    
    # Rotate around the origin
    rotated = R @ shifted.T
    rotated = rotated.T
    
    # Now shift everything so that the pivot sits at (pivot_x, pivot_y).
    # We'll place the COM a certain distance from the pivot to produce the rolling arc.
    # The pivot is about radius away from COM in a circular path:
    # We'll add to pivot the "arc" offset for the COM.
    # For a forward roll, let COM circle around pivot with the same rotation_angle.
    circle_x = radius * np.sin(rotation_angle)
    circle_y = radius * np.cos(rotation_angle)
    
    # Shift entire figure so COM is on that circle around the pivot
    # ( pivot_x + circle_x, pivot_y + circle_y )
    final = rotated + np.array([pivot_x + circle_x, pivot_y + circle_y])
    
    return final

# ------------------------------------------------------------------------------
# 3. Set up the figure and animation. We will draw 15 white points on a black
#    background.
# ------------------------------------------------------------------------------

# Create the figure and axes
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-0.4, 0.4)
ax.set_ylim(-0.2, 0.2)
ax.set_aspect('equal', adjustable='box')

# Set black background
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Turn off axis ticks/labels
plt.axis('off')

# Initialize a scatter plot for the 15 points (white dots)
scatter = ax.scatter([], [], c='white', s=50)

def init():
    """Initialize the scatter plot to empty for the animation."""
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    """Update function for each frame in the animation."""
    positions = get_frame_positions(frame)
    scatter.set_offsets(positions)
    return (scatter,)

# Create the animation
anim = animation.FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=NUM_FRAMES,
    interval=1000.0/FPS,
    blit=True
)

# ------------------------------------------------------------------------------
# 4. Display the animation
#    Note: In many environments, simply calling plt.show() will play the animation.
#          If you run this in certain notebooks, you might need additional inline
#          settings or to use HTML video display. For a standard Python script,
#          plt.show() suffices.
# ------------------------------------------------------------------------------
plt.show()