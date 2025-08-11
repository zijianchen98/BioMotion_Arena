
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define number of point-lights and fps
num_points = 15
fps = 30

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define point-light positions for a sadman waving a hand
def get_point_positions(frame):
    # Base positions for the sad man's body and head
    body_positions = np.array([
        [0, 9],   # Head
        [-1, 8],  # Left shoulder
        [1, 8],   # Right shoulder
        [0, 5],   # Body
        [-1, 6],  # Left elbow
        [1, 6],   # Right elbow
        [0, 3],   # Left hip
        [0, 2],   # Right hip
        [-1, 4],  # Left hand
        [1, 4],   # Right hand
    ])

    # Waving hand motion
    wave_amplitude = 1.5
    wave_position = wave_amplitude * np.sin(2 * np.pi * frame / (3 * fps))  # Wave motion
    body_positions[8, 0] += wave_position  # Right hand position changes

    return body_positions

# Initialize point lights
points = ax.scatter([], [], s=200, color='white')

# Animation update function
def update(frame):
    positions = get_point_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 90), interval=1000/fps, blit=True)

# Display the animation
plt.show()
