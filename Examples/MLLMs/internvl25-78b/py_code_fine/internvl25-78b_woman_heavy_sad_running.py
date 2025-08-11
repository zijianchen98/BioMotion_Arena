
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initial positions for the 15 point-lights
initial_positions = np.array([
    [5, 9],  # Head
    [4.5, 8], [5.5, 8],  # Shoulders
    [4, 7], [6, 7],  # Arms
    [4.5, 6], [5.5, 6],  # Waist
    [4, 5], [6, 5],  # Hips
    [4.5, 4], [5.5, 4],  # Thighs
    [4, 3], [6, 3],  # Knees
    [4.5, 2], [5.5, 2],  # Ankles
    [4, 1], [6, 1]  # Feet
])

# Scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def update(frame):
    # Simple running motion simulation
    phase = frame % 360
    new_positions = initial_positions.copy()
    
    # Moving hips and legs alternately
    if phase < 180:
        new_positions[8:, 1] -= 0.1 * np.sin(np.radians(phase))
    else:
        new_positions[8:, 1] += 0.1 * np.sin(np.radians(phase - 180))
    
    # Bobbing head and shoulders
    new_positions[0, 1] -= 0.05 * np.sin(np.radians(phase))
    new_positions[1:3, 1] -= 0.05 * np.sin(np.radians(phase))
    
    # Lateral movement for a running effect
    new_positions[:, 0] += 0.05 * np.cos(np.radians(phase))
    
    scat.set_offsets(new_positions)
    return scat,

# Animation setup
ani = animation.FuncAnimation(fig, update, frames=360, interval=50, blit=True)

plt.show()
