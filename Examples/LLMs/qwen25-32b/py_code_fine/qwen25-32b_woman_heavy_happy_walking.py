
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and frames
num_lights = 15
frames_per_cycle = 60

# Define the positions of the lights representing the body parts
initial_positions = {
    'left_shoulder': np.array([1.0, 1.0]),
    'right_shoulder': np.array([3.0, 1.0]),
    'left_elbow': np.array([0.5, 0.5]),
    'right_elbow': np.array([3.5, 0.5]),
    'left_hand': np.array([0.0, 0.0]),
    'right_hand': np.array([4.0, 0.0]),
    'left_hip': np.array([1.5, -1.0]),
    'right_hip': np.array([2.5, -1.0]),
    'left_knee': np.array([1.0, -2.0]),
    'right_knee': np.array([3.0, -2.0]),
    'left_ankle': np.array([0.5, -3.0]),
    'right_ankle': np.array([3.5, -3.0]),
    'head': np.array([2.0, 1.5]),
    'torso': np.array([2.0, 0.0]),
    'pelvis': np.array([2.0, -1.5])
}

# Convert the dictionary to a list of initial positions
initial_positions_list = [initial_positions[key] for key in sorted(initial_positions)]

# Function to update the position of the lights
def update_position(frame):
    # Walking cycle
    cycle = frame % frames_per_cycle
    amplitude = 0.5
    frequency = 2 * np.pi / frames_per_cycle
    
    positions = []
    for i, pos in enumerate(initial_positions_list):
        new_pos = np.copy(pos)
        
        if i in [0, 1]:  # shoulders
            new_pos[0] += amplitude * np.sin(frequency * cycle + i * np.pi)
        elif i in [2, 3]:  # elbows
            new_pos[0] += amplitude * np.sin(frequency * cycle + (i+1) * np.pi)
        elif i in [4, 5]:  # hands
            new_pos[0] += amplitude * np.sin(frequency * cycle + (i+2) * np.pi)
        elif i in [6, 7]:  # hips
            new_pos[0] += amplitude * np.sin(frequency * cycle + (i+3) * np.pi)
        elif i in [8, 9]:  # knees
            new_pos[0] += amplitude * np.sin(frequency * cycle + (i+4) * np.pi)
        elif i in [10, 11]:  # ankles
            new_pos[0] += amplitude * np.sin(frequency * cycle + (i+5) * np.pi)
        else:
            new_pos[0] += amplitude * np.sin(frequency * cycle + i * np.pi)
            
        positions.append(new_pos)
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 6)
ax.set_ylim(-4, 2)
ax.axis('off')

# Scatter plot for the lights
scatter = ax.scatter(*zip(*update_position(0)))

# Update function for the animation
def animate(frame):
    positions = update_position(frame)
    scatter.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames_per_cycle, interval=50, blit=False)

plt.show()
