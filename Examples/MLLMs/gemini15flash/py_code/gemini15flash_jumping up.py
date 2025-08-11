
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])

# Define the animation frames (adjust parameters for desired smoothness and duration)
num_frames = 60
jump_height = 4  #Adjust to change jump height
frames = []
for i in range(num_frames):
    # Simulate jumping motion - adjust this part for more complex or nuanced motion
    t = i / num_frames
    y_offset = jump_height * np.sin(np.pi * t)
    y_offset2 = jump_height * np.sin(np.pi * t)
    
    # Apply motion to point-light positions
    frame = initial_positions.copy()
    frame[:,1] += y_offset  # vertical displacement
    
    frames.append(frame)


# Create the animation figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-2, 8])  #adjust x limit as needed
ax.set_ylim([0, 15])  #adjust y limit as needed
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the scatter plot (point-lights)
scat = ax.scatter([], [], s=50, c='white')

# Animation update function
def animate(i):
    scat.set_offsets(frames[i])
    return scat,

# Create and display the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)
plt.show()
