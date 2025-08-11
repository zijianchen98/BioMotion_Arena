
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 0],  # Head
    [-10, 10],  # Left Shoulder
    [10, 10],  # Right Shoulder
    [-15, 20],  # Left Elbow
    [15, 20],  # Right Elbow
    [-20, 30],  # Left Hand
    [20, 30],  # Right Hand
    [-10, -10],  # Left Hip
    [10, -10],  # Right Hip
    [-15, -20],  # Left Knee
    [15, -20],  # Right Knee
    [-20, -30],  # Left Foot
    [20, -30],  # Right Foot
    [-5, -15], #Pelvis
    [5, -15] #Pelvis

])

# Define the animation function
def animate(i):
    global initial_positions
    # Simulate turning around motion
    angle = i * np.pi / 180  #increase angle with time 
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = np.dot(initial_positions, rotation_matrix.T)
    
    #add some realistic wobble
    wobble = np.random.normal(scale=2, size=(15,2))
    rotated_positions += wobble

    # Update the plot
    ln.set_offsets(rotated_positions)
    return ln,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the point lights
ln, = ax.plot([], [], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

# Show the animation
plt.show()

