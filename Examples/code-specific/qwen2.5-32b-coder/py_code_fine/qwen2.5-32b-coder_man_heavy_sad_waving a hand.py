
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initial positions of the points (simplified model of a person waving)
initial_positions = np.array([
    [0, 0],    # Head
    [-1, -1],  # Left Shoulder
    [-2, -2],  # Left Elbow
    [-3, -2],  # Left Hand
    [1, -1],   # Right Shoulder
    [2, -2],   # Right Elbow
    [3, -2],   # Right Hand
    [0, -1],   # Spine Top
    [0, -2],   # Spine Middle
    [0, -3],   # Spine Bottom
    [-1, -3],  # Left Hip
    [-2, -4],  # Left Knee
    [-3, -5],  # Left Foot
    [1, -3],   # Right Hip
    [2, -4],   # Right Knee
    [3, -5]    # Right Foot
])

# Function to update the positions for waving motion
def update(frame):
    t = frame / FPS
    new_positions = initial_positions.copy()

    # Waving motion for the right arm
    wave_angle = np.sin(t) * 0.5
    new_positions[5] += np.array([np.cos(wave_angle), np.sin(wave_angle)])
    new_positions[6] += np.array([np.cos(wave_angle + np.pi/2), np.sin(wave_angle + np.pi/2)])

    # Adjusting left arm to counterbalance
    new_positions[2] += np.array([np.cos(-wave_angle), np.sin(-wave_angle)])
    new_positions[3] += np.array([np.cos(-wave_angle + np.pi/2), np.sin(-wave_angle + np.pi/2)])

    scatter.set_offsets(new_positions)
    return scatter,

# Setting up the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-6, 1)
ax.set_aspect('equal')
ax.axis('off')
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

plt.show()
