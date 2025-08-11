
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters for the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')

# Define initial positions of point lights representing the sad man's body parts
points = np.array([
    [0, 1],    # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Elbows
    [-0.5, -0.5], [0.5, -0.5],  # Hands
    [0, 0.5],  # Torso
    [0, -0.5],  # Hips
    [-0.5, -1], [0.5, -1],  # Knees
    [-0.5, -1.5], [0.5, -1.5],  # Feet
    [0, -1],  # Center of Feet
    [0, 0.5],  # Center of Torso
    [0, -0.5]  # Center of Hips
])

# Function to update the position of point lights for waving action
def update(frame):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')
    ax.axis('off')
    
    # Update hand positions to create a waving effect
    amplitude = 0.2
    wave_speed = 0.1
    hand_movement = np.sin(frame * wave_speed) * amplitude
    
    # Update hand positions
    points[5, 1] += hand_movement  # Left hand
    points[6, 1] += -hand_movement  # Right hand
    
    # Plot each point-light
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
