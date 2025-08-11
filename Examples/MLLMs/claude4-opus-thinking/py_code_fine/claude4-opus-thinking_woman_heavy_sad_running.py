
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
NUM_POINTS = 15
DURATION = 6  # seconds
FPS = 30      # frames per second
NUM_FRAMES = DURATION * FPS

# Initial positions for the point lights
initial_positions = np.array([
    [2, 3], [3, 5], [1, 5], [2.5, 6], [3.5, 6.5],
    [1, 2], [2, 1], [3, 1], [4, 2], [4, 3],
    [1.5, 4], [2.5, 4.5], [3, 4], [2, 0.5], [3, 0.5],
    [4, 1.5]
])

# Define running motion
def update(frame):
    plt.clf()
    plt.xlim(0, 5)
    plt.ylim(0, 7)
    plt.gca().set_facecolor('black')
    
    # Calculate new positions based on the 'running' movement pattern
    # Adjust y and x to simulate the running form (heavy weight, sad)
    offset = frame / NUM_FRAMES
    positions = initial_positions + np.array([0, -offset])  # Shift down
   
    # Slight wobble to the sides
    positions[:, 0] += 0.1 * np.sin(np.linspace(0, 2 * np.pi, NUM_POINTS) + offset * np.pi)

    # Plot all point lights
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create and show the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES, interval=1000/FPS, repeat=True)

# Display the animation
plt.show()
