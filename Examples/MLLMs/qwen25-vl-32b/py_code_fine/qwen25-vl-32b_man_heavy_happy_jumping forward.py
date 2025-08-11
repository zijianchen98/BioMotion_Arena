
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    # Head
    [0, 1],
    # Shoulders
    [-0.5, 0], [0.5, 0],
    # Elbows
    [-1, -0.5], [1, -0.5],
    # Wrists
    [-1.5, -1], [1.5, -1],
    # Hips
    [-0.3, -1.5], [0.3, -1.5],
    # Knees
    [-0.8, -2.5], [0.8, -2.5],
    # Ankles
    [-1.2, -3.5], [1.2, -3.5]
])

# Define the amplitude and frequency for the jump
amplitude = 1.0  # Vertical displacement
frequency = 0.5  # Frequency of the jump (cycles per second)

# Define the time array
time = np.linspace(0, 2 * np.pi, num_frames)  # One full cycle

# Function to update the positions based on time
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Apply vertical oscillation for the jump
    vertical_displacement = amplitude * np.sin(frequency * frame)
    
    # Adjust head position
    positions[0, 1] += vertical_displacement
    
    # Adjust shoulders, elbows, wrists, hips, knees, and ankles
    for i in range(1, len(positions)):
        if i <= 2:  # Shoulders
            positions[i, 1] += vertical_displacement * 0.8
        elif i <= 4:  # Elbows
            positions[i, 1] += vertical_displacement * 0.6
        elif i <= 6:  # Wrists
            positions[i, 1] += vertical_displacement * 0.4
        elif i <= 8:  # Hips
            positions[i, 1] += vertical_displacement * 0.9
        elif i <= 10:  # Knees
            positions[i, 1] += vertical_displacement * 0.7
        else:  # Ankles
            positions[i, 1] += vertical_displacement * 0.5
    
    # Add horizontal forward motion (linear progression)
    horizontal_progression = frame / num_frames * 2  # Forward movement
    positions[:, 0] += horizontal_progression
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 4)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes
ax.set_facecolor('black')  # Set background to black

# Scatter plot for the point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Animation function
def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
