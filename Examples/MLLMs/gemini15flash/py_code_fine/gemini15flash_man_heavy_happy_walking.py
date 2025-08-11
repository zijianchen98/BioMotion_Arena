
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5],  # Head
    [-1, 4], [0, 4], [1, 4], # Shoulders
    [-1.5, 3], [-0.5, 3], [0.5, 3], [1.5, 3],  # Upper arms and torso
    [-1.5, 2], [-0.5, 2], [0.5, 2], [1.5, 2], # Lower arms and torso
    [0, 1], [0, 0]  # Legs
])


# Define a function to update the positions of the point-lights for each frame
def update_positions(frame_num, points, positions):
    # Simple walking animation:  Modify this to create more complex movements
    step_size = 0.1
    for i in range(len(positions)):
        if i == 0: #head moves slightly less 
            positions[i, 0] += step_size * np.sin(frame_num * 0.1) * 0.8
        elif i < 8: #upper body moves moderately
            positions[i, 0] += step_size * np.sin(frame_num * 0.1)
        else: # lower body moves more
            positions[i, 0] += step_size * np.sin(frame_num * 0.1) * 1.2


        positions[i, 1] = initial_positions[i, 1] + step_size * np.cos(frame_num*0.1) * 0.2  #Slight vertical bobbing
    points.set_offsets(positions)
    return points,

# Set up the figure and axes
fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-1, 8))
ax.set_facecolor('black')  # Set background to black

# Create the point-light scatter plot
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(points, initial_positions.copy()),
                              frames=200, interval=50, blit=True)

#Show the animation
plt.show()

