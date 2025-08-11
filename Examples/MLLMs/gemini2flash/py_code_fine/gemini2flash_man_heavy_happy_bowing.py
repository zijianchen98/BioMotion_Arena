
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (standing pose)
initial_positions = np.array([
    [0.0, 1.0],  # Head
    [-0.2, 0.8], # Left Shoulder
    [0.2, 0.8],  # Right Shoulder
    [-0.4, 0.6], # Left Elbow
    [0.4, 0.6],  # Right Elbow
    [-0.2, 0.4], # Left Hip
    [0.2, 0.4],  # Right Hip
    [-0.4, 0.2], # Left Knee
    [0.4, 0.2],  # Right Knee
    [-0.3, 0.0], # Left Foot
    [0.3, 0.0],  # Right Foot
    [0.0, 0.6],  # Torso Top
    [0.0, 0.4],  # Torso Middle
    [0.0, 0.2],  # Torso Bottom
    [-0.1, 0.4]   # Spine (slight offset to left to show depth)
])

# Normalize positions to range [-1, 1]
initial_positions[:, 0] /= 0.5 # Scale x
initial_positions[:, 1] = (initial_positions[:, 1] - 0.5) * 2  # Scale and shift y

# Define the motion of the points (bowing)
def bowing_motion(frame_num):
    """Defines the positions of the points for each frame of the bowing motion."""
    
    # Calculate bowing angle based on frame number
    bow_angle = np.sin(2 * np.pi * frame_num / 200) * 0.5  # Bow angle changes smoothly over 200 frames
    
    positions = initial_positions.copy()
    
    # Head moves down and forward
    positions[0, 1] -= bow_angle * 0.5  # y position of head
    positions[0, 0] += bow_angle * 0.2  # x position of head

    # Shoulders move down and slightly forward
    positions[1:3, 1] -= bow_angle * 0.3
    positions[1:3, 0] += np.array([-1, 1]) * bow_angle * 0.1

    # Elbows follow shoulders
    positions[3:5, 1] -= bow_angle * 0.2
    positions[3:5, 0] += np.array([-1, 1]) * bow_angle * 0.05

    # Torso bends forward
    positions[11:14, 1] -= bow_angle * 0.4
    positions[11:14, 0] += bow_angle * 0.1

    # Hips shift slightly backward as the person bows
    positions[5:7, 0] -= np.array([-1, 1]) * bow_angle * 0.05
    
    # Feet stay relatively still
    positions[9:11, 1] -= bow_angle * 0.05 # small adjustment to feet

    #spine bends
    positions[14, 1] -= bow_angle * 0.3
    positions[14, 0] += bow_angle * 0.1
    

    return positions

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Black background
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.axis('off')  # Hide axes

# Create the scatter plot for the points
scat = ax.scatter([], [], s=20, c='white') # White points

# Animation function
def animate(frame_num):
    """Updates the positions of the points for each frame."""
    positions = bowing_motion(frame_num)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

# Save the animation to a video file (optional)
# ani.save('bowing_animation.mp4', writer='ffmpeg', fps=30)

# Display the animation
plt.show()
