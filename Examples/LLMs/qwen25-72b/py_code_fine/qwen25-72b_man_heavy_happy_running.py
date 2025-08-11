
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 0],  # Center of mass
    [-2, 2], [2, 2],  # Shoulders
    [-3, 0], [3, 0],  # Hips
    [-4, -2], [4, -2],  # Knees
    [-5, -4], [5, -4],  # Ankles
    [-6, -6], [6, -6],  # Feet
    [-1, 3], [1, 3],  # Elbows
    [-2, 4], [2, 4],  # Hands
])

# Define the point-lights
points = [plt.Circle((pos[0], pos[1]), 0.2, color='white') for pos in initial_positions]

# Add the point-lights to the plot
for point in points:
    ax.add_patch(point)

# Function to update the positions of the point-lights
def update(frame):
    global initial_positions
    t = frame / 100.0  # Time parameter
    amplitude = 2.0  # Amplitude of the running motion
    frequency = 2.0  # Frequency of the running motion
    
    # Update the positions based on a simple running motion model
    new_positions = initial_positions.copy()
    new_positions[:, 0] += amplitude * np.sin(frequency * t)
    new_positions[:, 1] += amplitude * np.cos(frequency * t)
    
    # Adjust the positions of the limbs to simulate running
    new_positions[1:3, 1] += amplitude * np.sin(frequency * t + np.pi / 2)  # Shoulders
    new_positions[4:6, 1] += amplitude * np.sin(frequency * t + np.pi / 2)  # Hips
    new_positions[7:9, 1] += amplitude * np.sin(frequency * t + np.pi / 2)  # Knees
    new_positions[10:12, 1] += amplitude * np.sin(frequency * t + np.pi / 2)  # Ankles
    new_positions[13:15, 1] += amplitude * np.sin(frequency * t + np.pi / 2)  # Hands
    
    # Update the positions of the point-lights
    for i, point in enumerate(points):
        point.center = (new_positions[i, 0], new_positions[i, 1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=600, interval=20, blit=False)

# Show the animation
plt.show()
