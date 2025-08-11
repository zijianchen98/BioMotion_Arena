
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for a jumping woman
points = [
    [0, 0],  # Head
    [-0.1, -0.1],  # Left shoulder
    [0.1, -0.1],  # Right shoulder
    [-0.2, -0.3],  # Left elbow
    [0.2, -0.3],  # Right elbow
    [-0.3, -0.5],  # Left hand
    [0.3, -0.5],  # Right hand
    [0, -0.2],  # Torso
    [-0.1, -0.4],  # Left hip
    [0.1, -0.4],  # Right hip
    [-0.2, -0.6],  # Left knee
    [0.2, -0.6],  # Right knee
    [-0.3, -0.8],  # Left foot
    [0.3, -0.8],  # Right foot
    [0, -0.9]  # Pelvis
]

# Convert points to a NumPy array
points = np.array(points)

# Define the parameters for the jumping motion
amplitude = 0.2  # Jump height
frequency = 0.5  # Frequency of the jump
duration = 2  # Duration of the animation in seconds
frames_per_second = 30  # Frames per second

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1.2, 0.2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the point-lights
lights = [plt.plot([], [], 'o', color='white')[0] for _ in range(len(points))]

# Function to update the position of the points
def update(frame):
    t = frame / frames_per_second
    y_offset = amplitude * np.sin(2 * np.pi * frequency * t)
    
    for i, light in enumerate(lights):
        x, y = points[i]
        light.set_data(x, y + y_offset)
    
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(duration * frames_per_second), interval=1000/frames_per_second, blit=True)

# Display the animation
plt.show()
