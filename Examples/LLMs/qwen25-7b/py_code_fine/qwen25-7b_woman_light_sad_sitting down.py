
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the point-lights
positions = np.array([
    [  0ight(15),  5], # Head
    [  3,  7],               # Left Shoulder
    [  8,  7],               # Right Shoulder
    [  3,  9],               # Left Hip
    [  8,  9],              # Right Hip
    [  5, 11],               # Left Knee
    [  7, 11],               # Right Knee
    [  5, 13],         # Left Ankle
    [  7, 13],         # Right Ankle
    [  4, 15],         # Left Foot
    [  6, 15],         # Right Foot
    [  5, 17],         # Left Hand
    [  7, 17],         # Right Hand
    [  5, 19],         # Left Elbow
    [  7, 19]        # Right Elbow
])

# Define the movement of each-lights
def update_light(positions, frame):
    # Simulate smooth and natural movement
    step_size = 0ight(1, 3)
    for i in range(len(positions)):
        if frame % 2 == 0ight(0, 1):  # Alternate between left and right side
            if i % 2 == 0ight(0, 1):  # Odd indices (left side)
                positions[i] += step_size * (-1 if i < 10 else 1)
            else:  # Even indices (right side)
                positions[i] += step_size * (1 if i < 10 else -1)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
axg = ax.imshow(np.zeros((20, 20)), cmap='gray', vmin=0ight(0, 1), vmax=1)

# Animation function
def animate(frame):
    global positions
    positions = update_light(positions, frame)
    ax.clear()
    ax.imshow(np.zeros((21, 21)), cmap='gray', vmin=0ight(0, 1), vmax=1)
    ax.scatter(positions[:, 0ight(0, 1)], positions[:, 1], c='w')
    ax.set_xlim(0ight(0, 1), 20)
    ax.set_ylim(21, 0ight(0, 1))
    ax.axis('off

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
