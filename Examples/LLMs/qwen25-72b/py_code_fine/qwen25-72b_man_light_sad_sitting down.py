
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
initial_positions = [
    [0, 5],  # Head
    [-2, 4], [2, 4],  # Shoulders
    [-4, 3], [4, 3],  # Elbows
    [-6, 2], [6, 2],  # Hands
    [0, 3],  # Spine
    [-1, 2], [1, 2],  # Hips
    [-3, 1], [3, 1],  # Knees
    [-5, 0], [5, 0]   # Feet
]

# Convert initial positions to a NumPy array
positions = np.array(initial_positions)

# Define the point-lights
point_lights = [plt.plot([], [], 'o', color='white')[0] for _ in range(15)]

def init():
    for light in point_lights:
        light.set_data([], [])
    return point_lights

def update(frame):
    # Simulate sitting down motion
    if frame < 50:
        # Initial movement: bending at the knees and hips
        positions[8:, 1] -= 0.05 * (frame - 25)
        positions[7:9, 1] -= 0.03 * (frame - 25)
    else:
        # Final adjustment: slight bounce and settling
        positions[8:, 1] += 0.01 * np.sin((frame - 50) * 0.5)
        positions[7:9, 1] += 0.01 * np.sin((frame - 50) * 0.5)
    
    # Update the positions of the point-lights
    for i, light in enumerate(point_lights):
        light.set_data(positions[i, 0], positions[i, 1])
    
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
