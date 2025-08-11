
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])


# Define the animation frames
num_frames = 30
frames = []
for i in range(num_frames):
    #Simulate jumping forward
    positions = initial_positions.copy()
    positions[:, 0] += i * 0.2  # Move the points horizontally
    positions[:, 1] += np.sin(i/3) * 2  # Add a simple vertical jump

    frames.append(positions)



#Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1, 10]) # Adjust x limits for better visualization
ax.set_ylim([-1, 10]) # Adjust y limits for better visualization
ax.set_aspect('equal')
ax.set_facecolor('black')


#Create the scatter plot
scat = ax.scatter([], [], s=50, c='white')

# Animation update function
def animate(i):
    x = frames[i][:, 0]
    y = frames[i][:, 1]
    scat.set_offsets(np.c_[x, y])
    return scat,


#Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)


# Show the animation
plt.show()

