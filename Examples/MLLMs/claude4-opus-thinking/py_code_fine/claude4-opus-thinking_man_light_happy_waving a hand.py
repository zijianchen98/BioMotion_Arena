
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the point-light stimulus
NUM_POINTS = 15
FRAME_INTERVAL = 50  # milliseconds per frame

# Generate initial positions for the point-lights
def initialize_points():
    # Simulated skeletal structure in 2D coordinates (y, x)
    return np.array([
        [0.4, 0.5],  # Head
        [0.3, 0.5],  # Neck
        [0.2, 0.5],  # Shoulders
        [0.2, 0.45], # Elbows
        [0.1, 0.4],  # Hands (right)
        [0.2, 0.55], # Elbows (left)
        [0.1, 0.6],  # Hands (left)
        [0.4, 0.4],  # Hips
        [0.3, 0.3],  # Knees
        [0.3, 0.7],  # Feet (right)
        [0.5, 0.3],  # Feet (left)
        [0.5, 0.75], # Wrist (left)
        [0.5, 0.25], # Wrist (right)
        [0.25, 0.45],# Torso
        [0.25, 0.5]  # Center of Movement
    ]).T

# Function to update the point-light position for animation
def update(frame, points, line):
    angle = np.radians(10 * frame)  # Waving motion
    points[4, 1] = 0.4 + 0.1 * np.sin(angle)  # Right hand
    points[6, 1] = 0.6 + 0.05 * np.sin(angle)  # Left hand
    line.set_data(points[1], points[0])  # Update line data
    return line,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
plt.axis('off')  # Hide axes

# Initialize point-light positions
points = initialize_points()
line, = ax.plot([], [], 'o', color='white', markersize=12)  # White point-lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), fargs=(points, line),
                              interval=FRAME_INTERVAL, blit=True, repeat=True)

# Show the animation
plt.show()
