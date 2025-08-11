
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent key joints of a human body
initial_positions = np.array([
    [0, 0],  # Center of mass
    [-1, 1], [1, 1],  # Shoulders
    [-1.5, 1.5], [1.5, 1.5],  # Elbows
    [-2, 1.5], [2, 1.5],  # Wrists
    [-1, -1], [1, -1],  # Hips
    [-1.5, -1.5], [1.5, -1.5],  # Knees
    [-2, -1.5], [2, -1.5],  # Ankles
    [0, -2],  # Head
    [0, -3]  # Weight
])

# Function to simulate the forward roll motion
def forward_roll(t):
    angle = t * np.pi / 4  # Roll angle
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions = np.dot(initial_positions, rotation_matrix.T)
    
    # Adjust positions to simulate the forward roll
    if t < 2:
        positions[:, 1] += (t - 1) * 0.5
    elif t < 4:
        positions[:, 1] -= (t - 3) * 0.5
    else:
        positions[:, 1] += (t - 5) * 0.5
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, color='white')

# Update function for the animation
def update(frame):
    positions = forward_roll(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 8, 200), interval=50, blit=True)

# Show the animation
plt.show()
