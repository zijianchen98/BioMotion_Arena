
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points
# These positions should roughly correspond to the joints of a human figure
# Example: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],  # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 1.0], # Left Hip
    [0.2, 1.0],  # Right Hip
    [-0.2, 0.0], # Left Knee
    [0.2, 0.0],  # Right Knee
    [-0.2, -1.0],# Left Ankle
    [0.2, -1.0], # Right Ankle
    [-0.5, 0.5], # Torso Left
    [0.5, 0.5],   # Torso Right
])


# Define the animation function
def animate(i):
    # Update the positions of the points
    # Here, we'll simulate a simple waving motion
    # This is a placeholder and can be replaced with more realistic motion data
    positions = initial_positions.copy()

    # Waving motion for the right arm
    amplitude = 0.5
    frequency = 0.1
    phase = i * frequency
    right_elbow_angle = np.sin(phase) * amplitude
    right_wrist_angle = np.cos(phase * 1.5) * amplitude

    # Apply rotation to the right elbow and wrist
    rotation_matrix_elbow = np.array([[np.cos(right_elbow_angle), -np.sin(right_elbow_angle)],
                                      [np.sin(right_elbow_angle), np.cos(right_elbow_angle)]])
    rotation_matrix_wrist = np.array([[np.cos(right_wrist_angle), -np.sin(right_wrist_angle)],
                                      [np.sin(right_wrist_angle), np.cos(right_wrist_angle)]])
    
    # Update elbow and wrist positions relative to shoulder
    positions[4] = initial_positions[4] + np.dot(rotation_matrix_elbow, [0.0, -0.5])
    positions[5] = initial_positions[5] + np.dot(rotation_matrix_wrist, [0.0, -1.0])

    # Torso sway
    torso_sway = np.sin(phase * 0.5) * 0.1
    positions[13, 0] += torso_sway 
    positions[14, 0] += torso_sway 

    # Update the scatter plot
    scatter.set_offsets(positions)
    return (scatter,)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Set the limits of the plot
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 3)

# Remove the axes
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20)

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=50, blit=True, save_count=50)

# Show the animation
plt.show()
