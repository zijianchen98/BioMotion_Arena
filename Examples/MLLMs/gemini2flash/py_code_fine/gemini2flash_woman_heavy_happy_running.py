
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points
num_points = 15

# Define the initial positions of the points. Adjust these to represent a running woman.
# These are just initial positions; the animation will modify these based on the running motion.
initial_positions = np.array([
    [0, 2.0],   # Head
    [-0.2, 1.5],  # Left Shoulder
    [0.2, 1.5],   # Right Shoulder
    [-0.4, 1.0],  # Left Elbow
    [0.4, 1.0],   # Right Elbow
    [-0.6, 0.5],  # Left Wrist
    [0.6, 0.5],   # Right Wrist
    [-0.1, 1.2],  # Torso Top Left
    [0.1, 1.2],   # Torso Top Right
    [-0.1, 0.6],  # Torso Bottom Left
    [0.1, 0.6],   # Torso Bottom Right
    [-0.3, 0.0],  # Left Hip
    [0.3, 0.0],   # Right Hip
    [-0.5, -0.7], # Left Knee
    [0.5, -0.7]  # Right Knee
])


# Define the function that updates the positions of the points for each frame
def update_points(frame_num, points):
    # Simulate the running motion by oscillating the positions of the points
    # The oscillations should be coordinated to resemble a running motion
    # Make adjustments here to reflect heavy woman
    
    # Torso Movement (slight sway)
    torso_sway = np.sin(frame_num * 0.1) * 0.05 
    
    # Arm Movements
    left_arm_angle = np.sin(frame_num * 0.2) * 0.4
    right_arm_angle = np.sin(frame_num * 0.2 + np.pi) * 0.4
    
    # Leg Movements
    left_leg_angle = np.sin(frame_num * 0.2 + np.pi) * 0.7
    right_leg_angle = np.sin(frame_num * 0.2) * 0.7
    
    # Update point positions
    points.set_offsets([
        [initial_positions[0, 0], initial_positions[0, 1]], # Head
        [initial_positions[1, 0] + left_arm_angle * 0.5, initial_positions[1, 1] + left_arm_angle * 0.2], # Left Shoulder
        [initial_positions[2, 0] + right_arm_angle * 0.5, initial_positions[2, 1] + right_arm_angle * 0.2], # Right Shoulder
        [initial_positions[3, 0] + left_arm_angle * 1.0, initial_positions[3, 1] + left_arm_angle * 0.4], # Left Elbow
        [initial_positions[4, 0] + right_arm_angle * 1.0, initial_positions[4, 1] + right_arm_angle * 0.4], # Right Elbow
        [initial_positions[5, 0] + left_arm_angle * 1.5, initial_positions[5, 1] + left_arm_angle * 0.6], # Left Wrist
        [initial_positions[6, 0] + right_arm_angle * 1.5, initial_positions[6, 1] + right_arm_angle * 0.6], # Right Wrist
        [initial_positions[7, 0] + torso_sway, initial_positions[7, 1]], # Torso Top Left
        [initial_positions[8, 0] + torso_sway, initial_positions[8, 1]], # Torso Top Right
        [initial_positions[9, 0] + torso_sway, initial_positions[9, 1]], # Torso Bottom Left
        [initial_positions[10, 0] + torso_sway, initial_positions[10, 1]], # Torso Bottom Right
        [initial_positions[11, 0] + left_leg_angle * 0.3, initial_positions[11, 1] - left_leg_angle * 0.6], # Left Hip
        [initial_positions[12, 0] + right_leg_angle * 0.3, initial_positions[12, 1] - right_leg_angle * 0.6], # Right Hip
        [initial_positions[13, 0] + left_leg_angle * 1.2, initial_positions[13, 1] - left_leg_angle * 1.2], # Left Knee
        [initial_positions[14, 0] + right_leg_angle * 1.2, initial_positions[14, 1] - right_leg_angle * 1.2]  # Right Knee
    ])
    return points,


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
plt.axis('off') # Hide the axes

# Create the scatter plot for the points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), frames=num_frames, blit=False, repeat=True)

# Show the animation
plt.show()
