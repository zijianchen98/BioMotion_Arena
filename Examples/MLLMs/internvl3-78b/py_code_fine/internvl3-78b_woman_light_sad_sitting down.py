
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames in the animation
num_frames = 100

# Define the figure and axis
fig, ax = plt.subplots()

# Disable the axis
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 150)
ax.set_ylim(0, 150)

# Define the positions of the white point-lights
positions = np.array([
    [75, 20],   # Tip of the head
    [65, 45],   # Left eye
    [85, 45],   # Right eye
    [70, 65],   # Left shoulder
    [80, 65],   # Right shoulder
    [60, 100],  # Left knee
    [90, 100],  # Right knee
    [88, 125],  # Left foot
    [62, 125],  # Right foot
    [73, 75],   # Left elbow
    [77, 75],   # Right elbow
    [68, 90],   # Left hand
    [82, 90],   # Right hand
    [67, 55],   # Left hip
    [83, 55]    # Right hip
])

# Create a list of dots
dots = [ax.plot([], [], 'bo')[0] for _ in range(positions.shape[0])]

# Update function for the animation
def update(num, positions):
    for dot, pos in zip(dots, positions):
        dot.set_data(pos[0], pos[1])

    # Return list of objects to update
    return dots

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(positions,), frames=num_frames, interval=40)

# Display the animation
plt.show()
