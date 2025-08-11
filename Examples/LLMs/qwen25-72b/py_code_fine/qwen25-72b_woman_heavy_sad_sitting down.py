
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 5],  # Head
    [-2, 4], [2, 4],  # Shoulders
    [-3, 3], [3, 3],  # Elbows
    [-4, 2], [4, 2],  # Wrists
    [0, 3],  # Spine
    [0, 1],  # Hip
    [-2, 0], [2, 0],  # Knees
    [-3, -1], [3, -1],  # Ankles
    [-4, -2], [4, -2]  # Feet
])

# Define the point-lights
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    # Apply a simple sitting down motion
    t = frame / 100.0  # Time parameter
    for i, pos in enumerate(initial_positions):
        x, y = pos
        if i == 0:  # Head
            y -= 2 * t
        elif i in [1, 2]:  # Shoulders
            y -= 1.5 * t
        elif i in [3, 4]:  # Elbows
            y -= 1.5 * t
            x += (-1) ** i * 0.5 * t
        elif i in [5, 6]:  # Wrists
            y -= 1.5 * t
            x += (-1) ** i * 1.0 * t
        elif i == 7:  # Spine
            y -= 2 * t
        elif i == 8:  # Hip
            y -= 2 * t
        elif i in [9, 10]:  # Knees
            y -= 2 * t
            x += (-1) ** i * 0.5 * t
        elif i in [11, 12]:  # Ankles
            y -= 2 * t
            x += (-1) ** i * 0.5 * t
        elif i in [13, 14]:  # Feet
            y -= 2 * t
            x += (-1) ** i * 0.5 * t
        
        points[i].set_data(x, y)
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
