
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
# These positions are simplified and should be adjusted for more realistic movement
initial_positions = np.array([
    [0, 0],  # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Wrists
    [0, -4],  # Waist
    [-1, -5], [1, -5],  # Hips
    [-2, -6], [2, -6],  # Knees
    [-3, -7], [3, -7],  # Ankles
    [-4, -8], [4, -8]   # Feet
])

# Function to update the positions of the point-lights
def update(frame):
    # Apply a simple sine wave to simulate lying down motion
    amplitude = 0.5
    frequency = 0.1
    phase = frame * frequency
    new_positions = initial_positions.copy()
    
    # Adjust the positions to simulate lying down
    for i in range(len(new_positions)):
        if i == 0:  # Head
            new_positions[i][1] += amplitude * np.sin(phase)
        elif i in [1, 2]:  # Shoulders
            new_positions[i][1] += amplitude * np.sin(phase + np.pi / 4)
        elif i in [3, 4]:  # Elbows
            new_positions[i][1] += amplitude * np.sin(phase + np.pi / 2)
        elif i in [5, 6]:  # Wrists
            new_positions[i][1] += amplitude * np.sin(phase + 3 * np.pi / 4)
        elif i == 7:  # Waist
            new_positions[i][1] += amplitude * np.sin(phase + np.pi)
        elif i in [8, 9]:  # Hips
            new_positions[i][1] += amplitude * np.sin(phase + 5 * np.pi / 4)
        elif i in [10, 11]:  # Knees
            new_positions[i][1] += amplitude * np.sin(phase + 3 * np.pi / 2)
        elif i in [12, 13]:  # Ankles
            new_positions[i][1] += amplitude * np.sin(phase + 7 * np.pi / 4)
        elif i in [14, 15]:  # Feet
            new_positions[i][1] += amplitude * np.sin(phase + 2 * np.pi)
    
    scatter.set_offsets(new_positions)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
