
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-light positions for a jumping woman (simplified biomechanical model)
# Positions are approximate joint coordinates (x, y) normalized to [0, 1]
initial_positions = np.array([
    [0.5, 0.2],  # Head
    [0.45, 0.3], [0.55, 0.3],  # Shoulders
    [0.4, 0.4], [0.6, 0.4],  # Elbows
    [0.35, 0.5], [0.65, 0.5],  # Wrists
    [0.45, 0.5], [0.55, 0.5],  # Hips
    [0.4, 0.6], [0.6, 0.6],  # Knees
    [0.38, 0.8], [0.62, 0.8],  # Ankles
    [0.35, 0.9], [0.65, 0.9]  # Feet
])

# Define the animation frames (simplified jump cycle: crouch -> jump -> land)
def update(frame):
    global scatter
    # Normalize time for a smooth cycle (0 to 1 over 100 frames)
    t = frame / 100.0
    if t < 0.3:  # Crouch phase
        height_factor = 1 - (t / 0.3) * 0.3
    elif t < 0.6:  # Jump phase
        height_factor = 0.7 + (t - 0.3) / 0.3 * 0.3
    else:  # Land phase
        height_factor = 1 - (t - 0.6) / 0.4 * 0.3

    # Update positions with biomechanical plausibility
    positions = initial_positions.copy()
    positions[:, 1] *= height_factor  # Vertical movement
    if t < 0.3 or t > 0.6:  # Bend knees during crouch and land
        positions[10:12, 1] += 0.1 * (1 - height_factor)  # Knees
        positions[12:14, 1] += 0.2 * (1 - height_factor)  # Ankles
    if t > 0.3 and t < 0.6:  # Arm swing during jump
        positions[3:5, 1] -= 0.1  # Elbows up
        positions[5:7, 1] -= 0.2  # Wrists up

    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
scatter = ax.scatter([], [], c='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
