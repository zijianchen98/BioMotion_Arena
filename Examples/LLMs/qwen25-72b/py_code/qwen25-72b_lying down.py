
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a person lying down
def get_points(t):
    # t is the time parameter (0 to 1)
    # Define the positions of the 15 points
    points = np.array([
        [0.5, 0.9],  # Head
        [0.45, 0.8], [0.55, 0.8],  # Shoulders
        [0.4, 0.7], [0.6, 0.7],  # Elbows
        [0.35, 0.6], [0.65, 0.6],  # Wrists
        [0.5, 0.5],  # Spine
        [0.45, 0.4], [0.55, 0.4],  # Hips
        [0.4, 0.3], [0.6, 0.3],  # Knees
        [0.35, 0.2], [0.65, 0.2],  # Ankles
        [0.5, 0.1]  # Feet
    ])
    
    # Introduce a small sinusoidal movement to simulate breathing
    amplitude = 0.02
    frequency = 2 * np.pi
    points[:, 1] += amplitude * np.sin(frequency * t)
    
    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter([], [], s=50, color='white')

# Initialize the animation
def init():
    scat.set_offsets([])
    return scat,

# Update the animation frame
def update(frame):
    points = get_points(frame / 100)  # Normalize time to 0-1
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True)

# Display the animation
plt.show()
