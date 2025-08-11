
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the frame rate and duration
frame_rate = 30  # frames per second
duration = 5  # seconds

# Define the number of frames
num_frames = frame_rate * duration

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [-0.2, 0.6], [0.2, 0.6],  # shoulders
    [-0.3, 0.2], [0.3, 0.2],  # hips
    [-0.5, 0], [-0.3, 0], [0.3, 0], [0.5, 0],  # feet
    [-0.1, 0], [0.1, 0],  # hands
    [-0.3, -0.2], [-0.1, -0.2], [0.1, -0.2], [0.3, -0.2]  # arms
])

# Define the walking cycle (sine wave)
def walking_animation(t):
    t = t / num_frames * 2 * np.pi
    return np.sin(t)

# Update function for the animation
def update(frame):
    positions = initial_positions.copy()
    
    # Update positions based on walking cycle
    cycle = walking_animation(frame)
    
    # Move shoulders and hips
    positions[0, 1] += 0.1 * np.sin(cycle)
    positions[1, 1] -= 0.1 * np.sin(cycle)
    
    positions[2, 1] += 0.05 * np.sin(cycle)
    positions[3, 1] -= 0.05 * np.sin(cycle)
    
    # Move feet in opposite directions
    positions[4:6] += np.array([[0.2 * np.sin(cycle), 0.2 * np.cos(cycle)]])
    positions[6:8] += np.array([[0.2 * np.sin(cycle + np.pi), 0.2 * np.cos(cycle + np.pi)]])
    
    # Move hands in opposite directions
    positions[8] += np.array([0.1 * np.sin(cycle + np.pi/2), 0])
    positions[9] += np.array([0.1 * np.sin(cycle - np.pi/2), 0])
    
    # Move arms in a waving motion
    positions[10] += np.array([0.1 * np.sin(cycle), 0])
    positions[11] += np.array([0.1 * np.sin(cycle - np.pi), 0])
    positions[12] += np.array([0.1 * np.sin(cycle + np.pi), 0])
    positions[13] += np.array([0.1 * np.sin(cycle), 0])
    
    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')
scatter = ax.scatter(*zip(*initial_positions), c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 / frame_rate, blit=True)

# Display the animation
plt.show()
