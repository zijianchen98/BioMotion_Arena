
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 5000  # total duration of the animation (in milliseconds)
fps = 30  # frames per second
num_frames = duration // (1000 // fps)

# Initial positions of the point lights representing the joints
# These coordinates need to be adjusted to represent the biological motion.
points_initial = np.array([[0, 5], [-1, 3], [1, 3], [0, 1], [-0.5, 1], [0.5, 1],
                            [0, -1], [1, -2], [-1, -2], [0, -4], [-1, -3], 
                            [1, -3], [0, -5], [-1.75, -2.5], [1.75, -2.5]])

def update(frame):
    plt.clf()  # Clear the current frame
    # Calculate the positions of the points for the current frame
    roll_distance = frame / num_frames * 10  # Distance to roll forward
    new_points = points_initial.copy()
    new_points[:, 0] += roll_distance  # Move the points forward

    # Plot the points
    plt.scatter(new_points[:, 0], new_points[:, 1], color='white')
    plt.xlim(-12, 12)
    plt.ylim(-8, 8)
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axis

# Create a figure for the animation
fig = plt.figure()

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps)

# Save the animation as an MP4 file or display it
plt.show()
