
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Constants**
num_points = 15
frames = 100
point_lights = np.zeros((num_points, 2))

# **Initial Positions of Point Lights (representing key joints)**
# Here we define the initial positions for a simple human skeleton
point_lights[:, 0] = [0, 0.5, -0.5, 0, 1, -1, 0.5, -0.5, 0, -0.5, -1, 1, -1, 0, 0]
point_lights[:, 1] = [1, 1.5, 1.5, 1, 1.5, 1.5, 1, 1, 1, 0, 0, -1, -1, -1.5, -1.5]

# **Function to update the positions for each frame**
def update(frame):
    plt.clf()
    
    # **Jump Motion**
    y_offset = np.sin(np.pi * (frame / frames))  # Simulate jumping motion
    x_offset = 0.05 * frame  # Small forward movement
    
    # **Update point light positions**
    updated_positions = point_lights + np.array([[x_offset, y_offset]]).T
    
    # **Plotting**
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white')
    plt.xlim(-5, 5)
    plt.ylim(-3, 3)
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axis
    
# **Create Animation**
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=20)

# **Display Animation**
plt.show()
