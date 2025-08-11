
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the number of points
num_points = 15

# Define the initial positions of the points (estimated from the image)
initial_positions = np.array([
    [0.5, 0.95],  # Head
    [0.4, 0.85],  # Left shoulder
    [0.6, 0.85],  # Right shoulder
    [0.3, 0.75],  # Left elbow
    [0.7, 0.75],  # Right elbow
    [0.45, 0.65], # Left wrist
    [0.55, 0.65], # Right wrist
    [0.5, 0.65],  # Torso center
    [0.5, 0.5],   # Hip center
    [0.4, 0.4],   # Left hip
    [0.6, 0.4],   # Right hip
    [0.3, 0.25],  # Left knee
    [0.7, 0.25],  # Right knee
    [0.2, 0.1],   # Left ankle
    [0.8, 0.1]    # Right ankle
])


# Define the motion of the points for a jumping forward action (simplified)
def update_points(frame_num):
    # Create a copy of the initial positions
    positions = initial_positions.copy()

    # Simulate jumping forward motion
    jump_height = 0.1 * np.sin(2 * np.pi * frame_num / num_frames)  # Vertical movement
    forward_motion = 0.02 * frame_num / num_frames  # Gradual forward movement
    arm_swing = 0.05 * np.sin(4 * np.pi * frame_num / num_frames) #Arm movement
    leg_movement = 0.05 * np.cos(4 * np.pi * frame_num / num_frames) #Legs movement


    # Apply motion to specific points
    positions[0, 1] += jump_height  # Head moves up and down

    #Arms
    positions[3, 1] += arm_swing
    positions[4, 1] -= arm_swing
    positions[5, 1] += arm_swing
    positions[6, 1] -= arm_swing


    # Legs
    positions[11, 1] += leg_movement
    positions[12, 1] -= leg_movement
    positions[13, 1] += leg_movement
    positions[14, 1] -= leg_movement


    positions[:, 0] += forward_motion  # Move all points forward


    # Wrap around when reaching the end of the frame
    positions[:, 0] = positions[:, 0] % 1.0

    return positions


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=8)  # White points


# Define the animation function
def animate(frame_num):
    positions = update_points(frame_num)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
