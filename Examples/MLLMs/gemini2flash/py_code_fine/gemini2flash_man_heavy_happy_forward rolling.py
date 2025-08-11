
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
plt.axis('off')  # Hide axes

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=6)  # White points

# Define the initial positions of the points (stick figure)
initial_positions = np.array([
    [0, 4],      # Head
    [-1, 3],     # Left Shoulder
    [1, 3],      # Right Shoulder
    [-2, 2],     # Left Elbow
    [2, 2],      # Right Elbow
    [-3, 1],     # Left Wrist
    [3, 1],      # Right Wrist
    [0, 2],      # Torso
    [-1, 0],     # Left Hip
    [1, 0],      # Right Hip
    [-2, -1],    # Left Knee
    [2, -1],     # Right Knee
    [-1.5, -2],  # Left Ankle
    [1.5, -2],   # Right Ankle
    [0, -3]       # Foot
])

# Rolling motion parameters
amplitude = 1.0
frequency = 1.0
phase = 0.0
rotation_speed = 0.05 # Adjust rotation speed as needed

# Animation function
def animate(i):
    global phase
    phase += rotation_speed  # Adjust for speed

    # Create a copy of the initial positions to modify
    new_positions = initial_positions.copy()

    # Apply the rolling motion to each point
    angle = phase 
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    # Rotate the entire figure around the origin
    for j in range(num_points):
        new_positions[j] = np.dot(rotation_matrix, initial_positions[j])
    
    
    # Translate the entire figure horizontally to make it appear moving forward
    translation_x = i * 0.02  # Adjust for forward speed
    new_positions[:, 0] += translation_x

    # Update the positions of the points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=200)

plt.show()
