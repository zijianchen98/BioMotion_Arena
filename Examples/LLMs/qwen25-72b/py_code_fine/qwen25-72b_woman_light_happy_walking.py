
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a walking woman
def get_walking_points(t):
    # t is the time in seconds
    # Define the positions of the 15 points
    points = np.zeros((15, 2))
    
    # Head
    points[0] = [0.5 + 0.05 * np.sin(2 * np.pi * t), 0.9]
    
    # Shoulders
    points[1] = [0.4 + 0.05 * np.sin(2 * np.pi * t), 0.8]
    points[2] = [0.6 + 0.05 * np.sin(2 * np.pi * t), 0.8]
    
    # Elbows
    points[3] = [0.35 + 0.05 * np.sin(2 * np.pi * t), 0.7]
    points[4] = [0.65 + 0.05 * np.sin(2 * np.pi * t), 0.7]
    
    # Wrists
    points[5] = [0.3 + 0.05 * np.sin(2 * np.pi * t), 0.6]
    points[6] = [0.7 + 0.05 * np.sin(2 * np.pi * t), 0.6]
    
    # Hips
    points[7] = [0.4 + 0.05 * np.sin(2 * np.pi * t), 0.5]
    points[8] = [0.6 + 0.05 * np.sin(2 * np.pi * t), 0.5]
    
    # Knees
    points[9] = [0.35 + 0.05 * np.sin(2 * np.pi * t), 0.3]
    points[10] = [0.65 + 0.05 * np.sin(2 * np.pi * t), 0.3]
    
    # Ankles
    points[11] = [0.3 + 0.05 * np.sin(2 * np.pi * t), 0.1]
    points[12] = [0.7 + 0.05 * np.sin(2 * np.pi * t), 0.1]
    
    # Feet
    points[13] = [0.25 + 0.05 * np.sin(2 * np.pi * t), 0.0]
    points[14] = [0.75 + 0.05 * np.sin(2 * np.pi * t), 0.0]
    
    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create a list of scatter plots for each point
scatters = [ax.scatter([], [], c='white', s=50) for _ in range(15)]

# Animation update function
def update(frame):
    points = get_walking_points(frame / 100)  # 100 frames per second
    for i, sc in enumerate(scatters):
        sc.set_offsets(points[i])
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=10, blit=True)

# Display the animation
plt.show()
