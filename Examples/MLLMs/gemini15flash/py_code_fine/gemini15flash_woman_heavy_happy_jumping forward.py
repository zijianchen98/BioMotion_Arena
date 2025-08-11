
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0, 3], [1, 3], [2, 3], [3, 3],
    [0, 2], [1, 2], [2, 2], [3, 2],
    [1, 1], [2, 1], [1.5, 0]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Function to update the positions of the point-lights
def update(frame_num, points, lines):
    # Simple jumping motion for demonstration (replace with more realistic biomechanics)
    amplitude = 1.0  # Adjust for jump height
    frequency = 0.5  # Adjust for jump speed
    
    new_positions = initial_positions.copy()
    new_positions[:, 1] += amplitude * np.sin(2 * np.pi * frequency * frame_num * dt)
    new_positions[:, 0] += amplitude/2 * np.sin(2 * np.pi * frequency/2 * frame_num * dt) #Adding a slight horizontal motion
    
    for i, point in enumerate(points):
        point.set_data(new_positions[i, 0], new_positions[i, 1])
    return points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 5)
ax.set_ylim(-2, 8)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-lights
points = [plt.plot([], [], 'wo')[0] for _ in range(15)]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(points, []), interval=20, blit=True)

plt.show()

