
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define initial positions of the 15 point-lights for the sad woman forward rolling motion
initial_positions = [
    (0, 1.0), (0.2, 0.8), (0.4, 0.6), (0.6, 0.4), (0.8, 0.2),
    (1.0, 0), (0.8, -0.2), (0.6, -0.4), (0.4, -0.6), (0.2, -0.8),
    (0, -1.0), (-0.2, -0.8), (-0.4, -0.6), (-0.6, -0.4), (-0.8, -0.2)
]

# Function to update the positions of the point-lights for each frame
def update_positions(positions, frame):
    new_positions = []
    for x, y in positions:
        angle = frame / 10
        x_new = x * np.cos(angle) - y * np.sin(angle)
        y_new = x * np.sin(angle) + y * np.cos(angle)
        new_positions.append((x_new, y_new))
    return new_positions

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')

scatter = ax.scatter([], [], c='white', s=50)

def animate(frame):
    positions = update_positions(initial_positions, frame)
    scatter.set_offsets(positions)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)
plt.show()
