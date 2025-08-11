
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Define the size of the figure
fig_width = 6
fig_height = 10

# Define the initial positions of the points
initial_positions = np.array([
    [3, 9],  # Head
    [3, 7],  # Left Shoulder
    [3, 5],  # Left Elbow
    [3, 3],  # Left Hand
    [3, 7],  # Right Shoulder
    [3, 5],  # Right Elbow
    [3, 3],  # Right Hand
    [3, 6],  # Torso Upper
    [3, 4],  # Torso Lower
    [3, 2],  # Left Hip
    [3, 0],  # Left Knee
    [3, -2], # Left Foot
    [3, 2],  # Right Hip
    [3, 0],  # Right Knee
    [3, -2]  # Right Foot
])

# Define the range of motion for the points
motion_range = 0.5

# Function to generate the animation frames
def generate_frame(frame_num):
    # Define the positions of the points for this frame
    positions = initial_positions + np.random.uniform(-motion_range, motion_range, size=(num_points, 2))

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Set the background color to black
    ax.set_facecolor('black')

    # Plot the points as white circles
    ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white')

    # Set the limits of the axes
    ax.set_xlim(0, fig_width)
    ax.set_ylim(-3, 10)

    # Remove the axes ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Remove the spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Return the figure
    return fig

# Create the animation
fig = plt.figure(figsize=(fig_width, fig_height))
ani = animation.FuncAnimation(fig, generate_frame, frames=num_frames, repeat=True)

# Save the animation as a GIF file
ani.save('sadman_running_point_light.gif', writer='pillow', fps=20)

plt.close(fig)
