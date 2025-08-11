
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15  # Number of point-lights
duration = 5     # Duration of the animation in seconds
fps = 30         # Frames per second
num_frames = duration * fps  # Total number of frames

# Establish a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')  # Background color
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Initial point-light positions (static)
point_lights = np.zeros((num_points, 2))

# Neck and head positions
point_lights[0] = [0, 0.5]  # Neck
point_lights[1] = [0, 0.6]  # Head

# Shoulder positions
point_lights[2] = [-0.4, 0.4]  # Left shoulder
point_lights[3] = [0.4, 0.4]   # Right shoulder

# Elbow positions
point_lights[4] = [-0.6, 0.2]  # Left elbow
point_lights[5] = [0.6, 0.2]   # Right elbow

# Hand positions (static)
point_lights[6] = [-0.8, 0.0]  # Left hand
point_lights[7] = [0.8, 0.0]   # Right hand

# Spine positions (static)
point_lights[8] = [0, 0.3]     # Spine middle
point_lights[9] = [0, 0.1]     # Lower spine

# Hip positions
point_lights[10] = [-0.4, -0.3]  # Left hip
point_lights[11] = [0.4, -0.3]   # Right hip

# Knee positions
point_lights[12] = [-0.4, -0.8]  # Left knee
point_lights[13] = [0.4, -0.8]   # Right knee

# Feet positions (static)
point_lights[14] = [0, -1.0]     # Feet

# Set up the point-light objects
points, = ax.plot([], [], 'o', color='white')

# Animation update function
def update(frame):
    # Calculate sitting motion (simple interpolation)
    # The y-coordinate will change to represent movement downwards
    if frame < num_frames // 2:
        # First half: sitting down
        delta_y = -0.4 * (frame / (num_frames // 2))
    else:
        # Second half: holding still
        delta_y = -0.4

    # Update point-light positions
    point_lights[0][1] = 0.5 + delta_y      # Neck
    point_lights[1][1] = 0.6 + delta_y      # Head
    point_lights[2][1] = 0.4 + delta_y * 0.5  # Shoulders
    point_lights[3][1] = 0.4 + delta_y * 0.5  # Shoulders
    point_lights[8][1] = 0.3 + delta_y      # Spine middle
    point_lights[9][1] = 0.1 + delta_y      # Lower spine
    point_lights[10][1] = -0.3 + delta_y    # Hips
    point_lights[11][1] = -0.3 + delta_y    # Hips

    points.set_data(point_lights[:, 0], point_lights[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
