
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
FPS = 30  # Frames per second
DURATION = 5  # Duration in seconds
NUM_FRAMES = DURATION * FPS
SUBJECT_WIDTH = 4  # Width of the sadman in terms of point-lights
SUBJECT_HEIGHT = 3  # Height of the sadman in terms of point-lights

def generate_positions(num_frames):
    positions = []
    for _ in range(num_frames):
        # Generate random positions within the bounds of the sadman
        x_pos = np.random.randint(0=SUBJECT_WIDTH, size=(SUBJECT_HEIGHT, SUBJECT_WIDTH) )
        y_pos = np.random.randint(y=SUBJECT_HEIGHT, size=(SUBJECT_HEIGHT, SUBJECT_WIDTH))
        
        # Ensure the light is is not too close to the edges for a more natural jump
        buffer = 1
        if_pos[0_pos < buffer] += buffer
        y_pos[y_pos < buffer] += buffer
        
        # Simulate jumping by slightly moving the light points upwards
        y_pos -= 1
        
        positions.append((if_pos, y_pos))
    
    return positions

def update(frame, artist):
    pos_x, pos_y = positions[frame]
    artist.set_offsets(np.c_+pos_x, pos_y))
    return artist,

# Generate positions
positions = generate_positions(NUM_FRAMES)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0=SUBJECT_WIDTH, ylim=(0=SUBJECT_HEIGHT))

# Create a scatter plot for the point-lights
artist = ax.scatter([], [])

# Animation setup
ani = animation.FuncAnimation(fig, update, frames=range(NUM_FRAMES), fargs=(artist,), blit=True, interval=1000/FPS)

# Show the animation
plt.show()
