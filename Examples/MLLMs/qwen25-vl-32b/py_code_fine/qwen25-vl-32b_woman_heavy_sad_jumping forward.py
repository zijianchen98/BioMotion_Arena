
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are relative and can be adjusted for better visualization
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.25],
    'right_elbow': [1, 0.25],
    'left_hand': [-1.5, -0.25],
    'right_hand': [1.5, -0.25],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Function to update the positions based on the jump animation
def update_positions(frame, coords):
    # Define the jump cycle (e.g., sine wave for vertical displacement)
    amplitude = 0.5  # Jump height
    frequency = 0.1  # Frequency of the jump
    phase_shift = frame * 0.1  # Progress through the jump cycle
    
    # Apply vertical displacement to the torso and limbs
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * phase_shift)
    
    # Adjust the positions for the jump forward motion
    forward_displacement = 0.1 * np.sin(2 * np.pi * frequency * phase_shift)
    
    # Update each joint's position
    updated_coords = coords.copy()
    updated_coords[:, 1] += vertical_displacement  # Vertical jump
    
    # Forward motion: Move the entire body forward
    updated_coords[:, 0] += forward_displacement
    
    # Add specific adjustments for the "heavy weight" and "sad" appearance:
    # - Torso slightly slumped downward
    # - Arms and legs more pronounced in their movement
    updated_coords[1, 1] -= 0.1  # Slightly slumped torso
    updated_coords[4:, :] *= 1.2  # Amplify limb movements to show "heavy weight"
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Plot the initial points
points = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    new_coords = update_positions(frame, initial_coords)
    points.set_offsets(new_coords)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
