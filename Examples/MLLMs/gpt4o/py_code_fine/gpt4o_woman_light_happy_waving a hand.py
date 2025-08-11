
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create joint position data for a "happy woman waving a hand"
def generate_positions(frame):
    """
    This function generates the x, y positions of 15 points
    representing a waving motion for the right hand.
    """
    # Base positions of a static human body (head, torso, arms, legs) in normalized coordinates
    points = np.array(
        [
            [0, 0.9],  # Head
            [0, 0.7],  # Upper torso
            [-0.15, 0.4],  # Left shoulder
            [-0.3, 0.15],  # Left elbow
            [-0.3, -0.1],  # Left hand
            [0.15, 0.4],  # Right shoulder
            [0.3, 0.15],  # Right elbow
            [0.3, -0.1],  # Right hand (to be animated for waving)
            [0, 0.1],  # Hip
            [-0.15, -0.3],  # Left hip
            [-0.15, -0.7],  # Left knee
            [-0.15, -1.0],  # Left foot
            [0.15, -0.3],  # Right hip
            [0.15, -0.7],  # Right knee
            [0.15, -1.0],  # Right foot
        ]
    )

    # Animate the right hand waving (point index 7 - [0.3, -0.1])
    wave_amplitude = 0.15  # maximum vertical waving displacement
    wave_frequency = 0.05  # control the speed of waving motion
    wave_offset = wave_amplitude * np.sin(2 * np.pi * wave_frequency * frame)
    points[7, 1] = -0.1 + wave_offset  # Update y-coordinate of right hand

    return points

# Animation function
def update(frame, scatter, points):
    new_points = generate_positions(frame)
    scatter.set_offsets(new_points)
    return scatter,

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_facecolor("black")
ax.axis("off")

# Initialize scatter plot with 15 points
points = generate_positions(0)
scatter = ax.scatter(points[:, 0], points[:, 1], s=50, c="white")

# Call the animator
ani = animation.FuncAnimation(fig, update, frames=200, fargs=(scatter, points), interval=50, blit=True)

# Show the animation
plt.show()
