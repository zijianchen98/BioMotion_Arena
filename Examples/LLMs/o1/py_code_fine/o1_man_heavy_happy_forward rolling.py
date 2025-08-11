import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------
# Create a point-light biological motion stimulus in Python
# of a "happy man with heavy weight" doing a forward roll
# with 15 white point-lights on black background.
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1) Define the base skeleton (15 points) for an upright pose.
#    Coordinates are relative to a center near the torso.
# ------------------------------------------------------------
base_skeleton = np.array([
    [ 0.0,  1.8],  #  1. Head
    [ 0.0,  1.6],  #  2. Neck
    [ 0.2,  1.6],  #  3. Right shoulder
    [ 0.3,  1.2],  #  4. Right elbow
    [ 0.3,  0.9],  #  5. Right hand
    [-0.2,  1.6],  #  6. Left shoulder
    [-0.3,  1.2],  #  7. Left elbow
    [-0.3,  0.9],  #  8. Left hand
    [ 0.0,  1.1],  #  9. Torso center
    [ 0.15, 1.0],  # 10. Right hip
    [ 0.15, 0.6],  # 11. Right knee
    [ 0.15, 0.0],  # 12. Right foot
    [-0.15, 1.0],  # 13. Left hip
    [-0.15, 0.6],  # 14. Left knee
    [-0.15, 0.0],  # 15. Left foot
])

# We'll treat the "torso center" (index=8 in the array) as a reference.
# Shift base_skeleton so that "torso center" is at (0, 0) for ease of rotation.
torso_center = base_skeleton[8].copy()
base_skeleton_shifted = base_skeleton - torso_center  # center at (0,0)

# ------------------------------------------------------------
# 2) Define a function to rotate and translate the skeleton.
#    angle: rotation in radians
#    center: translation (x, y)
# ------------------------------------------------------------
def transform_skeleton(base_points, angle, center):
    # Rotation matrix (2x2) for given angle
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    R = np.array([[cos_a, -sin_a],
                  [sin_a,  cos_a]])
    
    # Rotate and then translate
    rotated = base_points.dot(R.T)
    translated = rotated + center
    return translated

# ------------------------------------------------------------
# 3) Configure and set up the animation using Matplotlib.
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 5))
# Make background black
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# Prepare scatter plot for the 15 white point-lights
scatter = ax.scatter([], [], s=50, c="white")

# Remove axes, ticks, etc.
ax.set_xlim(-1.5, 3.5)
ax.set_ylim(-0.5, 2.5)
plt.axis("off")

# ------------------------------------------------------------
# 4) Animation update function
# We'll simulate one full forward roll over N frames.
# ------------------------------------------------------------
frames = 100  # total number of frames for one roll

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Fraction of the roll completed
    t = frame / (frames - 1)
    
    # Move from x=0 to x=2 while rotating from angle=0 to angle=2*pi
    x_center = 2.0 * t
    y_center = 1.0
    angle = 2.0 * np.pi * t
    
    # Forward roll transformation
    changed_points = transform_skeleton(base_skeleton_shifted, angle, (x_center, y_center))
    
    # Update scatter data
    scatter.set_offsets(changed_points)
    return (scatter,)

anim = animation.FuncAnimation(
    fig, update, frames=frames, init_func=init, interval=50, blit=True
)

plt.show()