
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define the 15 body points for a sitting man (approximate coordinates)
body_points = np.array([
    [4, 9],     # Head
    [3, 7],     # Left shoulder
    [5, 7],     # Right shoulder
    [2, 5],     # Left elbow
    [4, 5],     # Torso
    [6, 5],     # Right elbow
    [1, 3],     # Left hip
    [3, 3],     # Left knee
    [5, 3],     # Right knee
    [7, 3],     # Right hip
    [2, 1],     # Left ankle
    [4, 1],     # Left foot
    [6, 1],     # Right foot
    [8, 1],     # Right ankle
    [4, 6]      # Spine
])

# Define a function to simulate smooth motion (sitting down)
def animate(frame):
    # Define a smooth motion path for each point
    # The motion is designed to simulate a person sitting down smoothly
    t = frame / 100.0
    points = body_points.copy()

    # Head
    points[0] = [4, 9 - 2 * t]

    # Left shoulder
    points[1] = [3 - 1 * t, 7 - 1.5 * t]
    # Right shoulder
    points[2] = [5 + 1 * t, 7 - 1.5 * t]

    # Left elbow
    points[3] = [2 - 0.5 * t, 5 - 1 * t]
    # Torso
    points[4] = [4, 5 - 1 * t]
    # Right elbow
    points[5] = [6 + 0.5 * t, 5 - 1 * t]

    # Left hip
    points[6] = [1 + 0.5 * t, 3 - 0.5 * t]
    # Left knee
    points[7] = [3 - 0.25 * t, 3 - 0.5 * t]
    # Right knee
    points[8] = [5 + 0.25 * t, 3 - 0.5 * t]
    # Right hip
    points[9] = [7 - 0.5 * t, 3 - 0.5 * t]

    # Left ankle
    points[10] = [2 + 0.25 * t, 1 - 0.25 * t]
    # Left foot
    points[11] = [4 - 0.5 * t, 1 - 0.25 * t]
    # Right foot
    points[12] = [6 + 0.5 * t, 1 - 0.25 * t]
    # Right ankle
    points[13] = [8 - 0.25 * t, 1 - 0.25 * t]

    # Spine
    points[14] = [4, 6 - 1 * t]

    # Clear previous points
    for patch in ax.patches:
        patch.remove()

    # Draw new points
    for x, y in points:
        circle = Circle((x, y), 0.2, color='white')
        ax.add_patch(circle)

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
