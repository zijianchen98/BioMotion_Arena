
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
wave_amplitude = 0.5
wave_frequency = 2 * np.pi / 20
background_color = 'black'
point_color = 'white'

# Generate initial positions for point-lights
body_positions = np.array([
    [0, 0],                # Center (torso)
    [0, 1],                # Head
    [-0.5, 0.5],          # Left shoulder
    [0.5, 0.5],           # Right shoulder
    [-1, 1],              # Left hand - starting position
    [1, 1],               # Right hand - starting position
    [0, -1],              # Left foot
    [0, -2],              # Right foot
    [-1, 0],              # Left knee
    [1, 0],               # Right knee
    [-0.5, -1],           # Left ankle
    [0.5, -1],            # Right ankle
])

# Hand position changes for waving
def update_points(frame):
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    # Update the hand position for the waving effect
    left_hand_wave = [-1 + 0.5 * np.sin(wave_frequency * frame), 1 + wave_amplitude * np.sin(wave_frequency * frame)]
    right_hand_wave = [1 + 0.5 * np.sin(wave_frequency * frame), 1 + wave_amplitude * np.sin(wave_frequency * frame)]
    
    positions = np.copy(body_positions)
    positions[4] = left_hand_wave     # Update left hand
    positions[5] = right_hand_wave    # Update right hand
    
    # Draw point-lights
    ax.plot(positions[:, 0], positions[:, 1], 'o', color=point_color, markersize=15)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(background_color)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=frames, interval=50)

# Show the animation
plt.show()
