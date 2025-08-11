
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15  # Total number of points
num_frames = 60  # Total number of frames in the animation

# Function to generate positions for the waving hand motion
def get_waving_positions(frame):
    # (x, y) coordinates for 15 points representing body and hand
    positions = np.zeros((num_points, 2))

    # Example positions (static) for the body
    positions[0] = [0, 5]    # Head
    positions[1] = [0, 4]    # Neck
    positions[2] = [-1, 3]   # Left Shoulder
    positions[3] = [1, 3]    # Right Shoulder
    positions[4] = [-1, 2]   # Left Elbow
    positions[5] = [1, 2]    # Right Elbow
    positions[6] = [-1, 1]   # Left Hand
    positions[7] = [1, 1]    # Right Hand
    positions[8] = [0, 1]    # Body Center
    positions[9] = [0, 0]    # Body base (hip)
    positions[10] = [-0.5, 0] # Left Leg
    positions[11] = [0.5, 0]  # Right Leg
    positions[12] = [-0.5, -1] # Left Foot
    positions[13] = [0.5, -1]  # Right Foot
    positions[14] = [0, 6]    # Raised hand for waving

    # Simulate waving motion by adjusting the y position of the raised hand and elbow
    waving_amplitude = 1.0
    wave_phase = frame * 2 * np.pi / num_frames
    positions[6][1] = np.sin(wave_phase) * waving_amplitude + 1  # Left Hand position
    positions[7][1] = np.sin(wave_phase) * waving_amplitude + 1  # Right Hand position
    return positions

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 7)
ax.set_facecolor('black')

# Create an empty scatter plot
points = ax.scatter([], [], s=100, c='white')

# Animation update function
def update(frame):
    positions = get_waving_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
