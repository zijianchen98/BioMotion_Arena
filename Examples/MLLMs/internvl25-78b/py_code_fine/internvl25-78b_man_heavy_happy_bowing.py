
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define frames for the animation
def update_points(num, data, points):
    points.set_data(data[:, 0, num], data[:, 1, num])
    return points,

# Generate initial positions of points
def generate_positions():
    positions = np.zeros((15, 2))
    base_y = np.linspace(1, 5, 5)
    base_x = np.array([0, 0.5, -0.5, 1, -1, 0.5, -0.5, 1, -1, 0, 0, 0, 0, 0, 0])
    
    for i in range(5):
        positions[i * 3:(i + 1) * 3, 0] = base_x[i * 3:(i + 1) * 3] + i * 0.2
        positions[i * 3:(i + 1) * 3, 1] = base_y[i]
    
    return positions

# Create animation data
def create_animation_data():
    num_frames = 60
    motion_data = np.zeros((15, 2, num_frames))
    positions = generate_positions()
    
    for i in range(num_frames):
        t = i / num_frames * 2 * np.pi
        bowing_motion = 0.3 * np.sin(t)
        
        for j in range(5):
            base_y = positions[j*3:(j+1)*3, 1]
            motion_data[j*3:(j+1)*3, 1, i] = base_y + bowing_motion
        
        motion_data[:, 0, i] = positions[:, 0]
    
    return motion_data

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 6)
ax.set_facecolor('black')

points, = ax.plot([], [], 'bo', ms=10)

data = create_animation_data()

ani = animation.FuncAnimation(fig, update_points, frames=data.shape[2],
                              fargs=(data, points),
                              interval=50, blit=True)

plt.show()
