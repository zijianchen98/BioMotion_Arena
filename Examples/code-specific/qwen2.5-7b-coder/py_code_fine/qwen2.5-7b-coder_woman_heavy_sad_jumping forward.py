
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 8 - 4  # Random positions between -4 and 4 on both axes

# Define the weights for each light
weights = np.linspace(0.1, 0.9, num_lights)

# Define the target position for the sad woman
target_position = np.array([0, 0])

# Define the spring constant for the motion
k = 0.1

# Define the time step
dt = 0.05

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')

lights, = ax.plot([], [], 'o', markersize=10, color='white')

def update(frame):
    global initial_positions
    
    # Calculate the distance from each light to the target position
    distances = np.linalg.norm(initial_positions - target_position, axis=1)
    
    # Calculate the force for each light
    forces = k * (distances - target_position[1])[:, np.newaxis] * initial_positions
    
    # Update the positions of the lights
    initial_positions += forces * dt / distances[:, np.newaxis]
    
    # Apply the weights to the positions
    initial_positions *= weights[:, np.newaxis]
    
    # Set the data for the scatter plot
    lights.set_data(initial_positions[:, 0], initial_positions[:, 1])
    
    return lights,

ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
