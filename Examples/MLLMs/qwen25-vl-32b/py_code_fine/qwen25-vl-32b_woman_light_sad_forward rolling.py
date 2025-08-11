
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
# Points: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.2, -0.2], # Left Shoulder
    [0.2, -0.2],  # Right Shoulder
    [-0.4, -0.6], # Left Elbow
    [0.4, -0.6],  # Right Elbow
    [-0.3, -1.0], # Left Wrist
    [0.3, -1.0],  # Right Wrist
    [0.0, -1.2],  # Hips
    [-0.2, -1.8], # Left Knee
    [0.2, -1.8],  # Right Knee
    [-0.3, -2.2], # Left Ankle
    [0.3, -2.2],  # Right Ankle
    [0.0, -2.5],  # Center of mass (additional point for rolling)
    [-0.1, -2.7], # Left Foot
    [0.1, -2.7]   # Right Foot
])

# Function to update the positions for rolling motion
def update_positions(frame, positions, center_of_mass):
    angle = np.radians(10 * frame)  # Rolling angle
    radius = 0.5  # Radius of the rolling circle
    
    # Update the center of mass position (rolling along x-axis)
    center_of_mass[0] += 0.05  # Forward rolling motion
    
    # Calculate new positions based on the rolling angle
    for i in range(len(positions)):
        if i == 12:  # Center of mass
            continue  # Keep it fixed relative to the rolling motion
        dx = positions[i][0] - center_of_mass[0]
        dy = positions[i][1] - center_of_mass[1]
        
        # Rotate around the center of mass
        x_new = center_of_mass[0] + dx * np.cos(angle) - dy * np.sin(angle)
        y_new = center_of_mass[1] + dx * np.sin(angle) + dy * np.cos(angle)
        
        # Apply vertical displacement to simulate rolling
        y_new -= radius * (1 - np.cos(angle))
        
        positions[i] = [x_new, y_new]
    
    return positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.axis('off')  # Hide axes
scat = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    global initial_positions
    updated_positions = update_positions(frame, initial_positions.copy(), initial_positions[12])
    scat.set_offsets(updated_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=72, interval=50, blit=True)

# Display the animation
plt.show()
