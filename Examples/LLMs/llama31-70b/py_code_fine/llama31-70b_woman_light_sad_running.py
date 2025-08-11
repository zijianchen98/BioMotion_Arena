
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
lights = np.array([
    [0, 0],  # Head
    [-0.1, 0.1], [0.1, 0.1],  # Shoulders
    [-0.2, 0.2], [0.2, 0.2],  # Elbows
    [-0.3, 0.3], [0.3, 0.3],  # Hands
    [-0.1, -0.1], [0.1, -0.1],  # Hips
    [-0.2, -0.2], [0.2, -0.2],  # Knees
    [-0.3, -0.3], [0.3, -0.3],  # Ankles
    [-0.2, 0], [0.2, 0],  # Torso
    [0, -0.1]  # Sad face
])

# Define the movement parameters
num_frames = 100
amplitude = 0.1
frequency = 0.1

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter(lights[:, 0], lights[:, 1], c='white')

def animate(frame):
    # Update the point-lights positions
    new_positions = np.copy(lights)
    new_positions[:, 0] += np.sin(frame * frequency) * amplitude
    
    # Move the arms and legs
    new_positions[1:3, 1] += np.sin(frame * frequency * 2) * amplitude * 0.5
    new_positions[3:5, 1] += np.sin(frame * frequency * 2 + np.pi) * amplitude * 0.5
    new_positions[5:7, 0] += np.sin(frame * frequency * 2) * amplitude * 0.5
    new_positions[7:9, 0] += np.sin(frame * frequency * 2 + np.pi) * amplitude * 0.5
    
    # Move the torso and head
    new_positions[10:12, 0] += np.sin(frame * frequency * 0.5) * amplitude * 0.2
    new_positions[0, 0] += np.sin(frame * frequency * 0.5) * amplitude * 0.1
    
    # Update the point-lights
    points.set_offsets(new_positions)
    
    return points,

ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, interval=50)

plt.show()
