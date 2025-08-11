
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and frames
num_lights = 15
num_frames = 100

# Initialize positions for the lights (happy woman bowing)
def initialize_positions():
    positions = np.zeros((num_lights, num_frames, 2))
    
    # Head
    positions[0, :, 1] = -0.8 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[0, :, 0] = 0
    
    # Shoulders
    positions[1, :, 1] = -1.0
    positions[1, :, 0] = 0.2
    positions[2, :, 1] = -1.0
    positions[2, :, 0] = -0.2
    
    # Elbows
    positions[3, :, 1] = -1.2 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[3, :, 0] = 0.4
    positions[4, :, 1] = -1.2 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[4, :, 0] = -0.4
    
    # Hands
    positions[5, :, 1] = -1.4 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[5, :, 0] = 0.6
    positions[6, :, 1] = -1.4 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[6, :, 0] = -0.6
    
    # Hips
    positions[7, :, 1] = -1.6
    positions[7, :, 0] = 0.2
    positions[8, :, 1] = -1.6
    positions[8, :, 0] = -0.2
    
    # Knees
    positions[9, :, 1] = -1.8 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[9, :, 0] = 0.4
    positions[10, :, 1] = -1.8 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[10, :, 0] = -0.4
    
    # Feet
    positions[11, :, 1] = -2.0 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[11, :, 0] = 0.6
    positions[12, :, 1] = -2.0 + np.sin(np.linspace(0, np.pi, num_frames)) * 0.1
    positions[12, :, 0] = -0.6
    
    # Bowing motion
    positions[:, :, 1] += np.sin(np.linspace(0, np.pi, num_frames)) * 0.5
    
    return positions

positions = initialize_positions()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.axis('off')

# Plot function for animation
def animate(frame):
    ax.clear()
    ax.scatter(positions[:, frame, 0], positions[:, frame, 1], color='white', s=10)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 1)
    ax.axis('off')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

plt.show()
