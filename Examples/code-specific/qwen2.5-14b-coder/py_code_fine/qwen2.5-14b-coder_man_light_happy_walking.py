
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 4  # seconds
FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.axis('off')

# Create point lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Generate keyframe positions for walking motion
def generate_keyframes(num_frames):
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.sin(x_positions * 2 * np.pi / 10) + 5  # Simple sine wave for y position
    
    # Add some noise to make it more realistic
    noise = np.random.normal(0, 0.2, size=num_frames)
    y_positions += noise
    
    # Distribute points along the path
    x_positions = np.interp(np.linspace(0, num_frames - 1, NUM_LIGHTS * num_frames), np.arange(num_frames), x_positions)
    y_positions = np.interp(np.linspace(0, num_frames - 1, NUM_LIGHTS * num_frames), np.arange(num_frames), y_positions)
    
    return x_positions, y_positions

x_keyframes, y_keyframes = generate_keyframes(FRAMES)

# Update function for animation
def update(frame):
    start_idx = frame * NUM_LIGHTS
    end_idx = (frame + 1) * NUM_LIGHTS
    points.set_data(x_keyframes[start_idx:end_idx], y_keyframes[start_idx:end_idx])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
