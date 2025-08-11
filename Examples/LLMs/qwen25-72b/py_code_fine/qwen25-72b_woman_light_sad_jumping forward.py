
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a jumping woman
key_points = [
    "head", "neck", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
    "left_hand", "right_hand", "left_hip", "right_hip", "left_knee", "right_knee",
    "left_foot", "right_foot", "center_of_mass"
]

# Define initial positions for the key points
initial_positions = {
    "head": [0, 1.8],
    "neck": [0, 1.6],
    "left_shoulder": [-0.3, 1.5],
    "right_shoulder": [0.3, 1.5],
    "left_elbow": [-0.6, 1.3],
    "right_elbow": [0.6, 1.3],
    "left_hand": [-0.9, 1.1],
    "right_hand": [0.9, 1.1],
    "left_hip": [-0.3, 1.0],
    "right_hip": [0.3, 1.0],
    "left_knee": [-0.6, 0.6],
    "right_knee": [0.6, 0.6],
    "left_foot": [-0.9, 0.2],
    "right_foot": [0.9, 0.2],
    "center_of_mass": [0, 0.8]
}

# Define the animation parameters
frame_rate = 30  # frames per second
total_time = 2  # seconds
num_frames = int(total_time * frame_rate)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(0, 2.5)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot for the point-lights
scatter = ax.scatter([], [], color='white', s=50)

# Function to update the positions of the point-lights
def update(frame):
    t = frame / frame_rate  # time in seconds
    amplitude = 0.5  # amplitude of the jump
    frequency = 1  # frequency of the jump

    # Update the positions of the key points
    new_positions = []
    for key in key_points:
        x, y = initial_positions[key]
        y += amplitude * np.sin(2 * np.pi * frequency * t)
        if key == "center_of_mass":
            x += 0.1 * t  # move forward
        new_positions.append([x, y])
    
    # Update the scatter plot
    scatter.set_offsets(new_positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, repeat=True)

# Show the animation
plt.show()
