
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for a lying down woman (15 points)
# Approximate joint positions for a simplified biomechanical model
def init_positions():
    # Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso
    positions = np.array([
        [0, 0],    # head
        [-0.2, 0.1], [-0.3, 0.2], [0.2, 0.1], [0.3, 0.2],  # shoulders, elbows
        [-0.4, 0.3], [0.4, 0.3],  # wrists
        [0, -0.1], [-0.1, -0.2], [0.1, -0.2],  # hips, knees
        [-0.2, -0.3], [0.2, -0.3],  # ankles
        [0, 0], [0, -0.1], [0, -0.2]  # torso points for stability
    ]) * 10  # Scale for visibility
    return positions

# Update function for animation
def update(frame, scat, positions):
    # Simple sinusoidal motion to simulate breathing and slight arm/leg movement
    t = frame * 0.1
    new_positions = positions.copy()
    # Breathing motion (torso and head)
    new_positions[0, 1] += np.sin(t) * 0.2  # head
    new_positions[10:13, 1] += np.sin(t) * 0.2  # torso
    # Slight arm and leg movement
    new_positions[2, 1] += np.sin(t) * 0.1  # left elbow
    new_positions[3, 1] += np.sin(t) * 0.1  # right elbow
    new_positions[9, 1] += np.sin(t) * 0.1  # left knee
    new_positions[10, 1] += np.sin(t) * 0.1  # right knee
    scat.set_offsets(new_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Initialize scatter plot
positions = init_positions()
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(scat, positions),
                             interval=50, blit=True)

plt.show()
