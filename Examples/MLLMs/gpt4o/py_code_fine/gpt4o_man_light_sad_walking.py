
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the coordinates for the point lights representing the walking human
def generate_human_coordinates(frame):
    """
    Generate coordinates of 15 points representing a biomechanically plausible walking human motion.
    """
    # Base settings for the motion
    stride_length = 0.6  # Length of strides
    oscillation_amplitude = 0.2  # Amplitude of vertical oscillations
    num_frames = 60  # Total frames in the animation

    # Normalize phase based on the frame number
    phase = 2 * np.pi * (frame % num_frames) / num_frames

    # 15 points for human figure (head, shoulders, elbows, hands, hips, knees, feet)
    points = np.zeros((15, 2))

    # Head
    points[0, :] = [0, 1.6 + oscillation_amplitude * np.sin(phase)]

    # Shoulders
    points[1, :] = [-0.2, 1.4 + oscillation_amplitude * np.sin(phase)]
    points[2, :] = [0.2, 1.4 + oscillation_amplitude * np.sin(phase)]

    # Elbows
    points[3, :] = [-0.3, 1.2 + 0.1 * np.cos(phase)]
    points[4, :] = [0.3, 1.2 - 0.1 * np.cos(phase)]

    # Hands
    points[5, :] = [-0.4, 1.0 + 0.2 * np.sin(phase + np.pi / 2)]
    points[6, :] = [0.4, 1.0 - 0.2 * np.sin(phase + np.pi / 2)]

    # Hips
    points[7, :] = [-0.1, 1.0 + oscillation_amplitude * np.sin(phase)]
    points[8, :] = [0.1, 1.0 + oscillation_amplitude * np.sin(phase)]

    # Knees
    points[9, :] = [-0.15, 0.6 + 0.15 * np.cos(phase)]
    points[10, :] = [0.15, 0.6 - 0.15 * np.cos(phase)]

    # Feet
    points[11, :] = [-0.15 + stride_length * np.sin(phase), 0.3]
    points[12, :] = [0.15 - stride_length * np.sin(phase), 0.3]

    # Invisible connector points for biomechanics coherence
    points[13, :] = [-0.2, 0.8 + 0.1 * np.sin(phase)]
    points[14, :] = [0.2, 0.8 - 0.1 * np.sin(phase)]

    return points


# Create the animation
def animate(frame):
    coordinates = generate_human_coordinates(frame)
    scatter.set_offsets(coordinates)
    return scatter,


# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_facecolor("black")
ax.axis("off")

# Initialize the scatter plot
scatter = ax.scatter([], [], s=50, c="white")

num_frames = 60
ani = FuncAnimation(fig, animate, frames=num_frames, interval=40, blit=True)

plt.show()
