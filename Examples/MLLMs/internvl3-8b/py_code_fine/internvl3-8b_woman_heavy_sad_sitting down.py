
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation

# Define initial positions for the point-lights
initial_positions = np.array([
    [-20, -8],  # Head
    [-12, -15],
    [-5, -8],
    [5, -8],   # Torso
    [12, -15],
    [20, -8],
    [-20, -19], # Left leg
    [-12, -21],
    [-5, -21],
    [-5, -19], # Left knee
    [20, -19],  # Right leg
    [12, -21],
    [5, -21],
    [5, -19],  # Right knee
    [0, -19]   # Seat
])

def update_positions(frame):
    # Simple animation to create a sitting motion
    t = frame / 100.0
    new_positions = np.copy(initial_positions)
    
    # Head movement
    if t < 0.1:
        new_positions[0] = [initial_positions[0,0], initial_positions[0,1] + (0.1 * t)]
    elif t < 0.5:
        new_positions[0] = [initial_positions[0,0] + (0.1 * (t - 0.1)), initial_positions[0,1] + (1.0 * (t - 0.1))]
    
    # Torso movement
    if t < 0.1:
        new_positions[1] = [initial_positions[1,0], initial_positions[1,1] + (0.05 * t)]
    elif t < 0.5:
        new_positions[1] = [initial_positions[1,0] + (0.05 * (t - 0.1)), initial_positions[1,1] + (1.0 * (t - 0.1))]
    
    # Legs movement (simple example)
    new_positions[2] = [initial_positions[2,0], initial_positions[2,1] + (0.1 * t)]
    new_positions[4] = [initial_positions[4,0], initial_positions[4,1] + (0.1 * t)]
    new_positions[5] = [initial_positions[5,0], initial_positions[5,1] + (0.1 * t)]
    new_positions[7] = [initial_positions[7,0], initial_positions[7,1] + (0.3 * t)]
    new_positions[9] = [initial_positions[9,0], initial_positions[9,1] + (0.3 * t)]
    new_positions[10] = [initial_positions[10,0], initial_positions[10,1] + (0.3 * t)]
    new_positions[12] = [initial_positions[12,0], initial_positions[12,1] + (0.3 * t)]
    new_positions[14] = [initial_positions[14,0], initial_positions[14,1] + (0.3 * t)]
    
    return new_positions,

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 10)
ax.set_xticks([])
ax.set_yticks([])

sc = plt.scatter(*initial_positions.T, c='white', s=100)

def update(frame):
    new_positions = update_positions(frame)[0]
    sc.set_offsets(new_positions)
    return sc,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
