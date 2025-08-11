
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize the point-lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0],  # Center of mass
    [-1, -2], [1, -2],  # Feet
    [-1, -1], [1, -1],  # Ankles
    [-2, -1], [2, -1],  # Knees
    [-2, 0], [2, 0],  # Hips
    [-3, 0], [3, 0],  # Shoulders
    [-3, 1], [3, 1],  # Elbows
    [-4, 1], [4, 1],  # Hands
    [0, 2]  # Head
])

# Function to update the positions of the points
def update(frame):
    # Simulate walking by adjusting the positions of the points
    x_offset = np.sin(frame * 0.1) * 2  # Side-to-side movement
    y_offset = np.cos(frame * 0.1) * 0.5  # Up-and-down movement
    
    # Apply the offsets to the initial positions
    new_positions = initial_positions + np.array([x_offset, y_offset])
    
    # Adjust the head position to indicate sadness
    head_offset = np.array([0, -0.5 * np.sin(frame * 0.1)])
    new_positions[-1] += head_offset
    
    # Update the positions of the points
    for i, point in enumerate(points):
        point.set_data(new_positions[i])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
