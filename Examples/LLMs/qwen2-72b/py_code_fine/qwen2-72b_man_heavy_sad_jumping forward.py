
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Number of points
n_points = 15

# Initial positions
positions = np.random.uniform(low=-0.5, high=0.5, size=(n_points, 2))

# Initial velocities
velocities = np.zeros((n_points, 2))
velocities[:, 1] = 1  # All points move upwards initially

# Points collection
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities
    
    # Apply gravity
    velocities[:, 1] -= 0.1
    
    # Bounce back if hit the ground
    hit_ground = positions[:, 1] < -0.5
    velocities[hit_ground, 1] *= -0.7  # Dampen bounce
    positions[hit_ground, 1] = -0.5
    
    # Update data for points
    points.set_data(positions[:, 0], positions[:, 1])
    
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200,
                              init_func=init, blit=True)

plt.show()
