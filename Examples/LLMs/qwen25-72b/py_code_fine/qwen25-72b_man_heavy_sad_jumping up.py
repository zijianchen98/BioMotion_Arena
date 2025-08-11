
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the point-lights
positions = np.array([
    [0, -5],  # Center of mass (hips)
    [-1, -4], [1, -4],  # Legs
    [-2, -3], [2, -3],  # Knees
    [-3, -2], [3, -2],  # Ankles
    [0, -3],  # Torso
    [-1, -2], [1, -2],  # Shoulders
    [-2, -1], [2, -1],  # Elbows
    [-3, 0], [3, 0],  # Wrists
    [0, 0]  # Head
])

# Define the scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=10)

# Define the parameters for the jumping motion
amplitude = 2
frequency = 0.5
phase = 0

def update(frame):
    global phase
    phase += frequency * 0.1
    
    # Update the positions of the point-lights
    new_positions = positions.copy()
    
    # Apply vertical displacement to simulate jumping
    displacement = amplitude * np.sin(phase)
    
    # Adjust the positions based on the displacement
    new_positions[:, 1] += displacement
    
    # Apply additional biomechanical adjustments
    if displacement > 0:
        # During the upward phase, the legs and arms extend
        new_positions[1:5, 1] -= displacement * 0.5
        new_positions[10:14, 1] -= displacement * 0.5
    else:
        # During the downward phase, the legs and arms contract
        new_positions[1:5, 1] += displacement * 0.5
        new_positions[10:14, 1] += displacement * 0.5
    
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
