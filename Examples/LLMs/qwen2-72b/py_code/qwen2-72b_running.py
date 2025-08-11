
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions and velocities of the point-lights
positions = np.array([
    [0.0, 0.0],  # Head
    [-0.2, -0.2],  # Left shoulder
    [0.2, -0.2],  # Right shoulder
    [-0.4, -0.6],  # Left hip
    [0.4, -0.6],  # Right hip
    [-0.3, -0.8],  # Left knee
    [0.3, -0.8],  # Right knee
    [-0.2, -1.0],  # Left ankle
    [0.2, -1.0],  # Right ankle
    [-0.1, -1.2],  # Left foot
    [0.1, -1.2],  # Right foot
    [0.0, -0.4],  # Waist
    [0.0, -0.7],  # Pelvis
    [0.0, -1.1],  # Heel
    [0.0, -1.3]   # Toe
])

velocities = np.zeros_like(positions)

# Define the update function for the animation
def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions += velocities
    
    # Apply simple physics to simulate running motion
    if frame % 10 == 0:
        velocities[0] = [0.0, 0.0]  # Head remains relatively still
        velocities[1] = [0.05 * (-1)**(frame//10), -0.1]  # Left shoulder
        velocities[2] = [-0.05 * (-1)**(frame//10), -0.1]  # Right shoulder
        velocities[3] = [0.1 * (-1)**(frame//10), -0.2]  # Left hip
        velocities[4] = [-0.1 * (-1)**(frame//10), -0.2]  # Right hip
        velocities[5] = [0.2 * (-1)**(frame//10), -0.3]  # Left knee
        velocities[6] = [-0.2 * (-1)**(frame//10), -0.3]  # Right knee
        velocities[7] = [0.3 * (-1)**(frame//10), -0.4]  # Left ankle
        velocities[8] = [-0.3 * (-1)**(frame//10), -0.4]  # Right ankle
        velocities[9] = [0.4 * (-1)**(frame//10), -0.5]  # Left foot
        velocities[10] = [-0.4 * (-1)**(frame//10), -0.5]  # Right foot
        velocities[11] = [0.0, -0.1]  # Waist
        velocities[12] = [0.0, -0.2]  # Pelvis
        velocities[13] = [0.0, -0.3]  # Heel
        velocities[14] = [0.0, -0.4]  # Toe
        
    # Clear the previous frame
    plt.cla()
    
    # Plot the point-lights
    plt.scatter(positions[:, 0], positions[:, 1], color='white')
    
    # Set the plot limits
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    # Set the background color to black
    ax = plt.gca()
    ax.set_facecolor('black')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
