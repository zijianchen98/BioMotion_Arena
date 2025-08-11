
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the frame rate
num_frames = 50
frame_rate = 30

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.0, 1.5],  # Head
    [-0.2, 1.3],  # Left Shoulder
    [0.2, 1.3],  # Right Shoulder
    [-0.4, 1.1],  # Left Elbow
    [0.4, 1.1],  # Right Elbow
    [-0.6, 0.9],  # Left Wrist
    [0.6, 0.9],  # Right Wrist
    [-0.1, 1.1],  # Neck
    [-0.1, 0.8],  # Torso
    [-0.3, 0.6],  # Left Hip
    [0.1, 0.6],  # Right Hip
    [-0.5, 0.4],  # Left Knee
    [0.3, 0.4],  # Right Knee
    [-0.7, 0.2],  # Left Ankle
    [0.5, 0.2]   # Right Ankle
])

# Define the function to update the positions of the point-lights for each frame
def update_points(num):
    # Calculate the new positions of the point-lights
    positions = initial_positions.copy()
    
    # Simulate bowing motion
    angle = np.sin(num / num_frames * 2 * np.pi) * 0.5  # Adjust amplitude as needed
    
    # Apply rotation to the upper body
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Rotate points around the 'Neck' point
    neck_point = initial_positions[7]
    for i in range(7):  # Only rotate upper body points
        positions[i] = neck_point + np.dot(rotation_matrix, (initial_positions[i] - neck_point))
    
    # Update the scatter plot
    scat.set_offsets(positions)
    return scat,

# Create the figure and axes
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, aspect='equal', facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 1.7)
ax.axis('off')

# Create the scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, interval=1000/frame_rate, blit=True, repeat=True)

# Save the animation
#ani.save('bowing_man.mp4', writer='ffmpeg', fps=frame_rate) #Requires ffmpeg

plt.show()
