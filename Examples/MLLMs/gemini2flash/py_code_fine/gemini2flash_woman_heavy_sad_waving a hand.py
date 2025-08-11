
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point-lights
num_points = 15

# Define the initial positions of the point-lights (x, y)
# These coordinates are approximate and may need adjustment
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.5, 0.75], # Shoulder center
    [0.3, 0.7],  # Left shoulder
    [0.7, 0.7],  # Right shoulder
    [0.3, 0.6],  # Left elbow
    [0.7, 0.6],  # Right elbow
    [0.3, 0.5],  # Left wrist
    [0.7, 0.4],  # Right wrist
    [0.5, 0.6],  # Spine
    [0.5, 0.5],  # Pelvis
    [0.4, 0.4],  # Left hip
    [0.6, 0.4],  # Right hip
    [0.4, 0.25], # Left knee
    [0.6, 0.25], # Right knee
    [0.5, 0.15]   # Ankle
])

# Define the motion of the point-lights over time
# This is a placeholder and should be replaced with realistic motion data
# Simulating a sad woman waving a hand
motion_data = np.zeros((num_frames, num_points, 2))
for frame in range(num_frames):
    # Slight swaying motion for sadness
    sway = 0.01 * np.sin(2 * np.pi * frame / num_frames)
    motion_data[frame, :, 0] = initial_positions[:, 0] + sway

    # Hand waving motion (right arm)
    wave_amplitude = 0.05
    wave_frequency = 5
    wave = wave_amplitude * np.sin(2 * np.pi * wave_frequency * frame / num_frames)
    motion_data[frame, 7, 1] = initial_positions[7, 1] + wave  # Right wrist moves up and down
    motion_data[frame, 5, 1] = initial_positions[5, 1] + 0.5 * wave  # Right elbow follows wrist


# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the point-lights
points, = ax.plot([], [], 'wo', markersize=8)  # White circles

# Animation function to update the positions of the point-lights in each frame
def animate(frame):
    x = motion_data[frame, :, 0]
    y = motion_data[frame, :, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Save the animation (optional)
# ani.save('biological_motion.mp4', writer='ffmpeg', fps=30)

# Display the animation
plt.show()
