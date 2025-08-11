
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the coordinates for each frame
def generate_coordinates(t):
    # Define the coordinates of the joints for a running motion
    x = np.array([
        0.25 * np.sin(t),       # Head
        0.5 * np.sin(t) - 0.1,  # Upper body
        0.8 * np.sin(t) - 0.2,  # Lower body
        0.5 * np.cos(t) - 0.3,  # Right arm
        0.5 * np.cos(t) + 0.1,  # Left arm
        0.8 * np.cos(t) - 0.4,  # Right leg
        0.8 * np.cos(t) + 0.2,  # Left leg
        0.1 * np.sin(t) - 0.3,  # Right foot
        0.1 * np.sin(t) + 0.3,  # Left foot
        0.4 * np.sin(t) - 0.2,  # Right hand
        0.4 * np.sin(t) + 0.2,  # Left hand
        0.2 * np.sin(t) - 0.1,  # Hips
        0.2 * np.sin(t) + 0.1,  # Shoulders
        0.3 * np.sin(t) - 0.15, # Right knee
        0.3 * np.sin(t) + 0.15   # Left knee
    ])

    y = np.array([
        0.5 * np.cos(t),       # Head
        0.7 * np.cos(t) - 0.1,  # Upper body
        0.8 * np.cos(t) - 0.2,  # Lower body
        0.6 * np.sin(t) + 0.1,  # Right arm
        0.6 * np.sin(t) - 0.1,  # Left arm
        0.7 * np.sin(t) + 0.2,  # Right leg
        0.7 * np.sin(t) - 0.2,  # Left leg
        0.3 * np.cos(t) + 0.3,  # Right foot
        0.3 * np.cos(t) - 0.3,  # Left foot
        0.4 * np.cos(t) + 0.2,  # Right hand
        0.4 * np.cos(t) - 0.2,  # Left hand
        0.5 * np.sin(t) - 0.2,  # Hips
        0.5 * np.sin(t) + 0.2,  # Shoulders
        0.4 * np.cos(t) + 0.15, # Right knee
        0.4 * np.cos(t) - 0.15   # Left knee
    ])
    
    return x, y

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Create a scatter plot for the points
point_lights, = ax.plot([], [], 'wo')

# Animation update function
def update(frame):
    x, y = generate_coordinates(frame)
    point_lights.set_data(x, y)
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.linspace(0, 2 * np.pi, 128),
    interval=50, blit=True
)

plt.show()
