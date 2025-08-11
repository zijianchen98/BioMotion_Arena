
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
positions = np.random.rand(num_lights, 2)

# Define the velocities of the point lights
velocities = np.random.randn(num_lights, 2)
velocities /= np.linalg.norm(velocities, axis=1, keepdims=True)

# Define the acceleration due to gravity
gravity = np.array([0, -9.8])

# Define the damping coefficient
damping = 0.95

# Define the time step
dt = 0.05

# Define the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

def update(frame):
    global positions, velocities
    
    # Apply gravity and damping
    accelerations = gravity + damping * (-velocities)
    
    # Update velocities
    velocities += accelerations * dt
    
    # Update positions
    positions += velocities * dt
    
    # Wrap around boundaries
    positions %= 2
    
    # Update scatter plot
    scatter.set_offsets(positions)
    
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)
plt.show()
