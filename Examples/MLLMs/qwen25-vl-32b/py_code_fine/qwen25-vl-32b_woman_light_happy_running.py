
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent:
# 0-Head, 1-Neck, 2-Spine, 3-Pelvis
# 4-R Shoulder, 5-R Elbow, 6-R Hand, 7-L Shoulder, 8-L Elbow, 9-L Hand
# 10-R Hip, 11-R Knee, 12-R Ankle, 13-L Hip, 14-L Knee, 15-L Ankle
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.5], # Neck
    [0, 0],   # Spine
    [0, -0.5],# Pelvis
    [-0.5, 0.5], # R Shoulder
    [-0.5, 0],   # R Elbow
    [-0.5, -0.5],# R Hand
    [0.5, 0.5],  # L Shoulder
    [0.5, 0],    # L Elbow
    [0.5, -0.5], # L Hand
    [-0.3, -0.5],# R Hip
    [-0.3, -1],  # R Knee
    [-0.3, -1.5],# R Ankle
    [0.3, -0.5], # L Hip
    [0.3, -1],   # L Knee
    [0.3, -1.5]  # L Ankle
])

# Function to update the positions based on the running cycle
def update_positions(frame, positions):
    # Define the amplitude and frequency for the running motion
    amplitude = 0.3
    frequency = 2 * np.pi / num_frames
    
    # Update the positions for each frame
    for i in range(len(positions)):
        if i == 0:  # Head
            positions[i][1] = 1 + amplitude * np.sin(frequency * frame)
        elif i == 2:  # Spine
            positions[i][1] = 0 + amplitude * np.sin(frequency * frame)
        elif i == 3:  # Pelvis
            positions[i][1] = -0.5 + amplitude * np.sin(frequency * frame)
        elif i in [4, 7]:  # Shoulders
            positions[i][1] = 0.5 + amplitude * np.sin(frequency * frame)
        elif i in [10, 13]:  # Hips
            positions[i][1] = -0.5 + amplitude * np.sin(frequency * frame)
        
        # Add cyclic motion to the legs (ankles and knees)
        if i in [11, 14]:  # Knees
            positions[i][1] = -1 + amplitude * np.sin(frequency * frame + np.pi / 2)
        elif i in [12, 15]:  # Ankles
            positions[i][1] = -1.5 + amplitude * np.sin(frequency * frame + np.pi)
        
        # Add side-to-side motion to the arms (hands and elbows)
        if i in [5, 8]:  # Elbows
            positions[i][0] += amplitude * np.cos(frequency * frame)
        elif i in [6, 9]:  # Hands
            positions[i][0] += amplitude * np.cos(frequency * frame + np.pi)
    
    # Simulate forward motion by shifting the entire body
    positions[:, 0] += 0.01  # Forward movement
    
    # Wrap around the screen horizontally to create a continuous loop
    positions[:, 0] = positions[:, 0] % 2
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    global initial_positions
    updated_positions = update_positions(frame, initial_positions.copy())
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
