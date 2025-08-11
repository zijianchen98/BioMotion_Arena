
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [-1, 4], [-2, 4],
    [0, 3], [1, 2], [2, 2], [-1, 2], [-2, 2],
    [0, 0], [1, 0],
    [0, -3], [1, -3],
    [0, -6]
])

# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 6)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=5)

# Function to update the positions of the point-lights for each frame
def animate(i):
    # Calculate the angle for the hand wave
    angle = np.sin(2 * np.pi * i / num_frames) * 0.5  # Reduced wave magnitude
    
    # Apply the wave motion to the right hand points (simplified wave)
    current_positions = initial_positions.copy()
    right_hand_indices = [2, 3, 7, 8]
    
    for idx in right_hand_indices:
        x = initial_positions[idx, 0]
        y = initial_positions[idx, 1]
        current_positions[idx, 0] = x + angle 
        current_positions[idx, 1] = y + angle * x # Slight y-axis adjustment based on x-position
    
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=40, blit=True)


plt.show()

