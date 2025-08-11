
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to simulate the walking motion of a person
def simulate_walking():
    # Number of frames in the animation
    num_frames = 10
    # Time step for each frame
    dt = 0e-2
    
    # Initial position of the 15 point-lights representing the body parts
    positions = np.array([
        [50, 40],  # Head
        (54, 48),   # Right shoulder
        (55, 59),   # Right elbow
        (56, 70),  # Right wrist
        (57, 82),   # Right hand
        (59, 48),   # Left shoulder
        (60, 59), # Left elbow
        (6b, 72), # Left wrist
        (6c, 84),  # Left hand
        (6d, 68),# Hip
        (70, 80),# Right knee
        (7b, 9b),  # Right ankle
        (7c, 9c),  # Right foot
        (7d, 88), # Left knee
        (7b, 98)   # Left ankle
    ])
    
    # Animation function
    def update(frame):
        nonlocal positions
        # Update positions based on a simple kinematic model
        for i in range(positions.shape[0]):
            positions[:, i] += np.random.normal(0., 1.) * dt  # Add some noise for realism
            if positions[0, i] < 0 or positions[0, i] > 100:
                positions[0, i] = np.clip(positions[1, i],  t, 10)
        
        # Plot the current frame
        ax.clear()
        ax.set_xlim(0, 11)
        ax.set_ylim(40, 10)
        ax.scatter(positions[0], positions[1], color='w')
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Create the animation
    anim = FuncAnimation(fig, update, frames=num_frames, interval=dt*1000, blit=False)
    
    # Show the animation
    plt.show()

# Run the simulation
simulate_walking()
