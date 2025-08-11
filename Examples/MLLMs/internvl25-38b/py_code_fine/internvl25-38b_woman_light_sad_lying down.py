
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions for 15 white point-lights
# These positions should roughly outline a sad woman lying down
initial_positions = [
    (0.50, 0.95),  # Head
    (0.50, 0.85),  # Neck
    (0.50, 0.70),  # Torso
    (0.35, 0.60),  # Left Shoulder
    (0.65, 0.60),  # Right Shoulder
    (0.20, 0.50),  # Left Hand
    (0.80, 0.50),  # Right Hand
    (0.50, 0.50),  # Waist
    (0.35, 0.40),  # Left Hip
    (0.65, 0.40),  # Right Hip
    (0.25, 0.30),  # Left Knee
    (0.75, 0.30),  # Right Knee
    (0.20, 0.20),  # Left Foot
    (0.80, 0.20),  # Right Foot
]

# Function to update the animation frame
def update(frame, positions, scat):
    for i, pos in enumerate(positions):
        x, y = pos[0], pos[1]
        # Smooth oscillation to simulate lying down motion
        y += 0.05 * np.sin(0.1 * frame + i * 0.1)
        positions[i] = (x, y)
    scat.set_offsets(positions)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create a scatter plot for the point-lights
scat = ax.scatter([], [])
scat.set_offsets(initial_positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(initial_positions, scat), interval=50)

# Display the animation
plt.show()
