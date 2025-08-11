
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the body joints and their connections for the point-light stimulus
# The 15 points represent major joints of the body
# These positions represent the initial positions for the joints
joints = np.array([
    [0, 8],  # Head
    [-1, 7], [1, 7],  # Shoulders
    [-1.5, 5.5], [1.5, 5.5],  # Elbows
    [-2, 4], [2, 4],  # Hands
    [0, 6],  # Chest
    [0, 3],  # Torso
    [-0.5, 2], [0.5, 2],  # Hips
    [-1, 0], [1, 0],  # Knees
    [-1, -2], [1, -2],  # Feet
])

# Connections between joints for visualization purposes
connections = [
    (0, 1), (0, 2),  # Head to shoulders
    (1, 3), (2, 4),  # Shoulders to elbows
    (3, 5), (4, 6),  # Elbows to hands
    (1, 7), (2, 7),  # Shoulders to chest
    (7, 8),  # Chest to torso
    (8, 9), (8, 10),  # Torso to hips
    (9, 11), (10, 12),  # Hips to knees
    (11, 13), (12, 14),  # Knees to feet
]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 9)
ax.set_facecolor('black')
ax.axis('off')

# Initialize plot elements
points, = ax.plot(joints[:, 0], joints[:, 1], 'o', color='white')
lines = [ax.plot([], [], '-', color='white')[0] for _ in connections]

# Define biomechanical motion for waving hand animation
def update(frame):
    wave_amplitude = 0.5
    wave_frequency = 0.1

    # Modify the 'right hand' motion to simulate waving
    right_hand_index = 6  # The index of the right hand joint
    torso_position_y = joints[8, 1]  # Reference torso position
    joints[right_hand_index, 0] = 2 + wave_amplitude * np.sin(frame * wave_frequency)
    joints[right_hand_index, 1] = torso_position_y + wave_amplitude * np.cos(frame * wave_frequency)

    # Update positions for points
    points.set_data(joints[:, 0], joints[:, 1])

    # Update positions for lines connecting the joints
    for i, (start, end) in enumerate(connections):
        lines[i].set_data([joints[start, 0], joints[end, 0]],
                          [joints[start, 1], joints[end, 1]])

    return points, *lines

# Generate the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
