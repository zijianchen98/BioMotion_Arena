
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
points = ax.scatter([], [], color='white')  # Create a scatter plot

# Define the number of points and their initial positions
n_points = 15
initial_positions = np.array([
    [5, 2],  # Hip
    [4, 3],  # Knee
    [5, 4],  # Ankle
    [6, 3],  # Hip
    [6, 2],  # Knee
    [7, 3],  # Ankle
    [3, 5],  # Shoulder
    [5, 6],  # Elbow
    [7, 5],  # Wrist
    [4, 1],  # Toe
    [5, 1],  # Toe
    [6, 1],  # Toe
    [4, 4],  # Hand
    [6, 4],  # Hand
    [4, 4],  # Head
])

# Define the running motion by updating the positions
def update(frame):
    # Calculate the new positions for running
    t = frame / 10  # Time scaling
    displacement = np.array([0.5 * np.sin(t + (i * np.pi / 7)), -0.1 * np.cos(t + (i * np.pi / 7)) for i in range(n_points)])
    
    # Update positions with the calculated displacement
    new_positions = initial_positions + displacement
    points.set_offsets(new_positions)  # Update the points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
