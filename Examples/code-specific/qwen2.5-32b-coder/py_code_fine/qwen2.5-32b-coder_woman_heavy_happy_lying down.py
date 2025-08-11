
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point lights
num_lights = 15

# Initialize the positions of the point lights
positions = np.zeros((num_frames, num_lights, 2))

# Define the initial positions of the point lights for a lying down woman
initial_positions = [
    (0.5, 0.9),  # Head
    (0.4, 0.8),  # Left Shoulder
    (0.6, 0.8),  # Right Shoulder
    (0.3, 0.7),  # Left Elbow
    (0.7, 0.7),  # Right Elbow
    (0.2, 0.6),  # Left Hand
    (0.8, 0.6),  # Right Hand
    (0.5, 0.7),  # Chest
    (0.5, 0.5),  # Belly
    (0.4, 0.4),  # Left Hip
    (0.6, 0.4),  # Right Hip
    (0.3, 0.3),  # Left Knee
    (0.7, 0.3),  # Right Knee
    (0.2, 0.2),  # Left Foot
    (0.8, 0.2)   # Right Foot
]

# Convert initial positions to numpy array
initial_positions = np.array(initial_positions)

# Define the movement of the point lights over time
def update_positions(frame):
    # Simple harmonic motion for breathing effect
    breath_amplitude = 0.02
    breath_frequency = 0.1
    breath_offset = 0.5
    
    # Movement parameters
    hip_movement_amplitude = 0.05
    hip_movement_frequency = 0.05
    knee_movement_amplitude = 0.05
    knee_movement_frequency = 0.05
    
    # Update positions for each light
    for i in range(num_lights):
        x, y = initial_positions[i]
        
        # Breathing effect for chest and belly
        if i in [7, 8]:
            y += breath_amplitude * np.sin(breath_frequency * frame + breath_offset)
        
        # Hip movement
        if i in [9, 10]:
            y += hip_movement_amplitude * np.sin(hip_movement_frequency * frame)
        
        # Knee movement
        if i in [11, 12]:
            y -= knee_movement_amplitude * np.sin(knee_movement_frequency * frame)
        
        positions[frame, i] = (x, y)

# Generate positions for all frames
for frame in range(num_frames):
    update_positions(frame)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], s=100, c='white')

# Update function for the animation
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
