
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 7], [3, 2], [3, 8],
    [4, 1], [4, 9], [5, 0], [5, 10], [6, 1], [6, 9], [7, 2], [7, 8]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Function to update the positions of the point-lights at each frame
def update(frame, points, lines):
    # Simulate a jumping motion (replace with a more realistic biomechanical model if needed)
    amp = 2  # Amplitude of jump
    freq = 0.5 # Frequency of jump
    phase = np.pi / 2 # Phase shift
    vertical_shift = amp * np.sin(2 * np.pi * freq * frame * dt + phase)

    new_positions = initial_positions.copy()
    new_positions[:, 1] += vertical_shift
    
    # Add some realistic motion to other point lights, simulating legs and arms movement.
    # Note: This is a simplified version and can be greatly improved to be more realistic.
    new_positions[6:8, 0] += 0.1 * np.sin(2 * np.pi * freq * frame * dt)
    new_positions[6:8, 1] -= 0.2 * np.cos(2 * np.pi * freq * frame * dt)
    new_positions[10:12, 0] -= 0.1 * np.sin(2 * np.pi * freq * frame * dt)
    new_positions[10:12, 1] -= 0.2 * np.cos(2 * np.pi * freq * frame * dt)



    for i, line in enumerate(lines):
        line.set_data(new_positions[i, 0], new_positions[i, 1])

    return lines


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-2, 10])
ax.set_ylim([-2, 12])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=8)
lines = [plt.Line2D([], [], marker='o', color='w', markersize=8, linestyle='None') for _ in range(15)]

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, fargs=(initial_positions, lines), interval=50, blit=True
)

# Save the animation as a GIF (optional)
# ani.save('jumping_man.gif', writer='imagemagick', fps=20)


plt.show()
