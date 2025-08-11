
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of frames in the animation
num_frames = 100

# Define the number of points
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [0, 2],  # Head
    [-0.5, 1.5],  # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1, 0.5],  # Left Elbow
    [1, 0.5],  # Right Elbow
    [-1.5, -0.5],  # Left Hand
    [1.5, -0.5],  # Right Hand
    [-0.2, 0.8],  # Left Hip
    [0.2, 0.8],  # Right Hip
    [-0.5, -0.8],  # Left Knee
    [0.5, -0.8],  # Right Knee
    [-0.5, -2.5],  # Left Foot
    [0.5, -2.5],  # Right Foot
    [-0.1, 0.2],  # Waist
    [0.1, 0.2]   # Stomach
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Set the axes limits
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    # Define the animation parameters
    amplitude = 0.3
    frequency = 0.1
    phase = i * frequency

    # Calculate the new positions of the points
    positions = initial_positions + np.array([
        [0, 0],  # Head
        [amplitude * np.sin(phase), 0],  # Left Shoulder
        [-amplitude * np.sin(phase), 0],  # Right Shoulder
        [amplitude * np.sin(phase + np.pi/4), 0],  # Left Elbow
        [-amplitude * np.sin(phase + np.pi/4), 0],  # Right Elbow
        [amplitude * np.sin(phase + np.pi/2), 0],  # Left Hand
        [-amplitude * np.sin(phase + np.pi/2), 0],  # Right Hand
        [0, amplitude * np.sin(phase)],  # Left Hip
        [0, amplitude * np.sin(phase)],  # Right Hip
        [0, amplitude * np.sin(phase + np.pi/4)],  # Left Knee
        [0, amplitude * np.sin(phase + np.pi/4)],  # Right Knee
        [0, 0],  # Left Foot
        [0, 0],  # Right Foot
        [0, amplitude * np.sin(phase)],  # Waist
        [0, amplitude * np.sin(phase)]   # Stomach
    ])

    # Make the person sit down
    sit_down_time = num_frames / 2
    if i > sit_down_time:
        sit_down_progress = (i - sit_down_time) / (num_frames - sit_down_time)
        positions[7:, 1] -= 1.5 * sit_down_progress

    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Remove axes labels and ticks
    plt.xticks([])
    plt.yticks([])

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Save the animation
ani.save('sitting_man.gif', writer='pillow', fps=20)

# Show the animation
plt.show()
