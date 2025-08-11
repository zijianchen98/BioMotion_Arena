
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 7], [3, 2], [3, 8],
    [4, 1], [4, 9], [5, 0], [5, 10], [6, 1], [6, 9], [7, 2], [7, 8]
])


# Function to update the positions of the point-lights at each frame
def update(frame_num, data, lines):
    #Simulate walking motion.  This is a simplified example, 
    #and a more sophisticated model would be needed for truly realistic motion.
    x_offsets = np.sin(frame_num * 0.1) * 0.5
    y_offsets = np.cos(frame_num * 0.1) * 0.2

    new_positions = initial_positions + np.column_stack((x_offsets, y_offsets))
    
    # Add some random jitter for a more natural look
    new_positions += np.random.normal(scale=0.1, size=new_positions.shape)

    for i, line in enumerate(lines):
        line.set_data(new_positions[i,0], new_positions[i,1])

    return lines,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 10)  # Adjust limits as needed
ax.set_ylim(-2, 12)  # Adjust limits as needed
ax.set_aspect('equal')  # Ensure circles appear circular
ax.set_facecolor('black') #Set background to black

# Create the point-light lines (initially at their starting position)
lines = [ax.plot([], [], 'wo', markersize=8)[0] for _ in range(15)]


# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, lines),
                              frames=200, interval=50, blit=True)


plt.show()
