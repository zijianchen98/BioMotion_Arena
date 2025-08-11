
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points (15 points)
initial_positions = np.array([
    [0, 0],  # Center of mass
    [-0.1, 0.5], [0.1, 0.5],  # Shoulders
    [-0.15, 0.7], [0.15, 0.7],  # Elbows
    [-0.2, 0.9], [0.2, 0.9],  # Hands
    [-0.1, -0.5], [0.1, -0.5],  # Hips
    [-0.15, -0.7], [0.15, -0.7],  # Knees
    [-0.2, -0.9], [0.2, -0.9],  # Feet
    [0, -0.3],  # Stomach
    [0, 0.3],  # Head
    [0, -0.6]  # Pelvis
])

# Define the animation parameters
frame_rate = 30  # frames per second
total_frames = 120  # total frames for one cycle of jumping
jump_height = 0.5  # height of the jump
gravity = 9.8  # gravitational acceleration
mass = 70  # mass of the woman in kg
weight_factor = 1.5  # factor to simulate the effect of carrying heavy weight

# Calculate the vertical position of the center of mass over time
time = np.linspace(0, total_frames / frame_rate, total_frames)
velocity = np.sqrt(2 * jump_height * gravity)
time_to_peak = velocity / gravity
time_to_ground = 2 * time_to_peak
y_position = np.maximum(jump_height - 0.5 * gravity * (time % time_to_ground - time_to_peak) ** 2, 0)

# Function to update the positions of the points
def update(frame):
    y = y_position[frame]
    new_positions = initial_positions.copy()
    new_positions[:, 1] += y * weight_factor
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/frame_rate, blit=True)

# Show the animation
plt.show()
