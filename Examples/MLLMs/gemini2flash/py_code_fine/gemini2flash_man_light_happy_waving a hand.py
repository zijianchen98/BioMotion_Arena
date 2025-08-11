
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial coordinates of the 15 points
points = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left shoulder
    [0.5, 1.5],  # Right shoulder
    [-1.0, 1.0], # Left elbow
    [1.0, 1.0],  # Right elbow
    [-1.5, 0.5], # Left wrist
    [1.5, 0.5],  # Right wrist
    [-0.2, 1.0], # Chest
    [0.2, 1.0],  # Chest
    [-0.2, 0.5], # Waist
    [0.2, 0.5],  # Waist
    [-0.3, -0.5],# Left Knee
    [0.3, -0.5], # Right Knee
    [-0.3, -1.0],# Left Ankle
    [0.3, -1.0]  # Right Ankle
])

# Define a function to update the positions of the points in each frame
def update_points(frame_num, points, scatter):
    # Example: Make the arms wave
    angle = np.sin(2 * np.pi * frame_num / num_frames)

    # Update left wrist position
    points[5, 0] = -1.5 + 0.5*np.sin(2 * np.pi * frame_num / num_frames)  # Move left wrist horizontally
    points[5, 1] = 0.5+ 0.2*np.cos(2 * np.pi * frame_num / num_frames)

    # Update right wrist position
    points[6, 0] = 1.5 - 0.5*np.sin(2 * np.pi * frame_num / num_frames) # Move right wrist horizontally
    points[6, 1] = 0.5 - 0.2*np.cos(2 * np.pi * frame_num / num_frames)
    # Update left elbow position
    points[3, 0] = -1.0 + 0.3*np.sin(2 * np.pi * frame_num / num_frames) # Move left elbow horizontally
    points[3, 1] = 1.0 + 0.1*np.cos(2 * np.pi * frame_num / num_frames)

    # Update right elbow position
    points[4, 0] = 1.0 - 0.3*np.sin(2 * np.pi * frame_num / num_frames) # Move right elbow horizontally
    points[4, 1] = 1.0 - 0.1*np.cos(2 * np.pi * frame_num / num_frames)
    
    # Scale the points to adjust size
    points_scaled = points * 50

    scatter.set_offsets(points_scaled)
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black

# Scale the points to adjust size
points_scaled = points * 50

# Create the scatter plot for the points
scatter = ax.scatter(points_scaled[:, 0], points_scaled[:, 1], color='white', s=50) # Increased point size

# Set the limits of the axes
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)

# Remove axis labels and ticks
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(axis='both', which='both', length=0)  # Hide ticks

# Remove the frame around the plot
for spine in ax.spines:
    ax.spines[spine].set_visible(False)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points, scatter),
                              interval=50, blit=True, save_count=num_frames)

# Save the animation (optional)
# ani.save('waving_happyman.gif', writer='pillow', fps=20)

# Show the animation
plt.show()
