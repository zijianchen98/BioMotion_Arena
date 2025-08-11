
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FRAMES = 100
WAVE_AMPLITUDE = 0.1
WAVE_FREQUENCY = 1.5
BODY_HEIGHT = 0.5
BODY_WIDTH = 0.1

# Define the initial positions of the point lights
def initialize_points():
    # Assuming the points are distributed along the body and limbs
    points = np.zeros((NUM_POINTS, 2))
    
    # Body main points
    points[0:5, 0] = -BODY_WIDTH  # Left side
    points[5:10, 0] = BODY_WIDTH   # Right side
    points[0:10, 1] = np.linspace(0, BODY_HEIGHT, 10)

    # Head points (adjust based on body height)
    points[10:15, 0] = 0  # Center for head
    points[10:15, 1] = BODY_HEIGHT + 0.1  # Slightly above the body

    return points

# Update function for animation
def update(frame, points, scat):
    hand_wave = np.sin(WAVE_FREQUENCY * frame / FRAMES) * WAVE_AMPLITUDE

    # Update the position of the hand
    points[5, 1] += hand_wave  # Right hand
    points[10, 1] += hand_wave  # Head right

    # Update scatter plot
    scat.set_offsets(points)
    return scat,

# Initialize
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.1, 1.0)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create initial scatter plot
points = initialize_points()
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FRAMES, fargs=(points, scat), interval=50, blit=True)

# Show animation
plt.show()
