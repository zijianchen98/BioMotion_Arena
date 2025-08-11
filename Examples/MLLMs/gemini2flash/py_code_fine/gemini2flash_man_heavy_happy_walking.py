
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Define the initial positions of the points (you'll need to adjust these)
initial_positions = np.array([
    [0, 1.8],  # Head
    [-0.3, 1.5],  # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.6, 1.2],  # Left Elbow
    [0.6, 1.2],  # Right Elbow
    [-0.8, 0.9],  # Left Wrist
    [0.8, 0.9],  # Right Wrist
    [-0.1, 1.2],  # Spine Top
    [0.1, 1.2],  # Spine Top
    [-0.1, 0.7], # Spine Bottom
    [0.1, 0.7],  # Spine Bottom
    [-0.4, 0.2],  # Left Hip
    [0.4, 0.2],  # Right Hip
    [-0.2, -0.4],  # Left Knee
    [0.2, -0.4]  # Right Knee
])

# Define the motion of each point over time (walking motion)
def walking_motion(frame_num):
    motion = np.zeros((num_points, 2))

    # Simulate walking motion with heavy weight (exaggerated movements)
    # Head (subtle sway)
    motion[0, 0] = 0.02 * np.sin(frame_num * 0.1)

    # Shoulders (alternating motion)
    motion[1, 0] = -0.05 * np.sin(frame_num * 0.1)
    motion[2, 0] = 0.05 * np.sin(frame_num * 0.1)

    # Elbows (follow shoulders with delay)
    motion[3, 0] = -0.07 * np.sin((frame_num - 5) * 0.1)
    motion[4, 0] = 0.07 * np.sin((frame_num - 5) * 0.1)

    # Wrists (more pronounced swing)
    motion[5, 0] = -0.1 * np.sin((frame_num - 10) * 0.1)
    motion[6, 0] = 0.1 * np.sin((frame_num - 10) * 0.1)

    # Spine (slight vertical bobbing)
    motion[7, 1] = -0.03 * np.sin(frame_num * 0.1)
    motion[8, 1] = -0.03 * np.sin(frame_num * 0.1)
    motion[9, 1] = -0.03 * np.sin(frame_num * 0.1)
    motion[10, 1] = -0.03 * np.sin(frame_num * 0.1)

    # Hips (alternating motion, opposite shoulders)
    motion[11, 0] = 0.06 * np.sin(frame_num * 0.1)
    motion[12, 0] = -0.06 * np.sin(frame_num * 0.1)

    # Knees (follow hips with delay)
    motion[13, 0] = 0.08 * np.sin((frame_num - 7) * 0.1)
    motion[14, 0] = -0.08 * np.sin((frame_num - 7) * 0.1)
    
    return motion

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the points
scat = ax.scatter([], [], c='white', s=50)

# Define the animation function
def animate(frame_num):
    # Calculate the new positions of the points based on the motion
    motion = walking_motion(frame_num)
    new_positions = initial_positions + motion

    # Update the scatter plot with the new positions
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
