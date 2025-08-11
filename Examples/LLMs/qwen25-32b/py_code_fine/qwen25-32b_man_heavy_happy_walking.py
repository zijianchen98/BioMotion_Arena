
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the frames per second for the animation
fps = 30

# Time in seconds
duration = 5

# Number of frames
frames = fps * duration

# Define the initial positions of the point-lights
positions = np.zeros((frames, num_points, 2))

# Function to generate walking motion for the point-lights
def walking_motion(t, amp=1, freq=1):
    return amp * np.sin(2 * np.pi * freq * t)

# Assigning positions to simulate a walking figure
for i in range(frames):
    t = i / fps  # time in seconds
    
    # Head
    positions[i, 0] = [0.5, 0.9]
    
    # Shoulders
    positions[i, 1] = [0.4, 0.7]
    positions[i, 2] = [0.6, 0.7]
    
    # Elbows
    positions[i, 3] = [0.3, 0.5 + walking_motion(t, amp=0.1, freq=1)]
    positions[i, 4] = [0.7, 0.5 + walking_motion(t, amp=0.1, freq=1)]
    
    # Hands
    positions[i, 5] = [0.2, 0.3 + walking_motion(t, amp=0.15, freq=2)]
    positions[i, 6] = [0.8, 0.3 + walking_motion(t, amp=0.15, freq=2)]
    
    # Hips
    positions[i, 7] = [0.4, 0.3]
    positions[i, 8] = [0.6, 0.3]
    
    # Knees
    positions[i, 9] = [0.3, 0.1 + walking_motion(t, amp=0.2, freq=1.5)]
    positions[i, 10] = [0.7, 0.1 + walking_motion(t, amp=0.2, freq=1.5)]
    
    # Feet
    positions[i, 11] = [0.2, -0.1 + walking_motion(t, amp=0.25, freq=2)]
    positions[i, 12] = [0.8, -0.1 + walking_motion(t, amp=0.25, freq=2)]
    
    # Heavy weight
    positions[i, 13] = [0.5, 0.1 + walking_motion(t, amp=0.1, freq=1.5)]
    positions[i, 14] = [0.5, 0.05 + walking_motion(t, amp=0.15, freq=1.5)]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 1)
ax.axis('off')  # Turn off the axis

# Scatter plot for the points
scat = ax.scatter(positions[0,:,0], positions[0,:,1], c='white', s=10)

# Update function for the animation
def update(num):
    scat.set_offsets(positions[num])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=False)

plt.show()
