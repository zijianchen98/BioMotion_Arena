
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Parameters for the animation
num_points = 15
time_steps = 200
speed = 0.05

# Initialize the positions of the point-lights
# Base positions on the body parts - head, shoulders, elbows, wrists, hips, knees, ankles
body_parts = [
    'head', 'shoulders right', 'elbows right', 'wrists right',
    'shoulders left', 'elbows left', 'wrists left',
    'hips', 'knees right', 'ankles right',
    'hips', 'knees left', 'ankles left'
]

# Initial positions (x, y)
positions = np.array([
    [5, 1.5],  # head
    [6, 1.3],  # shoulders right
    [6.7, 1.0],  # elbows right
    [7.0, 0.7],  # wrists right
    [4, 1.3],  # shoulders left
    [3.3, 1.0],  # elbows left
    [3.0, 0.7],  # wrists left
    [5, 1.0],  # hips
    [5.3, 0.5],  # knees right
    [5.6, 0.0],  # ankles right
    [5, 1.0],  # hips
    [4.7, 0.5],  # knees left
    [4.4, 0.0]   # ankles left
])

# Initialize the scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=50, color='white')

def update(frame):
    global positions
    
    # Animate walking movement based on time frame
    t = frame / time_steps * 2 * np.pi
    
    # Head
    positions[0, 0] = 5 + 0.2 * np.sin(t)
    
    # Right shoulder
    positions[1, 0] = 6 + 0.1 * np.sin(t)
    
    # Right elbow
    positions[2, 0] = 6.7 + 0.05 * np.sin(t)
    
    # Right wrist
    positions[3, 0] = 7.0 + 0.03 * np.sin(t)
    
    # Left shoulder
    positions[4, 0] = 4 + 0.1 * np.sin(t)
    
    # Left elbow
    positions[5, 0] = 3.3 + 0.05 * np.sin(t)
    
    # Left wrist
    positions[6, 0] = 3.0 + 0.03 * np.sin(t)
    
    # Move the whole body slightly to simulate walking
    positions[:, 0] += speed
    
    # Remove points that go out of bounds
    mask = (positions[:, 0] > 0) & (positions[:, 0] < 10)
    positions = positions[mask]
    
    # Re-add initial body parts if needed
    if len(positions) < num_points:
        # Adjust and re-add the necessary body parts
        positions = np.vstack([positions, [5, 1.5], [6, 1.3], [6.7, 1.0], [7.0, 0.7],
                             [4, 1.3], [3.3, 1.0], [3.0, 0.7], [5, 1.0], [5.3, 0.5], [5.6, 0.0],
                             [5, 1.0], [4.7, 0.5], [4.4, 0.0]])
        
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=50, blit=True)

plt.show()
