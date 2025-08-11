
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 points representing the body parts of a sad woman with heavy weight waving a hand
# Positions are approximate for a human figure in 2D (x, y)
body_points = np.array([
    [0.0, 0.8],   # Head
    [0.2, 0.6],   # Right shoulder
    [-0.2, 0.6],  # Left shoulder
    [0.3, 0.4],   # Right upper arm
    [-0.3, 0.4],  # Left upper arm
    [0.4, 0.2],   # Right lower arm
    [-0.4, 0.2],  # Left lower arm
    [0.35, 0.1],  # Right hand
    [-0.35, 0.1], # Left hand
    [0.0, 0.0],   # Torso
    [0.1, -0.2],  # Right hip
    [-0.1, -0.2], # Left hip
    [0.15, -0.4], # Right leg
    [-0.15, -0.4],# Left leg
    [0.0, -0.6]   # Feet (centered)
])

# Define a function to animate the points
def animate(frame):
    # Define a realistic motion pattern for a sad woman waving a hand
    # The hand moves up and down in a smooth, natural arc
    hand_y = 0.1 + 0.1 * np.sin(2 * np.pi * frame / 30)
    hand_x = 0.35 if frame % 60 < 30 else -0.35  # Waving motion
    hand_y = 0.1 + 0.1 * np.sin(2 * np.pi * frame / 30)

    # Update the hand positions
    body_points[7] = [hand_x, hand_y]
    body_points[8] = [-hand_x, hand_y]

    # Apply a smooth motion to the rest of the body
    for i in range(len(body_points)):
        if i == 7 or i == 8:
            continue  # Skip hands
        # Add a small oscillation to simulate subtle body movement
        body_points[i] += 0.01 * np.sin(2 * np.pi * frame / 30)

    # Clear the previous points
    for patch in points:
        patch.remove()

    # Create new point-light patches
    points.clear()
    for x, y in body_points:
        point = Circle((x, y), 0.02, color='white')
        ax.add_patch(point)
        points.append(point)

# Create the list to hold the point-light patches
points = []

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
