
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
# These points represent key joints in the body
initial_positions = np.array([
    [0, 0],  # Hip center
    [-0.1, 0.1],  # Left hip
    [0.1, 0.1],  # Right hip
    [-0.1, 0.3],  # Left knee
    [0.1, 0.3],  # Right knee
    [-0.1, 0.5],  # Left ankle
    [0.1, 0.5],  # Right ankle
    [0, 0.2],  # Waist
    [0, 0.4],  # Chest
    [0, 0.6],  # Neck
    [-0.05, 0.8],  # Left shoulder
    [0.05, 0.8],  # Right shoulder
    [-0.05, 1.0],  # Left elbow
    [0.05, 1.0],  # Right elbow
    [0, 1.2]  # Head
])

# Define the animation parameters
frame_rate = 60  # Frames per second
duration = 5  # Duration of the animation in seconds
num_frames = int(frame_rate * duration)

# Function to update the positions of the points
def update_positions(frame):
    t = frame / frame_rate  # Time in seconds
    amplitude = 0.1  # Amplitude of the jump
    frequency = 1  # Frequency of the jump
    
    # Update the y-coordinates to simulate jumping
    for i in range(len(initial_positions)):
        initial_positions[i, 1] += amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the x-coordinates to simulate forward motion
    for i in range(len(initial_positions)):
        initial_positions[i, 0] += 0.01 * t
    
    return initial_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Animation function
def animate(frame):
    new_positions = update_positions(frame)
    points.set_offsets(new_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/frame_rate, blit=True)

# Display the animation
plt.show()
