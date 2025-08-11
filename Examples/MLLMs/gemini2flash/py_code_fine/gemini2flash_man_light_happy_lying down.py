
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 200

# Define the initial positions of the 15 point-lights for a lying down person
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5],  # Left shoulder
    [0.3, 1.5],  # Right shoulder
    [-0.6, 1.0],  # Left elbow
    [0.6, 1.0],  # Right elbow
    [-0.9, 0.5],  # Left wrist
    [0.9, 0.5],  # Right wrist
    [-0.1, 1.0],  # Spine top
    [0.1, 1.0],
    [-0.1, 0.5],  # Spine bottom
    [0.1, 0.5],
    [-0.3, -0.5],  # Left hip
    [0.3, -0.5],  # Right hip
    [-0.1, -1.0],  # Left knee
    [0.1, -1.0]   # Right knee
])

# Define functions to create more realistic and coherent motion

# Example: Subtle arm movement
def arm_movement(frame):
    angle = np.sin(frame / 20) * 0.2  # Angle changes over time
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    left_elbow = initial_positions[3] + np.array([-0.1*np.sin(frame/10),0.05*np.cos(frame/10)])
    right_elbow = initial_positions[4] + np.array([0.1*np.sin(frame/10),0.05*np.cos(frame/10)])
    left_wrist = initial_positions[5] + np.array([-0.15*np.sin(frame/10),0.1*np.cos(frame/10)])
    right_wrist = initial_positions[6] + np.array([0.15*np.sin(frame/10),0.1*np.cos(frame/10)])

    return left_elbow,right_elbow,left_wrist,right_wrist

# Example: Subtle leg movement
def leg_movement(frame):
    angle = np.cos(frame / 20) * 0.1  # Angle changes over time

    left_knee = initial_positions[13] + np.array([-0.05*np.cos(frame/10),0.05*np.sin(frame/10)])
    right_knee = initial_positions[14] + np.array([0.05*np.cos(frame/10),0.05*np.sin(frame/10)])

    return left_knee,right_knee

# Function to update the positions of the points for each frame
def update_points(frame):
    positions = initial_positions.copy()
    left_elbow,right_elbow,left_wrist,right_wrist = arm_movement(frame)
    left_knee,right_knee = leg_movement(frame)

    positions[3] = left_elbow
    positions[4] = right_elbow
    positions[5] = left_wrist
    positions[6] = right_wrist
    positions[13] = left_knee
    positions[14] = right_knee

    # Add a small translation to give the illusion of moving forward slightly
    positions[:, 0] += np.sin(frame / 100) * 0.01

    # Make the entire figure slightly rotate back and forth
    angle = np.sin(frame / 50) * 0.02
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    positions = np.dot(positions, rotation_matrix)

    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=8)  # White circles

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    positions = update_points(frame)
    x = positions[:, 0]
    y = positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

# Save the animation (optional)
#ani.save('lying_down_stickman.mp4', writer='ffmpeg', fps=30)

plt.show()
