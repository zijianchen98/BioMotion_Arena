
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights (15 points)
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.6, 1.0], # Left Elbow
    [0.6, 1.0],  # Right Elbow
    [-0.8, 0.5], # Left Wrist
    [0.8, 0.5],  # Right Wrist
    [-0.1, 1.0], # Spine Top
    [0.1, 1.0],  # Spine Top
    [-0.1, 0.0], # Spine Bottom
    [0.1, 0.0],  # Spine Bottom
    [-0.4, -1.0],# Left Knee
    [0.4, -1.0], # Right Knee
    [-0.4, -2.0],# Left Ankle
    [0.4, -2.0]  # Right Ankle
])

# Define the movement of the point-lights to simulate bowing
def bowing_motion(frame_num):
    # Normalize frame number to a range of 0 to 1
    t = frame_num / num_frames

    # Define bowing parameters
    bow_angle = np.sin(t * 2 * np.pi) * 0.5  # Angle of bow, from -0.5 to 0.5 radians

    # Apply bowing motion to each point-light
    positions = initial_positions.copy()
    
    # Apply bowing motion to the spine points
    positions[7:11, 1] -= bow_angle * 1.0  # Adjust spine points to bend forward

    # Apply bowing motion to the head
    positions[0, 1] -= bow_angle * 1.5 # Adjust head to follow the bend

    # Adjust the arms to follow the bowing motion
    positions[3, 1] -= bow_angle * 0.5  # Move the elbows down
    positions[4, 1] -= bow_angle * 0.5  # Move the elbows down
    positions[5, 1] -= bow_angle * 0.5   # Move the wrists down
    positions[6, 1] -= bow_angle * 0.5   # Move the wrists down


    # Apply bending motion to legs
    positions[11, 1] += bow_angle * 0.3
    positions[12, 1] += bow_angle * 0.3
    positions[13, 1] += bow_angle * 0.5
    positions[14, 1] += bow_angle * 0.5

    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # Setting background to black
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
plt.axis('off') # Turning axes off

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20) # Adjust size of the points

# Define the animation function
def animate(frame_num):
    positions = bowing_motion(frame_num)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
