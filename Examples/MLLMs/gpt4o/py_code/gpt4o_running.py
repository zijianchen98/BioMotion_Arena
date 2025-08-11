
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define coordinates for 15-point biomechanical motion for running
# The data is simplified for demonstration, but can be expanded to model realistic motion.
def get_running_data(frame_num):
    """Generate frame data for running motion animation."""
    # Phase shift for running motion
    phase = frame_num * 0.1

    # Define point positions (simplified example for running motion)
    points = np.array([
        [0.0, 0.9 + 0.1 * np.sin(phase)],  # Head
        [-0.2, 0.75 + 0.05 * np.sin(phase)], [0.2, 0.75 - 0.05 * np.sin(phase)],  # Shoulders
        [-0.3, 0.5 + 0.1 * np.cos(phase)], [0.3, 0.5 - 0.1 * np.cos(phase)],  # Elbows
        [-0.4, 0.25 + 0.15 * np.sin(phase)], [0.4, 0.25 - 0.15 * np.sin(phase)],  # Hands
        [-0.1, 0.3], [0.1, 0.3],  # Hips
        [-0.2, 0 - 0.15 * np.sin(phase)], [0.2, 0 - 0.15 * np.sin(phase)],  # Knees
        [-0.25, -0.3 - 0.1 * np.cos(phase)], [0.25, -0.3 + 0.1 * np.cos(phase)],  # Feet
        [-0.1, 0.15], [0.1, 0.15]  # Chest points (additional details close to hips)
    ])
    return points

# Create animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)  # Set axis limits for black background
ax.set_ylim(-1, 1)
ax.set_facecolor('black')  # Black background
ax.axis('off')  # Turn off axes

scatter = ax.scatter([], [], c='white', s=50)  # White dots for point-light stimuli

def update(frame_num):
    """Update scatter points for each frame."""
    points = get_running_data(frame_num)
    scatter.set_offsets(points)

# Create and save the animation
ani = FuncAnimation(fig, update, frames=200, interval=50)

# Save or display animation
# ani.save('biological_motion_running.mp4', fps=20)
plt.show()
