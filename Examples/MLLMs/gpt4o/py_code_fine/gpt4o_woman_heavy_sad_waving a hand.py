
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 2.5)
ax.set_facecolor("black")
ax.axis('off')  # Disable axes for clean visuals

# Number of point-lights in the stimulus
NUM_POINTS = 15

# Helper function to generate joint positions
def generate_joint_positions():
    # Initially define positions similar to the example image
    positions = {
        'head': (0, 2),
        'shoulder_left': (-0.6, 1.6),
        'shoulder_right': (0.6, 1.6),
        'elbow_left': (-0.6, 1.2),
        'elbow_right': (0.6, 1.2),
        'hand_left': (-0.6, 1.0),
        'hand_right': (0.6, 1.0),
        'hip_left': (-0.5, 0.6),
        'hip_right': (0.5, 0.6),
        'knee_left': (-0.5, 0.2),
        'knee_right': (0.5, 0.2),
        'foot_left': (-0.5, -0.5),
        'foot_right': (0.5, -0.5),
        'spine_upper': (0, 1.4),
        'spine_lower': (0, 0.8)
    }
    return positions

# Update positions dynamically for animation
def update_motion(frame):
    # Get joint positions
    positions = generate_joint_positions()
    # Introduce simple hand waving motion
    hand_left_wave = np.sin(frame * 0.1) * 0.4
    hand_positions = {
        'hand_left': (positions['hand_left'][0], positions['hand_left'][1] + hand_left_wave)
    }
    positions.update(hand_positions)

    # Update point-lights for animation
    for i, joint in enumerate(positions.keys()):
        lights[i].set_data(positions[joint][0], positions[joint][1])
    return lights

# Generate initial positions
joint_positions = generate_joint_positions()

# Create white point-lights for joints
lights = [ax.plot([], [], 'o', color="white", markersize=6)[0] for _ in range(NUM_POINTS)]

# Animate
ani = animation.FuncAnimation(fig, update_motion, frames=100, interval=50, blit=True)

# Display animation
plt.show()
