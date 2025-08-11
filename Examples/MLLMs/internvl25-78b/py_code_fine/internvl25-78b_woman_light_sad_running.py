
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Frame-specific positions
def generate_frames():
    frames = []
    # Example positions (15 points), adjust for actual motion capture data
    positions = [
        (0.1, 0.9), (0.2, 0.9), (0.3, 0.9),
        (0.15, 0.8), (0.25, 0.8), (0.35, 0.8),
        (0.1, 0.7), (0.2, 0.7), (0.3, 0.7),
        (0.2, 0.6), (0.3, 0.6), (0.4, 0.6),
        (0.25, 0.5), (0.35, 0.5), (0.45, 0.5)
    ]
    
    for _ in range(30):  # 30 frames
        positions = [(x + 0.01, y - 0.02) for x, y in positions]
        frames.append(positions)
    return frames

# Init figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scatter = ax.scatter([], [], s=50, color='white')

# Animation update function
def update(frame):
    scatter.set_offsets(frame)
    return scatter,

# Generate frames
frames = generate_frames()

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

# Display animation
plt.axis('off')
plt.show()
