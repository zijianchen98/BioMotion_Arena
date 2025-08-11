
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the positions of the 15 points representing the human figure
# Points are initialized at a static posture (general human figure)
# These positions will be updated to create the waving motion
# Body structure: head, neck, torso, arms, and legs
points = np.array([
    [0, 8],  # Head
    [0, 7],  # Neck
    [0, 6],  # Torso
    [-1, 6], [1, 6],  # Shoulder joints
    [-2, 5], [2, 5],  # Elbow joints
    [-2, 4], [2, 4],  # Hand positions (waving right hand will move)
    [-1, 4], [1, 4],  # Hip joints
    [-1.5, 2], [-0.5, 2],  # Left leg (knee and foot)
    [1.5, 2], [0.5, 2]  # Right leg (knee and foot)
])

# Function to perform waving motion for the hand
def update_points(frame):
    # Simple sine wave motion for the right hand's y-coordinate
    hand_wave_amplitude = 1
    hand_wave_frequency = 0.2
    points[8, 1] = 4 + hand_wave_amplitude * np.sin(hand_wave_frequency * frame)
    return points

# Create the animation
def animate(frame):
    updated_points = update_points(frame)

    # Clear previous points and redraw in the animation frame
    ax.clear()
    ax.set_xlim([-3, 3])
    ax.set_ylim([0, 10])
    ax.set_facecolor('black')
    ax.scatter(updated_points[:, 0], updated_points[:, 1], color='white', s=75)

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([0, 10])
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis for clean visual aesthetics

# Run animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)
plt.show()
