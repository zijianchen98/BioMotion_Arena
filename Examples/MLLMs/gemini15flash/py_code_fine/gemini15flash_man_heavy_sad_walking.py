
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0.5, 3], [1.5, 3], [2.5, 3],
    [1, 2.5], [2, 2.5],
    [1, 2], [2, 2],
    [1, 1], [2,1],
    [1.5, 0], [1.5,-1]
])


# Function to update the positions of the point-lights at each frame
def update(frame_num, points, line_collections):
    # Simple walking animation.  Replace with more sophisticated biomechanical model if needed.
    dx = 0.1 * np.sin(frame_num * 0.1)  # Adjust frequency and amplitude for walking speed
    dy = 0.05 * np.sin(frame_num * 0.15) # Add a little up and down movement to simulate walking
    new_positions = points + np.array([dx, dy])
    
    #Ensure points stay within the frame (simple bounding box)
    new_positions[:,0] = np.clip(new_positions[:,0], -5, 5)
    new_positions[:,1] = np.clip(new_positions[:,1], -5, 5)

    for i, lc in enumerate(line_collections):
        lc.set_offsets(new_positions)


    return line_collections,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')


# Create the point-light scatter plot
points, = ax.plot(initial_positions[:,0], initial_positions[:,1], 'wo', markersize=10)
line_collections = [points]

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, line_collections),
                              frames=100, interval=50, blit=True)

# Show the animation
plt.show()

