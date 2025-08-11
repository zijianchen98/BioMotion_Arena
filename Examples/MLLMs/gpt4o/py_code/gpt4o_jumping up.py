
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis for the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set the background to black
ax.set_xlim(0, 10)  # Set x-axis limits
ax.set_ylim(0, 10)  # Set y-axis limits
ax.axis('off')  # Hide axes

# Number of point-lights
num_points = 15

# Define the initial coordinates of the 15 points representing a man
# These coordinates simulate the spatial skeleton layout of a human body
initial_coords = np.array([
    [5, 9],  # Head
    [4.5, 8], [5.5, 8],  # Shoulders (left/right)
    [4.5, 7], [5.5, 7],  # Elbows (left/right)
    [4, 6], [6, 6],      # Hands (left/right)
    [4.5, 6.5], [5.5, 6.5],  # Hips (left/right)
    [4, 5], [6, 5],  # Knees (left/right)
    [4, 4], [6, 4],  # Feet (left/right)
    [5, 7.5],  # Chest
    [5, 8.5]   # Neck
])

# Scatter object for the points in the animation
scatter = ax.scatter(initial_coords[:, 0], initial_coords[:, 1],
                     s=50, color='white')

# Motion simulation: Generate realistic jumping movement over time
def update(frame):
    animation_coords = initial_coords.copy()
    y_offset = 0.5 * np.sin(frame * np.pi / 30)  # Vertical oscillation
    animation_coords[:, 1] += y_offset

    # Apply biomechanical constraints (e.g., oscillating arms and legs)
    arm_swing = 0.3 * np.sin(frame * np.pi / 20)
    leg_swing = 0.4 * np.sin(frame * np.pi / 15)

    # Simulate swinging arms
    animation_coords[3, 1] -= arm_swing  # Left elbow
    animation_coords[4, 1] -= arm_swing  # Right elbow
    animation_coords[5, 1] -= 1.2 * arm_swing  # Left hand
    animation_coords[6, 1] -= 1.2 * arm_swing  # Right hand

    # Simulate swinging legs
    animation_coords[10, 1] += leg_swing  # Left knee
    animation_coords[11, 1] += leg_swing  # Right knee
    animation_coords[12, 1] += 1.5 * leg_swing  # Left foot
    animation_coords[13, 1] += 1.5 * leg_swing  # Right foot

    # Update scatter object
    scatter.set_offsets(animation_coords)

# Create the animation
ani = FuncAnimation(fig, update, frames=60, interval=50)

# Display the animation
plt.show()
