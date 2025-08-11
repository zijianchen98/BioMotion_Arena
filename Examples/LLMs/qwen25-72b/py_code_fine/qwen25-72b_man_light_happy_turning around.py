
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
points = [
    [0, 0],  # Center of rotation
    [1, 2],  # Head
    [-1, 1],  # Left shoulder
    [1, 1],  # Right shoulder
    [-2, 0],  # Left hip
    [2, 0],  # Right hip
    [-1, -1],  # Left knee
    [1, -1],  # Right knee
    [-2, -2],  # Left foot
    [2, -2],  # Right foot
    [0, 1],  # Spine
    [-1.5, 0.5],  # Left arm
    [1.5, 0.5],  # Right arm
    [-2, 0.5],  # Left elbow
    [2, 0.5],  # Right elbow
    [-2.5, 0.5],  # Left hand
    [2.5, 0.5]   # Right hand
]

# Create the scatter plot for the points
scat = ax.scatter([p[0] for p in points], [p[1] for p in points], color='white', s=50)

# Define the angle of rotation
angle = 0

def update(frame):
    global angle
    angle += 5  # Increment the angle by 5 degrees per frame
    new_points = []
    for p in points:
        x, y = p
        # Rotate the point around the center (0, 0)
        x_new = x * np.cos(np.radians(angle)) - y * np.sin(np.radians(angle))
        y_new = x * np.sin(np.radians(angle)) + y * np.cos(np.radians(angle))
        new_points.append([x_new, y_new])
    
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=50, blit=True)

# Display the animation
plt.show()
