
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the figure size
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6, 6))

# Initialize the point-lights
points = np.array([
    [0.5, 0.8], [0.4, 0.6], [0.6, 0.6],  # Head and shoulders
    [0.4, 0.4], [0.6, 0.4], [0.3, 0.2],  # Hips and upper legs
    [0.2, 0.0], [0.8, 0.0], [0.2, 0.2],  # Lower legs and feet
    [0.55, 0.6], [0.45, 0.6],  # Arms
    [0.55, 0.3], [0.45, 0.3],  # Forearms
    [0.5, 0.1], [0.5, 0.2]    # Weight on stomach
])

# Initialize the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Step variables
step = 0
step_size = 0.01

def update(frame):
    global points, step
    # Define walking movement
    amplitude = 0.1
    frequency = 0.5
    phase_shift = np.pi

    # Calculate movement based on sine wave
    points[:, 1] = (points[:, 1] + amplitude * np.sin(frequency * (frame + points[:, 0] * phase_shift))) % 1
    points[:, 0] = (points[:, 0] + amplitude * np.sin(frequency * (frame + points[:, 1] * phase_shift))) % 1

    # Update the scatter plot
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=50, blit=True)

plt.show()
