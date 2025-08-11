
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
N_POINTS = 15  # Number of point-lights
POINT_RADIUS = 0.02  # Radius of each point-light
FPS = 30  # Frames per second
DURATION = 4  # Duration in seconds

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)  # X-axis limits
ax.set_ylim(-1, 1)  # Y-axis limits
ax.set_facecolor('black')

# Points positions (static joints)
# Joint coordinates for a sad man
joints = np.array([
    [0, 1],  # Head
    [-0.5, 0.5],  # Left shoulder
    [0.5, 0.5],  # Right shoulder
    [-0.5, 0],  # Left elbow
    [0.5, 0],  # Right elbow
    [-0.5, -0.5],  # Left hand
    [0.5, -0.5],  # Right hand
    [0, 0],  # Body
])

# Function to update the animation
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')

    # Calculate hand position for waving
    hand_wave = 0.2 * np.sin(2 * np.pi * (frame / (FPS * DURATION)))

    # Update positions of point-lights
    positions = np.copy(joints)
    positions[5, 1] += hand_wave  # Left hand (waving)

    # Draw point-lights
    for (x, y) in positions:
        circle = plt.Circle((x, y), POINT_RADIUS, color='white')
        ax.add_artist(circle)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FPS * DURATION, interval=1000 / FPS)

# Display the animation
plt.show()
