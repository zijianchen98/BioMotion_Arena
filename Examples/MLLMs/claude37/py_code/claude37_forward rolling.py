
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up variables
num_points = 15
duration = 4  # Duration of animation in seconds
fps = 30  # Frames per second
total_frames = duration * fps
theta = np.linspace(0, 2*np.pi, total_frames)  # Angle for the rolling motion

# Initial positions for points representing a human figure (15 points)
# Here we're representing the head, shoulders, back, pelvis, thighs, and knees
initial_positions = np.array([
    [0, 0.5],    # head
    [-0.1, 0.3],  # left shoulder
    [0.1, 0.3],   # right shoulder
    [-0.2, 0.1],  # left elbow
    [0.2, 0.1],   # right elbow
    [-0.1, 0],    # left hand
    [0.1, 0],     # right hand
    [-0.1, -0.2], # left hip
    [0.1, -0.2],  # right hip
    [-0.2, -0.4], # left knee
    [0.2, -0.4],  # right knee
    [-0.1, -0.6], # left ankle
    [0.1, -0.6],  # right ankle
    [0, -0.7],    # pelvis
    [0, -0.8],    # center of mass
    [0, -0.5],    # thigh point
])

def update(frame):
    plt.clf()  # Clear the plot
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')  # Set background color

    # Calculate new positions with a forward roll transformation
    x_shift = np.sin(theta[frame])
    y_shift = -np.cos(theta[frame])
    
    # Apply shifting and update positions
    current_positions = initial_positions + np.array([[x_shift], [y_shift]])

    # Plot each point light
    plt.scatter(current_positions[0], current_positions[1], color='white', s=100)

# Set up the figure and animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps)

# Show the animation
plt.show()
