
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Define the initial positions of the point-lights
initial_positions = [
    [0, 5],  # Head
    [-1, 4], [1, 4],  # Shoulders
    [-2, 3], [2, 3],  # Elbows
    [-3, 2], [3, 2],  # Wrists
    [0, 2],  # Waist
    [-1, 1], [1, 1],  # Hips
    [-2, 0], [2, 0],  # Knees
    [-3, -1], [3, -1],  # Ankles
    [-4, -2], [4, -2]  # Feet
]

# Convert initial positions to a NumPy array
positions = np.array(initial_positions)

# Define the animation parameters
frames = 100
interval = 50

# Function to update the positions of the point-lights
def update(frame):
    global positions
    
    # Calculate the angle for the bowing motion
    angle = np.sin(2 * np.pi * frame / frames) * 0.5
    
    # Update the positions of the point-lights
    for i in range(len(positions)):
        if i == 0:  # Head
            positions[i, 1] = 5 + angle
        elif i in [1, 2]:  # Shoulders
            positions[i, 1] = 4 + angle
        elif i in [3, 4]:  # Elbows
            positions[i, 1] = 3 + angle
        elif i in [5, 6]:  # Wrists
            positions[i, 1] = 2 + angle
        elif i == 7:  # Waist
            positions[i, 1] = 2 + angle
        elif i in [8, 9]:  # Hips
            positions[i, 1] = 1 + angle
        elif i in [10, 11]:  # Knees
            positions[i, 1] = 0 + angle
        elif i in [12, 13]:  # Ankles
            positions[i, 1] = -1 + angle
        elif i in [14, 15]:  # Feet
            positions[i, 1] = -2 + angle
    
    # Clear the previous frame
    ax.cla()
    ax.set_facecolor('black')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axis('off')
    
    # Plot the point-lights
    for pos in positions:
        ax.plot(pos[0], pos[1], 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, repeat=True)

# Display the animation
plt.show()
