
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
BLACK = 'black'
POINT_COLOR = 'white'
NUMBER_OF_POINTS = 15
FRAME_RATE = 30
DURATION = 5  # seconds

# Create "turning around" point-light stimulus

# Define the coordinates for a walking animation
# NOTE: The example dataset below is idealized to create biomechanically plausible motion for turning around.
frames = 30  # Number of frames for a complete turn
angle_steps = np.linspace(0, 2 * np.pi, frames)  # Simulate circular motion around vertical axis

# Points layout (representing a simplified human stick figure layout)
# Order: Head, Body (spine), Shoulders, Elbows, Hands, Hips, Knees, Feet
initial_positions = np.array([
    [0, 1.5],  # Head
    [0, 1],    # Upper spine
    [-0.3, 1], [0.3, 1],  # Shoulders
    [-0.5, 0.7], [0.5, 0.7],  # Elbows
    [-0.6, 0.5], [0.6, 0.5],  # Hands
    [0, 0.3],  # Lower spine
    [-0.3, 0.3], [0.3, 0.3],  # Hips
    [-0.2, 0], [0.2, 0],  # Knees
    [-0.2, -0.2], [0.2, -0.2],  # Feet
])

# Prepare animation data: Rotate each point around a vertical axis to simulate turning around
def generate_positions():
    frames_positions = []
    
    for angle in angle_steps:
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        rotated_positions = np.dot(initial_positions, rotation_matrix.T)
        frames_positions.append(rotated_positions)
    
    return frames_positions

positions = generate_positions()


# Animation function
def update(frame):
    scat.set_offsets(positions[frame])  # Update scatter with new frame positions
    return scat,


# Create animation
fig, ax = plt.subplots()
fig.set_facecolor(BLACK)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor(BLACK)

# Scatter plot for points
scat = ax.scatter([], [], c=POINT_COLOR, s=50)

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(positions), interval=1000 / FRAME_RATE, blit=True
)

plt.show()
