
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points representing the human figure
initial_positions = np.array([
    [0.0, 4.0],  # Head
    [-0.5, 3.0],  # Left Shoulder
    [0.5, 3.0],  # Right Shoulder
    [-1.0, 2.0], # Left Elbow
    [1.0, 2.0],  # Right Elbow
    [-1.5, 1.0], # Left Wrist
    [1.5, 1.0],  # Right Wrist
    [-0.5, 2.0], # Left Hip
    [0.5, 2.0],  # Right Hip
    [-1.0, 0.5], # Left Knee
    [1.0, 0.5],  # Right Knee
    [-1.0, -1.0],# Left Ankle
    [1.0, -1.0], # Right Ankle
    [0.0, 1.0],  # Torso-middle
    [0.0, -2.0]   # Foot-middle
])

# Define the animation function
def animate(i):
    # Clear the current frame
    plt.cla()

    # Define the background color
    plt.gca().set_facecolor('black')

    # Define the plot limits
    plt.xlim(-3, 3)
    plt.ylim(-3, 5)

    # Hide the axis
    plt.axis('off')

    # Calculate the positions of the points in the current frame
    positions = initial_positions.copy()
    
    # Simulate a "jumping forward" action with some sorrowful weight.
    # This is just an example, you can modify the movement to better suit your needs.
    vertical_motion = np.sin(i / 10) * 0.5  # Oscillate vertically
    horizontal_motion = i / 50.0 # Move horizontally

    # Apply motion to the points. We add a slight variation based on the point index to make it more natural
    for idx in range(len(positions)):
        positions[idx, 1] += vertical_motion * (1 - (idx / len(positions)) * 0.3) # Less vertical movement at the bottom
        positions[idx, 0] += horizontal_motion
        positions[idx, 0] -= 0.1 * np.sin(i / 5 + idx) # Sad, slight swaying motion

    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8) # white circles

    return plt.gca(),

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=False, repeat=True)

# Save the animation (optional)
# ani.save('jumping_sadwoman.mp4', fps=20, extra_args=['-vcodec', 'libx264'])

# Show the animation
plt.show()
