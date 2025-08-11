
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the points for the happyman
# These positions are simplified and may need to be adjusted for more realism
initial_positions = np.array([
    [0, 0],   # Torso center
    [-1, 1],  # Left shoulder
    [1, 1],   # Right shoulder
    [-2, 2],  # Left elbow
    [2, 2],   # Right elbow
    [-3, 3],  # Left hand (waving)
    [3, 3],   # Right hand
    [-1, -1], # Left hip
    [1, -1],  # Right hip
    [-2, -2], # Left knee
    [2, -2],  # Right knee
    [-3, -3], # Left foot
    [3, -3],  # Right foot
    [0, -2],  # Head
    [0, -4]   # Heavy weight
])

# Define the wave motion for the left hand
def wave(t):
    amplitude = 0.5
    frequency = 1
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Animation update function
def update(frame):
    t = frame / 60.0  # Time in seconds
    positions = initial_positions.copy()
    
    # Update the position of the left hand to simulate waving
    positions[5, 1] += wave(t)
    
    # Update the positions of the points
    for i, point in enumerate(points):
        point.set_data(positions[i, 0], positions[i, 1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(600), blit=True, repeat=True)

# Show the animation
plt.show()
