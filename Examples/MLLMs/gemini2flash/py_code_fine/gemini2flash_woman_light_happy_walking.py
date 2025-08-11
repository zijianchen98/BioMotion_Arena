
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Define the initial positions of the points (adjust to resemble the example image)
initial_positions = np.array([
    [0, 20],    # Head
    [-3, 17],  # Left Shoulder
    [3, 17],   # Right Shoulder
    [-3, 13],  # Left Elbow
    [3, 13],   # Right Elbow
    [-3, 9],   # Left Wrist
    [3, 9],    # Right Wrist
    [0, 12],    # Torso Top
    [0, 8],     # Torso Bottom
    [-2, 4],   # Left Hip
    [2, 4],    # Right Hip
    [-2, 0],   # Left Knee
    [2, 0],    # Right Knee
    [-2, -4],  # Left Ankle
    [2, -4]   # Right Ankle
])

# Define the motion of the points (walking motion with a happywoman style)
# This is a simplified example; you would ideally use motion capture data or biomechanical models
motion_amplitude = 1.5
motion_frequency = 0.1

def update_points(frame_num):
    # Clear the previous frame
    plt.cla()

    # Set plot limits and appearance
    plt.xlim(-10, 10)
    plt.ylim(-10, 25)
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Calculate new positions for each point
    new_positions = initial_positions.copy()

    # Add sine wave motion to simulate walking
    new_positions[9:11, 0] += np.sin(motion_frequency * frame_num) * motion_amplitude  # Hips
    new_positions[11:13, 0] += np.cos(motion_frequency * frame_num) * motion_amplitude * 0.8 # Knees
    new_positions[13:15, 0] += np.sin(motion_frequency * frame_num + np.pi/4) * motion_amplitude * 0.6 # Ankles

    # Add slight swaying motion to simulate "happy woman"
    new_positions[0:8, 0] += np.sin(motion_frequency * frame_num * 0.5) * motion_amplitude * 0.2

    # Plot the points
    plt.plot(new_positions[:, 0], new_positions[:, 1], 'wo', markersize=8)  # White circles

    return plt.gca().lines

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_points, blit=False, frames=num_frames, repeat=True)

# Show the animation (this will open a window with the animation)
plt.show()
