
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin, cos, pi

# Initialize the points in a standing position
initial_points = np.array([
    [0, 1.8],    #0 head
    [0, 1.6],    #1 neck
    [-0.2, 1.5], #2 left_shoulder
    [0.2, 1.5],  #3 right_shoulder
    [-0.2, 1.1], #4 left_elbow
    [0.2, 1.1],  #5 right_elbow
    [-0.2, 0.7], #6 left_wrist
    [0.2, 0.7],  #7 right_wrist
    [0, 0.9],    #8 mid_hip
    [-0.2, 0.9], #9 left_hip
    [0.2, 0.9],  #10 right_hip
    [-0.2, 0.5], #11 left_knee
    [0.2, 0.5],  #12 right_knee
    [-0.2, 0],   #13 left_ankle
    [0.2, 0]     #14 right_ankle
])

# Set up the figure and axis
fig = plt.figure(figsize=(6, 8), facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initial scatter plot
scatter = ax.scatter(initial_points[:,0], initial_points[:,1], s=30, c='white')

# Animation update function
def update(frame):
    # Total frames per cycle: 100
    t = 2 * pi * frame / 100
    # Calculate trunk rotation angle (max 30 degrees) in radians
    trunk_angle = (30 * pi / 180) * sin(t)
    # Vertical drop of the body (max 0.2)
    drop = 0.2 * sin(t)
    # Slight forward shift (max 0.1)
    forward_shift = 0.1 * sin(t)
    
    # Calculate transformation parameters
    M0 = np.array([0.0, 0.9])
    new_mid_hip = np.array([forward_shift, 0.9 - drop])
    R_matrix = np.array([
        [cos(trunk_angle), -sin(trunk_angle)],
        [sin(trunk_angle), cos(trunk_angle)]
    ])
    
    # Initialize transformed points
    transformed_points = initial_points.copy()
    
    # Apply transformation to points 0 to 12
    for i in range(13):  # Transform points 0 to 12
        # Vector from the initial mid_hip to the current point
        v = initial_points[i] - M0
        # Rotate the vector
        v_rotated = R_matrix.dot(v)
        # Set new position
        transformed_points[i] = new_mid_hip + v_rotated
    
    # Keep ankles fixed at their initial positions (indices 13 and 14)
    # Adjust knees to be directly above ankles and below hips
    transformed_points[11] = [transformed_points[9][0], initial_points[11][1] - drop]   # left_knee
    transformed_points[12] = [transformed_points[10][0], initial_points[12][1] - drop]  # right_knee
    
    # Update scatter plot data
    scatter.set_offsets(transformed_points)
    return scatter,

# Create and save the animation
ani = animation.FuncAnimation(
    fig, update, frames=100, interval=100, blit=True
)

plt.tight_layout()
plt.show()
