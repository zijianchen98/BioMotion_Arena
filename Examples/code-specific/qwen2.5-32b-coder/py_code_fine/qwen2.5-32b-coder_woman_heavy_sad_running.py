
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100
dt = 0.1
g = 9.81
mass = 70  # Assuming a heavy weight
k = 0.1  # Spring constant for limbs
b = 0.1  # Damping coefficient

# Initial positions and velocities
positions = np.zeros((num_points, 2))
velocities = np.zeros((num_points, 2))

# Define the skeleton structure
skeleton = [
    (0, 1), (1, 2), (2, 3),  # Head, neck, torso
    (3, 4), (4, 5),           # Right arm
    (3, 6), (6, 7),           # Left arm
    (3, 8), (8, 9), (9, 10),   # Right leg
    (3, 11), (11, 12), (12, 13) # Left leg
]

# Initial configuration
positions[0] = [0, 1.5]  # Head
positions[1] = [0, 1.2]  # Neck
positions[2] = [0, 1]    # Torso
positions[3] = [0, 0.8]  # Hips

# Arms
positions[4] = [0.2, 1]  # Right shoulder
positions[5] = [0.4, 0.8]  # Right elbow
positions[6] = [-0.2, 1]  # Left shoulder
positions[7] = [-0.4, 0.8]  # Left elbow

# Legs
positions[8] = [0.2, 0.6]  # Right hip
positions[9] = [0.4, 0.4]  # Right knee
positions[10] = [0.6, 0.2]  # Right ankle
positions[11] = [-0.2, 0.6]  # Left hip
positions[12] = [-0.4, 0.4]  # Left knee
positions[13] = [-0.6, 0.2]  # Left ankle

def update(frame):
    global positions, velocities
    
    # Calculate forces
    forces = np.zeros_like(positions)
    
    # Gravity
    forces[:, 1] -= g * mass
    
    # Springs
    for i, j in skeleton:
        delta = positions[i] - positions[j]
        distance = np.linalg.norm(delta)
        force_magnitude = k * (distance - 1)  # Assuming rest length of 1
        force_direction = delta / distance
        forces[i] += force_magnitude * force_direction
        forces[j] -= force_magnitude * force_direction
    
    # Damping
    forces -= b * velocities
    
    # Update velocities and positions
    accelerations = forces / mass
    velocities += accelerations * dt
    positions += velocities * dt
    
    # Apply boundary conditions (ground)
    for i in range(num_points):
        if positions[i, 1] < 0:
            positions[i, 1] = 0
            velocities[i, 1] = 0
    
    # Update plot
    for line, (i, j) in zip(lines, skeleton):
        line.set_data([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]])
    
    return lines

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create lines for each bone
lines = [ax.plot([], [], 'o-', lw=2)[0] for _ in skeleton]

# Animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
