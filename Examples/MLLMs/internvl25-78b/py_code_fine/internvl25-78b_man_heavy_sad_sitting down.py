
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Define initial points for the sadman
points = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.35, 0.7],  # Left elbow
    [0.65, 0.7],  # Right elbow
    [0.45, 0.6],  # Left hand
    [0.55, 0.6],  # Right hand
    [0.5, 0.8],  # Center of body
    [0.45, 0.85],  # Left hip
    [0.55, 0.85],  # Right hip
    [0.4, 0.75],  # Left knee
    [0.6, 0.75],  # Right knee
    [0.42, 0.65],  # Left ankle
    [0.58, 0.65],  # Right ankle
    [0.5, 0.5],  # Lower back
    [0.5, 0.55]   # Lower body center
])

# Create scatter plot for points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Update positions for each frame
    t = frame / 100

    # Move head down
    points[0] = [0.5, 0.9 - 0.1 * t]

    # Move shoulders down and slightly forward
    points[1] = [0.4 - 0.05 * t, 0.8 - 0.1 * t]
    points[2] = [0.6 + 0.05 * t, 0.8 - 0.1 * t]

    # Adjust elbows
    points[3] = [0.35 - 0.05 * t, 0.7 - 0.1 * t]
    points[4] = [0.65 + 0.05 * t, 0.7 - 0.1 * t]

    # Move hands closer to body
    points[5] = [0.45 - 0.05 * t, 0.6 - 0.05 * t]
    points[6] = [0.55 + 0.05 * t, 0.6 - 0.05 * t]

    # Body and hips
    points[7] = [0.5, 0.8 - 0.12 * t]
    points[8] = [0.45 - 0.03 * t, 0.85 - 0.15 * t]
    points[9] = [0.55 + 0.03 * t, 0.85 - 0.15 * t]

    # Knees forward
    points[10] = [0.4 - 0.05 * t, 0.75 - 0.15 * t]
    points[11] = [0.6 + 0.05 * t, 0.75 - 0.15 * t]

    # Ankles moving closer to ground
    points[12] = [0.42 - 0.03 * t, 0.65 - 0.2 * t]
    points[13] = [0.58 + 0.03 * t, 0.65 - 0.2 * t]

    # Lower back and lower body center
    points[14] = [0.5, 0.5 - 0.1 * t]
    points[15] = [0.5, 0.55 - 0.1 * t]

    # Update scatter plot
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=30, blit=True)

plt.axis('off')
plt.show()
