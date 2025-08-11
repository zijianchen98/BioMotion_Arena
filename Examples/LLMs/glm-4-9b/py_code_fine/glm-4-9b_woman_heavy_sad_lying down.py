
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point lights
duration = 10  # Duration of the animation in seconds
fps = 30  # Frames per second
num_frames = duration * fps

# Lying down pose parameters
# Assuming a simplified lying down pose with head, shoulders, hips, and feet positions
# These positions will be animated to represent the motion
resting_positions = np.array([
    [-0.5, -0.3, 0],  # Head
    [-0.3, 0, 0],     # Neck
    [-0.1, 0.1, 0],   # Shoulders
    [0.1, 0.2, 0],    # Torso
    [0.3, 0.1, 0],    # Hips
    [0.5, 0, 0],      # Feet
])

# Define the base positions for the point lights corresponding to different body parts
point_base_positions = np.array([
    resting_positions[0],  # Head
    resting_positions[1],  # Neck
    resting_positions[2],  # Shoulders
    resting_positions[2] + np.array([0, 0.1, 0]),  # Upper Arm Left
    resting_positions[2] + np.array([0, -0.1, 0]), # Upper Arm Right
    resting_positions[3],  # Torso
    resting_positions[4],  # Hips
    resting_positions[4] + np.array([0, 0.2, 0]),  # Upper Leg Left
    resting_positions[4] + np.array([0, -0.2, 0]), # Upper Leg Right
    resting_positions[5],  # Feet
    resting_positions[5] + np.array([0, 0.1, 0]),  # Lower Leg Left
    resting_positions[5] + np.array([0, -0.1, 0]), # Lower Leg Right
    # Adding additional points for animation detail
    resting_positions[2] + np.array([0.05, 0.05, 0]),  # Elbow Left
    resting_positions[2] + np.array([0.05, -0.05, 0]), # Elbow Right
    resting_positions[4] + np.array([0.05, 0.05, 0]),  # Knee Left
    resting_positions[4] + np.array([0.05, -0.05, 0]), # Knee Right
])

# Time variable
t = np.linspace(0, 2 * np.pi, num_frames)

# Define the trajectories for each point to mimic the lying down motion
def trajectories(t, base_positions):
    # Simple sinusoidal motion along y-axis to simulate lying down smoothly
    y_displacement = 0.1 * np.sin(t)
    trajectories = []
    for i in range(len(base_positions)):
        trajectory = base_positions[i].copy()
        trajectory[1] += y_displacement[i % len(t)]  # Apply displacement based on base position index
        trajectories.append(trajectory)
    return np.array(trajectories)

# Compute the trajectories
trajectories = trajectories(t, point_base_positions)

# Setup the figure and axis for animation
fig = plt.figure(figsize=(8, 6))
ax = plt.subplot(111)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot for the moving points
sc = ax.scatter([], [], s=50, color='white')

# Animation update function
def update(frame):
    sc.set_offsets(trajectories[frame])
    return sc,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

# Save the animation (optional)
# ani.save('biological_motion_animation.mp4', writer='ffmpeg', fps=fps)

plt.show()
