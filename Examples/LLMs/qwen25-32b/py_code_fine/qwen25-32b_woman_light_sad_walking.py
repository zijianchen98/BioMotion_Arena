
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights
num_lights = 15

# Define the initial positions of the lights
positions = np.array([
    [0.5, 0.5], [0.4, 0.6], [0.6, 0.6], # Head and shoulders
    [0.3, 0.7], [0.7, 0.7],              # Arms
    [0.4, 0.4], [0.6, 0.4],              # Hips
    [0.2, 0.3], [0.8, 0.3],              # Legs
    [0.1, 0.2], [0.9, 0.2],              # Feet
    [0.2, 0.5], [0.8, 0.5],              # Elbows
    [0.15, 0.4], [0.85, 0.4]             # Knees
])

# Define the velocity vectors
velocities = np.zeros((num_lights, 2))

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes

# Create scatter plot for the lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(frame):
    global positions, velocities
    
    # Update the position of each light based on its velocity
    positions += velocities
    
    # Simulate walking by oscillating the legs and feet
    t = frame / 50.0  # Time in seconds
    amplitude = 0.1
    frequency = 1.0
    phase_legs = np.sin(t * 2 * np.pi * frequency)
    phase_feet = np.sin((t + 0.5) * 2 * np.pi * frequency)
    
    # Move legs and feet according to walking motion
    positions[7] += np.array([0, amplitude * phase_legs])
    positions[8] += np.array([0, amplitude * phase_legs])
    positions[9] += np.array([0, amplitude * phase_feet])
    positions[10] += np.array([0, amplitude * phase_feet])
    
    # Adjust arms slightly for natural movement
    positions[3] += np.array([amplitude * phase_legs, 0])
    positions[4] += np.array([-amplitude * phase_legs, 0])
    
    # Update the scatter plot
    scatter.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
