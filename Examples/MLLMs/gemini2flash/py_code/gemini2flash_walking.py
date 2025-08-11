
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the animation
num_points = 15

# Define the initial positions of the points
# These positions correspond to the joints of a walking person
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],   # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 0.8], # Hip Center
    [-0.8, 0.3], # Left Hip
    [0.8, 0.3],  # Right Hip
    [-1.2, -0.5],# Left Knee
    [1.2, -0.5], # Right Knee
    [-1.5, -1.5],# Left Ankle
    [1.5, -1.5], # Right Ankle
    [0.0, -1.8]   # Foot Center
])

# Define the function that will update the positions of the points in each frame
def update_points(frame_num):
    # Calculate the new positions of the points based on the frame number
    x = np.zeros((num_points))
    y = np.zeros((num_points))

    x[0] = initial_positions[0,0] + 0.01 * np.sin(frame_num * 0.1) # Head
    y[0] = initial_positions[0,1] + 0.02 * np.cos(frame_num * 0.1)

    x[1] = initial_positions[1,0] + 0.1 * np.sin(frame_num * 0.2) # Left Shoulder
    y[1] = initial_positions[1,1] + 0.05 * np.cos(frame_num * 0.2)

    x[2] = initial_positions[2,0] - 0.1 * np.sin(frame_num * 0.2) # Right Shoulder
    y[2] = initial_positions[2,1] - 0.05 * np.cos(frame_num * 0.2)

    x[3] = initial_positions[3,0] + 0.2 * np.sin(frame_num * 0.25) # Left Elbow
    y[3] = initial_positions[3,1] + 0.1 * np.cos(frame_num * 0.25)

    x[4] = initial_positions[4,0] - 0.2 * np.sin(frame_num * 0.25) # Right Elbow
    y[4] = initial_positions[4,1] - 0.1 * np.cos(frame_num * 0.25)

    x[5] = initial_positions[5,0] + 0.3 * np.sin(frame_num * 0.3) # Left Wrist
    y[5] = initial_positions[5,1] + 0.15 * np.cos(frame_num * 0.3)

    x[6] = initial_positions[6,0] - 0.3 * np.sin(frame_num * 0.3) # Right Wrist
    y[6] = initial_positions[6,1] - 0.15 * np.cos(frame_num * 0.3)

    x[7] = initial_positions[7,0] + 0.05 * np.sin(frame_num * 0.15) # Hip Center
    y[7] = initial_positions[7,1] + 0.03 * np.cos(frame_num * 0.15)

    x[8] = initial_positions[8,0] + 0.15 * np.sin(frame_num * 0.2) # Left Hip
    y[8] = initial_positions[8,1] + 0.12 * np.cos(frame_num * 0.2)

    x[9] = initial_positions[9,0] - 0.15 * np.sin(frame_num * 0.2) # Right Hip
    y[9] = initial_positions[9,1] - 0.12 * np.cos(frame_num * 0.2)

    x[10] = initial_positions[10,0] + 0.3 * np.sin(frame_num * 0.25) # Left Knee
    y[10] = initial_positions[10,1] + 0.25 * np.cos(frame_num * 0.25)

    x[11] = initial_positions[11,0] - 0.3 * np.sin(frame_num * 0.25) # Right Knee
    y[11] = initial_positions[11,1] - 0.25 * np.cos(frame_num * 0.25)

    x[12] = initial_positions[12,0] + 0.4 * np.sin(frame_num * 0.3) # Left Ankle
    y[12] = initial_positions[12,1] + 0.4 * np.cos(frame_num * 0.3)

    x[13] = initial_positions[13,0] - 0.4 * np.sin(frame_num * 0.3) # Right Ankle
    y[13] = initial_positions[13,1] - 0.4 * np.cos(frame_num * 0.3)

    x[14] = initial_positions[14,0] + 0.02 * np.sin(frame_num * 0.1) # Foot Center
    y[14] = initial_positions[14,1] + 0.15 * np.cos(frame_num * 0.1)
        
    # Update the positions of the points
    points.set_offsets(np.c_[x, y])

    # Return the updated points object
    return points,

# Create the figure and axes objects
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Set the limits of the axes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 3)

# Remove the axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])

# Create the points object
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation object
ani = animation.FuncAnimation(fig, update_points, interval=50, blit=True, save_count=num_frames)

# Show the animation
plt.show()
