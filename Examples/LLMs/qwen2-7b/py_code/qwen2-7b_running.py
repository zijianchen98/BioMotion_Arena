
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
NUM_LIGHTS = 15
FPS = 60
DURATION = 5 # in seconds
DURATION_FRAMES = int(FPS * DURATION)

def update(frame_number):
    global frame_counter
    
    # Increment frame counter
    frame_counter += 1
    
    # Calculate positions based on sine wave motion
    x_positions = np.sin( * 2 * np.pi * frame_counter / DURATION_FRAMES
    y_positions = np.cos * 2 * np.pi * frame_counter / DURATION_FRAMES
    
    # Plot lights
    for i in range(NUM_LIGHTS):
        ax.add_patch(
            plt.Circle((x_positions[i], y_positions[i]), radius=0.05, color='white')
        )
        
    # Ensure consistent frame rate
    ani.event_source.stop()
    ani.event_source.start()

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create animation
frame_counter = 0
ani = animation.FuncAnimation(fig, update, frames=DURATION_FRAMES, interval=1000/FPS)

plt.show()

