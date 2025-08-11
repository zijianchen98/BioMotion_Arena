
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
num_points = 15
frames = 100
background_color = 'black'
point_color = 'white'

# Define initial positions of points
# Upper body and arms positions (x, y)
points = np.array([
    [0, 6],   # Head
    [-1, 5],  # Shoulder Left
    [1, 5],   # Shoulder Right
    [0, 4],   # Elbow Left
    [0, 4],   # Elbow Right
    [-1, 3],  # Hand Left
    [1, 3],   # Hand Right
    [0, 2],   # Upper Body
    [0, 1],   # Hips
    [-0.5, 0], # Leg Left
    [0.5, 0],  # Leg Right
    [0, 1],   # Near mid torso, for balance
    [-0.5, 1], # Body width representation
    [0.5, 1],  # Body width representation
    [-0.5, 2], # Knee Left
    [0.5, 2],  # Knee Right
])

# Define the hand waving animation function
def update(frame):
    plt.cla() # Clear the current axes

    # Create a smooth waving motion
    wave_movement = np.sin(np.linspace(0, 2 * np.pi, num_points) + frame * 0.1)
    wave_y_offsets = np.clip(wave_movement, -1, 1)  # Limit the wave to realistic motion

    # Update hand positions (simulating a waving motion)
    points[5, 1] = 3 + wave_y_offsets[5]  # Left hand
    points[6, 1] = 3 + wave_y_offsets[6]  # Right hand
    
    # Draw points
    plt.scatter(points[:, 0], points[:, 1], color=point_color)
    plt.xlim(-2, 2)
    plt.ylim(-1, 7)
    plt.gca().set_facecolor(background_color)
    plt.axis('off')  # Turn off the axis

# Set up the figure for animation
fig = plt.figure(figsize=(5, 10))
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
