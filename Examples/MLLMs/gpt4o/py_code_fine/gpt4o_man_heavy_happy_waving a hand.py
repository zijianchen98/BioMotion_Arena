
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the structure of the happyman using point-light locations
# Each point represents a joint in the "happyman" model
initial_positions = {
    # Torso
    "head": [0, 4],
    "shoulder_left": [-1, 3],
    "shoulder_right": [1, 3],
    "elbow_left": [-1.5, 2],
    "elbow_right": [1.5, 2],
    "hand_left": [-2, 1],
    "hand_right": [2, 1],
    "hip_left": [-0.5, 1.5],
    "hip_right": [0.5, 1.5],
    # Legs
    "knee_left": [-0.75, 0.5],
    "knee_right": [0.75, 0.5],
    "foot_left": [-0.75, -0.5],
    "foot_right": [0.75, -0.5],
    # Core body
    "center": [0, 2],
}

# Update these to match initial_positions keys
joints = list(initial_positions.keys())

# Define the waving motion (periodic sinusoidal for hand and elbow movements)
def update_positions(frame, positions, joints):
    new_positions = positions.copy()

    # Hand waving simulation (left hand waving up and down)
    wave_frequency = np.pi * 0.1
    wave_amplitude = 0.5
    wave_offset = wave_amplitude * np.sin(wave_frequency * frame)
    new_positions["hand_left"][1] = positions["hand_left"][1] + wave_offset

    # Other parts may remain static for simplicity, but can add more biomechanics
    # Ensure biomechanical constraints for more realistic motion if needed

    return new_positions

# Create a pyplot figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')

# Initialize points for animation
points, = ax.plot([], [], 'w.', markersize=10)

# Update function for animation
def animate(frame):
    global initial_positions

    # Update positions of all joints
    updated_positions = update_positions(frame, initial_positions, joints)

    # Unpack x and y coordinates for plotting
    x = [updated_positions[joint][0] for joint in joints]
    y = [updated_positions[joint][1] for joint in joints]

    # Update data for the plot
    points.set_data(x, y)
    return points,

# Animate with desired number of frames and interval
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show animation
plt.show()
