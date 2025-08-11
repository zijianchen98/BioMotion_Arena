
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
# These positions are based on a simplified human body model
point_lights = np.array([
    [-0.2, 0.5],  # Head
    [-0.1, 0.4],  # Shoulder
    [0.1, 0.4],   # Shoulder
    [-0.2, 0.2],  # Elbow
    [0.2, 0.2],   # Elbow
    [-0.3, 0.1],  # Wrist
    [0.3, 0.1],   # Wrist
    [-0.1, 0.3],  # Hip
    [0.1, 0.3],   # Hip
    [-0.2, 0.0],  # Knee
    [0.2, 0.0],   # Knee
    [-0.3, -0.1], # Ankle
    [0.3, -0.1],  # Ankle
    [0.0, 0.1],   # Spine
    [0.0, -0.1]   # Spine
])

# Define the animation frames
def animate(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update point-light positions based on the sitting down action
    # These positions are based on a simplified human body model
    # and are adjusted to create a smooth and natural motion
    if frame < 30:
        # Initial standing position
        point_lights_frame = point_lights.copy()
    elif frame < 60:
        # Start sitting down
        point_lights_frame = point_lights.copy()
        point_lights_frame[8:12, 1] -= (frame - 30) / 30 * 0.2  # Hip and knee movement
        point_lights_frame[12:, 1] -= (frame - 30) / 30 * 0.1  # Spine movement
    elif frame < 90:
        # Continue sitting down
        point_lights_frame = point_lights.copy()
        point_lights_frame[8:12, 1] -= 0.2  # Hip and knee movement
        point_lights_frame[12:, 1] -= 0.1  # Spine movement
        point_lights_frame[8:10, 0] -= (frame - 60) / 30 * 0.05  # Hip movement
        point_lights_frame[10:12, 0] += (frame - 60) / 30 * 0.05  # Hip movement
    else:
        # Final sitting position
        point_lights_frame = point_lights.copy()
        point_lights_frame[8:12, 1] -= 0.2  # Hip and knee movement
        point_lights_frame[12:, 1] -= 0.1  # Spine movement
        point_lights_frame[8:10, 0] -= 0.05  # Hip movement
        point_lights_frame[10:12, 0] += 0.05  # Hip movement

    # Plot the point-lights
    ax.scatter(point_lights_frame[:, 0], point_lights_frame[:, 1], c='white', s=10)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50)

plt.show()
