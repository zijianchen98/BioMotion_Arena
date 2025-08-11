
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Constants for the animation appearance
POINT_COLOR = 'white'
BACKGROUND_COLOR = 'black'
FIGURE_SIZE = (6, 10)
POINT_SIZE = 60
FPS = 30
DURATION = 2  # seconds

# Biomechanical coordinates for jumping motion (normalizing for coherent motion)
# Using simplified 15-point coordinates to represent the body parts
jumping_motion = [
    # t = 0: Start of the jump
    [[0, 10], [-2, 9], [2, 9], [-3, 8], [3, 8], [-4, 7], [4, 7], [-2, 6], [2, 6], [0, 4], [-1, 2], [1, 2], [-2, 1], [2, 1], [0, 0]],
    # t = 1/4: Ascending
    [[0, 11], [-2, 10], [2, 10], [-3, 9], [3, 9], [-4, 8], [4, 8], [-2, 7], [2, 7], [0, 5], [-1, 3], [1, 3], [-2, 2], [2, 2], [0, 1]],
    # t = 2/4: Peak of the jump
    [[0, 12], [-2, 11], [2, 11], [-3, 10], [3, 10], [-4, 9], [4, 9], [-2, 8], [2, 8], [0, 6], [-1, 4], [1, 4], [-2, 3], [2, 3], [0, 2]],
    # t = 3/4: Descending
    [[0, 10.5], [-2, 9.5], [2, 9.5], [-3, 8.5], [3, 8.5], [-4, 7.5], [4, 7.5], [-2, 6.5], [2, 6.5], [0, 4.5], [-1, 2.5], [1, 2.5], [-2, 1.5], [2, 1.5], [0, 0.5]],
    # t = 1: Landing position
    [[0, 10], [-2, 9], [2, 9], [-3, 8], [3, 8], [-4, 7], [4, 7], [-2, 6], [2, 6], [0, 4], [-1, 2], [1, 2], [-2, 1], [2, 1], [0, 0]],
]

# Normalize the motion data for animation smoothness
def interpolate(body_parts, index, total_frames):
    n_points = len(body_parts)
    interpolated_coordinates = np.empty((total_frames, n_points, 2))
    for i in range(n_points):
        coords = np.array([frame[i] for frame in body_parts])
        for k in range(2):
            dim_coords = coords[:, k]
            interpolated_coordinates[:, i, k] = np.interp(
                np.linspace(0, len(body_parts) - 1, total_frames),
                np.arange(len(body_parts)), dim_coords)
    return interpolated_coordinates


# Set up the animation canvas
fig, ax = plt.subplots(figsize=FIGURE_SIZE)
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 15)
ax.axis('off')  # Remove the axes for a cleaner look

# Plot initialization
total_frames = int(FPS * DURATION)
coordinates = interpolate(jumping_motion, index=0, total_frames=total_frames)
points = ax.scatter([], [], c=POINT_COLOR, s=POINT_SIZE)

# Animation function
def update(frame):
    points.set_offsets(coordinates[frame])
    return points,

# Create and run the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000 / FPS, blit=True)

plt.show()
