
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],  # Right Elbow
    [-1.5, 0.5], # Left Hand
    [1.5, 0.5],  # Right Hand
    [-0.25, 0.75], # Left Hip
    [0.25, 0.75], # Right Hip
    [-0.75, 0.0], # Left Knee
    [0.75, 0.0],  # Right Knee
    [-0.5, -0.75], # Left Foot
    [0.5, -0.75],  # Right Foot
    [0.0, 0.5],  # Torso
    [0.0, -1.5]   # Ankle
])

# Define a function to update the positions of the point-lights for each frame
def update_points(frame_num, points):
    # Simulate the motion of a person sitting down
    # This is a simplified example, you can adjust the parameters to create more realistic motion
    for i in range(15):
        if i in [9, 10]: # Knees
            points.set_offsets(np.vstack((points.get_offsets(), initial_positions[i] + [0, -0.5 * np.sin(frame_num / 10)])))
        elif i in [11, 12]: # Feet
             points.set_offsets(np.vstack((points.get_offsets(), initial_positions[i] + [0, -0.25 * np.sin(frame_num / 10)])))
        elif i in [7, 8]: # Hips
            points.set_offsets(np.vstack((points.get_offsets(), initial_positions[i] + [0, -0.1 * np.sin(frame_num / 10)])))
        elif i in [14]: #Ankle
            points.set_offsets(np.vstack((points.get_offsets(), initial_positions[i] + [0, -0.2 * np.sin(frame_num / 10)])))
        else: # Others
            points.set_offsets(np.vstack((points.get_offsets(), initial_positions[i])))
    
    points.set_offsets(initial_positions)
    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,),
                              interval=50, blit=False, save_count=num_frames)

# Show the animation
plt.show()
