
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent key joints of the human body:
# 0-Head, 1-Neck, 2-Shoulder R, 3-Shoulder L, 4-Elbow R, 5-Elbow L,
# 6-Wrist R, 7-Wrist L, 8-Hip R, 9-Hip L, 10-Knee R, 11-Knee L,
# 12-Ankle R, 13-Ankle L, 14-Toes

initial_positions = np.array([
    [0.0, 1.0],  # Head
    [0.0, 0.8],  # Neck
    [0.2, 0.6],  # Shoulder R
    [-0.2, 0.6], # Shoulder L
    [0.3, 0.4],  # Elbow R
    [-0.3, 0.4], # Elbow L
    [0.4, 0.2],  # Wrist R
    [-0.4, 0.2], # Wrist L
    [0.1, 0.0],  # Hip R
    [-0.1, 0.0], # Hip L
    [0.2, -0.2], # Knee R
    [-0.2, -0.2],# Knee L
    [0.3, -0.4], # Ankle R
    [-0.3, -0.4],# Ankle L
    [0.0, -0.6]   # Toes
])

# Define the amplitude and frequency for the jump
amplitude = 0.3  # Vertical displacement for the jump
frequency = 0.5  # Frequency of the jump (cycles per second)

# Define the number of frames for the animation
num_frames = 100
dt = 0.1  # Time step between frames

# Function to update the positions based on time
def update_positions(t):
    # Apply vertical oscillation for the jump
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the y-coordinates of all points
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += vertical_displacement
    
    # Add some sagging effect for the "sad" appearance
    updated_positions[0:8, 1] -= 0.05  # Head and upper body sag slightly
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.8, 1.2)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_aspect('equal')

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame * dt  # Current time
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()
