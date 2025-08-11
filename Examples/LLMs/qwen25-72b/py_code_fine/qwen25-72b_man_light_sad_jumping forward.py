
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.axis('off')

# Define the initial positions of the point-lights
initial_positions = [
    [0, 0],  # Center of mass
    [-2, 2], [2, 2],  # Shoulders
    [-3, 1], [3, 1],  # Elbows
    [-4, 0], [4, 0],  # Hands
    [0, -2],  # Hip
    [-1, -3], [1, -3],  # Knees
    [-2, -4], [2, -4],  # Feet
    [0, 2],  # Head
    [0, -5]  # Ground
]

# Convert to numpy array
positions = np.array(initial_positions)

# Define the point-lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    global positions
    
    # Simulate jumping forward
    if frame < 30:
        # Ascend
        positions[:, 1] += 0.1 * np.sin(np.linspace(0, 2 * np.pi, 15))
    elif frame < 60:
        # Descend
        positions[:, 1] -= 0.1 * np.sin(np.linspace(0, 2 * np.pi, 15))
    else:
        # Reset
        positions = np.array(initial_positions)
    
    # Move forward
    positions[:, 0] += 0.1
    
    # Update the point-lights
    for i, point in enumerate(points):
        point.set_data(positions[i, 0], positions[i, 1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=90, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
