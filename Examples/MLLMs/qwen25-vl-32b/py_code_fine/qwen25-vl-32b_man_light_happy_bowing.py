
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, -0.5],
    'right_shoulder': [0.5, -0.5],
    'left_elbow': [-1, -1],
    'right_elbow': [1, -1],
    'left_wrist': [-1.5, -1.5],
    'right_wrist': [1.5, -1.5],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the bowing motion
def bowing_motion(t, amplitude=0.5, frequency=0.2):
    """
    Generate bowing motion for the torso and head.
    t: time in seconds
    amplitude: vertical displacement during the bow
    frequency: how fast the bowing happens
    """
    # Torso and head move vertically in a sinusoidal pattern
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    return vertical_displacement

# Create a function to update the positions over time
def update_positions(t):
    positions = initial_coords.copy()
    
    # Apply bowing motion to the torso and head
    vertical_displacement = bowing_motion(t)
    positions[0] += [0, vertical_displacement]  # Head
    positions[1] += [0, vertical_displacement]  # Torso
    
    # Adjust other joints based on the torso's movement
    for i in range(2, len(positions)):
        if i in [2, 3]:  # Shoulders
            positions[i][1] += vertical_displacement / 2
        elif i in [4, 5]:  # Elbows
            positions[i][1] += vertical_displacement / 3
        elif i in [6, 7]:  # Wrists
            positions[i][1] += vertical_displacement / 4
        elif i in [8, 9]:  # Hips
            positions[i][1] += vertical_displacement / 2
        elif i in [10, 11]:  # Knees
            positions[i][1] += vertical_displacement / 3
        elif i in [12, 13]:  # Ankles
            positions[i][1] += vertical_displacement / 4
    
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(t):
    positions = update_positions(t)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=np.linspace(0, 10, 200),  # Simulate 10 seconds of animation
    interval=50,  # 50ms between frames (20 FPS)
    blit=True
)

# Display the animation
plt.show()
