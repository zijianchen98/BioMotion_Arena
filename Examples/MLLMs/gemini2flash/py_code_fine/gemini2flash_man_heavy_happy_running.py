
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points
num_points = 15

# Define the initial positions of the points (replace with actual running motion data)
# This is a simplified example, you'll need to find or generate more realistic data
initial_positions = np.array([
    [0, 10],  # Head
    [-1, 9],  # Left Shoulder
    [1, 9],  # Right Shoulder
    [-2, 7],  # Left Elbow
    [2, 7],  # Right Elbow
    [-3, 5],  # Left Wrist
    [3, 5],  # Right Wrist
    [0, 7],  # Torso
    [0, 5],  # Hip
    [-1, 3],  # Left Knee
    [1, 3],  # Right Knee
    [-1.5, 1],  # Left Ankle
    [1.5, 1],  # Right Ankle
    [-1.5, 0],  # Left Foot
    [1.5, 0]   # Right Foot
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Set the axis limits
    ax.set_xlim(-5, 5)
    ax.set_ylim(-2, 12)

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Calculate the positions of the points for the current frame
    # This is a placeholder - replace with realistic motion calculations
    angle = np.sin(2 * np.pi * i / num_frames) # Simple sine wave for demo

    positions = initial_positions.copy()
    positions[3,0] += np.sin(2 * np.pi * i / num_frames)  #Left Elbow
    positions[6,0] -= np.sin(2 * np.pi * i / num_frames)   #Right Wrist
    positions[9,0] += np.sin(2 * np.pi * i / num_frames)   #Left Knee
    positions[12,0] -= np.sin(2 * np.pi * i / num_frames)   #Right Ankle

    positions[3,1] += 0.3 * np.sin(2 * np.pi * i / num_frames)  #Left Elbow
    positions[6,1] += 0.3 * np.sin(2 * np.pi * i / num_frames)   #Right Wrist
    positions[9,1] += 0.3 * np.sin(2 * np.pi * i / num_frames)   #Left Knee
    positions[12,1] += 0.3 * np.sin(2 * np.pi * i / num_frames)   #Right Ankle

    positions[13,1] -= 0.5* np.sin(2 * np.pi * i / num_frames)   #Left foot
    positions[14,1] -= 0.5* np.sin(2 * np.pi * i / num_frames)   #Right foot


    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

    return ax,

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=False, repeat=True)

# Save the animation (optional)
# ani.save('running_man.gif', writer='imagemagick', fps=30)

# Show the animation
plt.show()
