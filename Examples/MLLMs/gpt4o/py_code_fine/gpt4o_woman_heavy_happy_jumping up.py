
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
frame_rate = 60  # Frames per second
total_time = 2  # Total animation time in seconds
num_frames = frame_rate * total_time
point_size = 40  # Size of the white dots

# Body point definitions
points = {
    "head": (0, 10),
    "left_shoulder": (-2, 8),
    "right_shoulder": (2, 8),
    "left_elbow": (-3, 6),
    "right_elbow": (3, 6),
    "left_hand": (-4, 4),
    "right_hand": (4, 4),
    "mid_torso": (0, 6),
    "left_hip": (-2, 4),
    "right_hip": (2, 4),
    "left_knee": (-2, 2),
    "right_knee": (2, 2),
    "left_foot": (-2, 0),
    "right_foot": (2, 0),
    "pelvis": (0, 5)
}

# Convert to array for easier manipulation
point_names = list(points.keys())
point_positions = np.array([points[name] for name in point_names])

# Define jump motion: simulate vertical oscillation
def generate_motion(frame_idx, total_frames):
    t = frame_idx / total_frames  # Normalize time
    motion_amplitude = 5  # Maximum vertical displacement for the jump

    # Apply vertical sinusoidal motion to simulate jumping
    vertical_displacement = motion_amplitude * np.sin(2 * np.pi * t)

    # Apply the displacement only to the y-coordinates
    new_positions = point_positions.copy()
    new_positions[:, 1] += vertical_displacement

    return new_positions

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_xlim(-7, 7)
ax.set_ylim(-1, 12)
ax.set_facecolor("black")
ax.axis("off")

# Initialize scatter plot for the white dots
scatter = ax.scatter(
    point_positions[:, 0], point_positions[:, 1],
    s=point_size, c="white"
)

# Update function for the animation
def update(frame_idx):
    new_positions = generate_motion(frame_idx, num_frames)
    scatter.set_offsets(new_positions)
    return scatter,

# Generate animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000 / frame_rate, blit=True
)

plt.show()
