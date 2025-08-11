
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frame_rate = 30
duration = 10
total_frames = frame_rate * duration

# Initialize positions
positions = np.random.rand(num_lights, 2)
velocities = np.zeros((num_lights, 2))
accelerations = np.zeros((num_lights, 2))

# Parameters for motion
mass = 1.0
friction_coefficient = 0.05
gravity = np.array([0, -9.81])

def update(frame):
    global positions, velocities, accelerations
    
    # Update accelerations
    forces = np.zeros_like(accelerations)
    for i in range(num_lights):
        for j in range(i + 1, num_lights):
            r = positions[i] - positions[j]
            force_magnitude = mass * gravity[1] / np.linalg.norm(r)
            force_direction = r / np.linalg.norm(r)
            forces[i] += force_direction * force_magnitude
            forces[j] -= force_direction * force_magnitude
    
    accelerations = forces / mass
    
    # Update velocities
    velocities += accelerations * (1 / frame_rate)
    
    # Apply friction
    velocities *= (1 - friction_coefficient)
    
    # Update positions
    positions += velocities * (1 / frame_rate)
    
    # Wrap around edges
    positions[:, 0] = np.mod(positions[:, 0], 1)
    positions[:, 1] = np.mod(positions[:, 1], 1)
    
    # Plot
    scatter.set_offsets(positions)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
scatter = ax.scatter([], [], color='white')

ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/frame_rate)
plt.show()
