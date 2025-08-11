
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 50], [-10, 40], [10, 40],  # Head
    [-20, 30], [20, 30],  # Shoulders
    [-25, 20], [25, 20],  # Elbows
    [-20, 10], [20, 10],  # Hands
    [-10, 20], [10, 20],  # Torso
    [-15, 0], [15, 0],  # Hips
    [-10, -20], [10, -20]   # Knees/Feet (simplified)
])


# Function to simulate bowing movement
def bowing_motion(t, initial_positions):
    """Simulates a bowing motion by adjusting point light positions over time."""
    positions = initial_positions.copy()
    angle = 0.4 * np.sin(0.05 * t)  # bowing angle, modify for speed/depth
    # Head movement
    positions[:3, 1] -= 10 * angle  # Move head down during bow
    positions[:3, 0] += 2 * np.sin(0.1*t)

    # Torso bending
    positions[9:11, 1] -= 5 * angle # torso down
    positions[9:11, 0] += np.sin(0.1 * t)

    return positions




# Create figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim([-40, 40])  # Adjust limits based on movement range
ax.set_ylim([-30, 60])
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=20, c='white')

# Animation update function
def update(frame):
    positions = bowing_motion(frame, initial_positions)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200, 1), interval=20, blit=True)


plt.show()
