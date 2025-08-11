
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure:
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -3], # Left elbow
    [2, -3],  # Right elbow
    [-1, -4], # Left wrist
    [1, -4],  # Right wrist
    [0, -6],  # Hips
    [-1, -8], # Left hip
    [1, -8],  # Right hip
    [-1, -10], # Left knee
    [1, -10], # Right knee
    [-1, -12], # Left ankle
    [1, -12], # Right ankle
    [0, -14]  # Feet (center)
])

# Function to update the positions for running motion
def update_positions(frame, positions, dx, dy):
    """
    Update the positions of the points to simulate running.
    The left leg moves forward while the right leg moves backward,
    and vice versa in alternate frames.
    """
    # Running cycle: Left leg forward, right leg backward
    if frame % 2 == 0:
        # Move left leg forward and right leg backward
        positions[9][0] -= dx  # Left hip
        positions[10][0] -= dx  # Left knee
        positions[11][0] -= dx  # Left ankle
        positions[12][0] -= dx  # Left foot
        
        positions[10][1] += dy  # Left knee up
        positions[11][1] += dy  # Left ankle up
        
        positions[10][1] -= dy  # Right knee down
        positions[11][1] -= dy  # Right ankle down
        
    else:
        # Move right leg forward and left leg backward
        positions[10][0] += dx  # Right hip
        positions[11][0] += dx  # Right knee
        positions[12][0] += dx  # Right ankle
        positions[13][0] += dx  # Right foot
        
        positions[10][1] += dy  # Right knee up
        positions[11][1] += dy  # Right ankle up
        
        positions[9][1] -= dy  # Left knee down
        positions[10][1] -= dy  # Left ankle down
    
    # Adjust the head and torso to convey sadness
    positions[0][1] += 0.1 * np.sin(frame / 10)  # Slight bobbing of the head
    positions[1][1] += 0.1 * np.sin(frame / 10)  # Left shoulder
    positions[2][1] += 0.1 * np.sin(frame / 10)  # Right shoulder
    
    # Ensure the arms swing naturally
    positions[4][0] += 0.5 * np.cos(frame / 5)  # Left wrist
    positions[5][0] -= 0.5 * np.cos(frame / 5)  # Right wrist
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-15, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    global initial_positions
    updated_positions = update_positions(frame, initial_positions.copy(), dx=0.5, dy=1)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
