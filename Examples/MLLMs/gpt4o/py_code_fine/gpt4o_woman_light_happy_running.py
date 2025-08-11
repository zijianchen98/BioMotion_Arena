
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Positions for 15 point-lights, adjusted to display the biomechanical shape of a running human
# Initial positions (x, y) normalized to frame dimensions
keypoints = {
    'head': [0.5, 0.9],
    'shoulder_left': [0.45, 0.8], 'shoulder_right': [0.55, 0.8],
    'elbow_left': [0.4, 0.7], 'elbow_right': [0.6, 0.7],
    'hand_left': [0.35, 0.6], 'hand_right': [0.65, 0.6],
    'hip_left': [0.47, 0.6], 'hip_right': [0.53, 0.6],
    'knee_left': [0.45, 0.4], 'knee_right': [0.55, 0.4],
    'foot_left': [0.43, 0.2], 'foot_right': [0.57, 0.2],
    'back': [0.5, 0.7]
}

# Convert the keypoints dict to a numpy array of x, y coordinates
positions = np.array(list(keypoints.values()))

# Time series animation function
def run_cycle(positions, frames):
    animation_positions = []
    for frame in range(frames):
        # Introduce biomechanical variations simulating a running motion
        phase = 2 * np.pi * frame / frames
        variation = np.zeros_like(positions)

        # Oscillations on y-coordinates for running effect
        oscillation = 0.02 * np.sin(phase * 2)

        # Legs moving alternately
        leg_offset = 0.05 * np.sin(phase)
        variation[9] = [0, leg_offset]  # Left knee
        variation[10] = [0, -leg_offset]  # Right knee
        variation[11] = [0, 0.5 * leg_offset]  # Left foot
        variation[12] = [0, -0.5 * leg_offset]  # Right foot

        # Arms swinging alternately
        arm_offset = 0.04 * np.sin(phase)
        variation[3] = [0, -arm_offset]  # Left elbow
        variation[4] = [0, arm_offset]  # Right elbow
        variation[5] = [0, -0.5 * arm_offset]  # Left hand
        variation[6] = [0, 0.5 * arm_offset]  # Right hand

        # Apply oscillation to the whole body
        variation[:, 1] += oscillation

        # Calculate new positions
        new_positions = positions + variation
        animation_positions.append(new_positions)

    return animation_positions

# Generate animation data
frames = 60
animation_positions = run_cycle(positions, frames)

# Create the plot
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
plt.axis('off')

# Initialize scatter plot for the point-lights (15 points)
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white')

def animate(frame):
    scatter.set_offsets(animation_positions[frame])
    return scatter,

# Create animation object
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

# Show animation
plt.show()
