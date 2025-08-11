
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
duration = 200  # Duration in frames
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
sc = ax.scatter([], [], s=50, color='white')

# Define the walking motion for the points
def walking_motion(t):
    # Amplitude of the walk
    amplitude = 0.5
    # Frequency of the walk
    frequency = 0.1
    
    # Base positions for the points to create a human-like figure
    # 7 points for the legs, 6 for the upper body, and 2 for the head
    positions = []
    for i in range(num_points):
        if i < 7:
            # Legs
            x = 0 + i * 0.1
            y = amplitude * np.sin(frequency * t + i * 0.5) + (num_points - i - 1) * 0.1
        elif i < 13:
            # Upper body
            x = 0 + (i - 7) * 0.1
            y = amplitude * np.sin(frequency * t + i * 0.3) + (num_points - 7) * 0.1
        else:
            # Head
            x = 0.5
            y = amplitude * np.sin(frequency * t) + (num_points - 1) * 0.1
        positions.append((x, y))
    
    return np.array(positions)

# Animation update function
def update(frame):
    positions = walking_motion(frame)
    sc.set_offsets(positions)
    return sc,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, duration), blit=True)

# Show the animation
plt.show()
