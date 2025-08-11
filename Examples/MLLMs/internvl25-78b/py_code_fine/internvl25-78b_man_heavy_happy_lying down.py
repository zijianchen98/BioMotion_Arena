
import numpy as as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
def init_positions():
    positions = np.array([
        [0, 5], # head
        [-1, 4], [1, 4], # shoulders
        [-2, 3], [2, 3], # elbows
        [-1.5, 2], [1.5, 2], # wrists
        [-3, 1], [3, 1], # hands
        [0, 3], # center of body
        [-1, 2], [1, 2], # hips
        [-2, 1], [2, 1], # knees
        [-1.5, 0], [1.5, 0] # feet
    ])
    return positions

# Update function for the animation
def update(frame, scat, positions):
    # Simple sinusoidal motion to represent lying down
    amplitude = 0.5
    frequency = 0.05
    time = frame / 10.0
    movement = amplitude * np.sin(frequency * time + positions[:, 0])
    
    # Update positions
    new_positions = positions.copy()
    new_positions[:, 1] += movement
    
    # Update scatter plot
    scat.set_offsets(new_positions)
    return scat,

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 5])
ax.set_facecolor('black')

# Create scatter plot
positions = init_positions()
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, fargs=(scat, positions), interval=50, blit=True)

plt.axis('off')
plt.show()
