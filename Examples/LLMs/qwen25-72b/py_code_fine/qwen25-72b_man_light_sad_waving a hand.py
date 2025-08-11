
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0],  # Head
    [-2, -2], [2, -2],  # Shoulders
    [-4, -4], [4, -4],  # Hips
    [-3, -3], [3, -3],  # Elbows
    [-2, -4], [2, -4],  # Hands
    [-5, -5], [5, -5],  # Knees
    [-6, -6], [6, -6],  # Ankles
    [-7, -7], [7, -7]   # Feet
])

# Define the points
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    # Update the positions of the points to simulate waving a hand
    angle = frame * 0.1  # Waving speed
    hand_x = 2 + 2 * np.cos(angle)
    hand_y = -4 + 2 * np.sin(angle)
    
    new_positions = initial_positions.copy()
    new_positions[6] = [hand_x, hand_y]  # Update the right hand position
    
    for i, point in enumerate(points):
        point.set_data(new_positions[i][0], new_positions[i][1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(360), init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
